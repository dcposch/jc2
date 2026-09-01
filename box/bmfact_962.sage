# bmfact_962.sage
#
# Certified braid-monodromy factorisation of the realized (9,6,2) curve
#   q = t^6 + 8 t^2
#   p = t^9 + 12 t^5 + 24 t
#   D = image of t |-> (x,y) = (p(t), q(t))
# via Sage's SIROCCO interface (zariski_vankampen.braid_monodromy).
#
# Charged: REP-96-INNER §1, §5, §7 (R1). Affine curve F=0, x-projection.
#
# API (Sage 10.8 manuals dated 2025-12-27, plus develop source which adds
# a fifth return value -- the geometric-basis base point):
#   from sage.schemes.curves.zariski_vankampen import braid_monodromy
#   braid_monodromy(f, arrangement=(), vertical=False)
#   Sage 10.8 documented output:
#       (list_of_braids, strand_dict, vertical_dict, nstrands)
#   Sage develop (github sagemath/sage zariski_vankampen.py, 2026-09-01):
#       (list_of_braids, strand_dict, vertical_dict, nstrands, base_point)
#   This script unpacks both. The fifth slot is the Voronoi-vertex base
#   point p1 of the geometric basis; it is required to name the strands.
#   URL: https://doc.sagemath.org/html/en/reference/curves/sage/schemes/curves/zariski_vankampen.html
#
# CONVENTIONS -- the top hazard class. Read before interpreting the JSON.
#
# (B1) Projection. braid_monodromy projects over the FIRST generator of
#      the parent polynomial ring if there are no vertical asymptotes.
#      We put F in QQ[coord_x, coord_y] with generator order (coord_x,
#      coord_y), and we assert deg_y(F)=9=deg(F) so lc_y(F) is a nonzero
#      constant: no vertical asymptotes, no linear change of variables.
#
# (B2) Base point. The geometric basis is built from a corrected Voronoi
#      diagram of the discriminant points in the x-plane (function
#      geometric_basis in zariski_vankampen.py). The base point p is a
#      vertex of the unbounded cell. Develop returns p1 = p_real + i p_imag
#      as the fifth tuple entry. Sage 10.8 docs omit it: FLAG if missing.
#
# (B3) Strand order. Strands are the y-roots of F(p1, y), ordered by
#      Sage's sort of QQbar (real part, then imaginary part: see
#      strand_components, which does roots_base.sort()). Generator xi_j
#      of F_9, 1-based, is the meridian of strand j-1 (0-based). The
#      script emits the ordered y-roots so the enumerator does not guess.
#
# (B4) Geometric-basis orientation. Each returned braid is the monodromy
#      of one based loop that goes to a bounded Voronoi cell, runs once
#      around it, and returns. The concatenation of the listed loops is
#      equivalent to the counterclockwise boundary circuit E of the
#      unbounded cell (geometric_basis docstring: "The concatenation of
#      all these paths is equivalent to E"; orient_circuit forces
#      counterclockwise). The PRODUCT of the listed braids, in listed
#      order, is therefore the monodromy of a large counterclockwise
#      loop around ALL finite discriminant points: this is rho_inf in
#      the "positive finite-plane" convention of REP-96 §2 (as x
#      traverses one positive loop, x^{k/9} |-> x^{k/9} zeta_9^k).
#      The enumerator also runs the inverse-product variant.
#
# (B5) Positive Artin generator. braid_from_piecewise issues a positive
#      Tietze letter at a real-part crossing of two y-paths when the
#      currently-left strand has smaller imaginary part at the crossing
#      (source: zariski_vankampen.braid_from_piecewise, the sgn on Im).
#      Sage Tietze: BraidGroup(9)([1,2,-1]) = s0 * s1 * s0^{-1}, so
#      letter k>0 is generator s_{k-1} (strands k and k+1, 1-based).
#
# (B6) Artin action on F_9, matching REP-96's left Hurwitz and the
#      charged PI1-S4-DECISION §2:
#         sigma_k :  xi_k     |-> xi_k xi_{k+1} xi_k^{-1}
#                    xi_{k+1} |-> xi_k
#                    xi_j     |-> xi_j   (j != k, k+1)
#      Composition: (beta gamma) acts as beta after gamma
#      (phi_{beta gamma} = phi_beta o phi_gamma). A Sage Tietze word is
#      applied RIGHTMOST letter first. This is the dual of the left
#      Hurwitz action on tuples used by bmfact_enum.py:
#         sigma_k . (..., t_k, t_{k+1}, ...)
#           = (..., t_k t_{k+1} t_k^{-1}, t_k, ...)
#      ZvK: the relation is xi_j = phi_beta(xi_j) in pi_1, i.e. the
#      tuple of images is Hurwitz-fixed by beta.
#
# (B7) Affine vs projective. projective=False (the default of
#      fundamental_group / this call) presents pi_1(C^2 - D), NOT
#      pi_1(P^2 - Dbar). No relation xi_9 ... xi_1 = 1 is imposed.
#      That is the correct group: meridians of the affine curve.
#      Affine computation suffices; see the report derivation.
#
# Dialect: no variables named pi, gamma, I, or O.
# Long-form assertions. Unverified API calls marked FLAG.
#
# Usage:
#   sage bmfact_962.sage precheck
#   sage bmfact_962.sage monodromy
# Environment:
#   BRAID_JOB_OUT               output directory (default ./bmfact-962-out)
#   BRAID_JOB_RUN_MONODROMY=1   required for the SIROCCO call
#
# Campaign policy: SIROCCO homotopy is AWS-only. This script refuses
# monodromy unless BRAID_JOB_RUN_MONODROMY=1.

