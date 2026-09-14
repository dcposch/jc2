# FIRST final gate (Fable 5.1): exact finite leftover of the r2 infinity-forcing arithmetic

status=UNSEALED (no Seal, no charge_basis authored; adapter seals)
lane=f10-r2-infinity-forcing-final-gate-fable5-20260910
gate_model=claude-fable-5-1
first_action_utc=2026-09-10T11:13:48Z (hash command); stop = earlier of 11:27:48Z (first+14 min) and 11:29:00Z ROOT TERM; final-2-min reserve from 11:25:48Z; never reset
mode=manual mod-89 arithmetic/text/hash only; ZERO CAS/Python/subprocess/scripted arithmetic; tools date, ls, sha256sum, cat, wc, apply_patch only
owned=xmodel/f10-r2-infinity-forcing-final-gate-fable5-20260910.md, box/f10-r2-infinity-forcing-final-gate-fable5-20260910/ (both absent at 11:13:48Z)

## 0. Custody and read scope
All 4 snapshots under /tmp/jc2-lane.NSEJ09/inputs were hashed by sha256sum at 11:13:48Z BEFORE any body read; all 4 equal the charged pins (rows copied from the sha256sum output into box/input_custody.md; no digest typed in this body). Both owned targets absent at 11:13:48Z; skeleton by apply_patch at 11:16:43Z. All four read WHOLE by a single cat each (6397/13721/9432/13520 bytes, nothing clipped, no link followed). Nothing executed, imported or parsed. Premises consumed unchanged from the two FIRST reviews (not re-derived): C=T^3-6T-6, D=T^5-27T^3+39T^2+38T+37, 7a=47, 12b=88, U=-15q so U^2=47q^2, d0=50p, gap 1 zero, A2=(70,46,50)p, V2=(8,41,77,17,25)p, A3=(40,18,15)q, V3=(20,48,8,24,30)q, A4=(52,32)p^2, V4=(55,35,2,32)p^2, the h=5 column (36,77), y=38pq, N, particular (31,3,83), pair (88,80). Operator from produce.py `op`: L_h(A,V)=7CV'-(12-h)C'V+(7-h)AD'-12A'D; forcing W_h=sum_i (7-i)A_iV_{h-i}'-(12-h+i)A_i'V_{h-i}; `upper` solves j=2,1,0 with pivot 7j-3(12-h) against target-forcing starting from `fixed`, pair=([T^1],[T^0]) of op-(target-forcing); psi=base[1]*c1-base[0]*c0=[T^0]_part*[T^1]_var-[T^1]_part*[T^0]_var. All tuples ascending in T, residues mod 89. Derivatives: C'=(-6,0,3)=(83,0,3), D'=(38,78,8,0,5), A2'=(46,11), V2'=(41,65,51,11), A3'=(18,30), V3'=(48,16,72,31), A4'=(32), V4'=(35,4,7). Inverses used: 1/2=45, 1/4=67, 1/9=10, 1/11=81, 1/18=5 (each checked by product =1 mod 89).

## 1. Item 1: all six W5/(pq) coefficients: PASS
Source operator: h=5, i=2 gives (7-2)A2V3'-(12-5+2)A2'V3, i=3 gives (7-3)A3V2'-(12-5+3)A3'V2, i=1,4 vanish with gap 1; so W5/(pq)=5A2V3'-9A2'V3+4A3V2'-10A3'V2 as charged. Convolutions (integer sum, then residue):
- A2V3'=(70,46,50)*(48,16,72,31): 3360->67; 1120+2208=3328->35; 5040+736+2400=8176->77; 2170+3312+800=6282->52; 1426+3600=5026->42; 1550->37. So (67,35,77,52,42,37).
- A2'V3=(46,11)*(20,48,8,24,30): 920->30; 2208+220=2428->25; 368+528=896->6; 1104+88=1192->35; 1380+264=1644->42; 330->63. So (30,25,6,35,42,63).
- A3V2'=(40,18,15)*(41,65,51,11): 1640->38; 2600+738=3338->45; 2040+1170+615=3825->87; 440+918+975=2333->19; 198+765=963->73; 165->76. So (38,45,87,19,73,76).
- A3'V2=(18,30)*(8,41,77,17,25): 144->55; 738+240=978->88; 1386+1230=2616->35; 306+2310=2616->35; 450+510=960->70; 750->38. So (55,88,35,35,70,38).
Combination 5(.)-9(.)+4(.)-10(.): T^0: 335-270+152-550=-333->23; T^1: 175-225+180-880=-750->51; T^2: 385-54+348-350=329->62; T^3: 260-315+76-350=-329->27; T^4: 210-378+292-700=-576->47; T^5: 185-567+304-380=-458->76. W5/(pq)=(23,51,62,27,47,76): all six equal the producer. The T^5 entry 76 also satisfies the resonant row 13+W5_5=0 confirmed by the delta gate. Composition: with these six entries the delta gate's N=-W5-ypart, particular (31,3,83), pair (88,80) and psi=80*36-88*77=-3896->20 now rest on fully replayed inputs; alpha=20.

