#!/bin/bash
set -e # exit script on error

if [ $# = 0 ]; then
    echo "Script was run with no argumentss. try again."
    exit 1
fi

filename=$1

if [ ! -e $filename ]; then
    echo " File does not exist"
    exit 1
fi
