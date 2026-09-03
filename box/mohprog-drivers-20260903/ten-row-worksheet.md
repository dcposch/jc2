# Deterministic ten-row (1)--(13) arithmetic worksheet

Selection rule: all six p.202 printed rows, followed by the lexicographically first excess row at each observed length s=3,4,5, followed by the lexicographically last excess row. The independent 658-row JSON is sorted by `(n,m,M,V)`.

Scope warning: conditions (3) and the actual-realizability content of (4) cannot be checked from an integer tuple. Every `PASS` below is therefore an arithmetic-skeleton pass, not a proof that a polynomial pair exists.

## 1. printed (64,48)

Tuple: `n=64, m=48, M=[-48, 52, 62], V={'2': 3, '3': 3}, s=3`.

(1): `m=-M1`=True; `m<n<=100`=True.  (2): `n mod m=16`; `m∤n`=True; `Ms=n-2=62`=True.

(3): UNVERIFIED premise: J(f,g)=1 and simultaneous degree irreducibility are not tuple-arithmetic properties  
(4): ordered numeric shadow=True; UNVERIFIED: tuple arithmetic cannot prove that these are characteristic data of an actual (f,g).

(5) gcd chain: d2=gcd[64, -48]=16 (True); d3=gcd[64, -48, 52]=4 (True); d4=gcd[64, -48, 52, 62]=2 (True).

(6): `s=3` in [3,5]=True; `d_s=4>=4`=True.

(7) windows:

| r | lower | V_r | upper | strict/weak pass |
|---:|---:|---:|---:|:---:|
| 2 | 4/3 | 3 | 12 | True/True |
| 3 | 2 | 3 | 4 | True/True |

(8) radii (the JSON contains every raw product factor): delta_3=-1 (den 1, 1-delta=2, raw 2/1); delta_2=1/4 (den 4, 1-delta=3/4, raw 24/32); delta_1=9/16 (den 16, 1-delta=7/16, raw 4480/10240).

(8) denominator increments: j=2: den-list=[1], L=1, L*delta=1/4, A=4; j=1: den-list=[1, 4], L=4, L*delta=9/4, A=4.

(9)--(11):

| r/j | Q division | V_j | (10) | (11), multiplier | union |
|:---:|:---|---:|:---:|:---:|:---:|
| 3/2 | 12 = 3*4 + 0 | 3 | True | False, None | True |

(12)/(13): `A1=4, n*=4, m*=3, V2=3`. (12) tests `12 mod A1=0`, `8 mod A1=0` => True. (13) tests `9 mod A1=1`, `11 mod A1=3` => False. p.188 check: `20 mod A1=0`.

Arithmetic-skeleton verdict: **PASS**.

## 2. printed (84,56), M2=64

Tuple: `n=84, m=56, M=[-56, 64, 82], V={'2': 2, '3': 3}, s=3`.

(1): `m=-M1`=True; `m<n<=100`=True.  (2): `n mod m=28`; `m∤n`=True; `Ms=n-2=82`=True.

(3): UNVERIFIED premise: J(f,g)=1 and simultaneous degree irreducibility are not tuple-arithmetic properties  
(4): ordered numeric shadow=True; UNVERIFIED: tuple arithmetic cannot prove that these are characteristic data of an actual (f,g).

(5) gcd chain: d2=gcd[84, -56]=28 (True); d3=gcd[84, -56, 64]=4 (True); d4=gcd[84, -56, 64, 82]=2 (True).

(6): `s=3` in [3,5]=True; `d_s=4>=4`=True.

(7) windows:

| r | lower | V_r | upper | strict/weak pass |
|---:|---:|---:|---:|:---:|
| 2 | 7/5 | 2 | 21 | True/True |
| 3 | 2 | 3 | 4 | True/True |

(8) radii (the JSON contains every raw product factor): delta_3=-1 (den 1, 1-delta=2, raw 2/1); delta_2=2/7 (den 7, 1-delta=5/7, raw 40/56); delta_1=16/21 (den 21, 1-delta=5/21, raw 3360/14112).

(8) denominator increments: j=2: den-list=[1], L=1, L*delta=2/7, A=7; j=1: den-list=[1, 7], L=7, L*delta=16/3, A=3.

(9)--(11):

| r/j | Q division | V_j | (10) | (11), multiplier | union |
|:---:|:---|---:|:---:|:---:|:---:|
| 3/2 | 21 = 3*7 + 0 | 2 | True | False, None | True |

