# TD6 fixed-A3 q2-beta `C=-5U^2,V=0` source reconstruction (V73K)

Frozen status: **dual-AWS producer-exact on `D(U)`; hostile review
pending.**

In the fixed source-typed normalized A3 section with
`q_beta=t+beta*t^2+t^25` and direct
`q_beta'=1+2 beta t+25 t^24`, the previous-stage dependent row
`('X-1',11)` has a beta-independent residual whose exact coordinate
numerators have only factor `U`, with no residual denominator and inverse
denominator only `U`.  The normalized residual is the unit `-1` on `D(U)`.

The certificate reconstructs all twelve load-bearing original previous rows
`('X-1',d)`, `0<=d<=11`, with the hash-pinned parent compiler; the degree-11
direct-q-prime contribution is the full `4*beta*f2[10]`.  Their left-null
combination is reduced through the first-stage echelon and lifted to thirteen
original first rows.  V73K performs one complete direct convolution of the
stored previous-plus-first relation against those original rows and obtains
the raw target `-residual`; exact scalar normalization gives `-1`.

Omission, plus-one, and wrong-row controls are certified by exact nonzero
deltas in the integral polynomial domain, using a lexicographic monomial
order on exponent vectors and an explicitly nonzero leading-coefficient
product.  The complete numerator/denominator and source-leaf ledgers charge
only `U`.  A separate full direct-q-prime omission run is retained as a
source-support control; it is not the theorem run.

The dual theorem runs are byte-identical after removing only hostname, run
tag, and absolute artifact-path lines.  Their four theorem artifacts are
byte-identical.  Run `python3 verify.py` for the lightweight custody and
marker audit.  The portable source archive itself must be executed only on a
registered AWS/Linux host.

Exact scope: `V=0,C=-5U^2,D(U)` for all beta in this fixed source-typed A3
q2-beta section.  The endpoint `U=0` is not consumed here.  Nothing in this
package implies whole `B3`, whole A3, another TD6 modulus, TD6, SP-2,
landing, or JC2.
