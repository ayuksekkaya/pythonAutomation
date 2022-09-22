#!/bin/bash

cs-ansible = /target/var/cs-ansible

curtin in-target --target=/target -- groupadd --gid 777 cs-ansible
curtin in-target --target=/target -- useradd --create-home --home-dir /var/cs-ansible --password '*' --comment 'CoSci Local Ansible User' --gid cs-ansible --shell /bin/bash --uid 777 cs-ansible
mkdir -p /target/var/cs-ansible/.ssh && chmod 700 /target/var/cs-ansible/.ssh && touch /target/var/cs-ansible/.ssh/authorized_keys && chmod 600 /target/var/cs-ansible/.ssh/authorized_keys && echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC7TMIPh6SsGJplxPmlE/scLXn/ojaH99hfIbz4wmGMqL2KGo21E6pk03TAsYEURKSDljvGMNcWESUVjo27spBfs0w6G3JefrcZhp7MYDlwN4RjZ8vU3AE004qJVkXwbWsbVXVmYheUGmRqGamSOBrrnO7UBMKXL+amuzM4RIcnRYy6gJ9/j7Db311r8pK7iYTybj4MHg/ttYReYqUHY1wyfLZWyknlwt04bLOeAJo4iBJ7KjTLSg6SIkJK2GMCsbZxjNzBvwhTHPuORmt8+rD+bP3Evnipsupig2qSh8ZPoTZYvOMOTl4dIsJFWb8YN0YTYK8zAr62pJ1ciUMtRUebdM7OxpH9r1dn9NO64pUqBmfhzO51wgLyZ7BL6Xjdontu//O9SG+IGcxI8GNG1NQtfxV8E/gPlmfbGvrvL4FOsCTVVl1Hfw6s+EBUJnp2lzSKSIPtkJAMlMDNETSU7nnN6HblkNnSc5zvvu2Dnh80GrwgGR3futh+uxxs7t32cF8= root@ansible-control" >> /target/var/cs-ansible/.ssh/authorized_keys && chown -R cs-ansible:cs-ansible /target/var/cs-ansible/.ssh
echo 'cs-ansible    ALL=(root) NOPASSWD: ALL' > /target/etc/sudoers.d/cs-ansible && chmod --reference=/target/etc/sudoers /target/etc/sudoers.d/cs-ansible && chown --reference=/target/etc/sudoers /target/etc/sudoers.d/cs-ansible