(12)/(13): `A1=3, n*=3, m*=2, V2=2`. (12) tests `6 mod A1=0`, `3 mod A1=0` => True. (13) tests `4 mod A1=1`, `5 mod A1=2` => False. p.188 check: `9 mod A1=0`.

Arithmetic-skeleton verdict: **PASS**.

## 3. printed (84,56), M2=72

Tuple: `n=84, m=56, M=[-56, 72, 82], V={'2': 5, '3': 3}, s=3`.

(1): `m=-M1`=True; `m<n<=100`=True.  (2): `n mod m=28`; `m∤n`=True; `Ms=n-2=82`=True.

(3): UNVERIFIED premise: J(f,g)=1 and simultaneous degree irreducibility are not tuple-arithmetic properties  
(4): ordered numeric shadow=True; UNVERIFIED: tuple arithmetic cannot prove that these are characteristic data of an actual (f,g).

(5) gcd chain: d2=gcd[84, -56]=28 (True); d3=gcd[84, -56, 72]=4 (True); d4=gcd[84, -56, 72, 82]=2 (True).

(6): `s=3` in [3,5]=True; `d_s=4>=4`=True.

(7) windows:

| r | lower | V_r | upper | strict/weak pass |
|---:|---:|---:|---:|:---:|
| 2 | 7/3 | 5 | 21 | True/True |
| 3 | 2 | 3 | 4 | True/True |

(8) radii (the JSON contains every raw product factor): delta_3=-1 (den 1, 1-delta=2, raw 2/1); delta_2=1/4 (den 4, 1-delta=3/4, raw 24/32); delta_1=7/12 (den 12, 1-delta=5/12, raw 8960/21504).

(8) denominator increments: j=2: den-list=[1], L=1, L*delta=1/4, A=4; j=1: den-list=[1, 4], L=4, L*delta=7/3, A=3.

(9)--(11):

| r/j | Q division | V_j | (10) | (11), multiplier | union |
|:---:|:---|---:|:---:|:---:|:---:|
| 3/2 | 21 = 5*4 + 1 | 5 | True | True, 1 | True |

(12)/(13): `A1=3, n*=3, m*=2, V2=5`. (12) tests `15 mod A1=0`, `9 mod A1=0` => True. (13) tests `10 mod A1=1`, `14 mod A1=2` => False. p.188 check: `24 mod A1=0`.

Arithmetic-skeleton verdict: **PASS**.

## 4. printed (75,50), V2=3

Tuple: `n=75, m=50, M=[-50, 55, 73], V={'2': 3, '3': 4}, s=3`.

(1): `m=-M1`=True; `m<n<=100`=True.  (2): `n mod m=25`; `m∤n`=True; `Ms=n-2=73`=True.

(3): UNVERIFIED premise: J(f,g)=1 and simultaneous degree irreducibility are not tuple-arithmetic properties  
(4): ordered numeric shadow=True; UNVERIFIED: tuple arithmetic cannot prove that these are characteristic data of an actual (f,g).

(5) gcd chain: d2=gcd[75, -50]=25 (True); d3=gcd[75, -50, 55]=5 (True); d4=gcd[75, -50, 55, 73]=1 (True).

(6): `s=3` in [3,5]=True; `d_s=5>=4`=True.

(7) windows:

| r | lower | V_r | upper | strict/weak pass |
|---:|---:|---:|---:|:---:|
| 2 | 5/4 | 3 | 20 | True/True |
| 3 | 5/2 | 4 | 5 | True/True |

(8) radii (the JSON contains every raw product factor): delta_3=-1 (den 1, 1-delta=2, raw 2/1); delta_2=1/5 (den 5, 1-delta=4/5, raw 60/75); delta_1=1/2 (den 2, 1-delta=1/2, raw 13125/26250).

(8) denominator increments: j=2: den-list=[1], L=1, L*delta=1/5, A=5; j=1: den-list=[1, 5], L=5, L*delta=5/2, A=2.

(9)--(11):

| r/j | Q division | V_j | (10) | (11), multiplier | union |
|:---:|:---|---:|:---:|:---:|:---:|
| 3/2 | 20 = 4*5 + 0 | 3 | True | False, None | True |

(12)/(13): `A1=2, n*=3, m*=2, V2=3`. (12) tests `9 mod A1=1`, `5 mod A1=1` => False. (13) tests `6 mod A1=0`, `8 mod A1=0` => True. p.188 check: `14 mod A1=0`.

Arithmetic-skeleton verdict: **PASS**.

## 5. printed (75,50), V2=2

Tuple: `n=75, m=50, M=[-50, 55, 73], V={'2': 2, '3': 4}, s=3`.