import json
import os
import sys
import time
import traceback

from sage.schemes.curves.zariski_vankampen import braid_monodromy
from sage.schemes.curves.zariski_vankampen import conjugate_positive_form
from sage.schemes.curves.zariski_vankampen import discrim
from sage.schemes.curves.zariski_vankampen import strand_components

try:
    import sage.version as sage_version_module
    SAGE_VERSION_STRING = sage_version_module.version
except Exception as version_err:
    SAGE_VERSION_STRING = "UNKNOWN: %s" % version_err

DOC_URL_ZVK = "https://doc.sagemath.org/html/en/reference/curves/sage/schemes/curves/zariski_vankampen.html"
DOC_URL_AFFINE = "https://doc.sagemath.org/html/en/reference/curves/sage/schemes/curves/affine_curve.html"
DOC_URL_ARTIN = "https://doc.sagemath.org/html/en/reference/groups/sage/groups/artin.html"
DOC_URL_BRAID = "https://doc.sagemath.org/html/en/reference/groups/sage/groups/braid.html"
DOC_URL_SIROCCO_SPKG = "https://doc.sagemath.org/html/en/reference/spkg/sirocco.html"
DOC_RELEASE_NOTE = "Sage 10.8 reference manuals, pages dated 2025-12-27; develop braid_monodromy 5-tuple fetched 2026-09-01"

N_STRANDS_EXPECTED = 9
EXPONENT_LEDGER_EXPECTED = 16
N_TANGENCY_EXPECTED = 8
N_NODE_PAIRS_EXPECTED = 4
N_DISC_SUPPORT_EXPECTED = 9  # eight tangency x-values + x=0

# Closed form of F, independently of the resultant, from the identity
# x^2 - y^3 - 64 y = 64 t^2 on the curve. Used as a cross-check.
F_CLOSED_FORM_TERMS = (
    "coord_x^6"
    " - 3*coord_x^4*coord_y^3 - 192*coord_x^4*coord_y"
    " + 3*coord_x^2*coord_y^6 + 384*coord_x^2*coord_y^4"
    " + 12288*coord_x^2*coord_y^2 + 32768*coord_x^2"
    " - coord_y^9 - 192*coord_y^7 - 12288*coord_y^5"
    " - 294912*coord_y^3 - 2359296*coord_y"
)


def fail(message):
    """Abort with a self-describing message."""
    raise AssertionError(message)


def census_abort(message):
    """Loud abort: the REP-96 §1 census disagrees with the SIROCCO output."""
    banner = "=" * 72
    sys.stderr.write(banner + "\n")
    sys.stderr.write("CENSUS-DISAGREES-REP96\n")
    sys.stderr.write(banner + "\n")
    sys.stderr.write(message + "\n")
    sys.stderr.write(banner + "\n")
    sys.stderr.flush()
    raise AssertionError("CENSUS-DISAGREES-REP96: " + message)


def freely_reduce_tietze(word):
    """Cancel adjacent inverse letters in a Tietze word of F_9."""
    reduced = []
    for letter in word:
        letter = int(letter)
        if letter == 0:
            fail("freely_reduce_tietze: letter 0 is illegal")
        if reduced and reduced[-1] == -letter:
            reduced.pop()
        else:
            reduced.append(letter)
    return reduced


