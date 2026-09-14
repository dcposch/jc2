# D125 parity: avoid nonlinear B reconstruction

2026-09-07. DESK DESIGN / NEW CONSTANT-PIVOT COMPOSITION, pending independent review. No constructor, source-row traversal, CAS, AWS operation, point or ideal decision.

## Decision and measured baseline

**First choice: the moving-k normalized chart, eliminating only the standalone A and B linear polynomiality equations. Keep every Jacobian equation; do not reconstruct B from Jacobian blocks.** This gives 81 polynomial generators, with at most 1,362 possible coefficient monomials per Jacobian row and degree at most three. These are structural bounds, not measured runtime gains.

The sealed actual 22-coordinate attempt `d4f0ccc4…` exited1 after38.222s, peak RSS251,146,240 bytes. A B-forcing polynomial exceeded the100,000-term internal ceiling before serialization. The last accepted maximum was82,248 terms, degree12; it is not the failed polynomial's size. Both construction/replay outputs were empty; no complete system or803-row replay exists. The failing B degree was not recorded. Raising its cap or changing order would not test the representation proposed here.

## Exact 81-coordinate construction

Use the accepted odd unequal/rational contract with lambda2=0, and accepted moving-face normalization lambda3=1. Write k for the new unit parameter and impose **zk−1**. The normalized free slots are33 A and94 B, plus k,z:129 generators before elimination. The total faces remain A15=H³, B25=H5, H=p²(p³+g³). The moving lower coefficients are A_(2,1)=k, B_(8,5)=5k/3, B_(1,0)=5k²/9; the Jacobian target is c0*k³*g², c0=−5/9. Every other fixed zero and coefficient is retained.

First apply the entire target shear B→B−sA with s=[p15]B, imposing beta15=0. This is not subtraction of sH³ alone: its inverse restores every coefficient of sA. A15 has[p15]A=1. A's polygon lies inside B's, with inner weight3<5 and total degree15<25, so the shear preserves all B faces and zeros. Modulo ALL A-polynomiality equations it also preserves every B-polynomiality equation. The complete quotient is therefore a polynomial extension in s of its slice, not identical to its slice.

Solve the standalone Hermite polynomiality systems, descending total degree. Their diagonal entries are M_(t,i)=(-1)^(s-i-t) binom(s-i,t), independent of k. The accepted general proof gives13 odd A pivots and34 odd B pivots. **Do not use or subtract the92 nonlinear B-Jacobian pivots.** At B degree15 change the three pivot columns from i=0,1,2 to i=1,2,3, since i=0 is now fixed by the shear. The exact matrix and inverse are

    M = [  1, -1,  1]       M^-1 = [ 78,12,1]
        [-14, 13,-12]               [168,25,2]
        [ 91,-78, 66]               [ 91,13,1],   det M = -1.

All three shifted slots (i,15−i) lie strictly below the B outer and inner fixed faces:15<25 and5i−7(15−i)<5. All other pivots are the accepted ones. Hence this is still a constant-unit triangular graph over the entire base ring, including nonreduced quotients, with no exceptional k branch. It leaves20 A and94−1−34=59 B coordinates. With k,z, the count is **81**. All105 negative slots become identities:47 solved odd lower slots, eight fixed-top identities, and the remaining wrong-parity zero slots.

## Growth bound that addresses the failure

At lambda3=1 every negative-row coefficient matrix and forcing coefficient is rational constant. Descending Hermite elimination is linear in the member's raw coefficients. Thus each reconstructed A coefficient belongs to the vector space

    span_Q{1,k,a1,...,a20},

and each B coefficient belongs to

    span_Q{1,k,k²,b1,...,b59}.

Their sizes are at most22 and62. All A coefficients are integral linear combinations; B coefficient denominators divide9. The shifted inverse above is integral, so it preserves this property. The coefficient-variable monomial universe for ANY Jacobian row is contained in

    {a_i b_j} ∪ {a_i,ka_i,k²a_i} ∪ {b_j,kb_j} ∪ {1,k,k²,k³}.

Its size is20*59+3*20+2*59+4=**1362**, degree≤3; denominators divide9. Differentiation in g,p changes rational scalars only. Each individual coefficient product has at most22*62=1364 raw pairs. Recursive elimination cannot increase these supports, because it never multiplies free A/B coefficients. This avoids the observed nonlinear B-forcing expansion class altogether. Coefficient bit growth and total construction work remain to be measured.

Literal inverse-guard copies require care. Inverses of moving k,5k²/9,c0k³ may be represented by z,9z²/5,c0^-1*z³. Their inherited residuals are (kz)^r−1, r=1,2,3, of degrees2,4,6; **the entire literal row list is not cubic**. Either retain these tiny two-term copies or record exact cofactors

    (w^r−1)=(w−1)(1+w+...+w^(r−1)), w=kz.

