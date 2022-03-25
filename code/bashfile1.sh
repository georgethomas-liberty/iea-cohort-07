#!/bin/bash
if test $x = 1; then            
    echo "x = 1"                        
else                                     
    echo "x != 1"                        
fi                                          

if grep roads poem; then
    echo "found 'roads'"
fi