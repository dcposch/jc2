#!/bin/bash
# Replay batch: modular certificates t=5,6,7 + controls t=2,4, with per-job timeouts.
cd "$(dirname "$0")"
S=./laurent_spine.py; A=./jplus_hom.py; EV=./exact_vs_modular.py
B=../k16terminal-fable5-20260903

spine() { # t fibre modp tag  ; empty modp -> exact/rational
  local t=$1 fb=$2 mp=$3 tag=$4 extra=""
  [ -n "$fb" ] && extra="--fibre $fb"
  [ -n "$mp" ] && extra="$extra --modp $mp"
  python3 $S $t $extra --out ${tag}_rows.txt > ${tag}.sing || return 1
  timeout 1800 Singular -q ${tag}.sing < /dev/null > ${tag}.out 2> ${tag}.err
  echo "SPINE $tag exit=$?"
}
jplus() { # t rowsfile fibre modp tag lim
  local t=$1 rw=$2 fb=$3 mp=$4 tag=$5 lim=$6 extra=""
  [ -n "$fb" ] && extra="--fibre $fb"
  [ -n "$mp" ] && extra="$extra --modp $mp"
  python3 $A $t $rw $extra > an_${tag}.sing || return 1
  timeout $lim Singular -q an_${tag}.sing < /dev/null > an_${tag}.out 2> an_${tag}.err
  echo "JPLUS $tag exit=$?"
}

( # stream 1: t=7 (the long pole)
  spine 7 4425 32059 t7p32059r4425
  python3 $EV 7 $B/t7_rows.txt t7p32059r4425_rows.txt 32059 4425 > ev_t7.sing
  timeout 900 Singular -q ev_t7.sing < /dev/null > ev_t7.out 2> ev_t7.err; echo "EV t7 exit=$?"
  jplus 7 t7p32059r4425_rows.txt 4425 32059 t7p32059r4425 2400
) > s1.log 2>&1 &

( # stream 2: t=5 both roots
  for r in 1821 15639; do
    spine 5 $r 32009 t5p32009r$r
    python3 $EV 5 $B/t5_rows.txt t5p32009r${r}_rows.txt 32009 $r > ev_t5_$r.sing
    timeout 600 Singular -q ev_t5_$r.sing < /dev/null > ev_t5_$r.out 2> ev_t5_$r.err; echo "EV t5 $r exit=$?"
    jplus 5 t5p32009r${r}_rows.txt $r 32009 t5p32009r$r 1800
  done
) > s2.log 2>&1 &

( # stream 3: t=6 certificate, then t=4 exact-vs-modular agreement control
  spine 6 27617 32003 t6p32003r27617
  python3 $EV 6 $B/t6_rows.txt t6p32003r27617_rows.txt 32003 27617 > ev_t6.sing
  timeout 600 Singular -q ev_t6.sing < /dev/null > ev_t6.out 2> ev_t6.err; echo "EV t6 exit=$?"
  jplus 6 t6p32003r27617_rows.txt 27617 32003 t6p32003r27617 1800
  spine 4 "" "" t4exact
  jplus 4 t4exact_rows.txt "" "" t4exact 1800
  for r in 25378 31563; do
    spine 4 $r 32029 t4p32029r$r
    python3 $EV 4 t4exact_rows.txt t4p32029r${r}_rows.txt 32029 $r > ev_t4_$r.sing
    timeout 600 Singular -q ev_t4_$r.sing < /dev/null > ev_t4_$r.out 2> ev_t4_$r.err; echo "EV t4 $r exit=$?"
    jplus 4 t4p32029r${r}_rows.txt $r 32029 t4p32029r$r 1800
  done
) > s3.log 2>&1 &

( # stream 4: t=2 controls (exact both fibres + the modular negative control), t=3 positive control
  for f in 1/5 2/5; do
    g=$(echo $f | tr -d '/')
    spine 2 $f "" t2f$g
    jplus 2 t2f${g}_rows.txt $f "" t2f$g 600
  done
  spine 2 1/5 32003 t2f15p32003
  python3 $EV 2 t2f15_rows.txt t2f15p32003_rows.txt 32003 "19202" > ev_t2.sing
  timeout 300 Singular -q ev_t2.sing < /dev/null > ev_t2.out 2> ev_t2.err; echo "EV t2 exit=$?"
  jplus 2 t2f15p32003_rows.txt 19202 32003 t2f15p32003 600
  spine 3 "" "" t3exact
  jplus 3 t3exact_rows.txt "" "" t3exact 1200
) > s4.log 2>&1 &

wait
echo "=== BATCH DONE ==="
