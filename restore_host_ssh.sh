#!/bin/bash


cp -v -a '/root/ssh_host_keys/'* /etc/ssh/

systemctl disable restore_host_ssh.service 
rm -rf /etc/systemd/system/restore_host_ssh.service
rm -f /root/restore_host_ssh.sh
touch /root/host_keys_restored
