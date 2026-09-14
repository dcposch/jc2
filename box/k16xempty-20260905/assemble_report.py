#!/usr/bin/env python3
"""Assemble the requested report; sealing requires the completed job audit."""
import argparse, hashlib, json, re
from pathlib import Path

ROOT=Path(__file__).resolve().parent
REPORT=ROOT.parent.parent/'xmodel/k16-xempty-astra-20260905.md'

TRANSPORT=r'''For a fixed t, start with the verified identity (5). Let
`e_k=deg_b(a_k)`, with zero coefficient assigned degree zero, and put

```
m=max(4,max_k(e_k+d_k)),
Q_k=Delta^(m-e_k-d_k)*clear(a_k,e_k).
```

Homogenize (5) in b to degree m with independent numerator Y and
denominator Z. This is an identity in k[c,Y,Z]. Substitution
Y=A, Z=Delta is a polynomial ring map, and (3) gives

```
sum Q_k F_k=Delta^(m-4)*H^4.                         (9)
```

Every exponent is nonnegative. The identity is a polynomial identity
before localization, even if its coefficients are retained as finite
arithmetic circuits instead of expanded expressions. The exact t=3
check also expands (9) using the actual A,Delta,H and compares both
sides. The t=4 checker verifies the coefficientwise homogenization,
the actual maps (3), and equality with every saved main row.

The t=3 lift has b-degrees `(3,3,4,4,4)` and the t=4 lift has
`(0,0,4,4,4,4,4)`. Both have m=6. Consequently the literal main unit
certificate at these indices is

```
1=sum_k u^4*Delta^2*Q_k*F_k
  +(1-u*Delta*H)*sum_(j=0)^3 (u*Delta*H)^j.           (10)
```

For t=5 the determinant circuit has homogeneous source coefficients
and m may safely be taken as 7, whether or not an individual zero
coefficient could lower its actual b degree. The same proof gives
`sum Q_k F_k=Delta^3*H^4`; its main multiplier is `u^4*Delta`.
The selected rows are E5,...,E10, all quadratic in b; the selected
cofactor monomials have b degree at most five. The matrix circuit,
recorded row scalings, and coefficient-clearing operator specify every
cofactor in this certificate exactly. Its only scalar division is
by the proven nonzero exact determinant.

For the boundary use `eta-B=A-b*Delta`. Directly in the actual
coefficient ring,

```
B^4=(B*eta)^2-B^2*(eta+B)*(A-b*Delta).
```

Thus the following is a literal unit certificate in k[c,b,s]:

```
1=sum_k s^4*a_k*E_k
  -s^4*B^2*(eta+B)*A
  +s^4*B^2*(eta+B)*b*Delta
  +(1+s*B+(s*B)^2+(s*B)^3)*(1-s*B).                 (11)
```

Here eta is its saved polynomial in c,b, not an extra generator.
This covers the whole Delta=0 branch, including N=sigma=0 and all
root collisions. `transport_certificates.py` and the separate t=5
rank circuit give the exact source and generator-image checks.

There is also a uniform transport lemma without imposing n=2.
If `T^n=sum a_k E_k`, choose homogeneous cofactors of weight
`n(4t+1)-(4t+2-k)`. Then

```
e_k+d_k <= floor(n(4t+1)/(t+1)) < 4n.
```

With `m=max(2n,max(e_k+d_k))`, clearing gives
`sum Q_kF_k=Delta^(m-2n)H^(2n)`. Multiplying by
`u^(2n)Delta^(4n-m)` and adding the geometric-series multiple of
`1-uDeltaH` gives 1. On the boundary use

```
B^(2n)-T^n=B^n*(bDelta-A)*sum_(j=0)^(n-1) B^(n-1-j)*eta^j
```

and the length-2n geometric series for sB. These are all-t conversion
identities conditional on a source radical certificate. They do not
supply the missing n or a_k. This distinction is the uniform residual.
'''