(1): `m=-M1`=True; `m<n<=100`=True.  (2): `n mod m=25`; `m∤n`=True; `Ms=n-2=73`=True.

(3): UNVERIFIED premise: J(f,g)=1 and simultaneous degree irreducibility are not tuple-arithmetic properties  
(4): ordered numeric shadow=True; UNVERIFIED: tuple arithmetic cannot prove that these are characteristic data of an actual (f,g).

(5) gcd chain: d2=gcd[75, -50]=25 (True); d3=gcd[75, -50, 55]=5 (True); d4=gcd[75, -50, 55, 73]=1 (True).

(6): `s=3` in [3,5]=True; `d_s=5>=4`=True.

(7) windows:

| r | lower | V_r | upper | strict/weak pass |
|---:|---:|---:|---:|:---:|
| 2 | 5/4 | 2 | 20 | True/True |
| 3 | 5/2 | 4 | 5 | True/True |

(8) radii (the JSON contains every raw product factor): delta_3=-1 (den 1, 1-delta=2, raw 2/1); delta_2=1/5 (den 5, 1-delta=4/5, raw 60/75); delta_1=2/3 (den 3, 1-delta=1/3, raw 5625/16875).

(8) denominator increments: j=2: den-list=[1], L=1, L*delta=1/5, A=5; j=1: den-list=[1, 5], L=5, L*delta=10/3, A=3.

(9)--(11):

| r/j | Q division | V_j | (10) | (11), multiplier | union |
|:---:|:---|---:|:---:|:---:|:---:|
| 3/2 | 20 = 4*5 + 0 | 2 | True | False, None | True |

(12)/(13): `A1=3, n*=3, m*=2, V2=2`. (12) tests `6 mod A1=0`, `3 mod A1=0` => True. (13) tests `4 mod A1=1`, `5 mod A1=2` => False. p.188 check: `9 mod A1=0`.

Arithmetic-skeleton verdict: **PASS**.

## 6. printed (99,66)

Tuple: `n=99, m=66, M=[-66, 77, 97], V={'2': 8, '3': 8}, s=3`.

(1): `m=-M1`=True; `m<n<=100`=True.  (2): `n mod m=33`; `m∤n`=True; `Ms=n-2=97`=True.

(3): UNVERIFIED premise: J(f,g)=1 and simultaneous degree irreducibility are not tuple-arithmetic properties  
(4): ordered numeric shadow=True; UNVERIFIED: tuple arithmetic cannot prove that these are characteristic data of an actual (f,g).

(5) gcd chain: d2=gcd[99, -66]=33 (True); d3=gcd[99, -66, 77]=11 (True); d4=gcd[99, -66, 77, 97]=1 (True).

(6): `s=3` in [3,5]=True; `d_s=11>=4`=True.

(7) windows:

| r | lower | V_r | upper | strict/weak pass |
|---:|---:|---:|---:|:---:|
| 2 | 3/2 | 8 | 24 | True/True |
| 3 | 11/2 | 8 | 11 | True/True |

(8) radii (the JSON contains every raw product factor): delta_3=-1 (den 1, 1-delta=2, raw 2/1); delta_2=1/3 (den 3, 1-delta=2/3, raw 110/165); delta_1=4/9 (den 9, 1-delta=5/9, raw 117975/212355).

(8) denominator increments: j=2: den-list=[1], L=1, L*delta=1/3, A=3; j=1: den-list=[1, 3], L=3, L*delta=4/3, A=3.

(9)--(11):

| r/j | Q division | V_j | (10) | (11), multiplier | union |
|:---:|:---|---:|:---:|:---:|:---:|
| 3/2 | 24 = 8*3 + 0 | 8 | True | False, None | True |

(12)/(13): `A1=3, n*=3, m*=2, V2=8`. (12) tests `24 mod A1=0`, `15 mod A1=0` => True. (13) tests `16 mod A1=1`, `23 mod A1=2` => False. p.188 check: `39 mod A1=0`.

Arithmetic-skeleton verdict: **PASS**.

## 7. first lexicographic excess with s=3

Tuple: `n=36, m=24, M=[-24, 16, 34], V={'2': 1, '3': 3}, s=3`.

(1): `m=-M1`=True; `m<n<=100`=True.  (2): `n mod m=12`; `m∤n`=True; `Ms=n-2=34`=True.

(3): UNVERIFIED premise: J(f,g)=1 and simultaneous degree irreducibility are not tuple-arithmetic properties  
(4): ordered numeric shadow=True; UNVERIFIED: tuple arithmetic cannot prove that these are characteristic data of an actual (f,g).

