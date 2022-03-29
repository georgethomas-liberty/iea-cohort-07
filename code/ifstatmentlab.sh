#!/bin/bash
if [ -e $1 ]; then     # -e 'FILE exists'
    if [ -z $1 ]; then # -z 'the length of STRING is zero'
        echo 'Please add a file to the end of your command'
    fi
    >/dev/null # 'redirect output to /dev/null'
else
    echo 'File does not exist'
fi