BOUNDARY=r'''The weights of the four coefficients are

```
wt(M)=2t+1, wt(N)=t, wt(rho)=2t, wt(sigma)=t-1.
```

Therefore H is homogeneous of weight 3t, though Delta and A are
inhomogeneous. Before any terminal row is imposed,

```
H=N*eta-B*sigma.
```

On X, where B=eta is a unit, this becomes `H=B*Delta` and the slice
equation gives `A=b*Delta`. Consequently the complementary closed
piece is exactly V(H) in X, scheme-theoretically; the main piece is
D(H). Under U=G_m x X, homogeneity multiplies H by the unit v^(3t),
so these are the corresponding pieces of the localized homogeneous
cone as well. In particular

```
X_main=empty     <=> T*H in radical(J),
X_boundary=empty <=> T in radical(J+(H)).             (12)
```

This is a useful uniform reformulation, not an assertion that either
radical membership is automatic. It has an exact gluing rule. If
`(T*H)^r in J` and `T^s=H*L mod J`, then

```
T^(r(s+1))=T^r*(T^s)^r=T^r*H^r*L^r=0 mod J.
```

Thus any two branch certificates yield a certificate for T itself.
No r or s uniform in t was found.

The boundary is not a defective normalization. With C held fixed,
`partial_b(B/eta)=H/eta^2`; this is an ambient derivative, not a
vector field proved tangent to V(J). Let
`D_c=sum j*c_j*partial_(c_j)`. The weight identities give

```
D_c Delta=N+(t-1)Delta,
D_c A=-M+2t*A,
D_c(B-eta)=B modulo (Delta,A).
```

The last quantity is a unit on the boundary. Vanishing of the
b-direction derivative therefore does not make the full slice singular
or contradict its scaling transversality. It does not identify a
repeated-root stratum of C either.

An exact negative control at t=3 shows that the decoupled boundary
`(Delta,A,1-sB)` is NONUNIT of dimension one; imposing b=0 leaves
a NONUNIT scheme of length four. These standard bases were computed
over Q(d), 3d^2=4. There is an explicit algebraic description. Set
`c1=a`, `c2=a^2*z` and write

```
M=a^7*m(z), N=a^3*n(z), rho=a^6*r(z), sigma=a^2*sigma0(z),
H=a^9*h(z), h=n*r-m*sigma0.
```

The exact h is a squarefree quartic, and
`gcd(h,m*n*r*sigma0)=1`. For any of its roots z, choose

```
a=sigma0(z)/n(z), c1=a, c2=a^2*z, b=0,
s=1/(a^7*m(z)).
```

All denominators are nonzero and the decoupled equations hold.
The terminal E rows are essential to empty this branch. The raw
coefficient data, exact gcd checks, and dimensions are saved in
`boundary_structure_t3.sing` and its completed log.

The other proposed shortcut, reusing the first descent as a Keller
descent, also fails a literal hypothesis. The frozen reconstruction
gives

```
Jac_(h,x)(Q,P)=tau+c*b1*x+c*b2*x^2+c*b3*x^3-c*(h-b4)*x^4,
c=-yg.
```

Its h*x^4 coefficient is a scalar unit. Even when tau is invertible,
this is not a constant Jacobian on the plane. The other marked chart
has a nonzero linear Jacobian form; a change to a monomial-Jacobian
object does not restore the original constant-Jacobian source theorem.
A second descent would need an actual closed marked category, a
polynomial coefficient map, preservation of the inherited data, and a
strict decrease within that category. The equations Delta=A=0 supply
none of those missing arrows. The next section checks a concrete
degree-lowering substitution directly.
'''

OPS=r'''The fresh direct reconstruction and chart emission can be replayed by
running the frozen emitter with `t --raw-only --root
box/k16xempty-20260905`, then `emit_charts.py t`, then the emitted
Singular scripts. All exact coefficient fields and ring orders are
written in those scripts. For the completed literal certificates use:

```
stdbuf -oL python3 box/k16xempty-20260905/audit_t2.py
stdbuf -oL python3 box/k16xempty-20260905/transport_certificates.py 3 --run --expand-main
stdbuf -oL python3 box/k16xempty-20260905/transport_certificates.py 4 --run
stdbuf -oL python3 box/k16xempty-20260905/rank_minor_replay.py
stdbuf -oL python3 box/k16xempty-20260905/t5_rank_chart_circuit.py
```

The t=5 replay starts from the exact raw source rows, reconstructs the
complete weighted monomial basis and listed minor, checks the rational
field map and all denominators, and recomputes its determinant with a
different elimination implementation. The determinant/adjugate circuit
then gives both literal units; its full specification is
`t5_rank_chart_circuit.json`. The additional t=5 rational solve and
exact matrix-product check succeeded in about 587 seconds. Its expanded
source-cofactor file is 200,267,594 bytes. The optional fresh Singular
expansion hit its 600-second cap, returned 124, and was reaped; it is
typed INCONCLUSIVE_TIMEOUT. No t=5 expanded-source PASS is claimed.
The independently checked minor and exact adjugate circuit are the
accepted, complete t=5 proof.

Rejected or incomplete jobs are retained with their actual scope.
The naive exact t=3 main GB timed out at 180 seconds and the t=4
boundary GB at 300 seconds. Neither timeout was read as nonemptiness.
Local larger exact jobs were stopped and reaped before moving them
to the permitted workers. Fleet t=4 module lifting was stopped after
the separate exact linear certificate succeeded; fleet t=5 full-cone
GB was stopped after the independently replayed determinant certificate
succeeded. Neither produced an accepted basis. No msolve success string
or modular inverse-chart UNIT is part of the proof.

CAS processes ran in the foreground under stdbuf and fixed timeouts;
long Singular jobs set CPU, thread, and FLINT-thread flags to one,
and the linear-algebra processes were restricted to one thread. The lane stayed
within five CAS cores across the local machine and fleet. Only the
permitted workers 172.30.0.7 and 172.30.0.18 were used. The separate
same-model checks cover arithmetic and maps; they are not a
different-model campaign promotion vote. No task was left running at
sealing. Final job status, accepted-result hashes, source links,
and the artifact manifest are banked beside the report.
'''

