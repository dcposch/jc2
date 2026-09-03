# Exact band-6 successor system

Work over (K=\mathbf Q(a)).  Put

\[
L=z+3a,quad H=z^2L,quad D=z^3L^2,quad
W_3=-8z^4-18az^3,quad W_6=28z^5+45az^4.
\]

This setup uses exactly the band-1--5 definitions in `local_band_audit.py`
and its promoted band-5 condition in `band5_component_audit.json`.  More
explicitly,

\[
f_1=H^3U,quad f_2=(U^2+DV)/4,quad
f_3=6H^5W_3+f_3^{new},quad
f_4=\operatorname{tail}f_4+f_4^{new},quad
f_5=\operatorname{tail}f_5+f_5^{new},
\]

where the last two tails are the exact band-1 and band-2 inverse-Omega tails
recorded in `local_band_audit.json`.  Define (q_r=3H^3f_r-2g_r).  For
(r=1,\ldots,5), use the displayed `q2`--`q5` formulas in
`local_band_audit.py` (and (q_1=0)); equivalently
(g_r=(3H^3f_r-q_r)/2).  In particular

\[
g_3^{new}=g_3-9H^8W_3.
\]

The fixed band-6 tails are

\[
\begin{aligned}
\operatorname{tail}f_6={}&6H^5W_6+15H^4W_3^2
-\sum_{k=0}^{14}\alpha_k f^{new}_{3,k}z^{k+1},\\
\operatorname{tail}g_6={}&9H^8W_6+36H^7W_3^2
-\sum_{k=0}^{23}\beta_k[z^k]g_3^{new}z^{k+1},
\end{aligned}
\]

with

\[
\alpha=(6,8,10,13,15,17,19,22,24,26,28,31,33,35,37)
\]

and

\[
\beta=(10,12,14,16,19,21,23,25,28,30,32,34,37,39,41,43,46,48,50,52,55,57,59,61).
\]

Write (f_6=\operatorname{tail}f_6+f_6^{new}),
\(\deg f_6^{new}\le11\), and similarly
\(g_6=\operatorname{tail}g_6+g_6^{new}),
\(\deg g_6^{new}\le20\).  There are (12+21=33) new unknowns.

The exact equation is

\[
E_6=\sum_{r+s=6}\left((18-s)f'_rg_s+(r-12)f_rg'_s\right)=0.
\]

For (q_6=3H^3f_6-2g_6), its new-variable operator is

\[
L_6(q)=2Hq'-12H'q.
\]

On degree at most 20 it has rank 20, kernel (K H^6), 22 quotient rows
(z^1,\ldots,z^{22}), and cokernel dimension two.  After multiplication by
(3H^5), the 27 raw row positions are (z^{11},\ldots,z^{37}).  The full
new-solution kernel therefore has dimension (33-20=13).

An exact differential-jet-verified solution is

\[
\begin{aligned}
q_6={}&-\frac32\frac{f_1f_5+f_2f_4}{H^3}-\frac34\frac{f_3^2}{H^3}
+\frac38\frac{f_1^2f_4}{H^9}+\frac34\frac{f_1f_2f_3}{H^9}
+\frac18\frac{f_2^3}{H^9}\\
&-\frac3{16}\frac{f_1^3f_3}{H^{15}}
-\frac9{32}\frac{f_1^2f_2^2}{H^{15}}
+\frac{15}{128}\frac{f_1^4f_2}{H^{21}}
-\frac7{512}\frac{f_1^6}{H^{27}}\\
&+\frac43b_2H^2f_4+\frac49b_2\frac{f_1f_3}{H^4}
+\frac29b_2\frac{f_2^2}{H^4}
-\frac4{27}b_2\frac{f_1^2f_2}{H^{10}}
+\frac5{243}b_2\frac{f_1^4}{H^{16}}\\
&+\frac76b_4Hf_2+\frac7{72}b_4\frac{f_1^2}{H^5}+b_6H^6.
\end{aligned}
\]

After substituting (f_1=H^3U, f_2=(U^2+z^3L^2V)/4), and writing
(F=f_3,E=f_4,J=f_5,b=b_2), this is

\[
q_6=P_{pol}+\frac{R_6}{124416z^{12}L^5},
\]

where

\[
P_{pol}=-\frac32UJ+\frac43bH^2E+\frac7{18}b_4HU^2
+\frac7{24}b_4z^5L^3V+b_6H^6
\]

and

\[
\begin{aligned}
R_6={}&-93312z^6L^2F^2+55296bz^{10}L^4UF
+23328z^3LUVF-46656z^9L^4VE\\
&+1728bz^{10}L^5V^2-1152bz^7L^3U^2V
+243z^3L^2V^3\\
&-320bz^4LU^4-1458U^2V^2.
\end{aligned}
\]

Thus, in addition to (z^6L^2\mid N_5), the exact band-6 old-parameter
compatibility system is

\[
\boxed{z^{12}L^5\mid R_6}.
\]

It has 17 structurally nonzero CRT remainder rows: 12 jets at (z=0) and
five at (z=-3a).  Formal exact division gives quotient degree at most 29.
All nine apparent high-window coefficients (z^{21},\ldots,z^{29}) of

\[
P_{pol}+R_6/(124416z^{12}L^5)-q_{6,tail}
\]

cancel identically; there are no additional high-window equations.  The
driver verifies these cancellations coefficient-by-coefficient, the compact
(R_6) decomposition, the binomial generating formula, and the independent
differential-jet identity.

Replay:

```sh
python3 band6_exact_setup.py
```
