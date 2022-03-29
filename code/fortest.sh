#!/bin/bash
set -e # exit script on error
for files in "$@"; do

    if [ -e $files ]; then     # -e 'FILE exists'
        if [ -z $files ]; then # -z 'the length of STRING is zero'
            echo 'Please add a file to the end of your command'
        fi
        if [ -s $files ]; then # 'FILE exists and has a size greater than zero'
            echo 'inspected by George Thomas' >>$files
            >/dev/null # 'redirect output to /dev/null'
        else
            rm $files
            echo 'removed empty file '$files''
        fi

    else
        echo 'File '$files' does not exist'
    fi
done
