#!/bin/bash
# Append the exact-run status lines to §3.1, seal the report, hash artifacts.  Run only when no lane job is running.
cd /home/ubuntu/jc2; D=box/k16sq-20260905; R=xmodel/k16-exact-square-fable5-20260905.md
st() { f=$D/$1.out; if [ ! -f $f ]; then echo "not run"; elif grep -q "$2" $f; then echo "completed ($(cat $D/$1.time 2>/dev/null | cut -d' ' -f1-3))"; elif grep -q "exit=124\|status 124" $f $D/$1.time 2>/dev/null; then echo "TIMEOUT ($(cat $D/$1.time 2>/dev/null | cut -d' ' -f1-3))"; else echo "stopped/incomplete"; fi; }
t5w42=$(st t5_truncNL TRUNC_COMPLETE); t5w42_tau2=$(grep -h "TAU2_NF_ZERO" $D/t5_truncNL.out 2>/dev/null | head -1); t5w42_hf=$(grep -h "LAST_NONZERO" $D/t5_truncNL.out 2>/dev/null | head -1)
t6w25=$(st t6_low25 LOW_COMPLETE); t6w25_tau=$(grep -h "TAU_NF_ZERO" $D/t6_low25.out 2>/dev/null | head -1)
cat >> $R <<EOT

**Exact truncated runs, final status.**  `t5_low21` (W=21): completed, 139 s — `tau ∉ I_{5,+}`
exactly, exact H_5(w) for w ≤ 21 equal to the modular values.  `t4_trunc` (W=34): std 20 ms,
lift 0.4 s, verification of the lift product not finished in 15 min (number-field coefficient
size), memberships exact.  `t5_truncNL` (W=42, exact `tau^2` test): ${t5w42} ${t5w42_tau2} ${t5w42_hf}.
`t6_low25` (W=25, exact `tau ∉ I_{6,+}`): ${t6w25} ${t6w25_tau}.  The chained W=36 (t=5) and W=29
(t=7) exact runs were cancelled unstarted: above weight ≈ 21 the exact number-field truncations
(129-digit denominators at t=5) are far slower than the full modular bases, so every exact
`tau^2` membership at t ≥ 5 in this report rests on the semicontinuity argument of §5 (with
the p-integrality of all 2690 exact denominators at t=5 checked: none divisible by 32009).
EOT
echo "" >> $R; echo "<!-- BODY-END -->" >> $R
wc -c $R
( cd $D && sha256sum $(ls | grep -v "^artifacts.sha256$") > artifacts.sha256 ) && wc -l $D/artifacts.sha256
