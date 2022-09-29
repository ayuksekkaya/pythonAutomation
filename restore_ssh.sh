#!/bin/bash

# restore SSH keys
KEYS=$(ls /run/ssh/ssh_host_* | wc -l)
if [ $KEYS -ge 6 ]
  then
    cp -v -a /tmp/ssh/* /target/etc/ssh/
fi
