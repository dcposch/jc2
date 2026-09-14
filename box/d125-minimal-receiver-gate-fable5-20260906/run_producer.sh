#!/bin/bash
# producer controls under caps: 30 s wall, 25 s CPU, 512 MiB address space
run() { name=$1; shift; ( ulimit -t 25 -v 524288; /usr/bin/time -f "%e wall %U user %M KB" timeout 30 "$@" ) > "$name.out" 2> "$name.err"; echo "$name exit=$?"; }
run normal python3 producer_check.py
run optO python3 -O producer_check.py
run mut_map python3 producer_check.py --mutate
run mut_face python3 producer_check.py --mutate-face
run mut_map_O python3 -O producer_check.py --mutate
run mut_face_O python3 -O producer_check.py --mutate-face
