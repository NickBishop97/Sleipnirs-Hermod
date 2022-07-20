#!/bin/bash
########################################################################################################################
# Filename: build-container.sh
#
# Date: 2022-07-07
# Author: Christopher J. Mundt
#
# Desc: Build script to generate a UBI8 Minimal Dev Container
#
# Reference: https://www.redhat.com/sysadmin/building-buildah
#            https://gitlab.sde.sp.gc1.myngc.com/lts/Triton/-/tree/master/containers/buildenv-ubi8
#            https://github.com/containers/buildah/issues/2230 ----- Too Many Open Files
#            https://access.redhat.com/solutions/6301531 --- DefaultLimitNOFILE
#
# Info: Based this off of work previously completed under the Triton project.
#
#
#           ************************************************************************************************************
# History:  |Version    Date        Task         Author                Desc
#           |-----------------------------------------------------------------------------------------------------------
#           | 1.0       2022-07-07  LETS-4837    Christopher J. Mundt  Initial Rev.
#           | 1.1       2022-07-12  LETS-4837    Christopher J. Mundt  Updated to address "Too Many Open Files"
#           | 1.2       2022-07-14  LETS-4837    Christopher J. Mundt  Make script generic based on Containerfile
#           |-----------------------------------------------------------------------------------------------------------
#
########################################################################################################################
clear

#====================
#
# Check if script is already running
#
#====================
script_name=$(basename -- "$0")

if pidof -x "$script_name" -o $$ >/dev/null;then
    echo "An another instance of this script is already running, please clear all the sessions of this script before starting a new session"
    exit -1
fi

# **********************************************************************************************************************
#====================
#
# Variables/Constants
#
#====================
CONTAINER_FILE=""
NEW_IMAGE_NAME=""
NEW_CONTAINER_NAME=""
OPTSTRING="f:i:n:"
START_TIME=$(date +%s)
WORKING_DIR=$(pwd)

# **********************************************************************************************************************

# **********************************************************************************************************************
#====================
#
# Functions
#
#====================
function usage {
    echo 
    echo "Usage: $(basename $0) [-cif]" 2>&1
    echo '   -f Containerfile   Input the path to the Container File'
    echo '   -i [ImageName]     Optional: Will be used as name for the new Image'
    echo '   -n [ContainerName] Optional: Will be used as name for the Container'
    echo
    exit -1
}

function ts_echo()
{
    # Timestamped Echo Statement
    
    echo "$(date "+[%Y-%m-%d %H:%M:%S] ") $@"
}

function container_exists()
{
    buildah containers --format "{{.ContainerName}}" --filter name=$@ |grep -i -E "^$@\$"
}

# **********************************************************************************************************************

# **********************************************************************************************************************
#====================
#
# Begin Script
#
#====================

# Were Options Provided
if [[ ${#} -eq 0 ]]; then
    usage
fi

# Loop through Options
while getopts ${OPTSTRING} option; do

    # Validate that a value was provided for each option
    if [[ "${OPTARG}" == -* ]] || [[ "${#OPTARG}" -lt 2 ]]; then

        echo "Invalid value provided for option : -${option} ${OPTARG}"

        usage    

    fi

    case "${option}" in

        f)
            CONTAINER_FILE="${OPTARG}"
        ;;
        i)
            # Names must be all lowercase
            NEW_IMAGE_NAME=$(echo ${OPTARG} | tr '[:upper:]' '[:lower:]')
        ;;
        n)
            # Names must be all lowercase
            NEW_CONTAINER_NAME=$(echo ${OPTARG} | tr '[:upper:]' '[:lower:]')
        ;;
        
        :)
            echo "Error: ${OPTARG} requires an argument."
            usage
        ;;
        ?)
            echo
            usage
        ;;
    esac
done

# Validate Container File exists
if [[ ! -f "${CONTAINER_FILE}" ]]; then
    echo "Container File does not exist:   ${CONTAINER_FILE}"
    echo
    usage
fi

# Validate Names
TEMP="$(basename -- $CONTAINER_FILE)"
TEMP=${TEMP#*-}
if [[ -z ${NEW_IMAGE_NAME} ]]; then
    #NEW_IMAGE_NAME="${TEMP}-image-$(date +%Y%m%d-%H%M%S)"
    NEW_IMAGE_NAME="${TEMP}-image"
    #echo "No Image Name provided, so using: ${NEW_IMAGE_NAME}"    
#else    
    #echo "Image name will be: ${NEW_IMAGE_NAME}"
fi

if [[ -z ${NEW_CONTAINER_NAME} ]]; then
    #NEW_CONTAINER_NAME="${TEMP}-container-$(date +%Y%m%d-%H%M%S)"
    NEW_CONTAINER_NAME="${TEMP}-container"
    #echo "No Container Name provided, so using: ${NEW_CONTAINER_NAME}"
#else
    # echo "Container name will be: ${NEW_CONTAINER_NAME}"
fi

ts_echo "#===================="
ts_echo "# "
ts_echo "# Running Script: $0"
ts_echo "# "
ts_echo "#===================="
echo

#====================
#
# Begin of: Check if Container Exists
#
#====================
if [[ -n $(container_exists ${NEW_CONTAINER_NAME}) ]]
then
    ts_echo "#===================="
    ts_echo "# "
    ts_echo "# Removing existing container: ${NEW_CONTAINER_NAME} "
    ts_echo "# "
    ts_echo "#===================="
    buildah rm ${NEW_CONTAINER_NAME} > /dev/null 2>&1
    echo
fi
#====================
#
# End of:  Check if Container Exists
#
#====================

#====================
#
# Begin of: Create New Base Image from a Containerfile
#
#====================
ts_echo "#===================="
ts_echo "# "
ts_echo "# Creating New Image: ${NEW_IMAGE_NAME} from ${CONTAINER_FILE}"
ts_echo "# "
ts_echo "#===================="
# Use the --squash flag if you want to squash all layers into one for the image.
# This will reduce the space needed, but will decrease the ability to make use of
# cached image layers on new builds.
#buildah bud -t ${NEW_IMAGE_NAME} --file ${CONTAINER_FILE} --squash
buildah bud -t ${NEW_IMAGE_NAME} --file ${CONTAINER_FILE}
echo
#====================
#
# End of: Create New Base Image from a Containerfile
#
#====================

#====================
#
# Begin of: Create Tempoary Container and verify start
#
#====================
ts_echo "#===================="
ts_echo "# "
ts_echo "# Confirming that Image is Valid"
ts_echo "# "
ts_echo "#     Temporary Container: ${NEW_CONTAINER_NAME}"
ts_echo "#     From Image:          ${NEW_IMAGE_NAME}"
ts_echo "#===================="
ts_echo
ts_echo "${NEW_CONTAINER_NAME} is running $(podman run --rm --name=${NEW_CONTAINER_NAME} ${NEW_IMAGE_NAME} cat /etc/redhat-release)"
echo
#====================
#
# End of:   Create New Container and validate OS
#
#====================

#====================
#
# Calculate Runtime and Exit
#
#====================
END_TIME=$(date +%s)
ts_echo "Elapsed Runtime: $(($END_TIME-$START_TIME)) seconds"
exit 1
