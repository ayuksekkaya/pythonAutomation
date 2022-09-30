#!/bin/bash
exec > /target/root/autoinstall.log 2>&1
mkdir -p /run/oldroot
mkdir -p /run/ssh

mount /dev/mapper/ubuntu--vg-ubuntu--lv /run/oldroot/

if [ -d /run/oldroot/etc/ssh ]
  then
    ls /run/oldroot/etc/ssh/
    # Save old SSH keys to RAM filesystem. We will restore them in the %post section
    cp -v -a /run/oldroot/etc/ssh/moduli /run/ssh/
    
    for i in /run/oldroot/etc/ssh/ssh_host_*
    do
       cp -v -a $i /run/ssh/
    done
    echo "Copied old ssh keys to RAM"
  else
    echo "No old ssh directory found"
fi

# clean up
cd /
umount /run/oldroot