(5) gcd chain: d2=gcd[36, -24]=12 (True); d3=gcd[36, -24, 16]=4 (True); d4=gcd[36, -24, 16, 34]=2 (True).

(6): `s=3` in [3,5]=True; `d_s=4>=4`=True.

(7) windows:

| r | lower | V_r | upper | strict/weak pass |
|---:|---:|---:|---:|:---:|
| 2 | 3/5 | 1 | 9 | True/True |
| 3 | 2 | 3 | 4 | True/True |

(8) radii (the JSON contains every raw product factor): delta_3=-1 (den 1, 1-delta=2, raw 2/1); delta_2=2/7 (den 7, 1-delta=5/7, raw 40/56); delta_1=9/14 (den 14, 1-delta=5/14, raw 960/2688).

(8) denominator increments: j=2: den-list=[1], L=1, L*delta=2/7, A=7; j=1: den-list=[1, 7], L=7, L*delta=9/2, A=2.

(9)--(11):

| r/j | Q division | V_j | (10) | (11), multiplier | union |
|:---:|:---|---:|:---:|:---:|:---:|
| 3/2 | 9 = 1*7 + 2 | 1 | True | False, None | True |

(12)/(13): `A1=2, n*=3, m*=2, V2=1`. (12) tests `3 mod A1=1`, `1 mod A1=1` => False. (13) tests `2 mod A1=0`, `2 mod A1=0` => True. p.188 check: `4 mod A1=0`.

Arithmetic-skeleton verdict: **PASS**.

## 8. first lexicographic excess with s=4

Tuple: `n=48, m=32, M=[-32, -8, 36, 46], V={'2': 2, '3': 1, '4': 3}, s=4`.

(1): `m=-M1`=True; `m<n<=100`=True.  (2): `n mod m=16`; `m∤n`=True; `Ms=n-2=46`=True.

(3): UNVERIFIED premise: J(f,g)=1 and simultaneous degree irreducibility are not tuple-arithmetic properties  
(4): ordered numeric shadow=True; UNVERIFIED: tuple arithmetic cannot prove that these are characteristic data of an actual (f,g).

(5) gcd chain: d2=gcd[48, -32]=16 (True); d3=gcd[48, -32, -8]=8 (True); d4=gcd[48, -32, -8, 36]=4 (True); d5=gcd[48, -32, -8, 36, 46]=2 (True).

(6): `s=4` in [3,5]=True; `d_s=4>=4`=True.

(7) windows:

| r | lower | V_r | upper | strict/weak pass |
|---:|---:|---:|---:|:---:|
| 2 | 2/7 | 2 | 2 | True/True |
| 3 | 2/3 | 1 | 6 | True/True |
| 4 | 2 | 3 | 4 | True/True |

(8) radii (the JSON contains every raw product factor): delta_4=-1 (den 1, 1-delta=2, raw 2/1); delta_3=1/4 (den 4, 1-delta=3/4, raw 24/32); delta_2=17/24 (den 24, 1-delta=7/24, raw 448/1536); delta_1=13/18 (den 18, 1-delta=5/18, raw 61440/221184).

(8) denominator increments: j=3: den-list=[1], L=1, L*delta=1/4, A=4; j=2: den-list=[1, 4], L=4, L*delta=17/6, A=6; j=1: den-list=[1, 4, 24], L=24, L*delta=52/3, A=3.

(9)--(11):

| r/j | Q division | V_j | (10) | (11), multiplier | union |
|:---:|:---|---:|:---:|:---:|:---:|
| 4/3 | 6 = 1*4 + 2 | 1 | True | False, None | True |
| 3/2 | 2 = 0*6 + 2 | 2 | False | True, 0 | True |

(12)/(13): `A1=3, n*=3, m*=2, V2=2`. (12) tests `6 mod A1=0`, `3 mod A1=0` => True. (13) tests `4 mod A1=1`, `5 mod A1=2` => False. p.188 check: `9 mod A1=0`.

Arithmetic-skeleton verdict: **PASS**.

## 9. first lexicographic excess with s=5

Tuple: `n=96, m=64, M=[-64, -48, -8, 4, 94], V={'2': 24, '3': 12, '4': 6, '5': 3}, s=5`.

(1): `m=-M1`=True; `m<n<=100`=True.  (2): `n mod m=32`; `m∤n`=True; `Ms=n-2=94`=True.

