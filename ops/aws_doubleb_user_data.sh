#!/bin/bash
set -eux

export DEBIAN_FRONTEND=noninteractive
apt-get update
apt-get install -y singular msolve python3 rsync
install -d -o ubuntu -g ubuntu /home/ubuntu/jc2doubleb
date -u '+%Y-%m-%dT%H:%M:%SZ' > /home/ubuntu/jc2doubleb/BOOTSTRAP_DONE
chown ubuntu:ubuntu /home/ubuntu/jc2doubleb/BOOTSTRAP_DONE
