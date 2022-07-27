#!/bin/bash
########################################################################################################################
# Filename: run-container.sh
#
# Date: 2022-07-11
# Author: Christopher J. Mundt
#
# Desc: Run script to run a Container based off the assigned image
#
# Reference: https://www.redhat.com/sysadmin/building-buildah
#            https://gitlab.sde.sp.gc1.myngc.com/lts/Triton/-/tree/master/containers/buildenv-ubi8
#
# Info: Based this off of work previously completed under the Triton project.
#
#
#           ************************************************************************************************************
# History:  |Version    Date        Task         Author                Desc
#           |-----------------------------------------------------------------------------------------------------------
#           | 1.0       2022-07-11  LETS-4837    Christopher J. Mundt  Initial Rev.
#           |
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

##############
# UBI8 Dev FastDDS Environment
CONTAINER_IMAGE="ubi7-fastdds-python-image "
CONTAINER_NAME="myubi7-fastdds"
DEFAULT_COMMAND="/bin/bash"
#CONTAINER_IMAGE="ubi7-dev-image "
#CONTAINER_NAME="myubi7-dev"
#DEFAULT_COMMAND="/bin/bash"

START_TIME=$(date +%s)
WORKING_DIR=$(pwd)

# **********************************************************************************************************************

# **********************************************************************************************************************
#====================
#
# Functions
#
#====================
ts_echo()
{
    # Timestamped Echo Statement
    
    echo "$(date "+[%Y-%m-%d %H:%M:%S] ") $@"
}

container_exists()
{
    podman container list -a --format={{.Names}} --filter name=$@ |grep -i -E "^$@\$"
}


#====================
#
# Begin of: Start Container
#
#====================
if [[ -n $(container_exists ${CONTAINER_NAME}) ]]
then 
    ts_echo "#===================="
    ts_echo "# "
    ts_echo "# Container already exists. Starting : ${CONTAINER_NAME} "
    ts_echo "# "
    ts_echo "#===================="
    #podman start -a -e DISPLAY="$DISPLAY" --net=host -v ../../:/usr/src:Z -w /usr/src -v ~/.Xauthority:/root/.Xauthority:Z --name=${CONTAINER_NAME} ${DEFAULT_COMMAND}
    podman start -a ${CONTAINER_NAME}
    echo
    exit 1
else
    ts_echo "#===================="
    ts_echo "# "
    ts_echo "# Creating and starting new container : ${CONTAINER_NAME} based off: ${CONTAINER_IMAGE}"
    ts_echo "# "
    ts_echo "#===================="
    #podman run -it -e DISPLAY="$DISPLAY" --privileged --systemd=true --net=host -v ../../:/usr/src:Z -w /usr/src -v ~/.Xauthority:/root/.Xauthority:Z --name=${CONTAINER_NAME} ${CONTAINER_IMAGE} ${DEFAULT_COMMAND}
    podman run -it -e DISPLAY="$DISPLAY" --privileged --systemd=true --net=host -v ./:/usr/src:Z -w /usr/src -v ~/.Xauthority:/root/.Xauthority:Z --name=${CONTAINER_NAME} ${CONTAINER_IMAGE} ${DEFAULT_COMMAND}
    echo
    exit 2
fi
#====================
#
# End of:  Start Container
#
#====================