The essential Jacobian-plus-unit generating set is cubic/quadratic, while each original guard retains its explicit trace. Keep every one of the803 original labelled positions, transported to this chart, plus the new inverse row:804 trace/equation positions, including explicit zeros, fixed-map obligations and guards. The number of nonzero rows is not yet measured.

## Exact quotient and point arrows

Let O0 be the complete original odd source quotient, N the accepted normalized quotient over E=Q[k,k^-1], and D=Q[ell,ell^-1] with k=ell^-6. The accepted normalization proves O0 ≅ N tensor_E D; D/E is rank-six finite étale and faithfully flat. The whole shear and the constant-unit Hermite graphs above give N ≅ R81[s], where R81 is the81-generator quotient by every transported residual and zk−1. Consequently

    O0 ≅ R81[s] tensor_E D.

This preserves properness and algebraic-closure point nonemptiness, not necessarily same-field inverse points: lifting a normalized point can require a sixth root. Every guarded field point of R81 directly supplies the normalized ordinary degree75/125 source pair with determinant−5k³/9 by the accepted sufficient contract. No point is known or claimed.

The normalization transports each negative row by ell^((5t−e−Dmember)/2) and each even-degree-n Jacobian row by ell^((n−38)/2); all factors are units. This is a new versioned client, not unchanged original bytes. The old original-lambda3 replayer cannot silently be reused with different faces. Per-original-row transport, the whole-shear identity, Hermite identities and guard cofactors must accompany the constructor.

## Alternatives and ranking

1. **Normalized Hermite-only81**, above: strongest proved elimination-growth control. Implement the small constant affine maps first; emit all Jacobian rows without any nonlinear B reconstruction. No optional B compression is needed.
2. **Retain original B graph auxiliaries:** the conservative original-lambda3 fallback keeps20 A coordinates,93 B slots after the beta15 slice, and ell:114 generators. These are original B coefficient variables, so their graph definitions need not be added as extra equations when all803 original rows remain. Selected Jacobian blocks can carry their reviewed constant-pivot metadata. Eliminating those92 coordinates recovers the old22-coordinate quotient, but retaining them avoids expanded B forcing. This needs fewer normalization changes; it retains lambda-dependent A graph degree and lacks the first choice's cubic bound. Choosing a smaller unknown set of retained B layers is not justified by the failed run: its layer was not recorded.
3. **Arithmetic circuits / exact point certificates:** a DAG on22 slice inputs with N arithmetic gates gives22+N variables and803+N rows, via gate equations y−op(previous)=0 and every original source row. With only rational constants, addition and multiplication, eliminating gate variables is an exact graph-ring isomorphism. N and runtime are unknown; circuit counting alone proves no speed advantage. Given a candidate in a nonzero finite Q-algebra F=Q[t]/h(t), monic h of positive degree, one can evaluate all graph/source equations and guards exactly modulo h. A maximal quotient of F is a number field, so a successful complete certificate gives a field point; irreducibility of h is unnecessary for this existence implication. h=1, characteristic-p residues, numerical approximations, or missing original rows are not such certificates. This evaluation representation does not itself find a candidate; rank it third absent one.

## Next discriminator and custody

No failed-layer instrumentation is prerequisite to the81-coordinate choice: it builds none of the nonlinear B-Jacobian graphs. A future builder should nevertheless identify member/degree/pivots/output row before every capped operation and record pending term count, coefficient bits, time/RSS/bytes. Missing layer information remains missing; do not rerun the failed pipeline just to invent it.

After independent review and NEW root GREEN, acceptance would require one complete804-position construction/transport replay within the existing300s/4GiB and128MiB-per-file envelope, with no cap increase; verify the A22/B62 affine supports, J1362/degree3/denominator9 bounds, all105 polynomiality identities, fixed faces and every guard trace. Record actual total terms, bytes, coefficient bits, wall time and RSS. Completion of a fully checked system, versus the previous zero-byte failure, is the material cost discriminator. Solver performance and properness remain separate questions. This report authorizes no implementation or run.

Read perimeter: the sealed failed-attempt, unit-normalization producer/gate, standalone-Hermite producer/gate, B/A composition, and relevant accepted audit entries. No live peer artifact, source803 traversal, production metadata/expansion, AWS or protected project was accessed. Exact input/code/result pins are in the owned box. Tiny Fraction3x3, monomial-space, whole-shear, guard-cofactor and changed-object controls passed normally and−O; no Assert nodes, zero source rows evaluated, well below30wall/25CPU/512MiB. These are desk controls, not full-system certification. All writers idle after transactional sealing.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10067`.
- Body SHA-256:
  `69f458f29d27f6d242a7e2515d5689f66a33f75bbfe4c5ed3ec7e0ec40c7538f`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