def apply_artin_letter_to_word(word, tietze_letter, n_strands):
    """Substitute one Artin generator into a free-group Tietze word.

    sigma_k (tietze_letter = k > 0):
        x_k     |-> x_k x_{k+1} x_k^{-1}
        x_{k+1} |-> x_k
    sigma_k^{-1} (tietze_letter = -k < 0):
        x_k     |-> x_{k+1}
        x_{k+1} |-> x_{k+1}^{-1} x_k x_{k+1}
    """
    if tietze_letter == 0:
        fail("apply_artin_letter_to_word: Tietze letter 0")
    gen_abs = abs(int(tietze_letter))
    if gen_abs < 1 or gen_abs >= n_strands:
        fail(
            "apply_artin_letter_to_word: |letter|=%d outside 1..%d"
            % (gen_abs, n_strands - 1)
        )
    out = []
    positive = tietze_letter > 0
    for signed in word:
        letter_abs = abs(int(signed))
        letter_sign = 1 if signed > 0 else -1
        if positive:
            if letter_abs == gen_abs:
                if letter_sign > 0:
                    out.extend([gen_abs, gen_abs + 1, -gen_abs])
                else:
                    out.extend([gen_abs, -(gen_abs + 1), -gen_abs])
            elif letter_abs == gen_abs + 1:
                out.append(letter_sign * gen_abs)
            else:
                out.append(int(signed))
        else:
            if letter_abs == gen_abs:
                out.append(letter_sign * (gen_abs + 1))
            elif letter_abs == gen_abs + 1:
                if letter_sign > 0:
                    out.extend([-(gen_abs + 1), gen_abs, gen_abs + 1])
                else:
                    out.extend([-(gen_abs + 1), -gen_abs, gen_abs + 1])
            else:
                out.append(int(signed))
    return freely_reduce_tietze(out)


def artin_auto_images(tietze_word, n_strands):
    """Images of the n free generators under the Artin auto of a Tietze word.

    Rightmost letter first, matching left Hurwitz (B6) and Sage multiplication
    B([1,2]) = s0*s1 acting on the left on tuples.
    """
    images = [[idx] for idx in range(1, n_strands + 1)]
    position = len(tietze_word) - 1
    while position >= 0:
        letter = tietze_word[position]
        images = [
            apply_artin_letter_to_word(word, letter, n_strands)
            for word in images
        ]
        position -= 1
    return images


def build_F():
    """F(coord_x, coord_y) = Res_t(p(t)-x, q(t)-y), primitive in QQ[x,y].

    Ring map, declared:
      coefficient field = QQ
      generator order   = (coord_x, coord_y) so the x-projection is first
      param_t           = elimination variable
    Image check: the resultant is asserted equal to the closed form coming
    from x^2 - y^3 - 64 y = 64 t^2, not inferred from matching names.
    """
    ring_xy = QQ["coord_x", "coord_y"]
    coord_x, coord_y = ring_xy.gens()
    ring_t = ring_xy["param_t"]
    param_t = ring_t.gen(0)

    poly_p = param_t**9 + 12 * param_t**5 + 24 * param_t
    poly_q = param_t**6 + 8 * param_t**2
    poly_P = poly_p - coord_x
    poly_Q = poly_q - coord_y
    # FLAG: MultivariatePolynomial.resultant is classical Sage.
    poly_F_raw = poly_P.resultant(poly_Q)
    if poly_F_raw.parent() is not ring_xy:
        poly_F_raw = ring_xy(poly_F_raw)
    if poly_F_raw == 0:
        fail("build_F: resultant is the zero polynomial")
    content_rational = poly_F_raw.content()
    if content_rational == 0:
        fail("build_F: content of a nonzero polynomial was 0")
    poly_F = ring_xy(poly_F_raw / content_rational)

    # Closed-form cross-check (identity substitution).
    poly_F_closed = ring_xy(
        coord_x**6
        - 3 * coord_x**4 * coord_y**3
        - 192 * coord_x**4 * coord_y
        + 3 * coord_x**2 * coord_y**6
        + 384 * coord_x**2 * coord_y**4
        + 12288 * coord_x**2 * coord_y**2
        + 32768 * coord_x**2
        - coord_y**9
        - 192 * coord_y**7
        - 12288 * coord_y**5
        - 294912 * coord_y**3
        - 2359296 * coord_y
    )
    if poly_F != poly_F_closed and poly_F != -poly_F_closed:
        fail(
            "build_F: Res_t(p-x, q-y) disagrees with the identity closed form. "
            "resultant=%s closed=%s" % (poly_F, poly_F_closed)
        )
    # Prefer the closed-form sign (positive x^6).
    if poly_F == -poly_F_closed:
        poly_F = poly_F_closed
    return ring_xy, coord_x, coord_y, poly_F


