#!/bin/bash

# **************** Global variables
export HOME_PATH=$(pwd)

# **********************************************************************************
# Functions definition
# **********************************************************************************

function check_podman () {
    ERROR=$(podman ps 2>&1)
    RESULT=$(echo $ERROR | grep 'Cannot' | awk '{print $1;}')
    VERIFY="Cannot"
    if [ "$RESULT" == "$VERIFY" ]; then
        echo "Podman is not running. Stop script execution."
        exit 1 
    fi
}

#**********************************************************************************
# Execution
# *********************************************************************************

echo "************************************"
echo " Build and start containers with Podman compose " 
echo "- 'Postgres'"
echo "************************************"

check_podman

# 1. Load application environment configurations
source ${HOME_PATH}/.env
cd ${HOME_PATH}/../data
echo "$(pwd)"

# 2. Create directories
mkdir postgres
mkdir export

# 3. Set variable without `../..` statements
export POSTGRES_DATA=$(pwd)/postgres
export POSTGRES_EXPORT=$(pwd)/export

echo ${POSTGRES_EXPORT}

cd ${HOME_PATH}

# 3. Start compose
podman-compose version
echo "**************** START ******************" 
podman-compose -f ./podman_compose.yaml up # --detach

#podman-compose -f ./podman_compose.yaml stop