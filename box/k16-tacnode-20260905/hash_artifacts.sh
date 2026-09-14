#!/bin/bash
# sha256 of every file in the box (excluding this manifest), written to artifacts.sha256
B=/home/ubuntu/jc2/box/k16-tacnode-20260905
cd $B && find . -type f ! -name artifacts.sha256 -print0 | sort -z | xargs -0 sha256sum > artifacts.sha256 && wc -l artifacts.sha256
