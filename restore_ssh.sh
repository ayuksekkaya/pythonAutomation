#!/bin/bash

# restore SSH keys
mkdir /target/root/ssh_host_keys/

KEYS=$(ls /run/ssh/ssh_host_* | wc -l)
if [ $KEYS -ge 6 ]
  then
    cp -v -a '/run/ssh/'* /target/root/ssh_host_keys/
fi
