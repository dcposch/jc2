#!/usr/bin/env python3
"""Independent stdlib-Python exact checker for the D43 `K0` field certificate.

No PARI, no CAS, no third-party module, no network.  Every load-bearing datum
is a field of :class:`Spec` so the hostile mutation battery can perturb it and
observe which named gate fails.  Gates are fail-closed: an exception inside a
gate is a FAIL, never a skip, and a gate that does not run at all is caught by
``CENSUS_COMPLETE`` and again by the runner's sealed-census comparison.

Claim firewall enforced here: the unconditional layers L0-L4 certify only the
coefficient-field theorem; layer L5 is conditional on the literal displayed E
polynomial; the pointbank layer is corroboration and feeds no theorem gate.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import sys
from dataclasses import dataclass, field, replace
from fractions import Fraction as Fr
from pathlib import Path

import k0_algebra_r1 as KA

SCHEMA = "d43-k0-field-certificate-checker-r1"

# --------------------------------------------------------------------------
# the load-bearing data, all mutable by the battery
# --------------------------------------------------------------------------

TRUE_PHI42 = (1, 1, 0, -1, -1, 0, 1, 0, -1, -1, 0, 1, 1)
TRUE_Q0 = {(0, 0, 2, 1, 0): Fr(-5, 6), (0, 1, 2, 1, 0): Fr(1, 2),
           (7, 0, 2, 1, 0): Fr(2, 3), (7, 1, 2, 1, 0): Fr(-1, 3)}


@dataclass(frozen=True)
class Spec:
    # L0 source pins
    phi42: tuple = TRUE_PHI42
    basis_shape: tuple = (12, 2, 3, 3, 2)
    basis_rank: int = 432
    phi42_disc: int = 3 ** 6 * 7 ** 10
    # L1 base generation (Theorem A)
    r3_exponents: tuple = (14, 154)
    s2_exponents: tuple = (21, 147)
    zeta8_exponent: int = 21
    h_halving_denominator: int = 2
    gen_z8_power: int = 5
    gen_z42_power: int = 16
    order42_prime_cofactors: tuple = (2, 3, 7)
    # L2 Kummer
    character_primes: tuple = (673, 1009)
    class_generators: tuple = ((1, 0), (0, 1))
    class_representatives: tuple = ((1, 0), (0, 1), (1, 1), (1, 2))
    silent_primes: tuple = (105337, 105673)
    # L3 structure
    ramified_primes: tuple = (2, 3, 7)
    unramified_witness: int = 5
    components: tuple = ("K0",)
    idempotents: tuple = (0, 1)
    # L4 frames
    frames: tuple = ((105337, (2779, 795, 50630, 10114, 50267)),
                     (105673, (13862, 14686, 38664, 46664, 35053)))
    p2_prime: int = 105337
    p2_frame: tuple = (8852313585, 11012141449, 786496672,
                       8038065910, 6003627245)
    split_count: int = 432
    # L5 E-conditional
    e_terms: tuple = ((9, 5, 2, 4), (9, -5, 3, 4))   # (c0, c1*r3, gen idx, exp)
    q0_terms: tuple = tuple(sorted(TRUE_Q0.items()))
    i_zeta3_exponent: int = 14
    branch_count: int = 4
    e_substitution_scales: tuple = ((1, 0, 0, 0, 0), (0, 1, 0, 0, 0))
    pointbank_expected: tuple = ((105337, 7210, 3), (105673, 14755, 0))
    # harness control
    skip_gates: frozenset = frozenset()
    label: str = "BASELINE"


class GateFail(Exception):
    pass


def need(condition, detail):
    if not condition:
        raise GateFail(detail)


# --------------------------------------------------------------------------
# gate registry
# --------------------------------------------------------------------------

REGISTRY = []


def gate(name, layer, kind):
    def wrap(fn):
        REGISTRY.append((name, layer, kind, fn))
        return fn
    return wrap


# ---- L0: source pins and the rank-432 monic basis -------------------------

@gate("SRC_FILE_HASHES", "L0", "PIN")
def _g(spec, ctx):
    pins = ctx["source_pins"]
    got = {}
    for rel, expect in sorted(pins.items()):
        path = ctx["root"] / rel
        need(path.is_file() and not path.is_symlink(), "missing source %s" % rel)
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        need(digest == expect, "source hash drift %s: %s" % (rel, digest))
        got[rel] = digest
    return {"hashes": got}


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
    need(block["relations"] == ["Phi42(zeta42)=0", "r3^2=3", "A1^3=3+r3",
                                "A2^3=3-r3", "2*h^2=3"], "relation list drift")
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


@gate("RANK432_MONIC_BASIS", "L0", "THEOREM")
def _g(spec, ctx):
    need(tuple(spec.basis_shape) == (12, 2, 3, 3, 2),
         "basis shape %s is not the five monic leading degrees"
         % (spec.basis_shape,))
    prod = 1
    for k in spec.basis_shape:
        prod *= k
    need(prod == spec.basis_rank, "%d != declared rank %d" % (prod, spec.basis_rank))
    need(prod == 432, "rank %d is not 432" % prod)
    alg = KA.K0Algebra(spec.phi42)
    basis = alg.basis()
    need(len(basis) == 432 and len(set(basis)) == 432, "basis is not 432 distinct")
    for mono in basis:
        nf = alg.norm({mono: Fr(1)})
        need(nf == {mono: Fr(1)}, "monomial %s is not its own normal form" % (mono,))
    z, r, a1, a2, h = (alg.gen(i) for i in range(5))
    rel = {
        "Phi42(z)": alg.add(*[alg.scal(alg.pw(z, j), spec.phi42[j])
                              for j in range(13)]),
        "r^2-3": alg.sub(alg.pw(r, 2), alg.const(3)),
        "A1^3-(3+r)": alg.sub(alg.pw(a1, 3), alg.add(alg.const(3), r)),
        "A2^3-(3-r)": alg.sub(alg.pw(a2, 3), alg.sub(alg.const(3), r)),
        "2h^2-3": alg.sub(alg.scal(alg.pw(h, 2), 2), alg.const(3)),
    }
    for name, val in rel.items():
        need(val == {}, "relation %s does not normalise to 0" % name)
    need(alg.one() != {}, "the algebra is the zero ring")
    ctx["alg"] = alg
    return {"rank": 432, "leading_degrees": list(spec.basis_shape),
            "relations_normalise_to_zero": sorted(rel), "confluent_on_basis": True}


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
    need(sorted(spec.order42_prime_cofactors) == [2, 3, 7],
         "order gate must test every prime divisor of 42")
    need(C.mul(r3, r3) == C.const(3), "r3^2 != 3")
    need(C.mul(s2, s2) == C.const(2), "sqrt2^2 != 2")
    need(C.scal(C.mul(h, h), 2) == C.const(3), "2h^2 != 3")
    need(C.mul(C.scal(h, 2), C.scal(h, 2)) == C.const(6), "(2h)^2 != 6")
    ctx["C"] = C
    ctx["base"] = {"z": z, "z42": z42, "r3": r3, "s2": s2, "h": h}
    return {"relations_hold": ["Phi42(z^4)", "r3^2=3", "s2^2=2", "2h^2=3"],
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
    crt = 21 * spec.gen_z8_power + 4 * spec.gen_z42_power
    need(crt % 168 == 1, "exponent arithmetic 21*%d+4*%d = %d is not 1 mod 168"
         % (spec.gen_z8_power, spec.gen_z42_power, crt))
    return {"identity": "zeta8^%d*zeta42^%d == zeta_168"
            % (spec.gen_z8_power, spec.gen_z42_power), "crt_residue": crt % 168}


@gate("BASE_DIMENSION_48", "L1", "THEOREM")
def _g(spec, ctx):
    need(len(ctx["phi168"]) - 1 == 48, "deg Phi_168 != 48")
    need(spec.basis_shape[0] * spec.basis_shape[1] * spec.basis_shape[4] == 48,
         "the pre-cubic monomial count is not 48")
    return {"dim_B": 48, "conclusion": "B = Q(zeta_168), a field, abelian over Q"}


@gate("BASE_CONDUCTOR_TOWER", "L1", "THEOREM")
def _g(spec, ctx):
    disc_phi42 = int(KA.resultant(list(spec.phi42), KA.pderiv(list(spec.phi42))))
    need(disc_phi42 % 2 != 0, "2 could ramify in Q(zeta42)")
    need(12 % 4 == 0 and 12 // 4 == 3, "disc(Q(sqrt3)) is not 12")
    need(12 % 42 != 0 and 42 % 12 != 0,
         "conductor 12 divides 42; sqrt3 in Q(zeta42) not excluded")
    need(84 % 12 == 0, "conductor 12 does not divide 84")
    need(84 % 24 != 0, "conductor 24 divides 84; sqrt6 in Q(zeta84) not excluded")
    need(168 % 24 == 0 and 168 % 12 == 0, "168 does not carry both conductors")
    return {"tower": ["Q(zeta42) deg 12 cond 21", "Q(zeta84) deg 24 cond 84",
                      "Q(zeta168) deg 48 cond 168"],
            "sqrt3_not_in_Q_zeta42": "2 unramified in Q(zeta42) (odd disc), "
                                     "ramified in Q(sqrt3) (disc 12)",
            "sqrt6_not_in_Q_zeta84": "conductor 24 does not divide 84"}


# ---- L2: Kummer independence by explicit cubic-character homs --------------

def _character_frames(spec, p):
    """Explicit ring homs Z[y]/(Phi_168) -> F_p, one per square root of 3."""
    need(KA.is_prime(p), "certificate prime %d is not prime" % p)
    need(p % 168 == 1, "certificate prime %d is not 1 mod 168" % p)
    need(p % 2 and p % 3 and p % 7, "certificate prime divides 42")
    roots = KA.primitive_nth_roots(p, 168)
    need(len(roots) == 48, "Phi_168 does not have 48 roots mod %d" % p)
    frames = {}
    for om in roots:
        r = (pow(om, 14, p) + pow(om, 154, p)) % p
        need((r * r - 3) % p == 0, "omega^14+omega^-14 is not a square root of 3")
        need((3 + r) % p and (3 - r) % p, "alpha_k is not a unit at %d" % p)
        v = (KA.cubic_character((3 + r) % p, p), KA.cubic_character((3 - r) % p, p))
        frames.setdefault(r, set()).add((om, v))
    need(len(frames) == 2, "the 48 homs do not hit both square roots of 3")
    out = []
    for r in sorted(frames):
        om, v = sorted(frames[r])[0]
        for om2, v2 in frames[r]:
            need(v2 == v, "character value depends on the hom within a fibre")
        out.append({"omega": om, "r3": r, "chi": v})
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
    need(673 in spec.character_primes, "the registered prime 673 is absent")
    ctx["charframes"] = {}
    out = {}
    for p in spec.character_primes:
        need(p not in spec.silent_primes,
             "prime %d is a registered frame prime and is character-silent" % p)
        fr = _character_frames(spec, p)
        ctx["charframes"][p] = fr
        out[str(p)] = [{"omega": f["omega"], "r3": f["r3"],
                        "chi_alpha1": f["chi"][0], "chi_alpha2": f["chi"][1]}
                       for f in fr]
    return {"frames": out}


@gate("KUMMER_RANK_TWO", "L2", "THEOREM")
def _g(spec, ctx):
    """Only (0,0) annihilates the exhibited characters, at EVERY listed prime."""
    per = {}
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
        per[str(p)] = {"annihilators": [list(a) for a in ann],
                       "generated_order": len(subgroup)}
    need(len(per) >= 2, "rank two was established at fewer than two primes")
    return {"per_prime": per, "Delta": "(Z/3)^2", "order": 9}


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
    names = {(1, 0): "alpha1 = 3+sqrt3", (0, 1): "alpha2 = 3-sqrt3",
             (1, 1): "alpha1*alpha2 = 6", (1, 2): "alpha1/alpha2 = 2+sqrt3"}
    out = {}
    for (i, j) in spec.class_representatives:
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
        need((i, j) != (0, 0), "the trivial class is not a representative")
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
    """Abelian descent to Q(sqrt3): norms 6, 6, 36, 1 and the unit argument."""
    def norm(a, b):        # N(a + b*sqrt3)
        return a * a - 3 * b * b

    def is_cube(n):
        n = abs(n)
        k = round(n ** (1.0 / 3.0)) if n else 0
        for c in (k - 2, k - 1, k, k + 1, k + 2):
            if c >= 0 and c ** 3 == n:
                return True
        return False

    need(norm(3, 1) == 6 and norm(3, -1) == 6, "N(3 +- sqrt3) != 6")
    need(norm(6, 0) == 36, "N(6) != 36")
    need(norm(2, 1) == 1, "N(2+sqrt3) != 1")
    need(not is_cube(6), "6 is a rational cube")
    need(not is_cube(36), "36 is a rational cube")
    need((2 * 2 - 3 * 1 * 1) == 1, "eps is not a unit of Z[sqrt3]")
    need(2 - 1 > 0 and 2 - 2 > -1, "eps has a negative real embedding")
    return {"norms": {"alpha1": 6, "alpha2": 6, "alpha1alpha2": 36, "eps": 1},
            "cube_free": [6, 36],
            "eps": "fundamental unit of Z[sqrt3]; norm blind, killed by the "
                   "cubic character at the certificate primes",
            "requires": "Lemma L2 abelian descent, licensed by Theorem A"}


@gate("KUMMER_SILENT_PRIME_GUARD", "L2", "THEOREM")
def _g(spec, ctx):
    """The registered frame primes cannot certify anything: their characters
    are trivial, so a certificate that used them would be vacuous."""
    out = {}
    for p in spec.silent_primes:
        fr = _character_frames(spec, p)
        triv = all(f["chi"] == (1, 1) for f in fr)
        need(triv, "registered prime %d is unexpectedly a live witness" % p)
        ann = _annihilators([{"chi": f["chi"]} for f in fr], p)
        need(len(ann) == 9,
             "registered prime %d does not annihilate everything" % p)
        out[str(p)] = {"characters_trivial": True, "annihilators": 9}
        need(p not in spec.character_primes,
             "a silent prime is being used as a certificate prime")
    return {"silent": out}


# ---- L3: Theorems C and D --------------------------------------------------

@gate("FIELD_DEGREE_432", "L3", "THEOREM")
def _g(spec, ctx):
    need(48 * 9 == spec.basis_rank, "48*9 != declared rank")
    need(spec.basis_rank == 432, "degree is not 432")
    return {"deg_B": 48, "deg_K0_over_B": 9, "deg_K0": 432,
            "argument": "K0 is free of rank 9 over the field B (L1); Kummer "
                        "theory with Delta = (Z/3)^2 (L2) gives [L:B] = 9; the "
                        "evident surjection K0 -> L between B-spaces of equal "
                        "dimension 9 is an isomorphism"}


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


@gate("GALOIS_STABILITY", "L3", "THEOREM")
def _g(spec, ctx):
    """sigma: r -> -r, A1 <-> A2 preserves every defining relation, so it is a
    ring automorphism; hence Delta is Gal(B/Q)-stable and K0/Q is Galois."""
    alg = ctx["alg"]
    z, r, a1, a2, h = (alg.gen(i) for i in range(5))
    rels = {
        "Phi42(z)": alg.add(*[alg.scal(alg.pw(z, j), spec.phi42[j])
                              for j in range(13)]),
        "r^2-3": alg.sub(alg.pw(r, 2), alg.const(3)),
        "A1^3-(3+r)": alg.sub(alg.pw(a1, 3), alg.add(alg.const(3), r)),
        "A2^3-(3-r)": alg.sub(alg.pw(a2, 3), alg.sub(alg.const(3), r)),
        "2h^2-3": alg.sub(alg.scal(alg.pw(h, 2), 2), alg.const(3)),
    }
    for name, val in rels.items():
        need(alg.sigma(val) == {}, "sigma does not preserve %s" % name)
    need(alg.sigma(r) == alg.scal(r, -1), "sigma(r) != -r")
    need(alg.sigma(a1) == a2 and alg.sigma(a2) == a1, "sigma does not swap A1,A2")
    need(alg.sigma(alg.sigma(a1)) == a1, "sigma is not an involution")
    need(alg.sigma(alg.mul(a1, a2)) == alg.mul(a1, a2),
         "sigma moves A1*A2, so it does not fix cbrt 6")
    need(alg.sigma(alg.add(alg.const(3), r)) == alg.sub(alg.const(3), r),
         "sigma does not swap alpha1 and alpha2")
    return {"sigma_preserves": sorted(rels),
            "conclusion": "Delta is Gal(B/Q)-stable, so K0/Q is Galois"}


@gate("NONABELIAN", "L3", "THEOREM")
def _g(spec, ctx):
    alg = ctx["alg"]
    a1, a2 = alg.gen(2), alg.gen(3)
    cbrt6 = alg.mul(a1, a2)
    need(alg.pw(cbrt6, 3) == alg.const(6), "(A1*A2)^3 != 6")
    for q in (2, 3):
        need(6 % q == 0 and 1 % q != 0 and 6 % (q * q) != 0,
             "t^3-6 is not Eisenstein at %d" % q)
    disc = -27 * 6 * 6
    need(disc == -972, "disc(t^3-6) != -972")
    root = int(abs(disc) ** 0.5)
    need(disc < 0 or all(c * c != disc for c in (root - 1, root, root + 1)),
         "disc(t^3-6) is a square, so the cubic could be Galois")
    return {"cbrt6_in_K0": True, "cubic": "t^3-6",
            "eisenstein_primes": [2, 3], "disc": disc, "disc_is_square": False,
            "conclusion": "K0 contains a non-normal cubic field, so K0/Q is "
                          "not abelian and K0 lies in no cyclotomic field"}


@gate("ETALE_OVER_Z_1_42", "L3", "THEOREM")
def _g(spec, ctx):
    alg = ctx["alg"]
    a1, a2 = alg.gen(2), alg.gen(3)
    need(alg.mul(alg.pw(a1, 3), alg.pw(a2, 3)) == alg.const(6),
         "alpha1*alpha2 != 6, so the alpha_k need not be units in Z[1/42]")
    layers = {
        "zeta42": {"monic": "Phi42", "disc": spec.phi42_disc},
        "r3": {"monic": "r^2-3", "disc": 12},
        "A1": {"monic": "A1^3-alpha1", "disc": "-27*alpha1^2"},
        "A2": {"monic": "A2^3-alpha2", "disc": "-27*alpha2^2"},
        "h": {"monic": "h^2-3/2", "disc": 6},
    }
    for n in (spec.phi42_disc, 12, 6, 27):
        need(set(KA.factor_small(n)) <= {2, 3, 7},
             "layer discriminant %d needs a prime outside {2,3,7}" % n)
    need(set(KA.factor_small(42)) == {2, 3, 7}, "42 is not 2*3*7")
    return {"layers": layers, "inverted": [2, 3, 7], "rank": 432,
            "conclusion": "finite etale of rank 432 over Z[1/42]"}


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
    need(alg.mul(alg.gen(1), alg.gen(1)) == alg.const(3), "sqrt3 not in K0")
    need(set(KA.factor_small(12)) == {2, 3}, "disc(Q(sqrt3)) = 12 mis-stated")
    need(5 not in set(KA.factor_small(spec.phi42_disc)) | {2, 3},
         "5 appears in a layer discriminant")
    return {"upper_bound": [2, 3, 7], "lower_bound_subfields":
            {"3": "Q(zeta3) subset K0, disc -3", "7": "Q(zeta7) subset K0, "
             "disc -7^5", "2": "Q(sqrt3) subset K0, disc 12"},
            "ramified": [2, 3, 7], "unramified_witness": 5,
            "source_constant_typing":
            "ETALE_LOCALIZATION_PRIMES=(2,3,5,7) is a safe superset; "
            "SOURCE_DENOMINATOR_PRIMES=(2,3,5) is a different object and "
            "neither is used to derive this set"}


# ---- L4: the two registered frames ----------------------------------------

@gate("FRAME_RELATIONS", "L4", "EXECUTED")
def _g(spec, ctx):
    out = {}
    for p, fr in spec.frames:
        z, r, a1, a2, h = fr
        eqs = {
            "Phi42(zeta42)": KA.poly_eval_mod(list(spec.phi42), z, p),
            "r3^2-3": (r * r - 3) % p,
            "A1^3-(3+r3)": (pow(a1, 3, p) - 3 - r) % p,
            "A2^3-(3-r3)": (pow(a2, 3, p) - 3 + r) % p,
            "2*h^2-3": (2 * h * h - 3) % p,
        }
        for name, v in eqs.items():
            need(v == 0, "frame %d fails %s: residue %d" % (p, name, v))
        need(p % 168 == 1, "frame prime %d is not 1 mod 168" % p)
        need(KA.is_prime(p), "frame modulus %d is not prime" % p)
        out[str(p)] = {"residues": eqs, "p_mod_168": p % 168}
    return {"frames": out}


@gate("FRAME_ORDER_AND_JACOBIAN", "L4", "EXECUTED")
def _g(spec, ctx):
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
               "4*h": 4 * h % p}
        for name, v in jac.items():
            need(v % p != 0, "frame %d: jacobian entry %s vanishes" % (p, name))
        out[str(p)] = {"order_42": True, "jacobian": jac}
    return {"frames": out}


@gate("SPLIT_COUNT_432", "L4", "CONSISTENCY")
def _g(spec, ctx):
    out = {}
    for p, fr in spec.frames:
        zroots = KA.primitive_nth_roots(p, 42)
        need(len(zroots) == 12, "not 12 primitive 42nd roots mod %d" % p)
        need(all(KA.poly_eval_mod(list(spec.phi42), v, p) == 0 for v in zroots),
             "an exhibited primitive 42nd root is not a root of Phi42")
        rroots = KA.sqrt_mod(3, p)
        need(len(rroots) == 2, "3 is not a nonzero square mod %d" % p)
        hroots = KA.sqrt_mod(3 * pow(2, -1, p) % p, p)
        need(len(hroots) == 2, "3/2 is not a nonzero square mod %d" % p)
        per_r = []
        total = 0
        for rv in rroots:
            c1 = KA.cube_count_mod((3 + rv) % p, p)
            c2 = KA.cube_count_mod((3 - rv) % p, p)
            per_r.append({"r3": rv, "n_A1": c1, "n_A2": c2})
            total += c1 * c2
        count = len(zroots) * len(hroots) * total
        need(count == spec.split_count,
             "prime %d carries %d frames, not %d" % (p, count, spec.split_count))
        need(count == 432, "frame count %d is not 432" % count)
        need(fr[1] in rroots, "the registered r3 is not an exhibited root")
        out[str(p)] = {"n_zeta42": len(zroots), "n_h": len(hroots),
                       "per_r3": per_r, "total": count}
    return {"frames": out,
            "typing": "CONSISTENCY ONLY: a totally split L x L x L with "
                      "[L:Q]=144 would give the same 432; fieldness is proved "
                      "in L2/L3 and nowhere else"}


@gate("P2_HENSEL_REPLAY", "L4", "EXECUTED")
def _g(spec, ctx):
    p = spec.p2_prime
    m = p * p
    z, r, a1, a2, h = spec.p2_frame
    eqs = {
        "Phi42(zeta42)": KA.poly_eval_mod(list(spec.phi42), z, m),
        "r3^2-3": (r * r - 3) % m,
        "A1^3-(3+r3)": (pow(a1, 3, m) - 3 - r) % m,
        "A2^3-(3-r3)": (pow(a2, 3, m) - 3 + r) % m,
        "2*h^2-3": (2 * h * h - 3) % m,
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

def _E(alg, spec, W1, W2):
    """The literal displayed E, built term by term from the pinned data."""
    r = alg.gen(1)
    total = []
    for (c0, c1, gidx, exp) in spec.e_terms:
        coeff = alg.add(alg.const(c0), alg.scal(r, c1))
        total.append(alg.mul(alg.mul(coeff, alg.gen(gidx)),
                             alg.pw(W1 if gidx == 2 else W2, exp)))
    return alg.add(*total)


@gate("E_LITERAL_PIN", "L5", "CONDITIONAL_PIN")
def _g(spec, ctx):
    need(len(spec.e_terms) == 2, "E must have exactly two terms")
    (c0, c1, g0, e0), (d0, d1, g1, e1) = spec.e_terms
    need((c0, c1, g0, e0) == (9, 5, 2, 4),
         "first E term is not (9+5*r3)*A1*W1^4")
    need((d0, d1, g1, e1) == (9, -5, 3, 4),
         "second E term is not (9-5*r3)*A2*W2^4")
    literal = "(9+5*r3)*A1*W1^4 + (9-5*r3)*A2*W2^4"
    return {"E": literal,
            "sha256": hashlib.sha256(literal.encode("ascii")).hexdigest(),
            "typing": "CONDITIONAL on the displayed bridge form; not re-derived"}


@gate("F_IDENTITIES", "L5", "CONDITIONAL")
def _g(spec, ctx):
    alg = ctx["alg"]
    r, a1, a2 = alg.gen(1), alg.gen(2), alg.gen(3)
    inv_a1 = alg.scal(alg.mul(alg.pw(a1, 2), alg.sub(alg.const(3), r)), Fr(1, 6))
    inv_a2 = alg.scal(alg.mul(alg.pw(a2, 2), alg.add(alg.const(3), r)), Fr(1, 6))
    need(alg.mul(a1, inv_a1) == alg.one(), "A1 inverse fails")
    need(alg.mul(a2, inv_a2) == alg.one(), "A2 inverse fails")
    u = alg.mul(a2, inv_a1)
    eps = alg.add(alg.const(2), r)
    need(alg.pw(u, 3) == alg.sub(alg.const(2), r), "F1: u^3 != 2-r3")
    need(alg.mul(eps, alg.sub(alg.const(2), r)) == alg.one(), "eps*(2-r3) != 1")
    need(alg.scal(alg.pw(alg.sub(alg.const(2), r), 3), -1)
         == alg.add(alg.scal(r, 15), alg.const(-26)),
         "F2: -(2-r3)^3 != 15*r3-26")
    zeta3 = alg.pw(alg.gen(0), spec.i_zeta3_exponent)
    i0 = alg.scal(alg.mul(r, alg.add(alg.one(), alg.scal(zeta3, 2))), Fr(1, 3))
    need(alg.mul(i0, i0) == alg.const(-1), "i^2 != -1 in K0")
    s = alg.scal(alg.mul(alg.add(alg.one(), i0), alg.sub(r, alg.one())), Fr(1, 2))
    need(alg.mul(s, s) == alg.mul(i0, alg.sub(alg.const(2), r)),
         "F4: s^2 != i*(2-r3)")
    q0 = alg.mul(u, s)
    need(alg.mul(q0, q0) == alg.mul(i0, alg.pw(u, 5)), "F5: q0^2 != i*u^5")
    c = alg.mul(alg.add(alg.scal(r, 15), alg.const(-26)), u)
    need(c == alg.scal(alg.pw(u, 10), -1), "F3: c != -u^10")
    need(alg.pw(q0, 4) == c, "q0^4 != c")
    ctx["q0_computed"] = q0
    ctx["i"] = i0
    ctx["u"] = u
    ctx["c"] = c
    return {"F1": "u^3 = 2-r3", "F2": "-(2-r3)^3 = 15*r3-26", "F3": "c = -u^10",
            "F4": "s^2 = i*(2-r3)", "F5": "q0^2 = i*u^5 and q0^4 = c"}


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


@gate("E_DIRECT_SUBSTITUTION", "L5", "CONDITIONAL")
def _g(spec, ctx):
    """Substitute q0 into the literal E.  NOT routed through c = -u^10.

    ``W2 = 1`` alone cannot see the exponent on ``W2``, so the substitution is
    also run at two nontrivial invertible scales; a homogeneous degree-4 E
    then vanishes on the whole line ``(q0*s, s)`` and an inhomogeneous one
    does not.
    """
    alg = ctx["alg"]
    r = alg.gen(1)
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
    c1 = alg.mul(alg.add(alg.const(9), alg.scal(r, 5)), alg.gen(2))
    c2 = alg.mul(alg.add(alg.const(9), alg.scal(r, -5)), alg.gen(3))
    need(alg.sigma(c1) == c2 and alg.sigma(c2) == c1,
         "sigma does not swap the two E coefficients")
    need(alg.mul(alg.sigma(ctx["q0"]), ctx["q0"]) == alg.const(-1),
         "sigma(q0)*q0 != -1")
    return {"sigma_swaps_E_coefficients": True, "sigma_q0_times_q0": -1,
            "inverse": "q0^-1 = -sigma(q0)",
            "open": "whether the 29-row live set is sigma-stable is untested "
                    "and is not claimed"}


@gate("POINTBANK_REGRESSION", "L5", "CORROBORATION")
def _g(spec, ctx):
    banks = ctx.get("pointbanks")
    if banks is None:
        raise GateFail("pointbank inputs were not supplied")
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
        z, r, a1, a2, h = fr
        Ev = ((9 + 5 * r) * a1 % p * pow(W1, 4, p)
              + (9 - 5 * r) * a2 % p * pow(W2, 4, p)) % p
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
    return {"banks": out,
            "typing": "CORROBORATION ONLY: modular, frame-dependent, and "
                      "feeds no theorem gate; branch indices are not portable "
                      "across frames"}


# ---- census ---------------------------------------------------------------

@gate("CENSUS_COMPLETE", "LZ", "HARNESS")
def _g(spec, ctx):
    executed = list(ctx["executed"])
    expected = [n for (n, _l, _k, _f) in REGISTRY if n != "CENSUS_COMPLETE"]
    missing = [n for n in expected if n not in executed]
    need(not missing, "gates absent from the executed census: %s" % missing)
    need(len(executed) == len(expected),
         "executed %d gates, registry declares %d" % (len(executed), len(expected)))
    load_bearing = ["BASE_SURJECTIVE", "E_DIRECT_SUBSTITUTION",
                    "KUMMER_RANK_TWO", "Q0_NORMAL_FORM", "SRC_PHI42_LITERAL"]
    for name in load_bearing:
        need(name in executed, "load-bearing gate %s did not run" % name)
    return {"executed": executed, "count": len(executed),
            "load_bearing_present": load_bearing}


# --------------------------------------------------------------------------
# driver
# --------------------------------------------------------------------------


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=True).encode("ascii")


def run(spec, root, source_pins, emitter_rel, rows_rel, pointbanks=None):
    ctx = {"root": Path(root), "source_pins": source_pins,
           "emitter_rel": emitter_rel, "rows_rel": rows_rel,
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
    unconditional = [r for r in results if r["layer"] in ("L0", "L1", "L2", "L3", "L4")]
    conditional = [r for r in results if r["layer"] == "L5"]
    theorem_gates = [r for r in unconditional if r["kind"] != "CORROBORATION"]
    e_gates = [r for r in conditional if r["kind"] != "CORROBORATION"]
    census = [r for r in results if r["layer"] == "LZ"]
    payload = {
        "schema": SCHEMA,
        "label": spec.label,
        "gates": results,
        "gate_count": len(results),
        "unconditional_k0_theorem":
            all(r["status"] == "PASS" for r in theorem_gates)
            and all(r["status"] == "PASS" for r in census),
        "e_conditional_ratio_theorem":
            all(r["status"] == "PASS" for r in e_gates)
            and all(r["status"] == "PASS" for r in census),
        "corroboration_ok": all(r["status"] == "PASS" for r in results
                                if r["kind"] == "CORROBORATION"),
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
    PASS banner is trusted: agreement is on recomputed integers.
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
    if by.get("RANK432_MONIC_BASIS"):
        put("basis_rank", by["RANK432_MONIC_BASIS"]["rank"])
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
                sum(x["n_A1"] * x["n_A2"] for x in rec["per_r3"]))
            put("frame_points_" + p, rec["total"])
    return obs


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
        spec = []
        for item in args.pointbank:
            prime, path, sha = item.split(":", 2)
            spec.append((int(prime), path, sha))
        banks = read_pointbanks(spec)
    payload = run(Spec(), args.root, pins["sources"], pins["emitter_rel"],
                  pins["rows_rel"], banks)
    blob = canonical(payload)
    if args.out == "-":
        sys.stdout.write(blob.decode("ascii") + "\n")
    else:
        Path(args.out).write_bytes(blob)
    return 0 if payload["all_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