def precheck():
    """Degree, irreducibility, four nodes, discriminant support. Exact, no SIROCCO."""
    print("PRECHECK realized (9,6,2) curve p=t^9+12t^5+24t, q=t^6+8t^2")
    sys.stdout.flush()
    ring_xy, coord_x, coord_y, poly_F = build_F()

    total_deg = poly_F.total_degree()
    if total_deg != 9:
        fail("precheck: total_degree(F)=%s, expected 9" % total_deg)
    deg_y = poly_F.degree(coord_y)
    if deg_y != 9:
        fail(
            "precheck: deg_y(F)=%s, expected 9. Sage braid_monodromy "
            "projects over the first variable; deg_y=deg means no vertical "
            "asymptotes." % deg_y
        )
    deg_x = poly_F.degree(coord_x)
    if deg_x != 6:
        fail("precheck: deg_x(F)=%s, expected 6 (bidegree (6,9))" % deg_x)

    # FLAG: factor() of a bivariate QQ-polynomial is classical Sage.
    factored = poly_F.factor()
    unit_part = factored.unit()
    n_factors = len(factored)
    if n_factors != 1:
        fail(
            "precheck: F factored into %d non-unit factors %s; expected irreducible"
            % (n_factors, factored)
        )
    poly_irr, multiplicity = factored[0]
    if multiplicity != 1:
        fail(
            "precheck: irreducible factor has multiplicity %d. factorisation=%s"
            % (multiplicity, factored)
        )
    if hasattr(poly_F, "is_irreducible"):
        if not poly_F.is_irreducible():
            fail("precheck: F.is_irreducible() is False after factor() showed one factor")

    partial_x = poly_F.derivative(coord_x)
    partial_y = poly_F.derivative(coord_y)
    # FLAG: PolynomialRing.ideal / dimension / vector_space_dimension
    # not re-fetched from a dedicated commutative-algebra doc page.
    ideal_sing = ring_xy.ideal([poly_F, partial_x, partial_y])
    dim_sing = ideal_sing.dimension()
    if dim_sing != 0:
        fail(
            "precheck: singular locus has dimension %s, expected 0 (finite nodes)"
            % dim_sing
        )
    vdim_sing = ideal_sing.vector_space_dimension()
    if vdim_sing != 4:
        fail(
            "precheck: vector_space_dimension of Jacobian ideal = %s, expected 4 "
            "(four reduced affine nodes, all on x=0)"
            % vdim_sing
        )

    disc_raw = poly_F.resultant(partial_y, coord_y)
    disc_in_xy = ring_xy(disc_raw)
    ring_x = QQ["coord_x_only"]
    coord_x_only = ring_x.gen(0)
    disc_univariate = ring_x(0)
    for exponent_pair, coeff in disc_in_xy.dict().items():
        exp_x = exponent_pair[0]
        exp_y = exponent_pair[1]
        if exp_y != 0:
            fail("precheck: Res_y(F, dF/dy) still depends on y (term y^%d)" % exp_y)
        disc_univariate = disc_univariate + ring_x(coeff) * coord_x_only**exp_x
    if disc_univariate == 0:
        fail("precheck: discriminant in x is the zero polynomial")
    if disc_univariate.degree() != 16:
        fail(
            "precheck: deg(disc_y F)=%s, expected 16 = 2 delta_aff + d - 1"
            % disc_univariate.degree()
        )
    # FLAG: squarefree_part / valuation classical univariate.
    disc_squarefree = disc_univariate.squarefree_part()
    n_disc_support = disc_squarefree.degree()
    if n_disc_support != N_DISC_SUPPORT_EXPECTED:
        fail(
            "precheck: square-free discriminant in x has degree %s, expected %d "
            "(eight tangency values + x=0). REP-96 §1 census."
            % (n_disc_support, N_DISC_SUPPORT_EXPECTED)
        )
    val_at_zero = disc_univariate.valuation(coord_x_only)
    if val_at_zero != 8:
        fail(
            "precheck: valuation of disc_y F at x=0 is %s, expected 8 "
            "(four nodes, disc valuation 2 each)"
            % val_at_zero
        )

    record = {
        "curve": "realized (9,6,2)",
        "param_p": "t^9 + 12 t^5 + 24 t",
        "param_q": "t^6 + 8 t^2",
        "F": str(poly_F),
        "F_closed_form": F_CLOSED_FORM_TERMS,
        "F_unit_from_factor": str(unit_part),
        "total_degree": int(total_deg),
        "deg_x": int(deg_x),
        "deg_y": int(deg_y),
        "irreducible": True,
        "singular_ideal_dimension": int(dim_sing),
        "singular_vector_space_dimension": int(vdim_sing),
        "n_discriminant_x_squarefree": int(n_disc_support),
        "disc_degree": int(disc_univariate.degree()),
        "disc_valuation_at_zero": int(val_at_zero),
        "discriminant_x_squarefree": str(disc_squarefree),
        "conventions": {
            "projection": "first variable coord_x",
            "strand_order": "QQbar.sort of y-roots at geometric-basis base point",
            "tietze": "B([1,2,-1])=s0*s1*s0^-1; letter k>0 is s_{k-1}",
            "hurwitz": "left action, rightmost Tietze letter first",
            "artin_on_F9": "sigma_k: x_k |-> x_k x_{k+1} x_k^{-1}, x_{k+1} |-> x_k",
            "orientation": (
                "product of listed braids = counterclockwise large loop = rho_inf "
                "in REP-96 §2 positive-finite-plane convention; inverse is a variant"
            ),
        },
    }
    return ring_xy, coord_x, coord_y, poly_F, record


