#!/bin/bash
cd /home/ubuntu/jc2/box/k16galois-20260905
./run.sh boundary_t3_exact.sing 300
./run.sh colon_t3_mod_p32003_b0.sing 300
./run.sh colon_t3_exact.sing 900
./run.sh boundary_t5_exact.sing 1500
./run.sh boundary_t4_mod_p32029_b0.sing 300
./run.sh colon_t4_mod_p32029_b0.sing 1200
./run.sh boundary_t6_mod_p32003_b0.sing 900
./run.sh colon_t5_mod_p32009_b0.sing 2400
echo MISC_DESK_DONE
