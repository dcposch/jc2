#!/bin/bash
# deploy.sh <host> <files...>  : create the box path on the worker and copy files + run.sh
h="$1"; shift
SSH="ssh -o BatchMode=yes -o ConnectTimeout=8 -i /home/ubuntu/.ssh/jc2-fleet"
$SSH ubuntu@$h "mkdir -p /home/ubuntu/jc2/box/k16galois-20260905"
scp -q -o BatchMode=yes -i /home/ubuntu/.ssh/jc2-fleet run.sh "$@" ubuntu@$h:/home/ubuntu/jc2/box/k16galois-20260905/
