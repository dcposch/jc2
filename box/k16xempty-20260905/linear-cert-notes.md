# Exact homogeneous Macaulay certificates

This subtask constructs actual cofactor identities for T^2, T=B eta. It uses finite-field arithmetic only to select a square submatrix, then solves and verifies over characteristic zero.

For a fixed t, use the fresh raw ring

    k[c_1,...,c_(t-1),b],  k=Q(d), 3d^2=t+1,
    wt(c_j)=j, wt(b)=t+1.

The coefficient polynomial E_k has weight 4t+2-k, whereas T^2 has weight 8t+2. For each k=2,...,2t and each monomial m of weight 4t+k, form the polynomial m E_k. Their coefficient vectors in all monomials of weight 8t+2 form a rectangular matrix over k. These are actual polynomial multiples of the reconstructed rows; matching weights alone is not used as evidence of spanning.

The driver `linear_export.py` emits `linear_t{t}_export.sing`, which imports the fresh direct reconstruction and exports each coefficient as `leadcoef|leadexp`. No stored Groebner basis or basis transformation is imported. The exporter also expands the actual target^2. `linear_cert.py` parses those coefficients exactly as rational pairs.

For the rational block representation, put e=3d, so e^2=3(t+1) is integral. Each coefficient a+b d is represented by a+(b/3)e. A common rational scaling makes each E_k and T^2 integral in Z[e]. Writing a coefficient as a+b e, multiplication is represented by

    [ a, 3(t+1)b ]
    [ b,     a   ].

This defines the exact ring map into 2x2 rational matrices; it is not an identification inferred from variable names. The driver selects columns by row reduction after mapping e to a square root of 3(t+1) at a suitable prime. It then constructs the selected integer block matrix and solves the full rational system using FLINT. The resulting solution is verified by literal rational matrix multiplication A*solution=target. Rational row scalings and the conversion e=3d are reversed to emit source cofactors a_k in the original field.

Finally a separate Singular process imports the fresh raw model, parses the emitted cofactors, and expands

    sum_(k=2)^(2t) a_k E_k - (B eta)^2.

Only a zero polynomial is accepted. Thus the modular matrix determines which columns are tried; neither the source certificate nor its verification relies on modular-to-characteristic-zero promotion, homogeneous properness, or a conjectural Hilbert series.

At t=4, the degree-34 map has 340 coefficient coordinates and 726 available row multiples. The selected 340-column matrix produces a 680x680 rational block system. Exact solve plus matrix multiplication and certificate serialization took under four seconds; the separate source identity replay passed. The generated source certificate has 5,948,704 bytes. Some rational coefficients have over 5,000 decimal digits, explaining why the certificate is much larger than a standard-basis membership result.

`t4` artifacts:

- `linear_t4_terms.txt`: exact coefficient export.
- `linear_t4_cert.log`: matrix dimensions, selection prime, exact solve and replay markers.
- `linear_t4_certificate.sing`: the actual source cofactors in matrix `linear_cofs[7][1]` and their independent source expansion.
- `linear_t4_replay.log`: `LINEAR_COFACTOR_IDENTITY_PASS t=4`.
- `linear_t4_metadata.json`: reproducible pivot selection and counts.

The local `linear_python` directory contains python-flint 0.9.0, downloaded as its published cp310-abi3 manylinux x86_64 wheel. It does not change the system Python environment. Its upstream wheel metadata, including URL and digests, is recorded in `linear_python/download.json`. Both the FLINT context and every Singular command are restricted to one thread/core.

At t=5, the degree-42 map has 1,792 coefficient coordinates and 3,504 row multiples. Its selected integer block system has size 3,584. Final t=5 status is recorded in the t=5 logs and certificate, if produced; no success is inferred merely from its full modular selection rank.

## Direct exact rank proof at t=5

The lane also saves `linear_t5_rank_certificate.json`, a stand-alone description of a nonzero exact minor. The coefficient domain for the cleared matrix is Z[e]/(e^2-18), with e=3d. The reduction map sends e to 7868 modulo 32009 (hence d to 23962). It is a ring homomorphism because 7868^2=18 modulo 32009. The exact raw coefficient denominators are all units at this prime; this was checked individually. The determinant of the listed 1792x1792 minor is 29155 modulo 32009, which is nonzero.

This is an elementary characteristic-zero proof, not an unlicensed modular ideal promotion. If the exact determinant were zero in Z[e]/(e^2-18), every image of it under a ring homomorphism would be zero. Its nonzero residue therefore proves that it is nonzero. Since e^2-18 is irreducible over Q, the exact coefficient ring embeds in Q(e), where the determinant is invertible. Consequently the listed 1792 exact polynomial multiples span every monomial of weight 42 over Q(d). In particular (B eta)^2 belongs to the original ideal J over Q(d). An independently rebuilt nonzero minor from the raw model closes this proof without needing the very large explicit cofactor serialization.