def tietze_as_ints(braid_elt):
    raw = braid_elt.Tietze()
    return [int(letter) for letter in raw]


def permutation_images(braid_elt, n_strands):
    """Underlying permutation as the image tuple of (1..n).

    permutation(W=SymmetricGroup(n)) is documented on braid.html.
    """
    sym = SymmetricGroup(n_strands)
    perm_elt = braid_elt.permutation(W=sym)
    images = []
    for idx in range(1, n_strands + 1):
        images.append(int(perm_elt(idx)))
    return images


def permutation_cycle_type_list(braid_elt, n_strands):
    sym = SymmetricGroup(n_strands)
    perm_elt = braid_elt.permutation(W=sym)
    ctype = perm_elt.cycle_type()
    return [int(part) for part in ctype]


def serialise_cpf(braid_elt):
    """conjugate_positive_form -> JSON-able records.

    Documented return: list of [alpha, [beta_j]] with
    tau = (prod beta) * alpha * (prod beta)^{-1}, the tau pairwise
    commuting, product equal to the input braid.
    """
    try:
        cpf = conjugate_positive_form(braid_elt)
    except Exception as cpf_err:
        return {
            "ok": False,
            "error": "%s: %s" % (type(cpf_err).__name__, cpf_err),
            "FLAG": (
                "conjugate_positive_form raised. The conjugating words for this "
                "factor are therefore not certified by this helper; the Tietze "
                "word of the factor itself remains the SIROCCO output."
            ),
            "pieces": [],
        }
    pieces = []
    for item in cpf:
        alpha_elt = item[0]
        conjugators = item[1]
        pieces.append(
            {
                "alpha_tietze": tietze_as_ints(alpha_elt),
                "alpha_string": str(alpha_elt),
                "alpha_exponent_sum": int(alpha_elt.exponent_sum()),
                "conjugator_tietzes": [tietze_as_ints(conj) for conj in conjugators],
                "conjugator_strings": [str(conj) for conj in conjugators],
            }
        )
    return {"ok": True, "error": None, "FLAG": None, "pieces": pieces}


def classify_factor(rec):
    """Classify one geometric-basis braid against the REP-96 §1 census.

    tangency: exponent 1, permutation a single transposition, CPF one
              piece whose alpha has exponent 1.
    node_fibre: exponent 8, permutation the identity, CPF four pieces
                each of exponent 2 (four commuting sigma_i^2).
    """
    e_sum = rec["exponent_sum"]
    ctype = rec["permutation_cycle_type"]
    cpf_ok = rec["conjugate_positive_form_ok"]
    pieces = rec["conjugate_positive_form"] or []
    alpha_exps = [int(piece["alpha_exponent_sum"]) for piece in pieces] if cpf_ok else []

    is_transposition_perm = sorted(ctype) == [1, 1, 1, 1, 1, 1, 1, 2]
    is_identity_perm = (not ctype) or (max(ctype) == 1 and sum(ctype) == 9)

    if e_sum == 1 and is_transposition_perm:
        if cpf_ok and alpha_exps == [1]:
            return "tangency"
        if cpf_ok:
            return "tangency_cpf_unexpected"
        return "tangency_cpf_missing"
    if e_sum == 8 and is_identity_perm:
        if cpf_ok and sorted(alpha_exps) == [2, 2, 2, 2]:
            return "node_fibre"
        if cpf_ok and len(alpha_exps) == 1 and alpha_exps[0] == 8:
            return "node_fibre_unsplit"
        if cpf_ok:
            return "node_fibre_cpf_unexpected"
        return "node_fibre_cpf_missing"
    return "other"


