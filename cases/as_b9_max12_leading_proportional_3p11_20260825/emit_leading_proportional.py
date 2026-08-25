#!/usr/bin/env python3
"""Emit the exact full-family D12 leading-proportionality gate."""

from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
from pathlib import Path


ROOT = Path(os.environ["JC2_ROOT"])
PARENT = (ROOT / "cases/as_b9_max12_full_fibre_quadratic_3p11_20260825"
          / "compile_quadratic_3p11.py")
EXPECTED_PARENT = (
    "2a55f0d25328f4f443916c24764f1c7cd7436772353aece84c6284d8fa711c1e")
payload = PARENT.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED_PARENT
saved_output = os.environ["OUTPUT_JSON"]
saved_smt = os.environ["SMT2_OUTPUT"]
os.environ["OUTPUT_JSON"] = os.environ["PARENT_REPLAY_JSON"]
os.environ["PARENT_REPLAY_JSON"] = os.environ["GRANDPARENT_REPLAY_JSON"]
os.environ["ANF_OUTPUT"] = os.environ["PARENT_ANF_OUTPUT"]
os.environ["SMT2_OUTPUT"] = os.environ["PARENT_SMT_OUTPUT"]
scope = {"__file__": str(PARENT), "__name__": "__b9_quad_parent__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(payload, str(PARENT), "exec"), scope)
os.environ["OUTPUT_JSON"] = saved_output
os.environ["SMT2_OUTPUT"] = saved_smt

p5, q5 = scope["p5"], scope["q5"]
support, slots = list(scope["support"]), list(scope["slots"])
T_base = list(scope["T_base"])
directions = [list(vector) for vector in scope["directions"]]
assert len(support) == 91 and len(slots) == 276
assert len(T_base) == 182 and len(directions) == 165

MODULUS = 3 ** 11
WIDTH = 64


def bv(value):
    return f"(_ bv{value % MODULUS} {WIDTH})"


def ext(name):
    return f"((_ zero_extend 56) {name})"


def modterm(term):
    return f"(bvurem {term} {bv(MODULUS)})"


def modular_sum(terms):
    answer = bv(0)
    for term in terms:
        answer = modterm(f"(bvadd {answer} {term})")
    return answer


def affine_coefficient(base, coordinate, fresh_name):
    terms = [bv(base + 243 * T_base[coordinate])]
    for index, direction in enumerate(directions):
        value = 243 * direction[coordinate]
        if value % MODULUS:
            terms.append(f"(bvmul {bv(value)} {ext(f's{index}')})")
    terms.append(f"(bvmul {bv(3 ** 10)} {ext(fresh_name)})")
    return modular_sum(terms)


def determinant_terms(target):
    terms = []
    for left, (i, j) in enumerate(support):
        for right, (k, ell) in enumerate(support):
            if i and ell and (i - 1 + k, j + ell - 1) == target:
                terms.append(f"(bvmul {bv(i * ell)} (bvmul p{left} q{right}))")
            if j and k and (i + k - 1, j - 1 + ell) == target:
                terms.append(f"(bvmul {bv(-j * k)} (bvmul p{left} q{right}))")
    return terms


smt = Path(saved_smt)
with smt.open("w") as stream:
    stream.write("(set-logic QF_BV)\n(set-option :produce-models true)\n")
    for index in range(165):
        stream.write(f"(declare-fun s{index} () (_ BitVec 8))\n")
        stream.write(f"(assert (bvule s{index} #x02))\n")
    for index in range(182):
        stream.write(f"(declare-fun w{index} () (_ BitVec 8))\n")
        stream.write(f"(assert (bvule w{index} #x02))\n")
    for index, xy in enumerate(support):
        stream.write(f"(declare-fun p{index} () (_ BitVec 64))\n")
        stream.write(f"(assert (= p{index} ")
        stream.write(affine_coefficient(p5.get(xy, 0), index, f"w{index}"))
        stream.write("))\n")
        stream.write(f"(declare-fun q{index} () (_ BitVec 64))\n")
        stream.write(f"(assert (= q{index} ")
        stream.write(affine_coefficient(q5.get(xy, 0), 91 + index,
                                        f"w{91 + index}"))
        stream.write("))\n")
    for xy in slots:
        target = bv(1 if xy == (0, 0) else 0)
        stream.write(f"(assert (= {modular_sum(determinant_terms(xy))} {target}))\n")
    degree12 = [index for index, xy in enumerate(support) if sum(xy) == 12]
    y12 = support.index((0, 12))
    stream.write(f"(assert (not (= (bvurem q{y12} {bv(3)}) {bv(0)})))\n")
    for index in degree12:
        left = modterm(f"(bvmul p{index} q{y12})")
        right = modterm(f"(bvmul p{y12} q{index})")
        stream.write(f"(assert (= {left} {right}))\n")
    stream.write("(check-sat)\n(get-model)\n")

canonical = smt.read_bytes()
boolector = canonical.replace(b"(set-option :produce-models true)\n", b"")
boolector = boolector.replace(b"(get-model)\n", b"")
Path(os.environ["BOOLECTOR_SMT_OUTPUT"]).write_bytes(boolector)
result = {
    "status": "PASS-AS-B9-D12-LEADING-PROPORTIONAL-SMT-EMITTED",
    "parent_source_sha256": EXPECTED_PARENT,
    "parent_result_sha256": hashlib.sha256(
        Path(os.environ["PARENT_REPLAY_JSON"]).read_bytes()).hexdigest(),
    "modulus": MODULUS,
    "predecessor_variable_count": 165,
    "fresh_variable_count": 182,
    "determinant_row_count": 276,
    "leading_cross_row_count": 13,
    "q_y12_unit_constraint": True,
    "smt2_sha256": hashlib.sha256(canonical).hexdigest(),
    "boolector_smt2_sha256": hashlib.sha256(boolector).hexdigest(),
    "scope": "complete displayed mod3^11 D12 family over one B9 mod243 parent",
    "refusal_scope": [
        "necessary leading-form locus only",
        "no mod3^12 continuation or all-depth branch",
        "no complete earlier mod243 fibre, counterexample, maximum12 theorem, or JC2",
    ],
}
encoded = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
Path(saved_output).write_bytes(encoded + b"\n")
print("variables_rows", 347, 276, 13)
print("smt2_sha256", result["smt2_sha256"])
print("boolector_smt2_sha256", result["boolector_smt2_sha256"])
print("result_sha256", hashlib.sha256(encoded + b"\n").hexdigest())
print(result["status"])
