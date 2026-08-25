#!/usr/bin/env python3
"""Emit the exact normalized (9,12) common-cubic gate modulo 3^11."""

from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
from pathlib import Path


ROOT = Path(os.environ["JC2_ROOT"])
PARENT = (ROOT / "cases/as_b9_9_12_full_fibre_quadratic_3p11_20260825"
          / "compile_quadratic_9_12.py")
EXPECTED_PARENT = (
    "7a51c772b0df8c900eddd84e4388fe5f3d47e2bb755ef837d17d7cc28debde58")
payload = PARENT.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED_PARENT
saved_output = os.environ["OUTPUT_JSON"]
saved_smt = os.environ["SMT2_OUTPUT"]
os.environ["OUTPUT_JSON"] = os.environ["PARENT_REPLAY_JSON"]
os.environ["PARENT_REPLAY_JSON"] = os.environ["GRANDPARENT_REPLAY_JSON"]
os.environ["ANF_OUTPUT"] = os.environ["PARENT_ANF_OUTPUT"]
os.environ["SMT2_OUTPUT"] = os.environ["PARENT_SMT_OUTPUT"]
scope = {"__file__": str(PARENT), "__name__": "__b9_9_12_quad_parent__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(payload, str(PARENT), "exec"), scope)
os.environ["OUTPUT_JSON"] = saved_output
os.environ["SMT2_OUTPUT"] = saved_smt

p5, q5 = scope["p5"], scope["q5"]
T_base = list(scope["T_base"])
directions = [list(vector) for vector in scope["directions"]]
slots = list(scope["slots"])
support_p = [(i, degree - i) for degree in range(10)
             for i in range(degree + 1)]
support_q = [(i, degree - i) for degree in range(13)
             for i in range(degree + 1)]
assert len(support_p) == 55 and len(support_q) == 91
assert len(T_base) == 146 and len(directions) == 145

MODULUS = 3 ** 11
WIDTH = 64


def bv(value):
    return f"(_ bv{value % MODULUS} {WIDTH})"


def ext8(name):
    return f"((_ zero_extend 56) {name})"


def modterm(term):
    return f"(bvurem {term} {bv(MODULUS)})"


def addmod(terms):
    answer = bv(0)
    for term in terms:
        answer = modterm(f"(bvadd {answer} {term})")
    return answer


def mulmod(left, right):
    return modterm(f"(bvmul {left} {right})")


def affine(base, coordinate, fresh):
    terms = [bv(base + 243 * T_base[coordinate])]
    for index, direction in enumerate(directions):
        value = 243 * direction[coordinate]
        if value % MODULUS:
            terms.append(f"(bvmul {bv(value)} {ext8(f's{index}')})")
    terms.append(f"(bvmul {bv(3 ** 10)} {ext8(fresh)})")
    return addmod(terms)


def determinant_terms(target):
    terms = []
    for left, (i, j) in enumerate(support_p):
        for right, (k, ell) in enumerate(support_q):
            if i and ell and (i - 1 + k, j + ell - 1) == target:
                terms.append(f"(bvmul {bv(i * ell)} (bvmul p{left} q{right}))")
            if j and k and (i + k - 1, j - 1 + ell) == target:
                terms.append(f"(bvmul {bv(-j * k)} (bvmul p{left} q{right}))")
    return terms


def convolution(left, right):
    answer = [[] for _ in range(len(left) + len(right) - 1)]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            answer[i + j].append(mulmod(a, b))
    return [addmod(terms) for terms in answer]


smt = Path(saved_smt)
with smt.open("w") as stream:
    stream.write("(set-logic QF_BV)\n(set-option :produce-models true)\n")
    for index in range(145):
        stream.write(f"(declare-fun s{index} () (_ BitVec 8))\n")
        stream.write(f"(assert (bvule s{index} #x02))\n")
    for index in range(146):
        stream.write(f"(declare-fun w{index} () (_ BitVec 8))\n")
        stream.write(f"(assert (bvule w{index} #x02))\n")
    for index in range(1, 4):
        stream.write(f"(declare-fun h{index} () (_ BitVec 64))\n")
        stream.write(f"(assert (bvult h{index} {bv(MODULUS)}))\n")
        stream.write(f"(assert (= (bvurem h{index} {bv(3)}) {bv(0)}))\n")
    for index, xy in enumerate(support_p):
        stream.write(f"(declare-fun p{index} () (_ BitVec 64))\n")
        stream.write(f"(assert (= p{index} ")
        stream.write(affine(p5.get(xy, 0), index, f"w{index}"))
        stream.write("))\n")
    for index, xy in enumerate(support_q):
        stream.write(f"(declare-fun q{index} () (_ BitVec 64))\n")
        stream.write(f"(assert (= q{index} ")
        stream.write(affine(q5.get(xy, 0), 55 + index, f"w{55 + index}"))
        stream.write("))\n")
    for xy in slots:
        target = bv(1 if xy == (0, 0) else 0)
        stream.write(f"(assert (= {addmod(determinant_terms(xy))} {target}))\n")
    h = [bv(1), "h1", "h2", "h3"]
    h2 = convolution(h, h)
    h3 = convolution(h2, h)
    h4 = convolution(h3, h)
    for index, value in enumerate(h3):
        stream.write(f"(declare-fun h3_{index} () (_ BitVec 64))\n")
        stream.write(f"(assert (= h3_{index} {value}))\n")
    for index, value in enumerate(h4):
        stream.write(f"(declare-fun h4_{index} () (_ BitVec 64))\n")
        stream.write(f"(assert (= h4_{index} {value}))\n")
    p9 = [support_p.index((i, 9 - i)) for i in range(10)]
    q12 = [support_q.index((i, 12 - i)) for i in range(13)]
    stream.write(f"(assert (not (= (bvurem p{p9[0]} {bv(3)}) {bv(0)})))\n")
    stream.write(f"(assert (not (= (bvurem q{q12[0]} {bv(3)}) {bv(0)})))\n")
    for i, index in enumerate(p9):
        stream.write(f"(assert (= p{index} {mulmod(f'p{p9[0]}', f'h3_{i}')}))\n")
    for i, index in enumerate(q12):
        stream.write(f"(assert (= q{index} {mulmod(f'q{q12[0]}', f'h4_{i}')}))\n")
    stream.write("(check-sat)\n(get-model)\n")

canonical = smt.read_bytes()
boolector = canonical.replace(b"(set-option :produce-models true)\n", b"")
boolector = boolector.replace(b"(get-model)\n", b"")
Path(os.environ["BOOLECTOR_SMT_OUTPUT"]).write_bytes(boolector)
result = {
    "status": "PASS-AS-B9-9-12-COMMON-CUBIC-SMT-EMITTED",
    "parent_source_sha256": EXPECTED_PARENT,
    "parent_result_sha256": hashlib.sha256(
        Path(os.environ["PARENT_REPLAY_JSON"]).read_bytes()).hexdigest(),
    "modulus": MODULUS,
    "predecessor_variable_count": 145,
    "fresh_variable_count": 146,
    "common_cubic_variable_count": 3,
    "determinant_row_count": 276,
    "top_form_row_count": 23,
    "smt2_sha256": hashlib.sha256(canonical).hexdigest(),
    "boolector_smt2_sha256": hashlib.sha256(boolector).hexdigest(),
    "scope": "complete displayed normalized mod3^11 family over one B9 mod243 parent",
    "refusal_scope": [
        "finite-depth necessary common-cubic locus only",
        "no continuation, all-depth point, complete earlier fibre, or JC2",
    ],
}
encoded = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
Path(saved_output).write_bytes(encoded + b"\n")
print("variables_rows", 145 + 146 + 3, 276, 23)
print("smt2_sha256", result["smt2_sha256"])
print("boolector_smt2_sha256", result["boolector_smt2_sha256"])
print("result_sha256", hashlib.sha256(encoded + b"\n").hexdigest())
print(result["status"])