## 2. Item 2: W6/(p^3) and W6/(q^2): PASS
Source operator at h=6: i=2 gives 5A2V4'-8A2'V4, i=3 gives 4A3V3'-9A3'V3, i=4 gives 3A4V2'-10A4'V2, i=1,5 vanish. p^3 part:
- A2V4'=(70,46,50)*(35,4,7): 2450->47; 280+1610=1890->21; 490+184+1750=2424->21; 322+200=522->77; 350->83. So (47,21,21,77,83).
- A2'V4=(46,11)*(55,35,2,32): 2530->38; 1610+605=2215->79; 92+385=477->32; 1472+22=1494->70; 352->85. So (38,79,32,70,85).
- A4V2'=(52,32)*(41,65,51,11): 2132->85; 3380+1312=4692->64; 2652+2080=4732->15; 572+1632=2204->68; 352->85. So (85,64,15,68,85).
- A4'V2=32*(8,41,77,17,25): 256->78; 1312->66; 2464->61; 544->10; 800->88. So (78,66,61,10,88).
5(.)-8(.)+3(.)-10(.): T^0: 235-304+255-780=-594->29; T^1: 105-632+192-660=-995->73; T^2: 105-256+45-610=-716->85; T^3: 385-560+204-100=-71->18; T^4: 415-680+255-880=-890->0. W6/(p^3)=(29,73,85,18,0): equal (degree at most 4, T^5 absent).
q^2 part:
- A3V3'=(40,18,15)*(48,16,72,31): 1920->51; 640+864=1504->80; 2880+288+720=3888->61; 1240+1296+240=2776->17; 558+1080=1638->36; 465->20. So (51,80,61,17,36,20).
- A3'V3=(18,30)*(20,48,8,24,30): 360->4; 864+600=1464->40; 144+1440=1584->71; 432+240=672->49; 540+720=1260->14; 900->10. So (4,40,71,49,14,10).
4(.)-9(.): T^0: 204-36=168->79; T^1: 320-360=-40->49; T^2: 244-639=-395->50; T^3: 68-441=-373->72; T^4: 144-126=18; T^5: 80-90=-10->79. W6/(q^2)=(79,49,50,72,18,79): equal.

## 3. Item 3: h=6 homogeneous variation, column, particular solves, pairs: PASS
Operator at h=6: 12-h=6, 7-h=1, so L_6(A,V)=7CV'-6C'V+AD'-12A'D; the C'V coefficient is -6 (the value -18 is the j=0 pivot -3(12-h), not an operator coefficient). Expanding for V=v0+v1T+v2T^2 with A=0: 7CV'=-42v1+(-84v2-42v1)T-84v2T^2+7v1T^3+14v2T^4 and -6C'V=36v0+36v1T+(36v2-18v0)T^2-18v1T^3-18v2T^4, so L_hom(V) has T^4: -4v2; T^3: -11v1; T^2: -48v2-18v0; T^1: -84v2-6v1; T^0: 36v0-42v1. Pivots -4,-11,-18 as charged and as 7j-18. For the fixed term fT^3: 7C(3fT^2)-6C'(fT^3)=-126fT^2-90fT^3+3fT^5.
Variation (A_var=1, target 0, no fixed): op=L_hom(V)+D'. T^4: -4v2+5=0, v2=5*67=335->68. T^3: -11v1=0, v1=0. T^2: -18v0-48*68+8=0; 48*68=3264->60, so -18v0=52, v0=-52*5=-260->7. V_var=(7,0,68): equal. Pair: T^1: -84*68+78, 84*68=5712->16, gives 62; T^0: 36*7+38=290->23. Column (62,23): equal.
Particular p^3 (A=0, fixed 0, target-forcing=-(29,73,85,18,0)): T^4: -4v2=0, v2=0. T^3: -11v1=-18, v1=18*81=1458->34. T^2: -18v0=-85, v0=85*5=425->69. V=(69,34,0): equal. Pair: T^1: -6*34+73=-131->47; T^0: -42*34+36*69+29 with 1428->4 and 2484->81 gives -4+81+29=106->17. (47,17): equal.
Particular q^2 (A=0, fixed U^2T^3=47T^3, target -U^2T^5=-47T^5, target-forcing=(-79,-49,-50,-72,-18,-126)=(10,40,39,17,71,52)): fixed contributes 3*47=141->52 at T^5, -90*47=-4230->42 at T^3 (4230->47), -126*47=-5922->41 at T^2 (5922->48). T^5 row: op 52 = target 52, residual 0, i.e. 3U^2+W6_5=-U^2 with W6_5=79=-4U^2 (the theta5 control; dropping the fixed term would leave residual -4U^2 at T^5 and `upper` would raise). T^4: -4v2=71, v2=-71*67: -71=18, 18*67=1206->49. T^3: -11v1+42=17, v1=25*81=2025->67. T^2: -18v0-48*49+41=39; 48*49=2352->38, so -18v0=36, v0=-2->87. V=(87,67,49,47): equal. Pair: T^1: -84*49-6*67-40 with 4116->22, 402->46 gives -108->70; T^0: -42*67+36*87-10 with 2814->55, 3132->17 gives -48->41. (70,41): equal.
psi: beta=17*62-47*23=1054-1081=-27->62; gamma=41*62-70*23=2542-1610=932->42. Both equal. Denominators entering items 1-3: only the pivots -4,-11,-18 (and their inverses 67,81,5), all 89-units; no completion inverse, no ell inverse, no H7 inverse enters Psi6 before its own scalar substitution (produce.py forms psi before `value`). The prior column (36,77) and pair (88,80) at h=5 are consumed as FIRST-checked.