def unpack_braid_monodromy(bm_output):
    """Accept the Sage 10.8 4-tuple and the develop 5-tuple (base point)."""
    if isinstance(bm_output, (list, tuple)) and len(bm_output) == 5:
        braid_list, strand_dict, vertical_dict, n_strands, base_pt = bm_output
        return (
            list(braid_list),
            dict(strand_dict),
            dict(vertical_dict),
            int(n_strands),
            base_pt,
            "5-tuple (Sage develop: braids, strand_dict, vertical_dict, nstrands, base_point)",
        )
    if isinstance(bm_output, (list, tuple)) and len(bm_output) == 4:
        braid_list, strand_dict, vertical_dict, n_strands = bm_output
        return (
            list(braid_list),
            dict(strand_dict),
            dict(vertical_dict),
            int(n_strands),
            None,
            "4-tuple (Sage 10.8 docs: braids, strand_dict, vertical_dict, nstrands); base_point ABSENT",
        )
    if isinstance(bm_output, (list, tuple)):
        braid_list = list(bm_output)
        if len(braid_list) == 0:
            fail("unpack_braid_monodromy: empty braid list and no nstrands")
        n_strands = int(braid_list[0].parent().strands())
        return braid_list, {}, {}, n_strands, None, "bare list (AffinePlaneCurve.braid_monodromy?)"
    fail(
        "unpack_braid_monodromy: unexpected return type %s value %s"
        % (type(bm_output), bm_output)
    )


def emit_jsonl(path, records):
    with open(path, "w") as handle:
        for rec in records:
            handle.write(json.dumps(rec, sort_keys=False))
            handle.write("\n")
    print("WROTE %s (%d JSON lines)" % (path, len(records)))
    sys.stdout.flush()