The distinction from unsafe modular membership is essential. A relation f in I modulo p can acquire coefficients only on a special fibre and fail in characteristic zero, as with I=(x+p y), f=x. Here it is a full-rank square matrix of *all* degree-42 coefficient coordinates that is certified; a specific membership is then forced by invertibility over the exact field. No homogeneous projectivization, affine inverse-chart properness, or coefficient reconstruction conjecture occurs.

The JSON lists every target-weight monomial, the source row and multiplier monomial for each selected column, the exact rational scaling used to clear that row, the prime and root image, the determinant residue, and hashes of the raw model and exact coefficient export. The selection artifact itself was produced in 5.9 seconds. Independent replay is an additional obligation and is recorded in the audit agent's artifacts.

One weight of full rank does not imply V(J)={0} in a weighted polynomial ring: a variable whose weight does not divide 42 can be invisible on its pure axis in degree 42. This lane consumes the certified rank only to obtain (B eta)^2 in J and the consequent unit identities. No zero-cone assertion or uniform-in-t rank claim is inferred.

## Compact cofactor circuit and uniform chart transport

The rank certificate defines source cofactors even before an expanded exact solve finishes. Let A be the unscaled exact square coefficient matrix of the selected polynomial multiples m_j E_(k_j), and let h be the unscaled coefficient vector of T^2 in the listed monomial basis. The rank artifact uses columns multiplied by listed nonzero rational scales s_(k_j), so its determinant is (product_j s_(k_j)) det(A). Its nonzero residue proves det(A) is nonzero in the exact field. Then

    u=adj(A) h / det(A)

is a vector of scalars in Q(d). The nonzero determinant is proved by its nonzero residue. If the j-th column corresponds to m_j E_(k_j), define

    a_k=sum_(j:k_j=k) u_j m_j.

The elementary identity A adj(A)=det(A)I proves T^2=sum a_k E_k. This is a fully specified arithmetic circuit for source cofactors, with every matrix entry supplied by the exact raw model, source row scaling and monomial map. Expanding the enormous numerator determinants is unnecessary for its validity.

Every a_k is homogeneous of weight 4t+k. Since b has weight t+1 and 2<=k<=2t, its b degree is at most five. Let d_k=deg_b E_k<=3. For the main chart define

    a_main,k=Delta^(8-d_k) a_k(c,A/Delta).

This is polynomial: each b^j term contributes Delta^(8-d_k-j), whose exponent is nonnegative. Multiplying the substituted source identity by Delta^8 gives

    (Delta H)^4=sum_k a_main,k F_k.

The elementary geometric-series identity then gives the literal main-chart certificate

    1=u^4 sum_k a_main,k F_k
       +(1-u Delta H)(1+u Delta H+(u Delta H)^2+(u Delta H)^3).

Here u is the inverse variable of the main chart, unrelated to the scalar solution vector above. If Delta is the zero polynomial, the main inverse equation is already 1, so that case is immediate.

For the complementary chart use the identity B-eta=b Delta-A. It gives

    B^4=sum_k a_k E_k
        +b B^2(B+eta) Delta-B^2(B+eta) A.

Multiplying by s^4 and adding

    (1-sB)(1+sB+(sB)^2+(sB)^3)

produces 1. Thus source T^2 membership provides explicit unit-certificate circuits for both exhaustive charts, including the closed Delta=0 branch. The transport is uniform in t; only the existence of the source matrix certificate has been established at the computed indices.

## Final execution status

The t=5 exact selected block solve completed at 582.731 seconds; literal exact matrix multiplication passed at 587.141 seconds. Expanded source cofactors were serialized at 717.088 seconds. `linear_t5_certificate.sing` has 200,267,594 bytes and is retained as an exact-solve artifact. The source coefficients use only E_5,...,E_10; their term counts are 43,188,234,313,420,593. At t=4 the nonzero source cofactors use E_4,...,E_8 with counts 1,43,62,93,141. These finite supports are not extrapolated to arbitrary t.

The optional separate Singular expansion of the 191 MiB t=5 certificate reached its 600-second wall cap and returned exit code 124. Its log ends in `halt 1`; it did not emit an identity PASS marker. Its precise status is **INCONCLUSIVE_TIMEOUT for the optional expanded source replay**, not a failed identity. `linear_t5_replay_status.json` records this boundary. The t=4 expanded source replay did complete with PASS.

The accepted t=5 source proof is the independently rebuilt nonzero exact rank minor together with the explicitly specified adjugate cofactor circuit. Parent reports that the independent minor and both literal chart circuits all passed. No additional expanded source success is claimed. The exact FLINT matrix solve/product and retained expanded coefficients are supplementary artifacts, whose scope is distinct from the completed compact proof.

`linear_certificate_artifacts.sha256` hashes the t=4 and t=5 source cofactor files and the t=5 rank certificate. All subtask processes have completed or been reaped; no CAS job remains running. No further solve or replay is required.
