#!/bin/bash
set -e # exit script on error
for files in "$@"; do

    if [ "$@" = 0 ]; then
        echo 'Script was run with no argumentss. try again.'
        exit 1
    fi

    if [ ! -e $files ]; then
        echo 'File '$files' does not exist'
        exit 1
    fi
done
