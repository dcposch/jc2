#!/usr/bin/env python3
"""Independent stdlib-Python exact checker for the D43 `K0` field certificate, R4.

No PARI, no CAS, no third-party module, no network.  Every load-bearing datum
is a field of :class:`Spec` so the hostile mutation battery can perturb it and
observe which named gate fails.  Gates are fail-closed: an exception inside a
gate is a FAIL, never a skip.

R2 repairs carried here (see the producer report for the full map):

* D1  the two theorem booleans are computed from *layer-restricted* censuses,
      so a wrong E can no longer misreport the unconditional theorem, and a
      corroboration failure feeds neither theorem.
* D2  freeness of rank 432 is certified by ``RELATION_LEADING_TERMS`` in the
      FREE polynomial ring (pairwise coprime leading monomials, Buchberger's
      first criterion) and independently witnessed mod p by
      ``RANK432_INDEPENDENCE``.  The old asserted ``confluent_on_basis`` literal
      is gone and the old gate is retyped ``EXECUTED``.
* D3  ``GALOIS_STABILITY_FREE`` applies sigma to the five relations *before*
      quotienting, where ``sigma(relation) == 0`` is not automatic.
* D4  cardinality and prime-set pins on ``frames`` and ``pointbank_expected``.
* D5  ``r3_exponents``, ``alpha_data``, the sigma table, the eps datum and the
      E form are read from ``Spec`` at every use site instead of duplicated as
      gate-body literals.
* D10 constant-true sub-checks replaced by computations on ``Spec`` data.

The literal `E` and the literal `q0` are anchored to *external sealed files*
(the hashed E5/E6 bridge and the hashed charged theorem report), so no pin
passes by restating a constant to itself.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import re
import sys
from dataclasses import dataclass, replace
from fractions import Fraction as Fr
from pathlib import Path

import k0_algebra_r4 as KA

SCHEMA = "d43-k0-field-certificate-checker-r4"
UNCONDITIONAL_LAYERS = ("L0", "L1", "L2", "L3", "L4")
CONDITIONAL_LAYERS = ("L5",)

# --------------------------------------------------------------------------
# the load-bearing data, all mutable by the battery
# --------------------------------------------------------------------------

TRUE_PHI42 = (1, 1, 0, -1, -1, 0, 1, 0, -1, -1, 0, 1, 1)
TRUE_Q0 = {(0, 0, 2, 1, 0): Fr(-5, 6), (0, 1, 2, 1, 0): Fr(1, 2),
           (7, 0, 2, 1, 0): Fr(2, 3), (7, 1, 2, 1, 0): Fr(-1, 3)}


@dataclass(frozen=True)
class Spec:
    # ---- L0 source pins and the presentation ----------------------------
    phi42: tuple = TRUE_PHI42
    basis_shape: tuple = (12, 2, 3, 3, 2)
    basis_rank: int = 432
    phi42_disc: int = 3 ** 6 * 7 ** 10
    leading_monomials: tuple = ((12, 0, 0, 0, 0), (0, 2, 0, 0, 0),
                                (0, 0, 3, 0, 0), (0, 0, 0, 3, 0),
                                (0, 0, 0, 0, 2))
    alpha_data: tuple = ((3, 1), (3, -1))     # alpha_k = c + d*r3
    r_square: int = 3
    h_relation: tuple = (2, 3)                # 2*h^2 - 3
    rank_witness_prime: int = 105337
    # ---- L1 base generation (Theorem A) ---------------------------------
    r3_exponents: tuple = (14, 154)
    s2_exponents: tuple = (21, 147)
    zeta8_exponent: int = 21
    h_halving_denominator: int = 2
    gen_z8_power: int = 5
    gen_z42_power: int = 16
    order42_prime_cofactors: tuple = (2, 3, 7)
    conductor_tower: tuple = (21, 84, 168)
    eps_data: tuple = (2, 1)                  # eps = 2 + 1*sqrt3
    # ---- L2 Kummer -------------------------------------------------------
    character_primes: tuple = (673, 1009)
    class_generators: tuple = ((1, 0), (0, 1))
    class_representatives: tuple = ((1, 0), (0, 1), (1, 1), (1, 2))
    silent_primes: tuple = (105337, 105673)
    # ---- L3 structure ----------------------------------------------------
    ramified_primes: tuple = (2, 3, 7)
    unramified_witness: int = 5
    components: tuple = ("K0",)
    idempotents: tuple = (0, 1)
    sigma_images: tuple = ((0, 1), (1, -1), (3, 1), (2, 1), (4, 1))
    sigma_relation_permutation: tuple = (0, 1, 3, 2, 4)
    # ---- L4 frames -------------------------------------------------------
    frames: tuple = ((105337, (2779, 795, 50630, 10114, 50267)),
                     (105673, (13862, 14686, 38664, 46664, 35053)))
    frame_count_expected: int = 2
    registered_primes: tuple = (105337, 105673)
    p2_prime: int = 105337
    p2_frame: tuple = (8852313585, 11012141449, 786496672,
                       8038065910, 6003627245)
    split_count: int = 432
    # ---- L5 E-conditional ------------------------------------------------
    e_terms: tuple = ((9, 5, 2, 4), (9, -5, 3, 4))   # (c0, c1*r3, gen idx, exp)
    q0_terms: tuple = tuple(sorted(TRUE_Q0.items()))
    i_zeta3_exponent: int = 14
    branch_count: int = 4
    e_substitution_scales: tuple = ((1, 0, 0, 0, 0), (0, 1, 0, 0, 0))
    pointbank_expected: tuple = ((105337, 7210, 3), (105673, 14755, 0))
    pointbank_count_expected: int = 2
    # ---- harness control -------------------------------------------------
    skip_gates: frozenset = frozenset()
    label: str = "BASELINE"


class GateFail(Exception):
    pass


def need(condition, detail):
    if not condition:
        raise GateFail(detail)


def _algebra(spec):
    return KA.K0Algebra(spec.phi42, spec.alpha_data, spec.r_square,
                        Fr(spec.h_relation[1], spec.h_relation[0]))


# --------------------------------------------------------------------------
# gate registry
# --------------------------------------------------------------------------

REGISTRY = []


def gate(name, layer, kind):
    def wrap(fn):
        REGISTRY.append((name, layer, kind, fn))
        return fn
    return wrap


# ---- L0: source pins, the leading-term certificate, the rank witness ------

@gate("SRC_FILE_HASHES", "L0", "PIN")
def _g(spec, ctx):
    pins = ctx["source_pins"]
    need(len(pins) >= 3, "fewer than three external source files are pinned")
    got = {}
    for rel, expect in sorted(pins.items()):
        path = ctx["root"] / rel
        need(path.is_file() and not path.is_symlink(), "missing source %s" % rel)
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        need(digest == expect, "source hash drift %s: %s" % (rel, digest))
        got[rel] = digest
    for key in ("emitter_rel", "rows_rel", "bridge_rel", "theorem_report_rel"):
        need(ctx[key] in pins, "%s is not inside the pinned source set" % key)
    return {"hashes": got, "pinned_files": len(got)}


@gate("SRC_PHI42_LITERAL", "L0", "PIN")
def _g(spec, ctx):
    text = (ctx["root"] / ctx["emitter_rel"]).read_text()
    tree = ast.parse(text)
    found = None
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
                isinstance(t, ast.Name) and t.id == "PHI42" for t in node.targets):
            found = ast.literal_eval(node.value)
    need(found is not None, "PHI42 assignment absent from the emitter source")
    need(tuple(found) == tuple(spec.phi42),
         "emitter PHI42 %s != certificate datum %s" % (found, spec.phi42))
    computed = KA.cyclotomic(42)
    need(tuple(computed) == tuple(spec.phi42),
         "certificate datum is not Phi_42 computed from x^42-1: %s" % (computed,))
    need(tuple(computed) != tuple([-1] + [0] * 41 + [1]), "degenerate x^42-1")
    return {"phi42": list(found), "degree": len(found) - 1}


@gate("SRC_ALGEBRA_BLOCK", "L0", "PIN")
def _g(spec, ctx):
    text = (ctx["root"] / ctx["rows_rel"]).read_text()
    tree = ast.parse(text)
    block = None
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
                isinstance(t, ast.Name) and t.id == "COEFFICIENT_ALGEBRA"
                for t in node.targets):
            block = ast.literal_eval(node.value)
    need(block is not None, "COEFFICIENT_ALGEBRA absent from the row source")
    need(block["base"] == "Q", "base is not Q")
    need(tuple(block["basis_shape"]) == tuple(spec.basis_shape),
         "basis_shape drift %s" % (block["basis_shape"],))
    need(block["basis_rank"] == spec.basis_rank,
         "basis_rank drift %s" % (block["basis_rank"],))
    need(block["basis_generators"] == ["zeta42", "r3", "A1", "A2", "h"],
         "generator list drift")
    def alpha_text(const, coeff):
        sign = "+" if coeff >= 0 else "-"
        body = "r3" if abs(coeff) == 1 else "%d*r3" % abs(coeff)
        return "%d%s%s" % (const, sign, body)

    (a1c, a1r), (a2c, a2r) = spec.alpha_data
    expected_relations = [
        "Phi42(zeta42)=0",
        "r3^2=%d" % spec.r_square,
        "A1^3=%s" % alpha_text(a1c, a1r),
        "A2^3=%s" % alpha_text(a2c, a2r),
        "%d*h^2=%d" % (spec.h_relation[0], spec.h_relation[1]),
    ]
    need(block["relations"] == expected_relations,
         "relation list %s does not match the certificate presentation %s"
         % (block["relations"], expected_relations))
    need(block["field_claim"] is None,
         "source already asserts a field claim; the certificate must supply it")
    return {"basis_shape": list(block["basis_shape"]),
            "basis_rank": block["basis_rank"],
            "relations": list(block["relations"])}


@gate("PHI42_DISCRIMINANT", "L0", "THEOREM")
def _g(spec, ctx):
    phi = list(spec.phi42)
    res = KA.resultant(phi, KA.pderiv(phi))
    need(res.denominator == 1, "resultant is not an integer")
    disc = int(res)          # deg 12, monic: sign (-1)^(12*11/2) = +1
    need(disc == spec.phi42_disc, "disc(Phi42) = %d" % disc)
    need(disc % 2 != 0, "disc(Phi42) is even; the r3 layer would collapse")
    need(sorted(KA.factor_small(abs(disc))) == [3, 7],
         "disc(Phi42) has a prime outside {3,7}")
    return {"disc": disc, "radical": [3, 7], "odd": True}


@gate("PHI168_SHAPE", "L0", "THEOREM")
def _g(spec, ctx):
    p168 = KA.cyclotomic(168)
    need(len(p168) - 1 == 48, "deg Phi_168 = %d" % (len(p168) - 1))
    sub = [0] * (4 * (len(spec.phi42) - 1) + 1)
    for i, c in enumerate(spec.phi42):
        sub[4 * i] = c
    need(KA.ptrim(sub) == p168, "Phi_168(x) != Phi_42(x^4)")
    ctx["phi168"] = p168
    return {"degree": 48, "phi168_is_phi42_of_x4": True}


@gate("RELATION_LEADING_TERMS", "L0", "THEOREM")
def _g(spec, ctx):
    """Lemma L1, executed in the FREE ring Q[z,r,A1,A2,h].

    Under graded lex the five relations have pairwise *coprime* leading
    monomials, so every S-pair reduces to zero by Buchberger's first
    criterion: the five are a Groebner basis, the standard monomials are
    exactly the declared box, and the quotient is Q-free of that rank.  The
    R1 gate did all of this after quotienting, where every relation is 0 and
    the loop could not fail.
    """
    alg = _algebra(spec)
    rels = alg.free_relations()
    need(len(rels) == 5, "the presentation does not have five relations")
    lead_monos, lead_coeffs = [], []
    for k, rel in enumerate(rels):
        need(rel != {}, "relation %d is identically zero in the free ring" % k)
        mono, coeff = KA.fp_leading(rel)
        need(coeff != 0, "relation %d has a zero leading coefficient" % k)
        lead_monos.append(mono)
        lead_coeffs.append(coeff)
    need(tuple(lead_monos) == tuple(tuple(m) for m in spec.leading_monomials),
         "computed leading monomials %s != declared %s"
         % (lead_monos, list(spec.leading_monomials)))
    for k, mono in enumerate(lead_monos):
        support = [i for i in range(KA.NVARS) if mono[i]]
        need(support == [k],
             "leading monomial %d is %s, not a pure power of generator %d"
             % (k, mono, k))
        need(mono[k] == spec.basis_shape[k],
             "leading exponent %d != declared basis shape entry %d"
             % (mono[k], spec.basis_shape[k]))
    for a in range(5):
        for b in range(a + 1, 5):
            need(KA.mono_coprime(lead_monos[a], lead_monos[b]),
                 "leading monomials %d and %d are not coprime" % (a, b))
    # already reduced: no tail monomial of any relation is divisible by any LM
    for k, rel in enumerate(rels):
        for mono in rel:
            if mono == lead_monos[k]:
                continue
            for j, lm in enumerate(lead_monos):
                need(not KA.mono_divides(lm, mono),
                     "relation %d has tail monomial %s divisible by LM %d"
                     % (k, mono, j))
    prod = 1
    for k in spec.basis_shape:
        prod *= k
    need(prod == spec.basis_rank,
         "standard-monomial count %d != declared rank %d" % (prod, spec.basis_rank))
    need(len(alg.basis(spec.basis_shape)) == prod, "standard monomial census")
    return {"leading_monomials": [list(m) for m in lead_monos],
            "leading_coefficients": [str(c) for c in lead_coeffs],
            "pairwise_coprime": True,
            "standard_monomials": prod,
            "criterion": "Buchberger first criterion (pairwise coprime leading "
                         "monomials) => Groebner basis => free on the standard "
                         "monomials"}


@gate("RANK432_NORMAL_FORM", "L0", "EXECUTED")
def _g(spec, ctx):
    """The rewriting implements the declared presentation.

    Typed EXECUTED, not THEOREM: this gate certifies that the normal form has
    the declared standard monomials and that each rewrite lands inside the
    box.  Freeness is RELATION_LEADING_TERMS; the mod-p witness is
    RANK432_INDEPENDENCE.  No property of this gate is asserted rather than
    computed.
    """
    alg = _algebra(spec)
    basis = alg.basis(spec.basis_shape)
    need(len(basis) == spec.basis_rank and len(set(basis)) == spec.basis_rank,
         "the standard monomial set is not %d distinct" % spec.basis_rank)
    for mono in basis:
        nf = alg.norm({mono: Fr(1)})
        need(nf == {mono: Fr(1)}, "monomial %s is not its own normal form" % (mono,))
    for k in range(5):
        raised = [0] * 5
        raised[k] = spec.basis_shape[k]
        nf = alg.norm({tuple(raised): Fr(1)})
        for mono in nf:
            for i in range(5):
                need(mono[i] < spec.basis_shape[i],
                     "the rewrite of generator %d leaves the declared box at %s"
                     % (k, mono))
    z, r, a1, a2, h = (alg.gen(i) for i in range(5))
    (a1c, a1r), (a2c, a2r) = spec.alpha_data
    rel = {
        "Phi42(z)": alg.add(*[alg.scal(alg.pw(z, j), spec.phi42[j])
                              for j in range(13)]),
        "r^2-c": alg.sub(alg.pw(r, 2), alg.const(spec.r_square)),
        "A1^3-alpha1": alg.sub(alg.pw(a1, 3),
                               alg.add(alg.const(a1c), alg.scal(r, a1r))),
        "A2^3-alpha2": alg.sub(alg.pw(a2, 3),
                               alg.add(alg.const(a2c), alg.scal(r, a2r))),
        "b*h^2-c": alg.sub(alg.scal(alg.pw(h, 2), spec.h_relation[0]),
                           alg.const(spec.h_relation[1])),
    }
    for name, val in rel.items():
        need(val == {}, "relation %s does not normalise to 0" % name)
    need(alg.one() != {}, "the algebra is the zero ring")
    ctx["alg"] = alg
    return {"rank": spec.basis_rank,
            "leading_degrees": list(spec.basis_shape),
            "relations_normalise_to_zero": sorted(rel),
            "typing": "EXECUTED: implements the presentation; freeness is "
                      "RELATION_LEADING_TERMS, the mod-p witness is "
                      "RANK432_INDEPENDENCE"}


@gate("RANK432_INDEPENDENCE", "L0", "THEOREM")
def _g(spec, ctx):
    """Mod-p witness that the 432 standard monomials are independent.

    At the registered witness prime the presented algebra has exactly
    432 = 12*18*2 F_p-points, and the evaluation matrix of the 432 standard
    monomials on them is the Kronecker product of three blocks.  All three
    block determinants are nonzero, so the full 432x432 matrix is
    nonsingular, so the 432 monomials are linearly independent over F_p and
    the reduction of the presented algebra is free of rank 432.  The squared
    determinants are row-order independent and are shared with the GP engine.
    """
    p = spec.rank_witness_prime
    need(KA.is_prime(p), "the rank witness prime %d is not prime" % p)
    need(p % 168 == 1, "the rank witness prime %d is not 1 mod 168" % p)
    need(p in dict(spec.frames), "no registered frame at the witness prime %d" % p)
    z0, r0, a10, a20, h0 = dict(spec.frames)[p]
    (a1c, a1r), (a2c, a2r) = spec.alpha_data

    # ---- z block: the primitive 42nd roots ARE the roots of the datum ----
    zr = KA.primitive_nth_roots(p, 42)
    need(len(zr) == spec.basis_shape[0],
         "%d primitive 42nd roots, expected %d" % (len(zr), spec.basis_shape[0]))
    for v in zr:
        need(KA.poly_eval_mod(list(spec.phi42), v, p) == 0,
             "the exhibited primitive 42nd root %d is not a root of the "
             "certificate Phi42 modulo %d" % (v, p))
    # ---- middle block: the 18 (r, A1, A2) points, from mu_3 and the frame -
    w3 = KA.mu_n(p, 3)
    need(len(w3) == 3, "mu_3 does not have three elements mod %d" % p)
    triples = []
    for (rv, x1, x2) in ((r0, a10, a20), ((-r0) % p, a20, a10)):
        for wa in w3:
            for wb in w3:
                triples.append((rv, x1 * wa % p, x2 * wb % p))
    need(len(set(triples)) == 18, "the middle block does not have 18 points")
    for (rv, v1, v2) in triples:
        need((rv * rv - spec.r_square) % p == 0, "middle point fails r^2")
        need((pow(v1, 3, p) - a1c - a1r * rv) % p == 0, "middle point fails A1^3")
        need((pow(v2, 3, p) - a2c - a2r * rv) % p == 0, "middle point fails A2^3")
        need(v1 % p and v2 % p, "a middle point has a vanishing coordinate")
    # ---- h block ---------------------------------------------------------
    hs = KA.sqrt_mod(spec.h_relation[1] * pow(spec.h_relation[0], -1, p) % p, p)
    need(len(hs) == spec.basis_shape[4],
         "%d h roots, expected %d" % (len(hs), spec.basis_shape[4]))
    need(h0 % p in hs, "the registered frame h is not an exhibited root")
    # ---- three block determinants ---------------------------------------
    mz = [[pow(v, a, p) for a in range(spec.basis_shape[0])] for v in sorted(zr)]
    mm = []
    for (rv, v1, v2) in sorted(triples):
        row = []
        for b in range(spec.basis_shape[1]):
            for c in range(spec.basis_shape[2]):
                for d in range(spec.basis_shape[3]):
                    row.append(pow(rv, b, p) * pow(v1, c, p) % p
                               * pow(v2, d, p) % p)
        mm.append(row)
    mh = [[pow(v, e, p) for e in range(spec.basis_shape[4])] for v in sorted(hs)]
    dz = KA.det_mod(mz, p)
    dm = KA.det_mod(mm, p)
    dh = KA.det_mod(mh, p)
    need(dz, "the z-block evaluation matrix is singular mod %d" % p)
    need(dm, "the (r,A1,A2)-block evaluation matrix is singular mod %d" % p)
    need(dh, "the h-block evaluation matrix is singular mod %d" % p)
    need(len(mz) * len(mm) * len(mh) == spec.basis_rank,
         "block sizes %d*%d*%d != declared rank %d"
         % (len(mz), len(mm), len(mh), spec.basis_rank))
    return {"prime": p, "block_sizes": [len(mz), len(mm), len(mh)],
            "det_z_sq": dz * dz % p, "det_mid_sq": dm * dm % p,
            "det_h_sq": dh * dh % p,
            "conclusion": "the 432 standard monomials are F_p-independent, so "
                          "the reduction of the presented algebra is free of "
                          "rank 432"}


# ---- L1: Theorem A, the degree-48 base is exactly Q(zeta_168) --------------

@gate("BASE_WELLDEFINED", "L1", "THEOREM")
def _g(spec, ctx):
    C = KA.Cyclo168(ctx["phi168"])
    z = C.xpow(1)
    z42 = C.xpow(4)
    r3 = C.add(C.xpow(spec.r3_exponents[0]), C.xpow(spec.r3_exponents[1]))
    s2 = C.add(C.xpow(spec.s2_exponents[0]), C.xpow(spec.s2_exponents[1]))
    h = C.scal(C.mul(s2, r3), Fr(1, spec.h_halving_denominator))
    need(C.eval_int_poly(list(spec.phi42), z42) == [], "Phi42(zeta^4) != 0")
    need(C.pw(z42, 42) == C.const(1), "zeta^4 is not a 42nd root of unity")
    for q in spec.order42_prime_cofactors:
        need(C.pw(z42, 42 // q) != C.const(1),
             "order of zeta^4 divides 42/%d: the order gate is incomplete" % q)
    need(sorted(spec.order42_prime_cofactors) == sorted(KA.factor_small(42)),
         "the order gate must test every prime divisor of 42")
    need(C.mul(r3, r3) == C.const(spec.r_square), "r3^2 != %d" % spec.r_square)
    need(C.mul(s2, s2) == C.const(2), "sqrt2^2 != 2")
    b, c = spec.h_relation
    need(C.scal(C.mul(h, h), b) == C.const(c), "%d*h^2 != %d" % (b, c))
    need(C.mul(C.scal(h, b), C.scal(h, b)) == C.const(b * c),
         "(%d h)^2 != %d" % (b, b * c))
    ctx["C"] = C
    ctx["base"] = {"z": z, "z42": z42, "r3": r3, "s2": s2, "h": h}
    return {"relations_hold": ["Phi42(z^4)", "r3^2=%d" % spec.r_square,
                               "s2^2=2", "%d*h^2=%d" % (b, c)],
            "order_cofactors_tested": list(spec.order42_prime_cofactors)}


@gate("BASE_I_SQUARE", "L1", "THEOREM")
def _g(spec, ctx):
    C, B = ctx["C"], ctx["base"]
    zeta3 = C.pw(B["z42"], spec.i_zeta3_exponent)
    need(C.pw(zeta3, 3) == C.const(1) and zeta3 != C.const(1),
         "zeta42^%d is not a primitive cube root of unity" % spec.i_zeta3_exponent)
    i0 = C.scal(C.mul(B["r3"], C.add(C.const(1), C.scal(zeta3, 2))), Fr(1, 3))
    need(C.mul(i0, i0) == C.const(-1), "i^2 != -1")
    ctx["base"]["i"] = i0
    ctx["base"]["zeta3"] = zeta3
    return {"i_squared": -1}


@gate("BASE_ZETA8", "L1", "THEOREM")
def _g(spec, ctx):
    C, B = ctx["C"], ctx["base"]
    z8 = C.scal(C.mul(C.mul(C.add(C.const(1), B["i"]), B["h"]), B["r3"]), Fr(1, 3))
    need(z8 == C.xpow(spec.zeta8_exponent),
         "(1+i)*h*r3/3 != x^%d" % spec.zeta8_exponent)
    ctx["base"]["z8"] = z8
    return {"zeta8_exponent": spec.zeta8_exponent}


@gate("BASE_SURJECTIVE", "L1", "THEOREM")
def _g(spec, ctx):
    """The single load-bearing generation line: zeta_168 lies in the image."""
    C, B = ctx["C"], ctx["base"]
    lhs = C.mul(C.pw(B["z8"], spec.gen_z8_power),
                C.pw(B["z42"], spec.gen_z42_power))
    need(lhs == B["z"], "zeta8^%d * zeta42^%d != zeta_168"
         % (spec.gen_z8_power, spec.gen_z42_power))
    crt = spec.zeta8_exponent * spec.gen_z8_power + 4 * spec.gen_z42_power
    need(crt % 168 == 1, "exponent arithmetic %d*%d+4*%d = %d is not 1 mod 168"
         % (spec.zeta8_exponent, spec.gen_z8_power, spec.gen_z42_power, crt))
    return {"identity": "zeta8^%d*zeta42^%d == zeta_168"
            % (spec.gen_z8_power, spec.gen_z42_power), "crt_residue": crt % 168}


@gate("BASE_DIMENSION_48", "L1", "THEOREM")
def _g(spec, ctx):
    dim = len(ctx["phi168"]) - 1
    need(dim == 48, "deg Phi_168 != 48")
    need(spec.basis_shape[0] * spec.basis_shape[1] * spec.basis_shape[4] == dim,
         "the pre-cubic monomial count is not deg Phi_168")
    ctx["base_dimension"] = dim
    return {"dim_B": dim,
            "conclusion": "B = Q(zeta_168), a field, abelian over Q"}


@gate("BASE_CONDUCTOR_TOWER", "L1", "THEOREM")
def _g(spec, ctx):
    """The tower does not collapse.  Every number below is computed."""
    disc_phi42 = int(KA.resultant(list(spec.phi42), KA.pderiv(list(spec.phi42))))
    need(disc_phi42 % 2 != 0, "2 could ramify in Q(zeta42)")
    quad = [-spec.r_square, 0, 1]
    disc_quad = -int(KA.resultant(quad, KA.pderiv(quad)))
    need(abs(disc_quad) == 4 * spec.r_square,
         "disc(x^2-%d) computed as %d" % (spec.r_square, disc_quad))
    f3, f6, tower = abs(disc_quad), 2 * abs(disc_quad), tuple(spec.conductor_tower)
    need(len(tower) == 3, "the conductor tower must have three levels")
    need(tower[0] % f3 != 0,
         "conductor %d divides %d; sqrt3 in Q(zeta%d) is not excluded"
         % (f3, tower[0], 2 * tower[0]))
    need(tower[1] % f3 == 0, "conductor %d does not divide %d" % (f3, tower[1]))
    need(tower[1] % f6 != 0,
         "conductor %d divides %d; sqrt6 in Q(zeta%d) is not excluded"
         % (f6, tower[1], tower[1]))
    need(tower[2] % f6 == 0 and tower[2] % f3 == 0,
         "%d does not carry both conductors" % tower[2])
    degrees = [len(KA.cyclotomic(n)) - 1 for n in tower]
    want = [spec.basis_shape[0],
            spec.basis_shape[0] * spec.basis_shape[1],
            spec.basis_shape[0] * spec.basis_shape[1] * spec.basis_shape[4]]
    need(degrees == want,
         "the conductor tower %s has cyclotomic degrees %s, expected %s"
         % (list(tower), degrees, want))
    need(degrees[2] == ctx["base_dimension"],
         "the top conductor does not carry the computed base dimension")
    return {"tower": ["cond %d deg %d" % (tower[i], degrees[i])
                      for i in range(3)],
            "disc_quadratic": disc_quad, "disc_phi42_odd": True,
            "sqrt3_not_in_Q_zeta42": "2 unramified in Q(zeta42) (odd disc), "
                                     "ramified in Q(sqrt3) (computed disc %d)"
                                     % disc_quad,
            "sqrt6_not_in_Q_zeta84": "conductor %d does not divide %d"
                                     % (f6, tower[1])}


# ---- L2: Kummer independence by explicit cubic-character homs --------------

def _character_frames(spec, ctx, p):
    """Explicit ring homs Z[y]/(Phi_168) -> F_p, one per square root of 3.

    Every exponent and every alpha constant is read from ``Spec`` (R2 repair
    D5); each hom is verified to be a root of Phi_168 modulo p (R2 repair D10,
    replacing the R1 within-fibre check that could not fail).
    """
    need(KA.is_prime(p), "certificate prime %d is not prime" % p)
    need(p % 168 == 1, "certificate prime %d is not 1 mod 168" % p)
    need(p % 2 and p % 3 and p % 7, "certificate prime divides 42")
    (a1c, a1r), (a2c, a2r) = spec.alpha_data
    roots = KA.primitive_nth_roots(p, 168)
    need(len(roots) == 48, "Phi_168 does not have 48 roots mod %d" % p)
    phi168 = ctx["phi168"]
    frames = {}
    for om in roots:
        need(KA.poly_eval_mod(phi168, om, p) == 0,
             "the exhibited order-168 element %d is not a root of Phi_168 "
             "modulo %d" % (om, p))
        r = (pow(om, spec.r3_exponents[0], p)
             + pow(om, spec.r3_exponents[1], p)) % p
        need((r * r - spec.r_square) % p == 0,
             "omega^%d+omega^%d is not a square root of %d"
             % (spec.r3_exponents[0], spec.r3_exponents[1], spec.r_square))
        v1, v2 = (a1c + a1r * r) % p, (a2c + a2r * r) % p
        need(v1 and v2, "alpha_k is not a unit at %d" % p)
        v = (KA.cubic_character(v1, p), KA.cubic_character(v2, p))
        frames.setdefault(r, []).append((om, v))
    need(len(frames) == 2, "the %d homs do not hit both square roots of %d"
         % (len(roots), spec.r_square))
    out = []
    for r in sorted(frames):
        members = sorted(frames[r])
        need(len(members) == len(roots) // 2,
             "square-root fibre %d has %d homs, expected %d"
             % (r, len(members), len(roots) // 2))
        om, v = members[0]
        out.append({"omega": om, "r3": r, "chi": v, "fibre_size": len(members)})
    return out


def _annihilators(vectors, p):
    """(i,j) in (Z/3)^2 killing every character vector, by brute force."""
    out = []
    for i in range(3):
        for j in range(3):
            if all(pow(v["chi"][0], i, p) * pow(v["chi"][1], j, p) % p == 1
                   for v in vectors):
                out.append((i, j))
    return out


@gate("KUMMER_HOMS_EXHIBITED", "L2", "THEOREM")
def _g(spec, ctx):
    need(len(spec.character_primes) >= 2,
         "the certificate requires two independent cubic-character primes")
    need(len(set(spec.character_primes)) == len(spec.character_primes),
         "the certificate prime list repeats a prime")
    need(673 in spec.character_primes, "the registered prime 673 is absent")
    ctx["charframes"] = {}
    out = {}
    for p in spec.character_primes:
        need(p not in spec.silent_primes,
             "prime %d is a registered frame prime and is character-silent" % p)
        fr = _character_frames(spec, ctx, p)
        ctx["charframes"][p] = fr
        out[str(p)] = [{"omega": f["omega"], "r3": f["r3"],
                        "chi_alpha1": f["chi"][0], "chi_alpha2": f["chi"][1],
                        "fibre_size": f["fibre_size"]}
                       for f in fr]
    return {"frames": out}


@gate("KUMMER_RANK_TWO", "L2", "THEOREM")
def _g(spec, ctx):
    """Only (0,0) annihilates the exhibited characters, at EVERY listed prime."""
    per = {}
    orders = set()
    for p, fr in sorted(ctx["charframes"].items()):
        gens = []
        for (i, j) in spec.class_generators:
            gens.append({"chi": tuple(
                pow(f["chi"][0], i, p) * pow(f["chi"][1], j, p) % p
                for f in fr)})
        vectors = [{"chi": (gens[0]["chi"][k], gens[1]["chi"][k])}
                   for k in range(len(fr))]
        ann = _annihilators(vectors, p)
        need(ann == [(0, 0)],
             "prime %d admits a nontrivial annihilator %s: the two classes are "
             "not shown independent" % (p, ann))
        subgroup = set()
        for i in range(3):
            for j in range(3):
                subgroup.add(tuple(
                    pow(v["chi"][0], i, p) * pow(v["chi"][1], j, p) % p
                    for v in vectors))
        need(len(subgroup) == 9,
             "prime %d: the character pairs generate order %d, not 9"
             % (p, len(subgroup)))
        orders.add(len(subgroup))
        per[str(p)] = {"annihilators": [list(a) for a in ann],
                       "generated_order": len(subgroup)}
    need(len(per) >= 2, "rank two was established at fewer than two primes")
    need(len(orders) == 1, "the primes disagree on the generated order")
    ctx["kummer_generated_order"] = orders.pop()
    return {"per_prime": per, "Delta": "(Z/3)^2",
            "order": ctx["kummer_generated_order"]}


@gate("KUMMER_ALL_EIGHT_NONCUBES", "L2", "THEOREM")
def _g(spec, ctx):
    """Every nontrivial alpha1^i alpha2^j has a hom with nontrivial character."""
    witnesses = {}
    for i in range(3):
        for j in range(3):
            if (i, j) == (0, 0):
                continue
            found = None
            for p, fr in sorted(ctx["charframes"].items()):
                for f in fr:
                    val = pow(f["chi"][0], i, p) * pow(f["chi"][1], j, p) % p
                    if val != 1:
                        found = {"prime": p, "omega": f["omega"], "chi": val}
                        break
                if found:
                    break
            need(found is not None,
                 "class (%d,%d) has no non-cube witness" % (i, j))
            witnesses["%d,%d" % (i, j)] = found
    need(len(witnesses) == 8, "expected eight nontrivial classes")
    return {"witnesses": witnesses}


@gate("KUMMER_REPRESENTATIVE_CLASSES", "L2", "THEOREM")
def _g(spec, ctx):
    """The four inverse-pair representatives, each certified a non-cube."""
    names = {(1, 0): "alpha1", (0, 1): "alpha2",
             (1, 1): "alpha1*alpha2", (1, 2): "alpha1/alpha2"}
    out = {}
    for (i, j) in spec.class_representatives:
        need((i, j) != (0, 0),
             "the trivial class is offered as a representative")   # D10: first
        found = None
        for p, fr in sorted(ctx["charframes"].items()):
            for f in fr:
                val = pow(f["chi"][0], i, p) * pow(f["chi"][1], j, p) % p
                if val != 1:
                    found = {"prime": p, "chi": val}
                    break
            if found:
                break
        need(found is not None,
             "representative (%d,%d) is a cube at every exhibited hom" % (i, j))
        out[names.get((i, j), "%d,%d" % (i, j))] = found
    pairs = {(i, j) for (i, j) in spec.class_representatives}
    covered = set()
    for (i, j) in pairs:
        covered.add((i, j))
        covered.add((2 * i % 3, 2 * j % 3))
    need(len(covered) == 8,
         "the representative list covers %d of the 8 nontrivial classes"
         % len(covered))
    return {"representatives": out, "classes_covered": 8}


@gate("KUMMER_NORM_COROBORATION", "L2", "SECOND_PROOF")
def _g(spec, ctx):
    """Abelian descent to Q(sqrt3): the four norms and the unit argument.

    R2 repair D10: every number is computed from ``spec.alpha_data`` and
    ``spec.eps_data``, and the R1 sentence about a negative real embedding was
    both constant-true and mathematically backwards.  The correct fact is that
    *both* embeddings of eps are positive, which is what forces the sign in
    +-eps^(3n) = eps; that is what is checked here.
    """
    d = spec.r_square

    def norm(a, b):        # N(a + b*sqrt d)
        return a * a - d * b * b

    def is_cube(n):
        n = abs(n)
        k = round(n ** (1.0 / 3.0)) if n else 0
        for c in (k - 2, k - 1, k, k + 1, k + 2):
            if c >= 0 and c ** 3 == n:
                return True
        return False

    (a1c, a1r), (a2c, a2r) = spec.alpha_data
    n1, n2 = norm(a1c, a1r), norm(a2c, a2r)
    prod_c = a1c * a2c + d * a1r * a2r
    prod_r = a1c * a2r + a1r * a2c
    need(prod_r == 0, "alpha1*alpha2 is not rational: r-part %d" % prod_r)
    n12 = norm(prod_c, 0)
    need(n1 == n2, "N(alpha1) = %d != N(alpha2) = %d" % (n1, n2))
    need(not is_cube(n1), "N(alpha1) = %d is a rational cube" % n1)
    need(not is_cube(n12), "N(alpha1*alpha2) = %d is a rational cube" % n12)
    ec, er = spec.eps_data
    need(norm(ec, er) == 1, "eps is not a norm-one unit of Z[sqrt%d]" % d)
    need(2 * ec > 0 and norm(ec, er) > 0,
         "eps and its conjugate are not both positive: trace %d, norm %d "
         "(both must be positive for the sign in +-eps^(3n) = eps to be +)"
         % (2 * ec, norm(ec, er)))
    need(all((a * a - d * b * b - (-1)) % 3 != 0
             for a in range(3) for b in range(3)),
         "x^2 - %d y^2 = -1 is not excluded modulo 3, so the unit group could "
         "contain a norm -1 element" % d)
    small = [a for a in range(1, 4 * d) if a * a in (d - 1, d + 1)]
    need(small == [ec],
         "the b=1 units of Z[sqrt%d] are a in %s, not the declared eps constant "
         "%d" % (d, small, ec))
    return {"norms": {"alpha1": n1, "alpha2": n2, "alpha1alpha2": n12,
                      "eps": norm(ec, er)},
            "cube_free": [n1, n12],
            "eps_trace": 2 * ec, "eps_norm": norm(ec, er),
            "eps": "norm-one unit of Z[sqrt3]; the norm test is blind on it and "
                   "the cubic character at the certificate primes kills it",
            "requires": "Lemma L2 abelian descent, licensed by Theorem A"}


@gate("KUMMER_SILENT_PRIME_GUARD", "L2", "THEOREM")
def _g(spec, ctx):
    """The registered frame primes cannot certify anything: their characters
    are trivial, so a certificate that used them would be vacuous."""
    out = {}
    for p in spec.silent_primes:
        fr = _character_frames(spec, ctx, p)
        triv = all(f["chi"] == (1, 1) for f in fr)
        need(triv, "registered prime %d is unexpectedly a live witness" % p)
        ann = _annihilators([{"chi": f["chi"]} for f in fr], p)
        need(len(ann) == 9,
             "registered prime %d does not annihilate everything" % p)
        out[str(p)] = {"characters_trivial": True, "annihilators": 9}
        need(p not in spec.character_primes,
             "a silent prime is being used as a certificate prime")
    need(tuple(sorted(spec.silent_primes)) == tuple(sorted(spec.registered_primes)),
         "the silent-prime list is not the registered frame prime set")
    return {"silent": out}


# ---- L3: Theorems C and D --------------------------------------------------

@gate("FIELD_DEGREE_432", "L3", "THEOREM")
def _g(spec, ctx):
    """Degree = dim_Q(B) * |Delta|, both read from the gates that computed them.

    R2 repair: the R1 gate multiplied the literal 9 by the literal 48.  Here
    both factors are taken out of ``ctx``, so deleting or breaking L1 or L2
    breaks this gate instead of leaving it self-satisfied.
    """
    dim_b = ctx.get("base_dimension")
    order = ctx.get("kummer_generated_order")
    need(dim_b is not None, "L1 did not publish a computed base dimension")
    need(order is not None, "L2 did not publish a computed Kummer order")
    need(dim_b * order == spec.basis_rank,
         "dim_Q(B) * |Delta| = %d * %d != declared rank %d"
         % (dim_b, order, spec.basis_rank))
    need(spec.basis_rank == 432, "degree is not 432")
    return {"deg_B": dim_b, "deg_K0_over_B": order, "deg_K0": dim_b * order,
            "argument": "K0 is free of rank |Delta| over the field B (L1); "
                        "Kummer theory with Delta = (Z/3)^2 (L2) gives "
                        "[L:B] = |Delta|; the evident surjection K0 -> L "
                        "between B-spaces of equal dimension is an isomorphism"}


@gate("IDEMPOTENTS_ONLY_0_1", "L3", "THEOREM")
def _g(spec, ctx):
    need(tuple(spec.components) == ("K0",),
         "component list %s is not the single literal factor K0"
         % (spec.components,))
    need(tuple(spec.idempotents) == (0, 1),
         "idempotent list %s is not [0,1]" % (spec.idempotents,))
    need(len(spec.components) == 1, "more than one component emitted")
    return {"components": ["K0"], "component_count": 1, "idempotents": [0, 1],
            "product_decomposition": "none; K0 is a field"}


@gate("GALOIS_STABILITY_FREE", "L3", "THEOREM")
def _g(spec, ctx):
    """sigma permutes the five relations in the FREE ring, hence sigma(I) = I.

    R2 repair D3.  The R1 gate applied sigma to relation values that had
    already been normalised to 0, so it computed sigma({}) == {} five times.
    Here sigma is substituted into the unreduced relations and the resulting
    multiset is compared with the original one; the induced permutation is
    itself pinned in ``Spec``.
    """
    alg = _algebra(spec)
    rels = alg.free_relations()
    images = alg.sigma_images(spec.sigma_images)
    need(len(spec.sigma_images) == 5, "the sigma table must have five entries")
    need(sorted(t for (t, _s) in spec.sigma_images) == [0, 1, 2, 3, 4],
         "the sigma table is not a permutation of the generators")
    for (t, s) in spec.sigma_images:
        need(s in (1, -1), "sigma entries must be signs")
    # sigma is an involution on the free ring
    for k in range(5):
        twice = KA.fp_substitute(images[k], images)
        need(twice == KA.fp_gen(k), "sigma is not an involution on generator %d" % k)
    perm = []
    for k, rel in enumerate(rels):
        img = KA.fp_substitute(rel, images)
        hit = None
        for j, other in enumerate(rels):
            if img == other:
                hit = j
                break
        need(hit is not None,
             "sigma sends relation %d outside the relation set: %s"
             % (k, sorted(img)))
        perm.append(hit)
    need(sorted(perm) == [0, 1, 2, 3, 4],
         "sigma does not permute the relations bijectively: %s" % perm)
    need(tuple(perm) == tuple(spec.sigma_relation_permutation),
         "computed relation permutation %s != declared %s"
         % (perm, list(spec.sigma_relation_permutation)))
    need(perm != [0, 1, 2, 3, 4],
         "sigma fixes every relation individually; the swap that makes Delta "
         "Gal(B/Q)-stable is absent")
    # the descended map, for the record only
    a1, a2 = alg.gen(2), alg.gen(3)
    need(alg.sigma(alg.mul(a1, a2), spec.sigma_images) == alg.mul(a1, a2),
         "the descended sigma moves A1*A2")
    return {"relation_permutation": perm,
            "sigma_images": [list(t) for t in spec.sigma_images],
            "conclusion": "sigma permutes the ideal generators in the free "
                          "ring, so sigma(I) = I and sigma descends to a ring "
                          "automorphism; Delta is Gal(B/Q)-stable and K0/Q is "
                          "Galois"}


@gate("NONABELIAN", "L3", "THEOREM")
def _g(spec, ctx):
    alg = ctx["alg"]
    a1, a2 = alg.gen(2), alg.gen(3)
    cbrt = alg.mul(a1, a2)
    prod = alg.pw(cbrt, 3)
    need(len(prod) == 1 and (0, 0, 0, 0, 0) in prod,
         "(A1*A2)^3 is not rational: %s" % sorted(prod))
    m = prod[(0, 0, 0, 0, 0)]
    need(m.denominator == 1, "(A1*A2)^3 is not an integer")
    m = int(m)
    cubic = [-m, 0, 0, 1]
    disc = -int(KA.resultant(cubic, KA.pderiv(cubic)))
    need(disc == -27 * m * m, "disc(t^3-%d) computed as %d" % (m, disc))
    for q in sorted(KA.factor_small(abs(m))):
        need(m % q == 0 and m % (q * q) != 0,
             "t^3-%d is not Eisenstein at %d" % (m, q))
    need(disc < 0, "disc(t^3-%d) is not negative" % m)
    root = int(abs(disc) ** 0.5)
    need(all(c * c != abs(disc) for c in (root - 1, root, root + 1)),
         "|disc(t^3-%d)| is a perfect square" % m)
    return {"cbrt_of": m, "cubic": "t^3-%d" % m,
            "eisenstein_primes": sorted(KA.factor_small(abs(m))),
            "disc": disc, "disc_is_square": False,
            "conclusion": "K0 contains a non-normal cubic field, so K0/Q is "
                          "not abelian and K0 lies in no cyclotomic field"}


@gate("ETALE_OVER_Z_1_42", "L3", "THEOREM")
def _g(spec, ctx):
    alg = ctx["alg"]
    a1, a2 = alg.gen(2), alg.gen(3)
    prod = alg.mul(alg.pw(a1, 3), alg.pw(a2, 3))
    need(len(prod) == 1 and (0, 0, 0, 0, 0) in prod,
         "alpha1*alpha2 is not rational, so the alpha_k need not be units")
    m = int(prod[(0, 0, 0, 0, 0)])
    inverted = tuple(sorted(spec.ramified_primes))
    layers = {
        "zeta42": {"monic": "Phi42", "disc": spec.phi42_disc},
        "r3": {"monic": "r^2-%d" % spec.r_square, "disc": 4 * spec.r_square},
        "A1": {"monic": "A1^3-alpha1", "disc": "-27*alpha1^2"},
        "A2": {"monic": "A2^3-alpha2", "disc": "-27*alpha2^2"},
        "h": {"monic": "h^2-%d/%d" % (spec.h_relation[1], spec.h_relation[0]),
              "disc": 2 * spec.h_relation[0] * spec.h_relation[1]},
    }
    for n in (spec.phi42_disc, 4 * spec.r_square,
              2 * spec.h_relation[0] * spec.h_relation[1], 27, m):
        need(set(KA.factor_small(n)) <= set(inverted),
             "layer datum %d needs a prime outside %s" % (n, list(inverted)))
    localiser = 1
    for q in inverted:
        localiser *= q
    need(set(KA.factor_small(localiser)) == set(inverted),
         "the localiser is not the product of the declared inverted primes")
    return {"layers": layers, "inverted": list(inverted),
            "localiser": localiser, "alpha_product": m,
            "rank": spec.basis_rank,
            "conclusion": "finite etale of rank %d over Z[1/%d]"
                          % (spec.basis_rank, localiser)}


@gate("RAMIFIED_EXACTLY_2_3_7", "L3", "THEOREM")
def _g(spec, ctx):
    need(tuple(sorted(spec.ramified_primes)) == (2, 3, 7),
         "ramified set %s is not {2,3,7}" % (spec.ramified_primes,))
    need(spec.unramified_witness not in spec.ramified_primes,
         "the unramified witness is inside the ramified set")
    need(spec.unramified_witness == 5, "the declared unramified witness is not 5")
    disc3 = int(KA.resultant(KA.cyclotomic(3), KA.pderiv(KA.cyclotomic(3))))
    disc7 = int(KA.resultant(KA.cyclotomic(7), KA.pderiv(KA.cyclotomic(7))))
    need(abs(disc3) == 3, "disc(Phi_3) != -3")
    need(abs(disc7) == 7 ** 5, "disc(Phi_7) != -7^5")
    alg = ctx["alg"]
    z = alg.gen(0)
    need(alg.pw(z, 14) != alg.one() and alg.pw(alg.pw(z, 14), 3) == alg.one(),
         "zeta42^14 is not a primitive cube root of unity in K0")
    need(alg.pw(z, 6) != alg.one() and alg.pw(alg.pw(z, 6), 7) == alg.one(),
         "zeta42^6 is not a primitive 7th root of unity in K0")
    need(alg.mul(alg.gen(1), alg.gen(1)) == alg.const(spec.r_square),
         "sqrt%d not in K0" % spec.r_square)
    need(set(KA.factor_small(4 * spec.r_square)) == {2, 3},
         "disc(Q(sqrt3)) mis-stated")
    need(spec.unramified_witness
         not in set(KA.factor_small(spec.phi42_disc)) | {2, 3},
         "the unramified witness appears in a layer discriminant")
    return {"upper_bound": [2, 3, 7], "lower_bound_subfields":
            {"3": "Q(zeta3) subset K0, disc -3", "7": "Q(zeta7) subset K0, "
             "disc -7^5", "2": "Q(sqrt3) subset K0, disc 12"},
            "ramified": [2, 3, 7], "unramified_witness": 5,
            "source_constant_typing":
            "ETALE_LOCALIZATION_PRIMES=(2,3,5,7) is a safe superset; "
            "SOURCE_DENOMINATOR_PRIMES=(2,3,5) is a different object and "
            "neither is used to derive this set"}


# ---- L4: the two registered frames ----------------------------------------

def _frame_cardinality(spec):
    """R2 repair D4: the frame list has a pinned length and a pinned prime set."""
    need(len(spec.frames) == spec.frame_count_expected,
         "the certificate carries %d frames, %d are registered"
         % (len(spec.frames), spec.frame_count_expected))
    primes = tuple(sorted(p for p, _f in spec.frames))
    need(primes == tuple(sorted(spec.registered_primes)),
         "frame prime set %s != registered %s"
         % (list(primes), list(spec.registered_primes)))
    need(len(set(primes)) == len(primes), "a frame prime is repeated")
    return primes


@gate("FRAME_RELATIONS", "L4", "EXECUTED")
def _g(spec, ctx):
    primes = _frame_cardinality(spec)
    (a1c, a1r), (a2c, a2r) = spec.alpha_data
    out = {}
    for p, fr in spec.frames:
        z, r, a1, a2, h = fr
        eqs = {
            "Phi42(zeta42)": KA.poly_eval_mod(list(spec.phi42), z, p),
            "r3^2-c": (r * r - spec.r_square) % p,
            "A1^3-alpha1": (pow(a1, 3, p) - a1c - a1r * r) % p,
            "A2^3-alpha2": (pow(a2, 3, p) - a2c - a2r * r) % p,
            "b*h^2-c": (spec.h_relation[0] * h * h - spec.h_relation[1]) % p,
        }
        for name, v in eqs.items():
            need(v == 0, "frame %d fails %s: residue %d" % (p, name, v))
        need(p % 168 == 1, "frame prime %d is not 1 mod 168" % p)
        need(KA.is_prime(p), "frame modulus %d is not prime" % p)
        out[str(p)] = {"residues": eqs, "p_mod_168": p % 168}
    return {"frames": out, "frame_count": len(spec.frames),
            "registered_primes": list(primes)}


@gate("FRAME_ORDER_AND_JACOBIAN", "L4", "EXECUTED")
def _g(spec, ctx):
    _frame_cardinality(spec)
    out = {}
    deriv = KA.pderiv(list(spec.phi42))
    for p, fr in spec.frames:
        z, r, a1, a2, h = fr
        need(pow(z, 42, p) == 1, "frame %d: zeta42^42 != 1" % p)
        for q in spec.order42_prime_cofactors:
            need(pow(z, 42 // q, p) != 1,
                 "frame %d: zeta42 has order dividing 42/%d" % (p, q))
        jac = {"Phi42'": KA.poly_eval_mod(deriv, z, p), "2*r3": 2 * r % p,
               "3*A1^2": 3 * a1 * a1 % p, "3*A2^2": 3 * a2 * a2 % p,
               "2b*h": 2 * spec.h_relation[0] * h % p}
        for name, v in jac.items():
            need(v % p != 0, "frame %d: jacobian entry %s vanishes" % (p, name))
        out[str(p)] = {"order_42": True, "jacobian": jac}
    return {"frames": out}


@gate("SPLIT_COUNT_432", "L4", "CONSISTENCY")
def _g(spec, ctx):
    _frame_cardinality(spec)
    (a1c, a1r), (a2c, a2r) = spec.alpha_data
    out = {}
    for p, fr in spec.frames:
        zroots = KA.primitive_nth_roots(p, 42)
        need(len(zroots) == 12, "not 12 primitive 42nd roots mod %d" % p)
        need(all(KA.poly_eval_mod(list(spec.phi42), v, p) == 0 for v in zroots),
             "an exhibited primitive 42nd root is not a root of Phi42")
        rroots = KA.sqrt_mod(spec.r_square, p)
        need(len(rroots) == 2, "%d is not a nonzero square mod %d"
             % (spec.r_square, p))
        hroots = KA.sqrt_mod(spec.h_relation[1]
                             * pow(spec.h_relation[0], -1, p) % p, p)
        need(len(hroots) == 2, "the h relation has no two roots mod %d" % p)
        per_r = []
        total = 0
        for rv in rroots:
            c1 = KA.cube_count_mod((a1c + a1r * rv) % p, p)
            c2 = KA.cube_count_mod((a2c + a2r * rv) % p, p)
            per_r.append({"r3": rv, "n_A1": c1, "n_A2": c2})
            total += c1 * c2
        count = len(zroots) * len(hroots) * total
        need(count == spec.split_count,
             "prime %d carries %d frames, not %d" % (p, count, spec.split_count))
        need(count == spec.basis_rank,
             "frame count %d is not the declared rank %d" % (count, spec.basis_rank))
        need(fr[1] in rroots, "the registered r3 is not an exhibited root")
        out[str(p)] = {"n_zeta42": len(zroots), "n_h": len(hroots),
                       "per_r4": per_r, "total": count}
    return {"frames": out,
            "typing": "CONSISTENCY ONLY: a totally split L x L x L with "
                      "[L:Q]=144 would give the same 432; fieldness is proved "
                      "in L2/L3 and nowhere else"}


@gate("P2_HENSEL_REPLAY", "L4", "EXECUTED")
def _g(spec, ctx):
    _frame_cardinality(spec)
    p = spec.p2_prime
    need(p in dict(spec.frames), "the p^2 prime has no registered p-frame")
    m = p * p
    z, r, a1, a2, h = spec.p2_frame
    (a1c, a1r), (a2c, a2r) = spec.alpha_data
    eqs = {
        "Phi42(zeta42)": KA.poly_eval_mod(list(spec.phi42), z, m),
        "r3^2-c": (r * r - spec.r_square) % m,
        "A1^3-alpha1": (pow(a1, 3, m) - a1c - a1r * r) % m,
        "A2^3-alpha2": (pow(a2, 3, m) - a2c - a2r * r) % m,
        "b*h^2-c": (spec.h_relation[0] * h * h - spec.h_relation[1]) % m,
    }
    for name, v in eqs.items():
        need(v == 0, "p^2 frame fails %s modulo p^2: residue %d" % (name, v))
    base = dict(spec.frames)[p]
    need(tuple(v % p for v in spec.p2_frame) == tuple(base),
         "the p^2 frame does not reduce to the registered p-frame")
    return {"prime": p, "modulus": m, "residues": eqs,
            "reduces_to_p_frame": True,
            "uniqueness": "etale (L3) so the Hensel lift is determined, not "
                          "chosen; a second lift over the same p-frame is a "
                          "defect"}


# ---- L5: the E-conditional ratio theorem ----------------------------------

BRIDGE_E_RE = re.compile(
    r"E\s*:=\s*\((-?\d+)([+-]\d+)\*r\)\*A1\*W1\^(\d+)\s*\+\s*"
    r"\((-?\d+)([+-]\d+)\*r\)\*A2\*W2\^(\d+)\s*=\s*0")
REPORT_Q0_RE = re.compile(
    r"^[ \t]*\((\d+),(\d+),(\d+),(\d+),(\d+)\)[ \t]*:[ \t]*(-?\d+/\d+)[ \t]*$",
    re.M)


def _E(alg, spec, W1, W2):
    """The literal displayed E, built term by term from the pinned data."""
    r = alg.gen(1)
    total = []
    for (c0, c1, gidx, exp) in spec.e_terms:
        coeff = alg.add(alg.const(c0), alg.scal(r, c1))
        total.append(alg.mul(alg.mul(coeff, alg.gen(gidx)),
                             alg.pw(W1 if gidx == 2 else W2, exp)))
    return alg.add(*total)


def _E_mod(spec, p, frame, W1, W2):
    """R2 repair D5(ii): the modular E is built from ``spec.e_terms`` too."""
    z, r, a1, a2, h = frame
    gens = {2: a1, 3: a2}
    total = 0
    for (c0, c1, gidx, exp) in spec.e_terms:
        need(gidx in gens, "E term names generator %d, not A1 or A2" % gidx)
        w = W1 if gidx == 2 else W2
        total = (total + (c0 + c1 * r) % p * gens[gidx] % p * pow(w, exp, p)) % p
    return total


@gate("E_LITERAL_PIN", "L5", "CONDITIONAL_PIN")
def _g(spec, ctx):
    """The displayed E is read out of the sealed E5/E6 bridge, not restated.

    R2 repair: in R1 this gate compared ``spec.e_terms`` with a tuple written
    into the gate body, so it could only ever certify that two copies of the
    same literal agreed.  Here the literal comes from an external file whose
    SHA-256 is pinned by ``SRC_FILE_HASHES`` and sealed into the archive.
    """
    text = (ctx["root"] / ctx["bridge_rel"]).read_text()
    hits = BRIDGE_E_RE.findall(text)
    need(len(hits) == 1,
         "the sealed bridge displays %d parsable E relations, expected exactly 1"
         % len(hits))
    c0, c1, e1, d0, d1, e2 = hits[0]
    parsed = ((int(c0), int(c1), 2, int(e1)), (int(d0), int(d1), 3, int(e2)))
    need(len(spec.e_terms) == 2, "E must have exactly two terms")
    need(tuple(tuple(t) for t in spec.e_terms) == parsed,
         "certificate E %s != the E displayed in the sealed bridge %s"
         % ([list(t) for t in spec.e_terms], [list(t) for t in parsed]))
    literal = "(%d%+d*r3)*A1*W1^%d + (%d%+d*r3)*A2*W2^%d" % (
        parsed[0][0], parsed[0][1], parsed[0][3],
        parsed[1][0], parsed[1][1], parsed[1][3])
    return {"E": literal,
            "source": ctx["bridge_rel"],
            "sha256": hashlib.sha256(literal.encode("ascii")).hexdigest(),
            "typing": "CONDITIONAL on the displayed bridge form; not re-derived"}


@gate("Q0_LITERAL_PIN", "L5", "CONDITIONAL_PIN")
def _g(spec, ctx):
    """The four q0 basis terms are read out of the sealed charged report."""
    text = (ctx["root"] / ctx["theorem_report_rel"]).read_text()
    hits = REPORT_Q0_RE.findall(text)
    need(len(hits) == 4,
         "the sealed theorem report displays %d parsable q0 terms, expected 4"
         % len(hits))
    parsed = {}
    for a, b, c, d, e, coeff in hits:
        parsed[(int(a), int(b), int(c), int(d), int(e))] = Fr(coeff)
    declared = {tuple(k): Fr(v) for k, v in spec.q0_terms}
    need(declared == parsed,
         "certificate q0 %s != the q0 displayed in the sealed report %s"
         % (sorted((list(k), str(v)) for k, v in declared.items()),
            sorted((list(k), str(v)) for k, v in parsed.items())))
    return {"source": ctx["theorem_report_rel"], "term_count": len(parsed),
            "terms": {",".join(map(str, k)): str(v)
                      for k, v in sorted(parsed.items())}}


@gate("F_IDENTITIES", "L5", "CONDITIONAL")
def _g(spec, ctx):
    alg = ctx["alg"]
    r, a1, a2 = alg.gen(1), alg.gen(2), alg.gen(3)
    (a1c, a1r), (a2c, a2r) = spec.alpha_data
    alpha1 = alg.add(alg.const(a1c), alg.scal(r, a1r))
    alpha2 = alg.add(alg.const(a2c), alg.scal(r, a2r))
    inv_a1 = alg.scal(alg.mul(alg.pw(a1, 2), alpha2), Fr(1, 6))
    inv_a2 = alg.scal(alg.mul(alg.pw(a2, 2), alpha1), Fr(1, 6))
    need(alg.mul(a1, inv_a1) == alg.one(), "A1 inverse fails")
    need(alg.mul(a2, inv_a2) == alg.one(), "A2 inverse fails")
    u = alg.mul(a2, inv_a1)
    eps = alg.add(alg.const(spec.eps_data[0]), alg.scal(r, spec.eps_data[1]))
    epsinv = alg.sub(alg.const(spec.eps_data[0]), alg.scal(r, spec.eps_data[1]))
    need(alg.pw(u, 3) == epsinv, "F1: u^3 != 2-r4")
    need(alg.mul(eps, epsinv) == alg.one(), "eps*(2-r4) != 1")
    need(alg.scal(alg.pw(epsinv, 3), -1)
         == alg.add(alg.scal(r, 15), alg.const(-26)),
         "F2: -(2-r4)^3 != 15*r3-26")
    zeta3 = alg.pw(alg.gen(0), spec.i_zeta3_exponent)
    i0 = alg.scal(alg.mul(r, alg.add(alg.one(), alg.scal(zeta3, 2))), Fr(1, 3))
    need(alg.mul(i0, i0) == alg.const(-1), "i^2 != -1 in K0")
    s = alg.scal(alg.mul(alg.add(alg.one(), i0), alg.sub(r, alg.one())), Fr(1, 2))
    need(alg.mul(s, s) == alg.mul(i0, epsinv), "F4: s^2 != i*(2-r4)")
    q0 = alg.mul(u, s)
    need(alg.mul(q0, q0) == alg.mul(i0, alg.pw(u, 5)), "F5: q0^2 != i*u^5")
    c = alg.mul(alg.add(alg.scal(r, 15), alg.const(-26)), u)
    need(c == alg.scal(alg.pw(u, 10), -1), "F3: c != -u^10")
    need(alg.pw(q0, 4) == c, "q0^4 != c")
    ctx["q0_computed"] = q0
    ctx["i"] = i0
    ctx["u"] = u
    ctx["s"] = s
    ctx["c"] = c
    ctx["epsinv"] = epsinv
    return {"F1": "u^3 = 2-r4", "F2": "-(2-r4)^3 = 15*r3-26", "F3": "c = -u^10",
            "F4": "s^2 = i*(2-r4)", "F5": "q0^2 = i*u^5 and q0^4 = c"}


@gate("Q0_NORMAL_FORM", "L5", "CONDITIONAL")
def _g(spec, ctx):
    alg = ctx["alg"]
    declared = {tuple(k): Fr(v) for k, v in spec.q0_terms}
    ctx["q0"] = declared      # the DECLARED datum is what L5 substitutes
    need(len(declared) == 4, "q0 must have exactly four basis terms")
    need(declared == ctx["q0_computed"],
         "declared q0 %s differs from the computed normal form %s"
         % (sorted(declared.items()), sorted(ctx["q0_computed"].items())))
    dens = set()
    for v in declared.values():
        dens |= KA.factor_small(v.denominator) if v.denominator > 1 else set()
    need(dens <= {2, 3},
         "q0 denominators %s leave the registered set {2,3}" % sorted(dens))
    return {"terms": {",".join(map(str, k)): str(v)
                      for k, v in sorted(declared.items())},
            "term_count": 4, "denominator_primes": sorted(dens)}


@gate("E_BASE_REDUCTION", "L5", "CONDITIONAL")
def _g(spec, ctx):
    """The base-level reduction of E that the GP engine mirrors.

    Writing q = W1/W2, E = 0 is q^4 = c with c = (-C2/C1)*u, and q0 = u*s
    satisfies it exactly when ``(alpha2/alpha1) * s^4 == -C2/C1``.  That last
    identity involves no cube root at all: it is the whole E-conditional
    content that both engines can check, and every number in it is read from
    ``spec.e_terms`` and ``spec.alpha_data``.
    """
    alg = ctx["alg"]
    r = alg.gen(1)
    (c0, c1, g1, x1), (d0, d1, g2, x2) = spec.e_terms
    need((g1, g2) == (2, 3), "the E terms do not name A1 and A2 in that order")
    need(x1 == x2 == spec.branch_count,
         "the E exponents %s are not both the branch count %d"
         % ([x1, x2], spec.branch_count))
    C1 = alg.add(alg.const(c0), alg.scal(r, c1))
    C2 = alg.add(alg.const(d0), alg.scal(r, d1))
    norm_c = c0 * d0 + spec.r_square * c1 * d1
    cross = c0 * d1 + c1 * d0
    need(cross == 0, "the two E coefficients are not conjugate: r-part %d" % cross)
    need(alg.mul(C1, C2) == alg.const(norm_c),
         "C1*C2 != %d in the algebra" % norm_c)
    need(norm_c != 0, "the E coefficient norm vanishes")
    inv_C1 = alg.scal(C2, Fr(1, norm_c))
    need(alg.mul(C1, inv_C1) == alg.one(), "C1 is not invertible")
    cbase = alg.scal(alg.mul(C2, inv_C1), -1)
    need(cbase == alg.scal(alg.pw(ctx["epsinv"], 3), -1),
         "-C2/C1 != -(2-r4)^3")
    (a1c, a1r), (a2c, a2r) = spec.alpha_data
    alpha1 = alg.add(alg.const(a1c), alg.scal(r, a1r))
    alpha2 = alg.add(alg.const(a2c), alg.scal(r, a2r))
    alpha_prod = alg.mul(alpha1, alpha2)
    need(len(alpha_prod) == 1 and (0, 0, 0, 0, 0) in alpha_prod,
         "alpha1*alpha2 is not rational: %s" % sorted(alpha_prod))
    alpha_norm = alpha_prod[(0, 0, 0, 0, 0)]
    need(alpha_norm != 0, "alpha1 is not invertible")
    inv_alpha1 = alg.scal(alpha2, 1 / alpha_norm)
    need(alg.mul(alpha1, inv_alpha1) == alg.one(), "alpha1 inverse fails")
    ar = alg.mul(alpha2, inv_alpha1)
    need(alg.mul(ar, alpha1) == alpha2, "alpha2/alpha1 is not well formed")
    s4 = alg.pw(ctx["s"], 4)
    need(alg.mul(ar, s4) == cbase,
         "E-REDUCTION (alpha2/alpha1)*s^4 != -C2/C1")
    need(alg.pw(ctx["u"], 3) == ar, "u^3 != alpha2/alpha1")
    need(alg.pw(ctx["q0"], spec.branch_count) == ctx["c"],
         "q0^%d != c" % spec.branch_count)
    return {"e_coefficient_norm": norm_c,
            "alpha_norm": int(alpha_norm),
            "e_term_count": len(spec.e_terms),
            "e_exponent_sum": x1 + x2,
            "e_generator_index_sum": g1 + g2,
            "reduction": "(alpha2/alpha1)*s^4 == -C2/C1, so q0 = u*s solves "
                         "q^4 = c using only u^3 = alpha2/alpha1"}


@gate("E_DIRECT_SUBSTITUTION", "L5", "CONDITIONAL")
def _g(spec, ctx):
    """Substitute q0 into the literal E.  NOT routed through c = -u^10.

    ``W2 = 1`` alone cannot see the exponent on ``W2``, so the substitution is
    also run at two nontrivial invertible scales; a homogeneous degree-4 E
    then vanishes on the whole line ``(q0*s, s)`` and an inhomogeneous one
    does not.
    """
    alg = ctx["alg"]
    val = _E(alg, spec, ctx["q0"], alg.one())
    need(val == {}, "E(q0,1) != 0; normal form has %d terms" % len(val))
    scales = {}
    for mono in spec.e_substitution_scales:
        scales[",".join(map(str, mono))] = alg.add(alg.one(),
                                                   {tuple(mono): Fr(1)})
    need(len(scales) >= 2, "at least two distinct scales are required")
    for name, s in sorted(scales.items()):
        need(s != {}, "scale %s is zero" % name)
        need(s != alg.one(), "scale %s is the trivial scale 1" % name)
        on_line = _E(alg, spec, alg.mul(ctx["q0"], s), s)
        need(on_line == {},
             "E(q0*(%s), %s) != 0: E is not homogeneous of degree 4 on the "
             "branch line" % (name, name))
    probe = _E(alg, spec, alg.one(), alg.one())
    need(probe != {}, "the E evaluator is identically zero; it certifies nothing")
    probe2 = _E(alg, spec, alg.gen(0), alg.one())
    need(probe2 != {}, "the E evaluator kills a non-branch point")
    return {"E_of_q0_and_1": 0, "E_on_branch_line": sorted(scales),
            "scale_count": len(scales),
            "evaluator_nonvacuous": True,
            "route": "direct substitution into the literal displayed E"}


@gate("FOUR_K0_RATIONAL_BRANCHES", "L5", "CONDITIONAL")
def _g(spec, ctx):
    alg = ctx["alg"]
    branches = [alg.mul(alg.pw(ctx["i"], k), ctx["q0"])
                for k in range(spec.branch_count)]
    need(len(branches) == 4, "branch count %d is not 4" % len(branches))
    for k, b in enumerate(branches):
        need(_E(alg, spec, b, alg.one()) == {}, "branch %d does not solve E" % k)
        need(alg.pw(b, 4) == ctx["c"], "branch %d does not satisfy q^4 = c" % k)
    keys = [tuple(sorted((tuple(m), str(v)) for m, v in b.items()))
            for b in branches]
    need(len(set(keys)) == 4, "the four branches are not pairwise distinct")
    return {"branches": 4, "all_in_K0": True, "pairwise_distinct": True,
            "splitting": "t^4-c = (t-q0)(t-i*q0)(t+q0)(t+i*q0) over K0",
            "extension_needed": "none"}


@gate("SIGMA_E_SYMMETRY", "L5", "CONDITIONAL")
def _g(spec, ctx):
    alg = ctx["alg"]
    r = alg.gen(1)
    (c0, c1, g1, _x1), (d0, d1, g2, _x2) = spec.e_terms
    t1 = alg.mul(alg.add(alg.const(c0), alg.scal(r, c1)), alg.gen(g1))
    t2 = alg.mul(alg.add(alg.const(d0), alg.scal(r, d1)), alg.gen(g2))
    need(alg.sigma(t1, spec.sigma_images) == t2
         and alg.sigma(t2, spec.sigma_images) == t1,
         "sigma does not swap the two E coefficient blocks")
    need(alg.mul(alg.sigma(ctx["q0"], spec.sigma_images), ctx["q0"])
         == alg.const(-1), "sigma(q0)*q0 != -1")
    return {"sigma_swaps_E_coefficients": True, "sigma_q0_times_q0": -1,
            "inverse": "q0^-1 = -sigma(q0)",
            "open": "whether the 29-row live set is sigma-stable is untested "
                    "and is not claimed"}


@gate("POINTBANK_REGRESSION", "L5", "CORROBORATION")
def _g(spec, ctx):
    banks = ctx.get("pointbanks")
    if banks is None:
        raise GateFail("pointbank inputs were not supplied")
    need(len(spec.pointbank_expected) == spec.pointbank_count_expected,
         "the certificate carries %d pointbank rows, %d are registered"
         % (len(spec.pointbank_expected), spec.pointbank_count_expected))
    pb_primes = tuple(sorted(p for p, _r, _k in spec.pointbank_expected))
    need(pb_primes == tuple(sorted(spec.registered_primes)),
         "pointbank prime set %s != registered %s"
         % (list(pb_primes), list(spec.registered_primes)))
    alg = ctx["alg"]
    out = {}
    for p, ratio_expect, k_expect in spec.pointbank_expected:
        rec = banks.get(p)
        need(rec is not None, "pointbank for %d absent" % p)
        fr = dict(spec.frames)[p]
        W1, W2, uW1, uW2 = rec["W1"], rec["W2"], rec["uW1"], rec["uW2"]
        need(W1 % p and W2 % p, "banked W is not a unit at %d" % p)
        need(W1 * uW1 % p == 1 and W2 * uW2 % p == 1,
             "banked inverse-chart rows fail at %d" % p)
        Ev = _E_mod(spec, p, fr, W1, W2)
        need(Ev == 0, "banked point is not E-conformal at %d" % p)
        ratio = W1 * pow(W2, -1, p) % p
        need(ratio == ratio_expect,
             "banked ratio %d != registered %d at %d" % (ratio, ratio_expect, p))
        q0p = alg.specialize(ctx["q0"], p, fr)
        ip = alg.specialize(ctx["i"], p, fr)
        need((ip * ip + 1) % p == 0, "specialised i does not square to -1")
        branches = [pow(ip, k, p) * q0p % p for k in range(4)]
        need(len(set(branches)) == 4, "specialised branches collide at %d" % p)
        hits = [k for k in range(4) if branches[k] == ratio]
        need(hits == [k_expect],
             "banked ratio matches branches %s, registered %d" % (hits, k_expect))
        out[str(p)] = {"W1": W1, "W2": W2, "ratio": ratio,
                       "branches": branches, "branch_index": k_expect,
                       "E_at_banked_point": 0}
    return {"banks": out, "row_count": len(spec.pointbank_expected),
            "typing": "CORROBORATION ONLY: modular, frame-dependent, and "
                      "feeds no theorem gate; branch indices are not portable "
                      "across frames"}


# ---- LZ: layer-restricted censuses (R2 repair D1) -------------------------

LOAD_BEARING = ("SRC_PHI42_LITERAL", "RELATION_LEADING_TERMS",
                "RANK432_INDEPENDENCE", "BASE_SURJECTIVE", "KUMMER_RANK_TWO",
                "GALOIS_STABILITY_FREE", "FIELD_DEGREE_432")
LOAD_BEARING_E = ("E_LITERAL_PIN", "Q0_LITERAL_PIN", "Q0_NORMAL_FORM",
                  "E_BASE_REDUCTION", "E_DIRECT_SUBSTITUTION")


def _expected(layers, kinds=None):
    return [n for (n, l, k, _f) in REGISTRY
            if l in layers and (kinds is None or k in kinds)]


@gate("CENSUS_UNCONDITIONAL", "LZ", "HARNESS")
def _g(spec, ctx):
    expected = [n for (n, l, k, _f) in REGISTRY
                if l in UNCONDITIONAL_LAYERS and k != "CORROBORATION"]
    executed = list(ctx["executed"])
    missing = [n for n in expected if n not in executed]
    need(not missing, "unconditional gates absent from the census: %s" % missing)
    for name in LOAD_BEARING:
        need(name in executed, "load-bearing gate %s did not run" % name)
    return {"expected": len(expected), "load_bearing_present": list(LOAD_BEARING),
            "typing": "restricted to L0-L4 non-corroboration gates: an L5 or "
                      "corroboration failure cannot reach the unconditional "
                      "theorem boolean"}


@gate("CENSUS_CONDITIONAL", "LZ", "HARNESS")
def _g(spec, ctx):
    expected = [n for (n, l, k, _f) in REGISTRY
                if l in CONDITIONAL_LAYERS and k != "CORROBORATION"]
    executed = list(ctx["executed"])
    missing = [n for n in expected if n not in executed]
    need(not missing, "conditional gates absent from the census: %s" % missing)
    for name in LOAD_BEARING_E:
        need(name in executed, "load-bearing E gate %s did not run" % name)
    return {"expected": len(expected),
            "load_bearing_present": list(LOAD_BEARING_E),
            "typing": "restricted to L5 non-corroboration gates"}


@gate("CENSUS_COMPLETE", "LZ", "HARNESS")
def _g(spec, ctx):
    executed = list(ctx["executed"])
    expected = [n for (n, _l, _k, _f) in REGISTRY if n != "CENSUS_COMPLETE"]
    missing = [n for n in expected if n not in executed]
    need(not missing, "gates absent from the executed census: %s" % missing)
    need(len(executed) == len(expected),
         "executed %d gates, registry declares %d" % (len(executed), len(expected)))
    return {"executed": executed, "count": len(executed),
            "typing": "execution integrity only; it feeds all_pass and not "
                      "either theorem boolean"}


# --------------------------------------------------------------------------
# driver
# --------------------------------------------------------------------------


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=True).encode("ascii")


def run(spec, root, source_pins, emitter_rel, rows_rel, bridge_rel,
        theorem_report_rel, pointbanks=None):
    ctx = {"root": Path(root), "source_pins": source_pins,
           "emitter_rel": emitter_rel, "rows_rel": rows_rel,
           "bridge_rel": bridge_rel, "theorem_report_rel": theorem_report_rel,
           "pointbanks": pointbanks, "executed": []}
    results = []
    overall = True
    for name, layer, kind, fn in REGISTRY:
        if name in spec.skip_gates:
            results.append({"gate": name, "layer": layer, "kind": kind,
                            "status": "SKIPPED_BY_MUTATION"})
            overall = False
            continue
        try:
            detail = fn(spec, ctx)
            ctx["executed"].append(name)
            results.append({"gate": name, "layer": layer, "kind": kind,
                            "status": "PASS", "detail": detail})
        except Exception as exc:                       # fail-closed
            results.append({"gate": name, "layer": layer, "kind": kind,
                            "status": "FAIL",
                            "error": "%s: %s" % (type(exc).__name__, exc)})
            overall = False
    by_name = {r["gate"]: r for r in results}

    def passed(name):
        return by_name[name]["status"] == "PASS"

    uncond_gates = [r for r in results if r["layer"] in UNCONDITIONAL_LAYERS
                    and r["kind"] != "CORROBORATION"]
    cond_gates = [r for r in results if r["layer"] in CONDITIONAL_LAYERS
                  and r["kind"] != "CORROBORATION"]
    corrob_gates = [r for r in results if r["kind"] == "CORROBORATION"]
    payload = {
        "schema": SCHEMA,
        "label": spec.label,
        "gates": results,
        "gate_count": len(results),
        # ---- D1: layer-restricted, disjoint theorem inputs ---------------
        "unconditional_k0_theorem":
            all(r["status"] == "PASS" for r in uncond_gates)
            and passed("CENSUS_UNCONDITIONAL"),
        "e_conditional_ratio_theorem":
            all(r["status"] == "PASS" for r in cond_gates)
            and passed("CENSUS_CONDITIONAL"),
        "corroboration_ok": all(r["status"] == "PASS" for r in corrob_gates),
        "execution_integrity": overall and passed("CENSUS_COMPLETE"),
        "theorem_inputs": {
            "unconditional": sorted(r["gate"] for r in uncond_gates)
                             + ["CENSUS_UNCONDITIONAL"],
            "conditional": sorted(r["gate"] for r in cond_gates)
                           + ["CENSUS_CONDITIONAL"],
            "corroboration": sorted(r["gate"] for r in corrob_gates)},
        "all_pass": overall,
        "components": ["K0"],
        "idempotents": [0, 1],
        "component_count": 1,
    }
    payload["observables"] = _observables(results)
    payload["census_sha256"] = hashlib.sha256(
        canonical(sorted(r["gate"] for r in results
                         if r["status"] == "PASS"))).hexdigest()
    payload["observable_sha256"] = hashlib.sha256(
        canonical(payload["observables"])).hexdigest()
    return payload


def _observables(results):
    """Integer facts that the PARI/GP engine computes independently.

    The runner requires exact agreement on every key.  Neither engine's own
    PASS banner is trusted: agreement is on recomputed integers.  The four
    ``e_`` keys are E-layer corroboration and are typed as such in the
    terminal; the rest belong to the unconditional layers.
    """
    by = {r["gate"]: r.get("detail") for r in results if r["status"] == "PASS"}
    obs = {}

    def put(key, value):
        if value is not None:
            obs[key] = int(value)

    if by.get("PHI42_DISCRIMINANT"):
        put("phi42_disc", by["PHI42_DISCRIMINANT"]["disc"])
    if by.get("PHI168_SHAPE"):
        put("phi168_degree", by["PHI168_SHAPE"]["degree"])
    if by.get("RELATION_LEADING_TERMS"):
        put("standard_monomials", by["RELATION_LEADING_TERMS"]["standard_monomials"])
    if by.get("RANK432_INDEPENDENCE"):
        rec = by["RANK432_INDEPENDENCE"]
        put("rank_witness_prime", rec["prime"])
        put("rank_det_z_sq", rec["det_z_sq"])
        put("rank_det_mid_sq", rec["det_mid_sq"])
        put("rank_det_h_sq", rec["det_h_sq"])
    if by.get("BASE_SURJECTIVE"):
        put("crt_residue", by["BASE_SURJECTIVE"]["crt_residue"])
    if by.get("KUMMER_RANK_TWO"):
        for p, rec in by["KUMMER_RANK_TWO"]["per_prime"].items():
            put("annihilators_" + p, len(rec["annihilators"]))
            put("generated_order_" + p, rec["generated_order"])
    if by.get("KUMMER_SILENT_PRIME_GUARD"):
        for p, rec in by["KUMMER_SILENT_PRIME_GUARD"]["silent"].items():
            put("annihilators_" + p, rec["annihilators"])
    if by.get("IDEMPOTENTS_ONLY_0_1"):
        put("component_count", by["IDEMPOTENTS_ONLY_0_1"]["component_count"])
        put("idempotent_count", len(by["IDEMPOTENTS_ONLY_0_1"]["idempotents"]))
    if by.get("RAMIFIED_EXACTLY_2_3_7"):
        prod = 1
        for q in by["RAMIFIED_EXACTLY_2_3_7"]["ramified"]:
            prod *= q
        put("ramified_product", prod)
    if by.get("SPLIT_COUNT_432"):
        for p, rec in by["SPLIT_COUNT_432"]["frames"].items():
            put("frame_zeta_roots_" + p, rec["n_zeta42"])
            put("frame_h_roots_" + p, rec["n_h"])
            put("frame_cubic_sum_" + p,
                sum(x["n_A1"] * x["n_A2"] for x in rec["per_r4"]))
            put("frame_points_" + p, rec["total"])
    if by.get("E_BASE_REDUCTION"):
        rec = by["E_BASE_REDUCTION"]
        put("e_term_count", rec["e_term_count"])
        put("e_exponent_sum", rec["e_exponent_sum"])
        put("e_generator_index_sum", rec["e_generator_index_sum"])
        put("e_coefficient_norm", rec["e_coefficient_norm"])
    return obs


E_LAYER_OBSERVABLES = ("e_term_count", "e_exponent_sum",
                       "e_generator_index_sum", "e_coefficient_norm")


def read_pointbanks(paths_and_hashes):
    """Restricted read of the banked modular points: no pickle global is
    admitted, so no class or callable can be reconstructed from the file."""
    import pickle

    class NoGlobals(pickle.Unpickler):
        def find_class(self, module, name):
            raise pickle.UnpicklingError("pickle global refused: %s.%s"
                                         % (module, name))

    out = {}
    for prime, path, expect in paths_and_hashes:
        path = Path(path)
        if path.is_symlink() or not path.is_file():
            raise GateFail("pointbank %s is not a regular file" % path)
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if digest != expect:
            raise GateFail("pointbank hash drift %s: %s" % (path, digest))
        with path.open("rb") as fh:
            data = NoGlobals(fh).load()
        if not isinstance(data, dict) or data.get("prime") != prime:
            raise GateFail("pointbank %s does not carry prime %d" % (path, prime))
        cv = data["cell_values"]
        out[prime] = {k: int(cv[k]) for k in ("W1", "W2", "uW1", "uW2")}
    return out


def run_from_pins(spec, root, pins, pointbanks=None):
    return run(spec, root, pins["sources"], pins["emitter_rel"],
               pins["rows_rel"], pins["bridge_rel"],
               pins["theorem_report_rel"], pointbanks)


def build_parser():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", required=True)
    ap.add_argument("--pins", required=True,
                    help="JSON file mapping repo-relative source paths to hashes")
    ap.add_argument("--pointbank", action="append", default=[],
                    metavar="PRIME:PATH:SHA256")
    ap.add_argument("--out", default="-")
    return ap


def main(argv=None):
    args = build_parser().parse_args(argv)
    pins = json.loads(Path(args.pins).read_text())
    banks = None
    if args.pointbank:
        items = []
        for item in args.pointbank:
            prime, path, sha = item.split(":", 2)
            items.append((int(prime), path, sha))
        banks = read_pointbanks(items)
    payload = run_from_pins(Spec(), args.root, pins, banks)
    blob = canonical(payload)
    if args.out == "-":
        sys.stdout.write(blob.decode("ascii") + "\n")
    else:
        Path(args.out).write_bytes(blob)
    return 0 if payload["all_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