(3): UNVERIFIED premise: J(f,g)=1 and simultaneous degree irreducibility are not tuple-arithmetic properties  
(4): ordered numeric shadow=True; UNVERIFIED: tuple arithmetic cannot prove that these are characteristic data of an actual (f,g).

(5) gcd chain: d2=gcd[96, -64]=32 (True); d3=gcd[96, -64, -48]=16 (True); d4=gcd[96, -64, -48, -8]=8 (True); d5=gcd[96, -64, -48, -8, 4]=4 (True); d6=gcd[96, -64, -48, -8, 4, 94]=2 (True).

(6): `s=5` in [3,5]=True; `d_s=4>=4`=True.

(7) windows:

| r | lower | V_r | upper | strict/weak pass |
|---:|---:|---:|---:|:---:|
| 2 | 2/9 | 24 | 24 | True/True |
| 3 | 2/13 | 12 | 12 | True/True |
| 4 | 2/23 | 6 | 6 | True/True |
| 5 | 2 | 3 | 4 | True/True |

(8) radii (the JSON contains every raw product factor): delta_5=-1 (den 1, 1-delta=2, raw 2/1); delta_4=11/34 (den 34, 1-delta=23/34, raw 184/272); delta_3=25/77 (den 77, 1-delta=52/77, raw 113152/167552); delta_2=35/107 (den 107, 1-delta=72/107, raw 193019904/286849024); delta_1=39/119 (den 119, 1-delta=80/119, raw 734333501440/1092321083392).

(8) denominator increments: j=4: den-list=[1], L=1, L*delta=11/34, A=34; j=3: den-list=[1, 34], L=34, L*delta=850/77, A=77; j=2: den-list=[1, 34, 77], L=2618, L*delta=91630/107, A=107; j=1: den-list=[1, 34, 77, 107], L=280126, L*delta=91806, A=1.

(9)--(11):

| r/j | Q division | V_j | (10) | (11), multiplier | union |
|:---:|:---|---:|:---:|:---:|:---:|
| 5/4 | 6 = 0*34 + 6 | 6 | False | True, 0 | True |
| 4/3 | 12 = 0*77 + 12 | 12 | False | True, 0 | True |
| 3/2 | 24 = 0*107 + 24 | 24 | False | True, 0 | True |

(12)/(13): `A1=1, n*=3, m*=2, V2=24`. (12) tests `72 mod A1=0`, `47 mod A1=0` => True. (13) tests `48 mod A1=0`, `71 mod A1=0` => True. p.188 check: `119 mod A1=0`.

Arithmetic-skeleton verdict: **PASS**.

## 10. last lexicographic excess

Tuple: `n=100, m=80, M=[-80, 85, 98], V={'2': 5, '3': 4}, s=3`.

(1): `m=-M1`=True; `m<n<=100`=True.  (2): `n mod m=20`; `m∤n`=True; `Ms=n-2=98`=True.

(3): UNVERIFIED premise: J(f,g)=1 and simultaneous degree irreducibility are not tuple-arithmetic properties  
(4): ordered numeric shadow=True; UNVERIFIED: tuple arithmetic cannot prove that these are characteristic data of an actual (f,g).

(5) gcd chain: d2=gcd[100, -80]=20 (True); d3=gcd[100, -80, 85]=5 (True); d4=gcd[100, -80, 85, 98]=1 (True).

(6): `s=3` in [3,5]=True; `d_s=5>=4`=True.

(7) windows:

| r | lower | V_r | upper | strict/weak pass |
|---:|---:|---:|---:|:---:|
| 2 | 4/3 | 5 | 16 | True/True |
| 3 | 5/2 | 4 | 5 | True/True |

(8) radii (the JSON contains every raw product factor): delta_3=-1 (den 1, 1-delta=2, raw 2/1); delta_2=2/11 (den 11, 1-delta=9/11, raw 45/55); delta_1=17/44 (den 44, 1-delta=27/44, raw 29700/48400).

(8) denominator increments: j=2: den-list=[1], L=1, L*delta=2/11, A=11; j=1: den-list=[1, 11], L=11, L*delta=17/4, A=4.

(9)--(11):

| r/j | Q division | V_j | (10) | (11), multiplier | union |
|:---:|:---|---:|:---:|:---:|:---:|
| 3/2 | 16 = 1*11 + 5 | 5 | False | True, 0 | True |

(12)/(13): `A1=4, n*=5, m*=4, V2=5`. (12) tests `25 mod A1=1`, `19 mod A1=3` => False. (13) tests `20 mod A1=0`, `24 mod A1=0` => True. p.188 check: `44 mod A1=0`.

Arithmetic-skeleton verdict: **PASS**.

