# Source reading notes (Moh 1983, charged PDF; printed page = PDF ordinal + 139)

Pages were rendered from the frozen PDF at 130 dpi into /tmp (not retained) and read
as images; the OCR layer was used only to locate statements.

- p149-150 (PDF 10-11): §2 standing setup. f,g monic in y, deg_y f=m, deg_y g=n, g=eta^{-n},
  f=eta^{-m}+sum_{j>-m} f_j(x) eta^j. "Suppose y in k(x,f,g)". Definitions: d_1=n,
  d_{j+1}=gcd(n,M_1..M_j), M_j=min{i: f_i(x)!=0, d_j does not divide i}, M_{h+1}=inf;
  n_0=1, n_j=d_j/d_{j+1}; q_1=M_1, q_j=M_j-M_{j-1}; lambda_j=sum_{i<=j} q_i d_i;
  mu_j=lambda_j/d_j; theta_j=mu_j-M_j.
- p151 (PDF 12): Lemma 2.1 is an IFF: J(f,g)=c!=0 iff ord_eta(sum f_i(x)eta^i - sum f_i(0)eta^i)=n-1
  and deg_x f_{n-1}=1. Note after proof: under the Jacobian condition all M_i<=n-1, f has n
  conjugates, and y in k(x,f,g) (so the p150 supposition is a consequence of Keller).
  psi: k[x]->k, psi(x)=0.
- p152 (PDF 13): Prop 2.1 (approximate root commutes with psi). e:=ord_eta(sum f_j(x)eta^j-sum f_j(0)eta^j).
  Prop 2.2: M_r<=e => (1) deg_y T_r^psi(f,g)=deg_y T_r(f,g)=-mu_r; M_r<e => (2) both monic in y;
  M_r=e => (3) T_r^psi(f,g)=c f_e(x) y^{-mu_r}+lower in y.
- p153-154 (PDF 14-15): proof; "monic means the coefficient of the highest term is a unit" (p154);
  gcd{n,mu_1..mu_r}=gcd{n,M_1..M_r}; recovery formula
  M_j=(1/(d_j-d_{j+1}))[mu_j d_j - sum_{i<j}(d_i-d_{i+1})M_i].
- p155 (PDF 16): §3 chain rule J_{x,y}(H(f,g),g)=H(f,g)_f * J_{x,y}(f,g) for H in k[f,g];
  the subscript f IS the partial derivative d/df (defined here). Properties (1)-(3);
  restrictions (5) 0<=alpha_i<n_i for i<r, (6) 0<=alpha_r<inf.
- p156 (PDF 17): Lemma 3.1 unique expansion H=sum c_{j,alpha} g^j T_alpha over k[x]; distinct
  alpha give distinct f-degrees.
- p157-159 (PDF 18-20): Prop 3.1: T_{r+1}=T_r^{n_r}+sum c_{j,alpha} g^j T_alpha; for M_r<e and
  c!=0: (1) alpha_r<n_r; (2) deg_y g^j T_alpha(f,g)<=(-mu_r)n_r; unique (j,alpha) attains
  equality and has alpha_r=0. Proof: (10) deg_y T_{r+1}=-mu_{r+1}=(-mu_r)n_r-q_{r+1}<(-mu_r)n_r;
  (11) y-degree of a term = jn+sum(-mu_i)alpha_i; distinct (j,alpha) give distinct y-degrees
  (unit residue of -mu_r/d_{r+1} mod n_r). Remark p159: Prop 3.1 remains valid after psi.
- p159-161 (PDF 20-22): Prop 3.2: (1) T_1(f,g)_f=1; (2) T_{r+1}(f,g)_f=n_r T_r^{n_r-1}T_{r,f}
  + sum C_{i,beta} g^i T_beta with the first term of strictly larger y-degree than every summand;
  (3) deg_y T_{r+1}(f,g)_f=-mu_{r+1}+M_{r+1}=theta_{r+1}. Proof p160-161: (14)
  deg_y g^j T_{alpha^(i)}(T_i)_f=deg_y g^j T_alpha+M_i; case < or =, in the = case alpha_r=0 so
  M_i<M_r. Remark p161: for M_{r+1}<=e one may specialize psi for all i<=r+1; all conclusions valid.
- p166 (PDF 27): Prop 4.3: deg g=deg_y g=n>1 and M_i!=n-2 for all i => top forms of g and T_i^psi
  (M_i<n-2) are powers of one linear form. Proof: delta=min root order; delta>-1 gives tops y^n;
  else delta<=-1, cases M_h<n-2 / M_h=n-1 via Prop 4.2 (Jacobian).
- p169 (PDF 30): Prop 4.5: deg g=deg_y g=n>1, M_r=n-2 for some r => tops of g, T_i (i<r) are
  powers of a common form with at most two distinct linear factors, of different multiplicities.
  Remarks p169/p171: J=x^l variants with (6)*, (3)* shifted by l.
- p170-171 (PDF 31-32): Prop 4.6 conditions (1)-(5); at lambda=-1, v=d_r condition (2)
  ord T_i^psi(sigma)=(-mu_i)lambda says total degree = y-degree of T_i^psi(f,g) for i<=r.
- p172 (PDF 33): proof of Prop 4.5: reduce to delta<=-1; claim delta=-1 (else Prop 4.2 with r-1
  contradicts the definition of delta); apply Prop 4.6 with r, lambda=-1, v=d_r, "trivial to verify
  all conditions"; deg q(pi)=2 distinct roots; p(pi) at most two roots, distinct multiplicities.
- p173-174 (PDF 34-35): Prop 5.1(1),(2); Definition-Remark: effective pairs exclude M_h if
  M_h=n-1; last effective pair is M_s.

# Arzhantsev-Petravchuk arXiv math/0608157v2, p5 (native text; excerpt retained)
Lemma 4 (char 0): f,g nonconstant algebraically dependent iff Jacobi matrix rank 1 (all 2x2 minors 0);
proof cited to [7, Ch.3, Th. III] or [18, Cor. 2], not proved in the paper.
Lemma 5 (any field): algebraically dependent iff exists closed h with f,g in k[h]; proof via Noether
normalization and Proposition 1 (integral closure of k[r] in k[x_1..x_n] is k[h]), proved on p3.
Fetched copy SHA-256 70429c3820eede008640a0d462d67ddb1f32c1f6e37f6b35f3589a0be2081e28, identical to
box/char-degree-20260905/arzhantsev-petravchuk-closed-polynomials.pdf; duplicate not retained here.
