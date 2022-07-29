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
#           | 2.0       2022-07-28  LETS-4837    Christopher J. Mundt  Add Menu Functionality
#           |-----------------------------------------------------------------------------------------------------------
#
########################################################################################################################
clear

#====================
#
# Check if script is already running
#
#====================
#script_name=$(basename -- "$0")
#
#if pidof -x "$script_name" -o $$ >/dev/null;then
#    echo "An another instance of this script is already running, please clear all the sessions of this script before starting a new session"
#    exit -1
#fi

# **********************************************************************************************************************

#====================
#
# Variables/Constants
#
#====================
CONTAINER_IMAGE=""
CONTAINER_NAME=""
DEFAULT_COMMAND="/usr/bin/bash"
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
# Begin of: Option Menu
#
#====================

title="Select Image you like to Run"
prompt="Pick an option:"
options=("UBI7-Dev" "UBI7-Fast-DDS" "UBI8-Dev" "UBI8-Fast-DDS" "UBI7-Sleipnir" "UBI8-Sleipnir")

echo "$title"
PS3="$prompt "
select opt in "${options[@]}" "Quit"; do 
    case "$REPLY" in
    1) # UBI7-DEV
        echo "You picked $opt which is option 1"
        CONTAINER_IMAGE="ubi7-dev-image"
        CONTAINER_NAME="myubi7-dev"
        DEFAULT_COMMAND="cat /etc/redhat-release"
        break;;
    2) # UBI7-Fast-DDS-Python
        echo "You picked $opt which is option 2"
        CONTAINER_IMAGE="ubi7-fastdds-python-image"
        CONTAINER_NAME="myubi7-fastdds"
        break;;
    3) # UBI8-DEV
        echo "You picked $opt which is option 3"
        CONTAINER_IMAGE="ubi8-dev-image"
        CONTAINER_NAME="myubi8-dev"
        DEFAULT_COMMAND="cat /etc/redhat-release"
        break;;
    4) # UBI8-Fast-DDS-Python
        echo "You picked $opt which is option 4" 
        CONTAINER_IMAGE="ubi8-fastdds-python-image"
        CONTAINER_NAME="myubi8-fastdds"        
        break;;
    5) # UBI7-Sleipnir
        echo "You picked $opt which is option 5" 
        CONTAINER_IMAGE="ubi7-sleipnir-image"
        CONTAINER_NAME="myubi7-sleipnir" 
        break;;
    6) # UBI8-Sleipnir
        echo "You picked $opt which is option 6" 
        CONTAINER_IMAGE="ubi8-sleipnir-image"
        CONTAINER_NAME="myubi8-sleipnir" 
        break;;
    $((${#options[@]}+1))) echo "Goodbye!";break;;
    *) 
        echo "Invalid option. Try another one.";
        continue;;
    esac
done
#====================
#
# End of: Option Menu
#
#====================

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
    #podman run -it -e DISPLAY="$DISPLAY" --privileged --systemd=true --net=host -v ./:/usr/src:Z -w /usr/src -v ~/.Xauthority:/root/.Xauthority:Z --name=${CONTAINER_NAME} ${CONTAINER_IMAGE} ${DEFAULT_COMMAND}
    
    # Mount current host directory as container:/opt/containers
    # Mount current host ~/code as container:/opt/code
    # Start working directory as container:/opt
    #podman run -it -e DISPLAY="$DISPLAY" --privileged --systemd=true --net=host -v ./:/opt/containers:Z -v ~/code:/opt/code:Z -w /opt -v ~/.Xauthority:/root/.Xauthority:Z --name=${CONTAINER_NAME} ${CONTAINER_IMAGE} ${DEFAULT_COMMAND}
   

     #podman run -it -e DISPLAY="$DISPLAY" --privileged --systemd=true --net=host -v ./:/opt/containers:Z -w /opt -v ~/.Xauthority:/root/.Xauthority:Z --name=${CONTAINER_NAME} ${CONTAINER_IMAGE} ${DEFAULT_COMMAND}
     podman run -it -p 5000:5000/tcp -e DISPLAY="$DISPLAY" --privileged --systemd=true --net=host -v ./:/opt/containers:Z -w /opt -v ~/.Xauthority:/root/.Xauthority:Z --name=${CONTAINER_NAME} ${CONTAINER_IMAGE} ${DEFAULT_COMMAND}
    echo
    exit 2
fi
#====================
#
# End of:  Start Container
#
#====================
