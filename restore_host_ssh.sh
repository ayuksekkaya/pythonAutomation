#!/bin/bash


KEYS=$(ls /root/ssh_host_keys/ssh_host_* | wc -l)
if [ $KEYS -ge 6 ]
  then
    cp -v -a '/root/ssh_host_keys/'* /etc/ssh/
    systemctl disable restore_host_ssh.service 
    rm -rf /etc/systemd/system/restore_host_ssh.service
    rm -f $0
    touch /root/host_keys_restored
    else
        echo "No old ssh directory found"
fi

lvextend -l +100%FREE /dev/mapper/ubuntu--vg-ubuntu--lv
resize2fs /dev/mapper/ubuntu--vg-ubuntu--lv
