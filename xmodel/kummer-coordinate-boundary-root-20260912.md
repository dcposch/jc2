# Kummer control: a translated-coordinate source boundary

ROOT manual scope check, September12,2026. INTERNAL/UNPROMOTED.
Basis0d39df3c9fd69c939a8420c54d03228b9077777d. Own transaction owns exact
opening time; original reserve02:12/HARD02:15 UTC. The concurrently running
Astra report is NOT an input; no live body, receipt or log was read.

Sole scientific inputs: frozen TASK
box/kummer-weyl-selection-astra-20260912/TASK.md SHA
c3a7b2bda57e8d47f544c81179e0a3aa152353c6f63854a59ed3d5f1ae81f4d7,
read WHOLE; Bass1989 PDF
box/bass-resonant-operators-root-20260911/bass-1989.pdf SHA
86f642941d2cea0f1d438996d8e81833ac53b6039c4c81e1564adc411f614b1e,
printed39--43/PDF2--6 read through pdftotext to stdout. Theorem1.4's
statement and normalization are charged; its full proof is an external
import, not newly verified here. This note needs no proposed Mellin-rank,
regularity, simplicity or no-line conclusion from the TASK.

## 1. Exact coordinate test

Let G(p)=(p-1)(p-2) and take the explicit Weyl module

 M=C[p,G(p)^-1]e tensor_C C[q,(q-1)^-1]f,
 dp(he)=(h'+G'h/(2G))e,
 dq(hf)=(h'+h/(2(q-1)))f.

Set q'=q-1, p'=p-a for ANY a in C, and let
 B'=C[e_p',e_q'], e_p'=(p-a)dp, e_q'=(q-1)dq.
Every m in M has a finite Laurent expansion

 m=sum_(k in I) m_k(p) tensor (q')^k f,
 e_q'((q')^k f)=(k+1/2)(q')^k f.

Consequently the NONZERO polynomial

 P_m(T)=product_(k in I)(T-k-1/2)

kills m after substituting T=e_q'. The empty expansion means m=0 and
is harmless. Thus M is entirely B'-torsion, and Frac(B') tensor_B' M=0.
This is literal tensor localization, not a claim that the old field
C[ep,eq]'s fraction field is unchanged by a coordinate translation.
In particular the section e tensor f is killed by e_q'-1/2.

QUANTITY: whether the explicit module remains Euler-torsion-free after
this translation. CHEAPEST TEST: the displayed diagonal action, manual
minutes, no execution. Answer NO, irrespective of the unfinished fixed-
coordinate rank-two/no-line argument. No stronger all-module theorem is
asserted.

## 2. Why this is an actual-source mismatch

Suppose P,Q in R=C[x,y] are an actual Keller pair, and N=R/C[P,Q].
The polynomial Q-1 is nonconstant, hence a nonunit with a complex zero.
Choose a source point s with Q(s)=1 and put a=P(s). Translate the source
point to its origin and target coordinates to P-a,Q-1. The Jacobian
condition and the subalgebra C[P,Q] are unchanged; these are precisely
normalized coordinates to which the stipulated Bass1.4 applies.

At that conditional theorem tier N is torsion-free over
C[(P-a)partial_P,(Q-1)partial_Q]. Therefore the module in section1 cannot
be this actual N: every one of its sections is torsion and it is nonzero.
The argument does NOT need a missing target point, surjectivity of the
Keller map, or a rank-invariance theorem. It only uses that the fibre
Q=1 is nonempty and that normalization may be done at one of its points.

This also explains why verifying many source-like properties in one
chosen coordinate frame cannot settle source selection. The proposed
control can at most refute an implication from those explicitly verified
fixed-frame properties. It cannot refute the same implication with all
compatible actual-source coordinate normalizations as extra hypotheses.
Neither do those extra hypotheses here prove that an arbitrary nonzero
source has a first-order relation. That implication remains unproved.

## 3. Scope and allocation

The source exclusion of this Kummer module is elementary conditional on
the already imported Bass theorem, not a new properness or JC2 theorem.
No no-Galois-intermediate statement or generic differential-rank claim is
used. Function-field rank, Euler-localized rank and delta-cyclic rank
remain different notions. The original TASK may still provide a useful
stronger abstract control if Astra verifies it; this note prevents that
control from being mistaken for an actual source obstruction.

No canonical OPEN, changed global ranking, second model gate, automatic
countermodel-hardening family, computation or descendant is selected.
The next real proof contribution must use an actual-source condition
and derive a new consequence; simply restoring full Weyl structure is
not itself that contribution. This is an independent manual boundary
attachment only. No scientific process, AWS worker or protected access.

Preseal: own entire partial read back; TASK and PDF postpins equal the
listed inputs. The only deciding calculation is printed above. No new
canonical OPEN or preliminary Astra content is charged. Substantive
work closed02:04UTC, before the original reserve; documentary transaction
and own final/manifest readback remain.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `4678`.
- Body SHA-256:
  `d01ffcd4ca6b7c1e28eb7703ce186890a924b4cba0c4b9562849064f5d07b8cc`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