def run_monodromy(poly_F, precheck_record, out_dir):
    """Call SIROCCO via braid_monodromy. AWS-only; gated by the driver."""
    print("MONODROMY starting (this is the SIROCCO homotopy)")
    sys.stdout.flush()
    t0 = time.time()
    bm_output = braid_monodromy(poly_F)
    elapsed = time.time() - t0
    print("MONODROMY returned in %.3f sec" % elapsed)
    sys.stdout.flush()

    (
        braid_list,
        strand_dict,
        vertical_dict,
        n_strands,
        base_pt,
        unpack_shape,
    ) = unpack_braid_monodromy(bm_output)
    print("MONODROMY unpack_shape=%s nstrands=%s n_factors=%s"
          % (unpack_shape, n_strands, len(braid_list)))
    sys.stdout.flush()

    if n_strands != N_STRANDS_EXPECTED:
        census_abort(
            "nstrands = %s, expected 9 (x-projection of a degree-9 curve "
            "with no vertical asymptotes)" % n_strands
        )

    # Strand y-roots at the geometric-basis base point, if we have it.
    ordered_y_roots = []
    strand_order_FLAG = None
    if base_pt is None:
        strand_order_FLAG = (
            "FLAG: braid_monodromy did not return a base point (Sage 10.8 "
            "4-tuple). Ordered y-roots below are NOT claimed to be Sage's "
            "strand order. OPEN[BMFACT-BASEPOINT] in the report."
        )
        print("WARNING %s" % strand_order_FLAG)
        sys.stdout.flush()
    else:
        try:
            roots_base, strand_map = strand_components(poly_F, [poly_F], base_pt)
            ordered_y_roots = [str(pair[0]) for pair in roots_base]
            if len(ordered_y_roots) != 9:
                fail(
                    "strand_components at base_point returned %d y-roots, expected 9"
                    % len(ordered_y_roots)
                )
        except Exception as strand_err:
            strand_order_FLAG = (
                "FLAG: strand_components failed: %s: %s"
                % (type(strand_err).__name__, strand_err)
            )
            print("WARNING %s" % strand_order_FLAG)
            sys.stdout.flush()

    # Cross-check against the curve method. FLAG: same library twice.
    affine_plane = AffineSpace(QQ, 2, names=("coord_x", "coord_y"))
    curve_D = affine_plane.curve(poly_F)
    t1 = time.time()
    braid_list_curve = list(curve_D.braid_monodromy())
    elapsed_curve = time.time() - t1
    print(
        "MONODROMY AffinePlaneCurve.braid_monodromy returned %d braids in %.3f sec"
        % (len(braid_list_curve), elapsed_curve)
    )
    sys.stdout.flush()
    curve_matches = [str(a) for a in braid_list] == [str(b) for b in braid_list_curve]

    try:
        disc_points = discrim((poly_F,))
        disc_points_str = [str(pt) for pt in disc_points]
    except Exception as disc_err:
        disc_points_str = []
        print(
            "WARNING discrim((F,)) failed: %s: %s"
            % (type(disc_err).__name__, disc_err)
        )
        sys.stdout.flush()

    factor_records = []
    jsonl_records = []
    product_elt = None
    for idx, braid_elt in enumerate(braid_list):
        if braid_elt.parent().strands() != N_STRANDS_EXPECTED:
            fail(
                "monodromy factor %d: braid lives in B_%s, expected B_9"
                % (idx, braid_elt.parent().strands())
            )
        e_sum = int(braid_elt.exponent_sum())
        ctype = permutation_cycle_type_list(braid_elt, N_STRANDS_EXPECTED)
        perm_images = permutation_images(braid_elt, N_STRANDS_EXPECTED)
        cpf_record = serialise_cpf(braid_elt)
        tietze = tietze_as_ints(braid_elt)
        free_auto = artin_auto_images(tietze, N_STRANDS_EXPECTED)
        rec = {
            "index": int(idx),
            "string": str(braid_elt),
            "tietze": tietze,
            "exponent_sum": e_sum,
            "permutation_images": perm_images,
            "permutation_cycle_type": ctype,
            "free_auto_F9": free_auto,
            "conjugate_positive_form": cpf_record.get("pieces"),
            "conjugate_positive_form_ok": cpf_record.get("ok"),
            "conjugate_positive_form_error": cpf_record.get("error"),
            "conjugate_positive_form_FLAG": cpf_record.get("FLAG"),
        }
        rec["census_class"] = classify_factor(rec)
        factor_records.append(rec)
        jsonl_records.append({"type": "braid", **rec})
        if product_elt is None:
            product_elt = braid_elt
        else:
            product_elt = product_elt * braid_elt

    if product_elt is None:
        fail("monodromy: no braids to form a product")
    product_tietze = tietze_as_ints(product_elt)
    product_record = {
        "string": str(product_elt),
        "tietze": product_tietze,
        "exponent_sum": int(product_elt.exponent_sum()),
        "permutation_images": permutation_images(product_elt, N_STRANDS_EXPECTED),
        "permutation_cycle_type": permutation_cycle_type_list(
            product_elt, N_STRANDS_EXPECTED
        ),
        "free_auto_F9": artin_auto_images(product_tietze, N_STRANDS_EXPECTED),
    }

    # ----- REP-96 §1 census -----
    classes = [rec["census_class"] for rec in factor_records]
    n_tangency = sum(1 for c in classes if c.startswith("tangency"))
    n_node = sum(1 for c in classes if c.startswith("node_fibre"))
    n_other = sum(1 for c in classes if c == "other")
    ledger = sum(rec["exponent_sum"] for rec in factor_records)
    print("CENSUS classes=%s" % classes)
    print("CENSUS n_tangency=%d n_node_fibre=%d n_other=%d ledger=%d"
          % (n_tangency, n_node, n_other, ledger))
    sys.stdout.flush()

    if n_other:
        census_abort(
            "unclassified geometric-basis braids: %s. "
            "REP-96 §1 requires eight simple tangency braids (single sigma_i) "
            "in eight distinct fibres plus one fibre (x=0) with four commuting "
            "sigma_i^2." % classes
        )
    if n_tangency != N_TANGENCY_EXPECTED:
        census_abort(
            "tangency-class count = %d, expected 8. classes=%s" % (n_tangency, classes)
        )
    if n_node != 1:
        census_abort(
            "node-fibre-class count = %d, expected 1 (the unique x=0 fibre). "
            "classes=%s" % (n_node, classes)
        )
    if ledger != EXPONENT_LEDGER_EXPECTED:
        census_abort(
            "exponent ledger = %d, expected 16 = 8*1 + 4*2. "
            "A sign error in orientation would typically give -16: that is "
            "still a census disagreement and must not be papered over. "
            "classes=%s" % (ledger, classes)
        )
    if abs(product_record["exponent_sum"]) != EXPONENT_LEDGER_EXPECTED:
        census_abort(
            "product exponent_sum = %s, expected |e|=16" % product_record["exponent_sum"]
        )
    # One-place at infinity: permutation of rho_inf is a 9-cycle.
    product_ctype = product_record["permutation_cycle_type"]
    if sorted(product_ctype) != [9] and product_ctype != [9]:
        # Not a census item of REP-96 §1 (that is local types), but a
        # one-place check. Loud, not silent.
        print(
            "WARNING product permutation cycle type %s is not a 9-cycle "
            "(one-place-at-infinity expects a 9-cycle or its inverse)."
            % product_ctype
        )
        sys.stdout.flush()

    print("CENSUS-OK 8 tangency + 1 node-fibre (four commuting squares); ledger 16")
    sys.stdout.flush()

    jsonl_records.insert(
        0,
        {
            "type": "meta",
            "job": "bmfact_962",
            "sage_version": SAGE_VERSION_STRING,
            "unpack_shape": unpack_shape,
            "nstrands": int(n_strands),
            "n_factors": int(len(braid_list)),
            "base_point": str(base_pt) if base_pt is not None else None,
            "ordered_y_roots_at_base_point": ordered_y_roots,
            "strand_order_FLAG": strand_order_FLAG,
            "conventions": precheck_record["conventions"],
            "doc_url_zvk": DOC_URL_ZVK,
            "doc_release_note": DOC_RELEASE_NOTE,
        },
    )
    jsonl_records.append({"type": "product", **product_record})
    jsonl_records.append(
        {
            "type": "census",
            "ok": True,
            "classes": classes,
            "n_tangency": int(n_tangency),
            "n_node_fibre": int(n_node),
            "exponent_ledger": int(ledger),
            "marker": "CENSUS-OK",
        }
    )

    out = dict(precheck_record)
    out.update(
        {
            "nstrands": int(n_strands),
            "n_factors": int(len(braid_list)),
            "unpack_shape": unpack_shape,
            "base_point": str(base_pt) if base_pt is not None else None,
            "ordered_y_roots_at_base_point": ordered_y_roots,
            "strand_order_FLAG": strand_order_FLAG,
            "strand_dict": {str(k): int(v) for (k, v) in strand_dict.items()},
            "vertical_dict": {str(k): int(v) for (k, v) in vertical_dict.items()},
            "braids": factor_records,
            "product": product_record,
            "census": {
                "ok": True,
                "classes": classes,
                "n_tangency": int(n_tangency),
                "n_node_fibre": int(n_node),
                "exponent_ledger": int(ledger),
            },
            "curve_method_matches_module_function": bool(curve_matches),
            "discrim_points": disc_points_str,
            "sirocco_elapsed_seconds": float(elapsed),
            "curve_method_elapsed_seconds": float(elapsed_curve),
            "sage_version": SAGE_VERSION_STRING,
            "doc_url_zvk": DOC_URL_ZVK,
            "doc_url_affine": DOC_URL_AFFINE,
            "doc_release_note": DOC_RELEASE_NOTE,
        }
    )
    bundle_path = os.path.join(out_dir, "bmfact_962.json")
    with open(bundle_path, "w") as handle:
        json.dump(out, handle, indent=2, sort_keys=False)
        handle.write("\n")
    print("WROTE %s" % bundle_path)
    jsonl_path = os.path.join(out_dir, "bmfact_962.jsonl")
    emit_jsonl(jsonl_path, jsonl_records)
    sys.stdout.flush()
    return out