## 4. Item 4: verdicts and exactly what is licensed
alpha=20 CONFIRMED, beta=62 CONFIRMED, gamma=42 CONFIRMED as mod-89 residues of the source operators on the FIRST-checked premises; every previously unreplayed entry (six W5, five W6/p^3, six W6/q^2, variation, column, two particular solves, two pairs, two psi products) is now replayed and agrees. The passage from nonzero residue to B-unit is NOT a mod-89 point computation: it is the accepted integral-order/Cramer/field argument (compat section 2, delta gate A): the coefficients live in the (89,Z)-localized torsion-free integral model with all denominators 89-units, a zero element of B cannot specialize to a nonzero residue, and accepted irreducibility of P7 makes nonzero elements of the field B units on every geometric component. The union of the FIRST reviews therefore licenses exactly: on the CLOSED divisor X1=0 of the top-form system H5=alpha*pq, H6=beta*p^3+gamma*q^2, H7=delta*p^2*q (weight-forced shapes, generic geometry consumed, not re-reviewed), there is no geometric common zero on any geometric component of B, since pq=0 and then H6 kills the remaining coordinate. UNKNOWN and untouched: the X1!=0 chart (compat (7) plus the retained fibre (8)), origin-only, the actual 35-dimension, coefficient growth, and the source C/A zero. No global JC2 result. No dependent-row correction is needed: no coefficient failed.

## 5. Timing (honest)
The previous delta run stopped at its own 11:06:18Z first+14 min stop after 623 s of work in which item 4 was not reached; its 'GAP (cap)' wording denotes work not done within its stop, not an exhausted cap. This run: hashes 11:13:48Z, skeleton 11:16:43Z, body before the 11:25:48Z reserve; all arithmetic by hand, never reset.

## Verdicts
| item | verdict |
|---|---|
| 1 W5/(pq)=(23,51,62,27,47,76) from four convolutions | PASS |
| 2 W6/(p^3)=(29,73,85,18,0), W6/(q^2)=(79,49,50,72,18,79) | PASS |
| 3 V_var=(7,0,68), column (62,23), coefficient -6, pivots -4,-11,-18, pairs (47,17),(70,41), beta 62, gamma 42 | PASS |
| 4 alpha 20 / beta 62 / gamma 42 | CONFIRMED / CONFIRMED / CONFIRMED |
REFUTED: nothing. Remaining coefficient list: empty.

## OPEN(S) RAISED
None. No new canonical OPEN; the remaining questions are the pre-existing compat (7)+(8), origin-only and source GAPs. No execution, registration, promotion or follow-on authority is issued.

## COLLISIONS
status: EMPTY

- NONE. Own-only check: this lane wrote exactly xmodel/f10-r2-infinity-forcing-final-gate-fable5-20260910.md and box/f10-r2-infinity-forcing-final-gate-fable5-20260910/input_custody.md, both absent at 11:13:48Z; all writes by apply_patch; no Seal, no charge_basis, no corpus scan, no other lane, no network, no scientific subprocess.

## Completion
Authoring attestation: every byte of both owned files was written by apply_patch; no Write/Edit tool, no shell redirection, no helper, no source edit, no execution, no network. Own WHOLE read of this report and of box/input_custody.md done before the marker with the custody rows rechecked against live sha256sum. The marker below is the only standalone marker in this file and nothing follows it. All writers idle at the marker.

<!-- BODY-END -->