def subset(text,begin,end):
    return text[text.index(begin):text.index(end)].strip()

def build():
    body=(ROOT/'report-prefix.md').read_text()
    body=body.replace('**Final verdict placeholder: finite chart certificates are being completed;\nuniform emptiness is OPEN. This draft is not sealed.**',
       '**VERDICT: PROVED for t=2,3,4,5, on every field factor; the all-t\n+emptiness assertion remains OPEN. Both literal charts at t=3,4,5 are\n+unit in characteristic zero. No whole-ray theorem (T) is promoted.**'.replace('\n+','\n'))
    table='''| t / factor | source certificate | X_main | X_boundary |
|---|---|---|---|
| 2, d=-1 | exact Q identity for T | UNIT | UNIT |
| 2, d=+1 | exact Q identity for T | UNIT | UNIT |
| 3, 3d^2=4 | exact source cofactors for T^2, expanded main replay | UNIT | UNIT |
| 4, 3d^2=5 | exact rational block solve and independent polynomial replay | UNIT | UNIT |
| 5, 3d^2=6 | exact full-rank minor, independent model/determinant replay, adjugate circuit | UNIT | UNIT |
'''
    body=body.replace('FINITE_RESULT_TABLE',table)
    body=body.replace('RANK_AUDIT_RESULT','''The producer used FLINT to obtain (6). The independent replay began
with a new Singular coefficient export from `controls_t5_raw.sing`,
parsed the rational field coefficients separately, checked all 1792
weight-42 monomials and all selected multiplier weights, and rebuilt
the integral matrix from scratch. NumPy integer Gaussian elimination
with row pivoting reproduced 29155. All raw denominators are p-units.
The accepted result is `INDEPENDENT_T5_RANK_MODEL_AND_DETERMINANT_PASS`
in `t5_rank_independent_result.json`. Thus (6) is a checked minor of
the stated characteristic-zero coefficient matrix, not a rank from
an unmatched modular presentation.''')
    body=body.replace('CERTIFICATE_TRANSPORT',TRANSPORT.strip())
    body=body.replace('BOUNDARY_STRUCTURE',BOUNDARY.strip())
    note=(ROOT/'uniform-notes.md').read_text()
    pieces=[subset(note,'## 2. A t-independent','## 3. Why'),subset(note,'## 3. Why','## 4. Local'),subset(note,'## 6. Global','## 7. Precise')]
    pieces=[re.sub(r'^(##+) ',lambda m:'#'+m[1]+' ',p,flags=re.M) for p in pieces]
    pieces[0]=pieces[0].replace('### 2.','### 7.1.',1)
    pieces[1]=pieces[1].replace('### 3.','### 7.2.',1)
    pieces[2]=pieces[2].replace('### 6.','### 7.3.',1)
    body=body.replace('UNIFORM_STRUCTURE','\n\n'.join(pieces))
    body=body.replace('OPERATIONAL_RECORD',OPS.strip())
    return body.rstrip()+'\n'

def main():
    p=argparse.ArgumentParser();p.add_argument('--seal',action='store_true');a=p.parse_args()
    body=build()
    assert '<!-- BODY-END -->' not in body
    if a.seal:
        final=json.loads((ROOT/'final-audit.json').read_text())
        assert final['all_lane_jobs_finished'] and final['accepted_artifacts_pass']
        body+='\n<!-- BODY-END -->\n'
        raw=body.encode()
        body+='\n## Seal\n\n'
        body+='Body includes every byte through the unique standalone body-end marker and its newline.\n\n'
        body+=f'- Body bytes: {len(raw)}.\n- Body SHA-256: `{hashlib.sha256(raw).hexdigest()}`.\n'
        body+='- Frozen basis: `5a378d76e1b5c1b0728412715eeb45d7b0370176`.\n'
    assert 20000<=len(body.encode())<=40000,len(body.encode())
    REPORT.write_text(body)
    print(json.dumps({'path':str(REPORT),'bytes':len(body.encode()),'sealed':a.seal}))

if __name__=='__main__':main()