def main(argv):
    if len(argv) == 0:
        mode = "precheck"
    else:
        mode = argv[0]
    if mode not in ("precheck", "monodromy"):
        fail("usage: sage bmfact_962.sage [precheck|monodromy]  (got %r)" % mode)
    out_dir = os.environ.get("BRAID_JOB_OUT", os.path.join(os.getcwd(), "bmfact-962-out"))
    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)

    print("sage_version=%s" % SAGE_VERSION_STRING)
    print("mode=%s" % mode)
    print("out_dir=%s" % out_dir)
    print("doc_zvk=%s" % DOC_URL_ZVK)
    print("doc_release=%s" % DOC_RELEASE_NOTE)
    sys.stdout.flush()

    ring_xy, coord_x, coord_y, poly_F, record = precheck()
    rec_path = os.path.join(out_dir, "precheck.json")
    with open(rec_path, "w") as handle:
        json.dump(record, handle, indent=2, sort_keys=False)
        handle.write("\n")
    print("WROTE %s" % rec_path)
    print("PRECHECK-OK")
    sys.stdout.flush()

    if mode == "precheck":
        return 0

    run_flag = os.environ.get("BRAID_JOB_RUN_MONODROMY", "")
    if run_flag != "1":
        fail(
            "monodromy mode refused: BRAID_JOB_RUN_MONODROMY is %r, not '1'. "
            "Campaign policy: SIROCCO homotopy is AWS-only."
            % run_flag
        )
    try:
        run_monodromy(poly_F, record, out_dir)
    except AssertionError:
        raise
    except Exception as mono_err:
        print("MONODROMY-FAILED")
        traceback.print_exc()
        fail("monodromy raised %s: %s" % (type(mono_err).__name__, mono_err))
    print("MONODROMY-OK")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
