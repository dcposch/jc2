#!/bin/bash
# Sequential modular spine + homogeneous dim test for given t values (one root of H_t mod p).
cd "$(dirname "$0")"
for t in "$@"; do
  q=$((2*t+1)); root=""; prime=""
  for p in 32003 32009 32027 32029 32051 32057 32059 32063 32069 32077 32083 32089 32099; do
    r=$(python3 -c "
t=$t;p=$p;q=2*t+1
for r in range(p):
    if (12*q*q*r*r-12*q*(t+1)*r+(t+1)*(3*t+2))%p==0: print(r); break
")
    if [ -n "$r" ]; then root=$r; prime=$p; break; fi
  done
  [ -z "$root" ] && { echo "t=$t no splitting prime" >> queue_modular.log; continue; }
  tag="t${t}_p${prime}_r${root}"
  python3 laurent_spine.py $t --fibre $root --modp $prime --out ${tag}_rows.txt > ${tag}.sing; rm -f ${tag}_rows.txt
  /usr/bin/time -v Singular -q ${tag}.sing > ${tag}.out 2> ${tag}.err
  echo "$tag spine exit=$? $(grep -c SPINE_OK ${tag}.out)" >> queue_modular.log
  python3 analyze_rows.py $t ${tag}_rows.txt --fibre $root --modp $prime --nmax 400 > an_${tag}.sing
  /usr/bin/time -v Singular -q an_${tag}.sing > an_${tag}.out 2> an_${tag}.err
  echo "$tag analysis exit=$? $(grep -E '^JPLUS t' an_${tag}.out)" >> queue_modular.log
done
