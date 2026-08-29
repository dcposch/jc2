#!/usr/bin/env python3
"""Exact a00pp D43 source-row producer, revision 4.

The mathematical payload is revision 2 unchanged (via the reviewed v3 lane): HW1=h*W1 and HW2=h*W2 are
collapsed into the 432-term radical quotient before any expensive jet
multiplication, the B orbits are replaced by their exact EB-free block before
joining the A-side jets, and rows are emitted only, never solved.

Revision 4 repairs the fail-closed operational contract found deficient by
the v2 hostile review: every production authorization, custody, semantic,
and algebraic check is an explicit exception rather than an ``assert`` (and
optimized Python is refused outright); the collapsed D21 gate performs
literal structural equality with literal refusal of each mutation, keeping
digests only as receipts; every receipt binds the exclusive run lease and
its nonce; and terminal publication is replaced by a non-authoritative
finalize candidate consumed by the single job-contract terminal decision.
"""

from __future__ import annotations

import argparse
import calendar
import hashlib
import importlib.util
import json
import os
import pickle
import sys
import time
from fractions import Fraction
from pathlib import Path

if sys.flags.optimize:
    raise RuntimeError(
        "OPTIMIZED_PYTHON_REFUSED_FAIL_CLOSED: jc2 d43 v4 producer must run "
        "without -O/-OO/PYTHONOPTIMIZE; validation in this module and its "
        "frozen dependencies must never be stripped")


class CustodyError(ValueError):
    """A fail-closed authorization, custody, semantic, or algebra failure."""


def require(condition, message: str) -> None:
    if not condition:
        raise CustodyError(message)


HERE = Path(__file__).resolve().parent
CASES = HERE.parent
ROOT = CASES.parent
sys.path.insert(0, str(CASES))

import d43_common_integral_emitter as COMMON
import r1_experiment as R1

_base_spec = importlib.util.spec_from_file_location(
    "d43_exact_sparse_rows_v1", HERE.parent /
    "d43_exact_sparse_rows_20260828" / "selected_rows.py")
BASE = importlib.util.module_from_spec(_base_spec)
sys.modules[_base_spec.name] = BASE
_base_spec.loader.exec_module(BASE)


SCHEMA = "jc2.d43.a00pp-exact-source-rows.v4"
MANIFEST_SCHEMA = "jc2.d43.a00pp-exact-source-manifest.v4"
SIDE_SCHEMA = SCHEMA + ".side"
PAIR_SCHEMA = SCHEMA + ".pair"
GATE_SCHEMA = SCHEMA + ".collapsed-d21-band20-gate"
SHARD_SCHEMA = SCHEMA + ".shard"
MERGE_SCHEMA = SCHEMA + ".merge"
PREFLIGHT_SCHEMA = SCHEMA + ".aws-preflight"
LEASE_SCHEMA = SCHEMA + ".run-lease"
CANDIDATE_SCHEMA = SCHEMA + ".finalize-candidate"
CANDIDATE_STATUS = "CANDIDATE_PENDING_TERMINAL_DECISION"

D = BASE.D
ABSOLUTE_DEPTH = BASE.ABSOLUTE_DEPTH
SUPPORT = BASE.SUPPORT
LOW_SUPPORT = BASE.LOW_SUPPORT
TARGETS = BASE.TARGETS
BANDS = BASE.BANDS
BAND_TARGETS = BASE.BAND_TARGETS
EXPECTED_REGISTRY_SHA256 = BASE.EXPECTED_REGISTRY_SHA256

# Re-validated here because the frozen v1 module guards these facts only
# with assert statements of its own.
require(len(TARGETS) == 184, "target registry census drift")
require(len(SUPPORT) == 22 and set(LOW_SUPPORT) <= set(SUPPORT),
        "support census drift")

COEFFICIENT_ALGEBRA = {
    "base": "Q",
    "basis_generators": ["zeta42", "r3", "A1", "A2", "h"],
    "basis_shape": [12, 2, 3, 3, 2],
    "basis_rank": 432,
    "relations": [
        "Phi42(zeta42)=0", "r3^2=3", "A1^3=3+r3",
        "A2^3=3-r3", "2*h^2=3",
    ],
    "polynomial_coordinates": ["W1", "W2"],
    "literal_a00pp_substitution": ["HW1=h*W1", "HW2=h*W2"],
    "EB": "ELIMINATED_BEFORE_A_B_JOIN_AND_REFUSED_IF_SURVIVING",
    "field_claim": None,
}

RESOURCE_CONTRACT = {
    "conditional_emitter_address_space_bytes": 549755813888,
    "cpu_f": "2", "cpu_g": "3",
    "file_size_bytes": 137438953472,
    "kill_after_seconds": 60,
    "maximum_memory_total_kib": 1073741824,
    "memory_swap_max_bytes": 0,
    "minimum_disk_free_bytes": 107374182400,
    "minimum_memory_available_kib": 838860800,
    "monitor_interval_seconds": 5,
    "side_address_space_bytes": 412316860416,
    "timeout_seconds": 86400,
    "whole_job_memory_max_bytes": 962072674304,
    "whole_job_pids_max": 512,
    "whole_job_timeout_seconds": 259200,
    "zero_swap_required": True,
}


def canonical_json(value) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=True).encode("ascii")


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_path(path: Path) -> str:
    return BASE.sha256_path(path)


def coefficient_algebra_sha256() -> str:
    return sha256_bytes(canonical_json(COEFFICIENT_ALGEBRA))


def support_sha256() -> str:
    return BASE.support_sha256()


def target_registry_sha256() -> str:
    return BASE.target_registry_sha256()


def atomic_json(path: Path, value) -> None:
    BASE.atomic_json(path, value)


def atomic_pickle(path: Path, value) -> None:
    BASE.atomic_pickle(path, value)


def require_registry(names, registry_hash, pin42) -> None:
    """Re-validate v1 registry facts with explicit fail-closed checks."""
    require(registry_hash == EXPECTED_REGISTRY_SHA256,
            "registry hash drift outside frozen v1 asserts")
    require(set(SUPPORT) <= set(names), "support escapes registry names")
    require(not any(name in ("Xf_alpha", "Xg_beta") for name in names),
            "alpha/beta coordinates present in registry")
    require(tuple(pin42) == ("tf1_74", "tf2_74", "tg01_74", "tg02_74",
                             "tg1_74", "tg2_74"),
            "PIN42 census drift")


def require_sparse_free_support() -> None:
    free = tuple(name for name, state
                 in zip((variable["name"] for variable in R1.VARS), R1.VSTAT)
                 if state is None)
    require(free == SUPPORT, "sparse registry free set is not the support")


# A collapsed coefficient is a sparse K0[W1,W2] polynomial:
# {(W1 exponent, W2 exponent): RadicalCoefficient}.
CP_ZERO = {}
CP_ONE = {(0, 0): COMMON.RadicalCoefficient.scalar(1)}


def cp_add(left, right):
    result = dict(left)
    for monomial, coefficient in right.items():
        value = result.get(monomial, COMMON.RadicalCoefficient()) + coefficient
        if value:
            result[monomial] = value
        else:
            result.pop(monomial, None)
    return result


def cp_neg(value):
    return {monomial: -coefficient
            for monomial, coefficient in value.items() if coefficient}


def cp_mul(left, right):
    result = {}
    for (w1a, w2a), ca in left.items():
        for (w1b, w2b), cb in right.items():
            monomial = (w1a + w1b, w2a + w2b)
            value = result.get(monomial, COMMON.RadicalCoefficient()) + ca * cb
            if value:
                result[monomial] = value
            else:
                result.pop(monomial, None)
    return result


def cp_pow(value, exponent):
    if int(exponent) != exponent or exponent < 0:
        raise ValueError("bad collapsed-polynomial exponent")
    result = CP_ONE
    base = value
    exponent = int(exponent)
    while exponent:
        if exponent & 1:
            result = cp_mul(result, base)
        base = cp_mul(base, base)
        exponent >>= 1
    return result


def cp_rc(coefficient):
    return {(0, 0): coefficient} if coefficient else {}


def rc_k3(value):
    value = R1.mk(value)
    terms = {}
    if value[0]:
        terms[(0, 0, 0, 0, 0)] = Fraction(value[0])
    if value[1]:
        terms[(0, 1, 0, 0, 0)] = Fraction(value[1])
    return COMMON.RadicalCoefficient(terms)


def cp_k3(value):
    return cp_rc(rc_k3(value))


def cp_w(power1=0, power2=0, coefficient=None):
    coefficient = coefficient or COMMON.RadicalCoefficient.scalar(1)
    return {(int(power1), int(power2)): coefficient} if coefficient else {}


def collapse_r1_ring_element(element, hw_signs=(1, 1)):
    """Literal a00pp collapse, with signed variants only for mutation tests."""
    if tuple(hw_signs) not in ((1, 1), (-1, 1), (1, -1), (-1, -1)):
        raise ValueError("HW mutation signs must be +/-1")
    signed = {}
    for key, coefficient in element.items():
        if len(key) != 8:
            raise ValueError("bad R_ext key")
        factor = hw_signs[0] ** int(key[4]) * hw_signs[1] ** int(key[6])
        value = coefficient * factor
        if not value.iszero():
            signed[key] = value
    collapsed = COMMON.collapse_r1_ring_element(signed)
    require(all(len(key) == 2 and min(key) >= 0 for key in collapsed),
            "collapsed monomial escapes the two W coordinates")
    return collapsed


def cp_zeta(power):
    return collapse_r1_ring_element(R1.rmono(za=int(power)))


def canonical_cp(value):
    return [[list(monomial), coefficient.json_terms()]
            for monomial, coefficient in sorted(value.items())]


def semantic_cp_sha256(value) -> str:
    return sha256_bytes(canonical_json(canonical_cp(value)))


def cv_add(left, right):
    result = dict(left)
    for monomial, coefficient in right.items():
        if tuple(monomial) != tuple(sorted(monomial)):
            raise ValueError("variable monomial is not registry ordered")
        value = cp_add(result.get(monomial, CP_ZERO), coefficient)
        if value:
            result[monomial] = value
        else:
            result.pop(monomial, None)
    return result


def cv_mul(left, right):
    result = {}
    for ma, ca in left.items():
        for mb, cb in right.items():
            monomial = tuple(sorted(ma + mb))
            if len(monomial) > D:
                raise ValueError("variable-degree cap exceeded in exact v3 lane")
            coefficient = cp_mul(ca, cb)
            if coefficient:
                value = cp_add(result.get(monomial, CP_ZERO), coefficient)
                if value:
                    result[monomial] = value
                else:
                    result.pop(monomial, None)
    return result


def cv_scale(expression, coefficient):
    if not coefficient:
        return {}
    return {monomial: product
            for monomial, value in expression.items()
            if (product := cp_mul(value, coefficient))}


def cv_constant(coefficient):
    return {(): coefficient} if coefficient else {}


def collapse_vexpr(expression, hw_signs=(1, 1)):
    result = {}
    for monomial, coefficient in expression.items():
        if monomial and monomial[-1] == R1.HIVAR:
            raise ValueError("raw sentinel before a00pp collapse")
        collapsed = collapse_r1_ring_element(coefficient, hw_signs)
        if collapsed:
            result[tuple(monomial)] = collapsed
    return result


def canonical_cvexpr(expression, registry_names):
    result = []
    for monomial, coefficient in expression.items():
        if tuple(monomial) != tuple(sorted(monomial)):
            raise ValueError("variable monomial is not registry ordered")
        result.append([[registry_names[index] for index in monomial],
                       canonical_cp(coefficient)])
    return sorted(result, key=lambda item: (item[0], item[1]))


def semantic_cvexpr_sha256(expression, registry_names):
    return sha256_bytes(canonical_json(
        canonical_cvexpr(expression, registry_names)))


def canonical_rows(rows, registry_names):
    return [[list(target), canonical_cvexpr(rows[target], registry_names)]
            for target in sorted(rows)]


def semantic_rows_sha256(rows, registry_names):
    return sha256_bytes(canonical_json(canonical_rows(rows, registry_names)))


CV_ONE = cv_constant(CP_ONE)
CJ_ONE = {(0, 0): CV_ONE}


def cs_add(left, right):
    result = dict(left)
    for slot, expression in right.items():
        value = cv_add(result.get(slot, {}), expression)
        if value:
            result[slot] = value
        else:
            result.pop(slot, None)
    return result


def cs_mul(left, right, depth):
    result = {}
    for sa, va in left.items():
        for sb, vb in right.items():
            slot = sa + sb
            if slot >= depth:
                continue
            product = cv_mul(va, vb)
            if product:
                result[slot] = cv_add(result.get(slot, {}), product)
                if not result[slot]:
                    del result[slot]
    return result


def cj_add(left, right):
    result = dict(left)
    for target, expression in right.items():
        value = cv_add(result.get(target, {}), expression)
        if value:
            result[target] = value
        else:
            result.pop(target, None)
    return result


def cj_mul(left, right, depth):
    result = {}
    for (eta_a, slot_a), va in left.items():
        for (eta_b, slot_b), vb in right.items():
            target = (eta_a + eta_b, slot_a + slot_b)
            if target[1] >= depth:
                continue
            product = cv_mul(va, vb)
            if product:
                result[target] = cv_add(result.get(target, {}), product)
                if not result[target]:
                    del result[target]
    return result


def convert_a_orbit(raw_orbit):
    series = {}
    for level, expression in raw_orbit["series"].items():
        value = collapse_vexpr(expression)
        if value:
            series[level] = value
    return {"name": raw_orbit["name"], "size": raw_orbit["size"],
            "series": series}


def assert_raw_b_orbits(raw_orbits):
    expected = {12: R1.vC(R1.rmono(B=1))}
    require(raw_orbits["B"]["series"] == expected,
            "raw B source series drift")
    require(raw_orbits["GB42"]["series"] == expected,
            "raw GB42 source series drift")
    require(raw_orbits["GB21"]["series"] == expected,
            "raw GB21 source series drift")
    require(raw_orbits["B"]["size"] == raw_orbits["GB42"]["size"] == 42,
            "raw B/GB42 orbit size drift")
    require(raw_orbits["GB21"]["size"] == 21, "raw GB21 orbit size drift")
    try:
        collapse_vexpr(expected[12])
    except ValueError as error:
        if "EB exponent survives" not in str(error):
            raise
    else:
        raise CustodyError("uncancelled EB was accepted")


def collapsed_gm_jet2(orbit_names, orbits, depth, tag=""):
    """R1.gm_jet2 over the already-collapsed K0[W1,W2] coefficient ring."""
    jet = CJ_ONE
    P = {12: CV_ONE}  # every stretch coordinate is literally pinned to zero
    for orbit_name in orbit_names:
        orbit = orbits[orbit_name]
        series = orbit["series"]
        n7 = R1.C7SUB[orbit["size"]]
        aside = series.get(12) == CV_ONE
        for k in range(7):
            if aside and k == 0:
                for j in range(n7):
                    phase = 7 * j
                    factor = {(1, 0): CV_ONE}
                    for level, expression in series.items():
                        if level >= 32 and level - 32 < depth:
                            twisted = cv_scale(
                                expression, cp_zeta(phase * level))
                            if twisted:
                                factor[(0, level - 32)] = cv_scale(
                                    twisted, cp_k3(-1))
                    jet = cj_mul(jet, factor, depth)
                continue
            delta = {}
            for slot in range(depth):
                level = 12 + slot
                value = P.get(level, {})
                source = series.get(level)
                if source:
                    twisted = cv_scale(source, cp_zeta(k * level))
                    value = cv_add(value, cv_scale(twisted, cp_k3(-1)))
                if value:
                    delta[slot] = value
            powers = {0: {0: CV_ONE}, 1: delta}
            for power in range(2, n7 + 1):
                powers[power] = cs_mul(powers[power - 1], delta, depth)
            power_sums = {
                power: {slot: cv_scale(value, cp_k3(n7))
                        for slot, value in powers[power].items()
                        if slot % 6 == 0}
                for power in range(1, n7 + 1)
            }
            elementary = [{0: CV_ONE}]
            for degree in range(1, n7 + 1):
                accumulator = {}
                for power in range(1, degree + 1):
                    term = cs_mul(elementary[degree - power],
                                  power_sums[power], depth)
                    term = {slot: cv_scale(value,
                                           cp_k3((-1) ** (power - 1)))
                            for slot, value in term.items()}
                    accumulator = cs_add(accumulator, term)
                elementary.append({
                    slot: cv_scale(value, cp_k3(Fraction(1, degree)))
                    for slot, value in accumulator.items()
                })
            block = {}
            for eta_power in range(n7 + 1):
                shift = 20 * eta_power
                if shift >= depth and eta_power:
                    break
                for slot, value in elementary[n7 - eta_power].items():
                    if slot + shift < depth:
                        block[(eta_power, slot + shift)] = value
            jet = cj_mul(jet, block, depth)
        print("[a00pp-gm %s] orbit %s complete: %d components" %
              (tag, orbit_name, len(jet)), flush=True)
    return jet


def collapsed_b_block(power, depth):
    """Exact ((1+eta*t^20)^7-3/2)^power block; no EB generator exists."""
    seed = {(0, 0): CV_ONE}
    if 20 < depth:
        seed[(1, 20)] = CV_ONE
    seventh = CJ_ONE
    for _ in range(7):
        seventh = cj_mul(seventh, seed, depth)
    seventh = cj_add(seventh, {(0, 0): cv_constant(
        cp_k3(Fraction(-3, 2)))})
    result = CJ_ONE
    for _ in range(power):
        result = cj_mul(result, seventh, depth)
    return result


def build_collapsed_side(side, depth=D):
    if side not in ("f", "g"):
        raise ValueError("side must be f or g")
    raw_orbits, names, registry_hash, pin42 = BASE.sparse_registry()
    require_registry(names, registry_hash, pin42)
    require_sparse_free_support()
    assert_raw_b_orbits(raw_orbits)
    if side == "f":
        orbit_names = ("P1", "P2")
        b_power = 6
    else:
        orbit_names = ("Gp1", "Gp2", "G0p1", "G0p2")
        b_power = 9
    collapsed_orbits = {
        name: convert_a_orbit(raw_orbits[name]) for name in orbit_names}
    a_jet = collapsed_gm_jet2(orbit_names, collapsed_orbits, depth,
                              "D43-v3-%s" % side)
    jet = cj_mul(a_jet, collapsed_b_block(b_power, depth), depth)
    return jet, names, registry_hash, pin42


def _selected_product(left, right, target):
    target_eta, target_slot = target
    result = {}
    for (eta, slot), expression in left.items():
        complement = (target_eta - eta, target_slot - slot)
        other = right.get(complement)
        if other is not None:
            result = cv_add(result, cv_mul(expression, other))
    return result


def selected_source_rows(jf, jg, targets, add_target=True):
    targets = tuple(targets)
    if len(targets) != len(set(targets)) or not set(targets) <= set(TARGETS):
        raise ValueError("bad selected target set")
    theta_f = {(eta, slot): cv_scale(value, cp_k3(slot - 12))
               for (eta, slot), value in jf.items() if slot != 12}
    theta_g = {(eta, slot): cv_scale(value, cp_k3(slot - 18))
               for (eta, slot), value in jg.items() if slot != 18}
    f_eta = {(eta - 1, slot): cv_scale(value, cp_k3(eta))
             for (eta, slot), value in jf.items() if eta}
    g_eta = {(eta - 1, slot): cv_scale(value, cp_k3(eta))
             for (eta, slot), value in jg.items() if eta}
    result = {}
    for target in targets:
        value = cv_add(_selected_product(theta_f, g_eta, target),
                       cv_scale(_selected_product(f_eta, theta_g, target),
                                cp_k3(-1)))
        if add_target and target == (0, 20):
            value = cv_add(value, cv_constant(cp_k3(42)))
        result[target] = value
    return result


def _parse_source_list(path: Path):
    result = {}
    for line in path.read_text().splitlines():
        if not line.strip():
            continue
        digest, relative = line.split(None, 1)
        relative = relative.strip()
        if len(digest) != 64 or relative in result:
            raise ValueError("malformed operational source list")
        result[relative] = digest
    return result


def load_manifest(path: Path):
    raw = path.read_bytes()
    manifest = json.loads(raw)
    require(manifest["schema"] == MANIFEST_SCHEMA, "manifest schema drift")
    require(manifest["D"] == D and
            manifest["absolute_depth"] == ABSOLUTE_DEPTH,
            "manifest depth drift")
    require(manifest["expected_registry_sha256"] == EXPECTED_REGISTRY_SHA256,
            "manifest registry hash drift")
    require(manifest["support"] == list(SUPPORT), "manifest support drift")
    require(manifest["support_sha256"] == support_sha256(),
            "manifest support hash drift")
    require(manifest["target_registry_sha256"] == target_registry_sha256(),
            "manifest target registry hash drift")
    require(manifest["coefficient_algebra"] == COEFFICIENT_ALGEBRA,
            "manifest coefficient algebra drift")
    require(manifest["coefficient_algebra_sha256"] ==
            coefficient_algebra_sha256(),
            "manifest coefficient algebra hash drift")
    require(manifest["authorization"] == {
        "build_independent_sides": True,
        "conditional_band20_then_all184": True,
        "solve": False,
    }, "manifest authorization drift")
    require(0 < manifest["preflight_receipt_max_age_seconds"] <= 259200,
            "manifest preflight age bound drift")
    require(manifest["resource_contract"] == RESOURCE_CONTRACT,
            "manifest resource contract drift")
    return manifest, sha256_bytes(raw)


def verify_operational_sources(manifest):
    list_path = ROOT / manifest["operational_source_list"]
    if sha256_path(list_path) != manifest["operational_source_list_sha256"]:
        raise CustodyError("operational source-list hash drift")
    inventory = _parse_source_list(list_path)
    required = set(manifest["required_operational_paths"])
    if set(inventory) != required:
        raise CustodyError("operational source inventory path-set drift")
    for relative, expected in sorted(inventory.items()):
        actual = sha256_path(ROOT / relative)
        if actual != expected:
            raise CustodyError("operational source drift for %s" % relative)
    return inventory


def assert_operational_registration(manifest):
    aws = manifest["aws"]
    required = (
        aws["expected_hostname"], aws["expected_instance_id"],
        aws["expected_instance_type"], aws["expected_region"],
        aws["expected_account_id"], aws["required_tag_key"],
        aws["required_tag_value"],
    )
    if (not all(required) or int(aws["expected_nproc"]) <= 0 or
            aws.get("registration_status") != "REGISTERED_IMMUTABLE"):
        raise CustodyError("v3 manifest is review-only and AWS-unregistered")


def probe_lock_held(lock_path: Path) -> bool:
    import fcntl
    descriptor = os.open(lock_path, os.O_RDWR | os.O_CREAT, 0o600)
    try:
        try:
            fcntl.flock(descriptor, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError:
            return True
        fcntl.flock(descriptor, fcntl.LOCK_UN)
        return False
    finally:
        os.close(descriptor)


def load_run_lease(path: Path, run_dir: Path):
    """Parse, validate, and probe the exclusive one-shot run lease."""
    lease = json.loads(path.read_text())
    require(isinstance(lease, dict) and lease.get("schema") == LEASE_SCHEMA,
            "run lease schema drift")
    nonce = lease.get("run_nonce")
    require(isinstance(nonce, str) and len(nonce) == 64 and
            all(ch in "0123456789abcdef" for ch in nonce),
            "run lease nonce malformed")
    require(lease.get("job_root") == str(run_dir.resolve()),
            "run lease job_root drift")
    require(lease.get("job_tag") == run_dir.name, "run lease job_tag drift")
    require(lease.get("terminal_authority") is False,
            "run lease claims terminal authority")
    lock_path = Path(lease["lock_path"])
    lock_stat = os.stat(lock_path)
    require([lock_stat.st_dev, lock_stat.st_ino] ==
            list(lease["lock_dev_ino"]), "run lease lock identity drift")
    require(probe_lock_held(lock_path),
            "run lease lock is no longer held")
    require(os.environ.get("RUN_NONCE") == nonce,
            "environment RUN_NONCE does not match the lease")
    return lease, sha256_path(path)


def lease_binding(lease, lease_hash):
    return {"run_nonce": lease["run_nonce"], "lease_sha256": lease_hash,
            "terminal_authority": False}


def require_lease_binding(record, lease, lease_hash, what: str):
    require(record.get("run_nonce") == lease["run_nonce"],
            what + " run_nonce does not match the lease")
    require(record.get("lease_sha256") == lease_hash,
            what + " lease digest does not match the lease")
    require(record.get("terminal_authority") is False,
            what + " claims terminal authority")


def validate_preflight_receipt(path: Path, manifest, manifest_hash,
                               lease, lease_hash):
    receipt = json.loads(path.read_text())
    require(receipt["schema"] == PREFLIGHT_SCHEMA,
            "preflight receipt schema drift")
    require(receipt["pass"] is True, "preflight receipt did not pass")
    require(receipt["terminal_authority"] is False,
            "preflight receipt claims terminal authority")
    require(receipt["manifest_sha256"] == manifest_hash,
            "preflight receipt manifest hash drift")
    require(receipt["operational_source_list_sha256"] ==
            manifest["operational_source_list_sha256"],
            "preflight receipt source list hash drift")
    require(receipt["live_identity"] == {
        key: manifest["aws"]["expected_" + key]
        for key in ("account_id", "hostname", "instance_id",
                    "instance_type", "region")
    }, "preflight live identity drift")
    require(receipt["live_tag"] == {
        "key": manifest["aws"]["required_tag_key"],
        "value": manifest["aws"]["required_tag_value"],
    }, "preflight live tag drift")
    require(receipt["run_lease"]["nonce"] == lease["run_nonce"],
            "preflight receipt lease nonce drift")
    require(receipt["run_lease"]["lease_sha256"] == lease_hash,
            "preflight receipt lease digest drift")
    require(receipt["run_lease"]["lock_held_probe"] is True,
            "preflight receipt did not observe a held lease")
    require(sys.platform.startswith("linux"),
            "compute entry points require Linux")
    require(os.uname().nodename == manifest["aws"]["expected_hostname"],
            "hostname drift")
    require(os.environ.get("AWS_RUN_TAG") ==
            manifest["aws"]["required_tag_value"],
            "AWS_RUN_TAG environment drift")
    require(os.environ.get("JOB_TAG") ==
            manifest["aws"]["required_tag_value"],
            "JOB_TAG environment drift")
    require(os.environ.get("AWS_EXPECTED_HOSTNAME") ==
            manifest["aws"]["expected_hostname"],
            "AWS_EXPECTED_HOSTNAME environment drift")
    expected_path = Path(receipt["run_dir"]) / "records" / "PREFLIGHT.json"
    require(path.resolve() == expected_path.resolve(),
            "preflight receipt path drift")
    require(Path(receipt["run_dir"]).resolve() ==
            Path(lease["job_root"]).resolve(),
            "preflight run_dir does not match the lease")
    issued = calendar.timegm(time.strptime(
        receipt["utc"], "%Y-%m-%dT%H:%M:%SZ"))
    age = time.time() - issued
    require(-300 <= age <= manifest["preflight_receipt_max_age_seconds"],
            "preflight receipt age out of bounds")
    return receipt, sha256_path(path)


def banked_pin_audit(manifest):
    result = []
    for prime in (105337, 105673):
        relative = "cases/d43_full_certificate_p%d.json" % prime
        path = ROOT / relative
        if sha256_path(path) != manifest["input_sha256"][relative]:
            raise CustodyError("banked certificate drift")
        point = json.loads(path.read_text())["point"]
        graph = point["graph_156"]
        require(graph["Xf_alpha"] == graph["Xg_beta"] == 0,
                "banked alpha/beta drift")
        nonzero = set()
        for name, value in graph.items():
            if value and name not in ("Xf_alpha", "Xg_beta"):
                nonzero.add(BASE.GRAPH_TO_SOURCE.get(name, name))
        require(nonzero == set(SUPPORT), "banked support drift")
        result.append({"prime": prime, "support_exact": True,
                       "alpha_beta_zero": True})
    return result


def build_side(manifest_path: Path, preflight_path: Path, lease_path: Path,
               side: str, output_path: Path):
    manifest, manifest_hash = load_manifest(manifest_path)
    assert_operational_registration(manifest)
    inventory = verify_operational_sources(manifest)
    run_dir = Path(os.environ.get("JOB_ROOT", ""))
    lease, lease_hash = load_run_lease(lease_path, run_dir)
    _preflight, preflight_hash = validate_preflight_receipt(
        preflight_path, manifest, manifest_hash, lease, lease_hash)
    if not manifest["authorization"]["build_independent_sides"]:
        raise CustodyError("side builds are not authorized")
    started_ns = time.time_ns()
    jet, names, registry_hash, pin42 = build_collapsed_side(side)
    completed_ns = time.time_ns()
    used = {names[index] for expression in jet.values()
            for monomial in expression for index in monomial}
    require(used <= set(SUPPORT), "side jet escapes the registered support")
    payload = {
        "schema": SIDE_SCHEMA,
        "status": "EXACT_A00PP_%s_SIDE_COMPLETE" % side.upper(),
        "side": side,
        "manifest_sha256": manifest_hash,
        "preflight_receipt_sha256": preflight_hash,
        "operational_source_list_sha256":
            manifest["operational_source_list_sha256"],
        "operational_source_sha256": inventory,
        "registry_sha256": registry_hash,
        "registry_names": names,
        "support": SUPPORT,
        "support_sha256": support_sha256(),
        "pin42_names": pin42,
        "coefficient_algebra": COEFFICIENT_ALGEBRA,
        "coefficient_algebra_sha256": coefficient_algebra_sha256(),
        "pure_y": True,
        "alpha_beta": (0, 0),
        "worker": {"pid": os.getpid(), "hostname": os.uname().nodename,
                   "started_epoch_ns": started_ns,
                   "completed_epoch_ns": completed_ns},
        "jet": jet,
        "jet_semantic_sha256": semantic_rows_sha256(jet, names),
        "banked_pin_audit": banked_pin_audit(manifest),
    }
    payload.update(lease_binding(lease, lease_hash))
    atomic_pickle(output_path, payload)
    receipt = {key: payload[key] for key in (
        "schema", "status", "side", "manifest_sha256",
        "preflight_receipt_sha256", "operational_source_list_sha256",
        "registry_sha256", "support_sha256", "coefficient_algebra_sha256",
        "jet_semantic_sha256", "worker",
        "run_nonce", "lease_sha256", "terminal_authority")}
    receipt.update({"payload": output_path.name,
                    "payload_bytes": output_path.stat().st_size,
                    "payload_sha256": sha256_path(output_path)})
    receipt_path = output_path.with_suffix(output_path.suffix + ".receipt.json")
    atomic_json(receipt_path, receipt)
    return receipt


def _load_pickle_after_hash(path: Path, expected_hash: str):
    if not expected_hash or len(expected_hash) != 64:
        raise CustodyError("missing explicit SHA-256")
    if sha256_path(path) != expected_hash:
        raise CustodyError("payload hash drift before unpickle")
    with path.open("rb") as stream:
        return pickle.load(stream)


def load_side_receipt(receipt_path: Path, manifest_hash: str,
                      preflight_hash: str, lease, lease_hash):
    receipt = json.loads(receipt_path.read_text())
    require(receipt["schema"] == SIDE_SCHEMA, "side receipt schema drift")
    require(receipt["manifest_sha256"] == manifest_hash,
            "side receipt manifest hash drift")
    require(receipt["preflight_receipt_sha256"] == preflight_hash,
            "side receipt preflight hash drift")
    require_lease_binding(receipt, lease, lease_hash, "side receipt")
    payload_path = receipt_path.parent / receipt["payload"]
    payload = _load_pickle_after_hash(payload_path, receipt["payload_sha256"])
    require(payload["schema"] == SIDE_SCHEMA, "side payload schema drift")
    require(payload["manifest_sha256"] == manifest_hash,
            "side payload manifest hash drift")
    require(payload["preflight_receipt_sha256"] == preflight_hash,
            "side payload preflight hash drift")
    require_lease_binding(payload, lease, lease_hash, "side payload")
    require(payload["jet_semantic_sha256"] == semantic_rows_sha256(
        payload["jet"], payload["registry_names"]),
        "side payload semantic digest drift")
    require(payload["jet_semantic_sha256"] == receipt["jet_semantic_sha256"],
            "side payload/receipt semantic digest mismatch")
    require(payload["worker"] == receipt["worker"],
            "side payload/receipt worker mismatch")
    require(payload["worker"]["pid"] > 1 and
            payload["worker"]["completed_epoch_ns"] >=
            payload["worker"]["started_epoch_ns"],
            "side worker interval malformed")
    require(payload["coefficient_algebra"] == COEFFICIENT_ALGEBRA,
            "side payload coefficient algebra drift")
    _orbits, expected_names, registry_hash, expected_pin42 = \
        BASE.reconstruct_registry()
    del _orbits
    require_registry(expected_names, registry_hash, expected_pin42)
    require(tuple(payload["registry_names"]) == expected_names,
            "side payload registry names drift")
    require(tuple(payload["support"]) == SUPPORT,
            "side payload support drift")
    require(tuple(payload["pin42_names"]) == expected_pin42,
            "side payload pin42 drift")
    require(payload["pure_y"] and tuple(payload["alpha_beta"]) == (0, 0),
            "side payload scope drift")
    return payload, receipt


def assemble_pair(manifest_path: Path, preflight_path: Path,
                  lease_path: Path, f_receipt_path: Path,
                  g_receipt_path: Path, output_path: Path):
    manifest, manifest_hash = load_manifest(manifest_path)
    assert_operational_registration(manifest)
    verify_operational_sources(manifest)
    run_dir = Path(os.environ.get("JOB_ROOT", ""))
    lease, lease_hash = load_run_lease(lease_path, run_dir)
    _preflight, preflight_hash = validate_preflight_receipt(
        preflight_path, manifest, manifest_hash, lease, lease_hash)
    side_metadata = {}
    receipts = {}
    for side, path in (("f", f_receipt_path), ("g", g_receipt_path)):
        payload, receipt = load_side_receipt(path, manifest_hash,
                                             preflight_hash, lease,
                                             lease_hash)
        require(payload["side"] == side, "side receipt side drift")
        side_metadata[side] = {
            key: payload[key] for key in (
                "manifest_sha256", "preflight_receipt_sha256",
                "operational_source_list_sha256", "registry_sha256",
                "support_sha256", "coefficient_algebra_sha256",
                "run_nonce", "lease_sha256")}
        del payload
        receipts[side] = receipt
    matching = ("manifest_sha256", "preflight_receipt_sha256",
                "operational_source_list_sha256", "registry_sha256",
                "support_sha256", "coefficient_algebra_sha256",
                "run_nonce", "lease_sha256")
    for key in matching:
        require(side_metadata["f"][key] == side_metadata["g"][key],
                "side receipts disagree on %s" % key)
    require(side_metadata["f"]["operational_source_list_sha256"] ==
            manifest["operational_source_list_sha256"],
            "side receipts bind a different source list")
    workers = {side: receipts[side]["worker"] for side in ("f", "g")}
    require(workers["f"]["pid"] != workers["g"]["pid"],
            "side builds share a PID")
    require(workers["f"]["hostname"] == workers["g"]["hostname"] ==
            manifest["aws"]["expected_hostname"],
            "side builds are not on the registered host")
    overlap = (workers["f"]["started_epoch_ns"] <=
               workers["g"]["completed_epoch_ns"] and
               workers["g"]["started_epoch_ns"] <=
               workers["f"]["completed_epoch_ns"])
    if not overlap:
        raise CustodyError("f/g build intervals do not prove concurrency")
    pair = {
        "schema": PAIR_SCHEMA,
        "status": "MATCHED_INDEPENDENT_F_G_PAIR_COMPLETE",
        "manifest_sha256": manifest_hash,
        "preflight_receipt_sha256": preflight_hash,
        "operational_source_list_sha256":
            manifest["operational_source_list_sha256"],
        "registry_sha256": EXPECTED_REGISTRY_SHA256,
        "support_sha256": support_sha256(),
        "coefficient_algebra_sha256": coefficient_algebra_sha256(),
        "side_receipts": {
            side: {"path": os.path.relpath(path, output_path.parent),
                   "sha256": sha256_path(path),
                   "payload_sha256": receipts[side]["payload_sha256"],
                   "jet_semantic_sha256":
                       receipts[side]["jet_semantic_sha256"]}
            for side, path in (("f", f_receipt_path),
                               ("g", g_receipt_path))
        },
        "worker_concurrency": {"status": "PASS_OVERLAPPING_DISTINCT_PIDS",
                               "workers": workers},
    }
    pair.update(lease_binding(lease, lease_hash))
    pair["pair_custody_sha256"] = sha256_bytes(canonical_json({
        "run_nonce": pair["run_nonce"],
        "side_receipts": pair["side_receipts"],
        "worker_concurrency": pair["worker_concurrency"],
    }))
    atomic_json(output_path, pair)
    return pair


def load_pair(pair_path: Path, manifest_hash: str, preflight_hash: str,
              lease, lease_hash):
    pair = json.loads(pair_path.read_text())
    require(pair["schema"] == PAIR_SCHEMA, "pair schema drift")
    require(pair["status"] == "MATCHED_INDEPENDENT_F_G_PAIR_COMPLETE",
            "pair status drift")
    require(pair["manifest_sha256"] == manifest_hash,
            "pair manifest hash drift")
    require(pair["preflight_receipt_sha256"] == preflight_hash,
            "pair preflight hash drift")
    require_lease_binding(pair, lease, lease_hash, "pair")
    require(pair["registry_sha256"] == EXPECTED_REGISTRY_SHA256,
            "pair registry hash drift")
    require(pair["support_sha256"] == support_sha256(),
            "pair support hash drift")
    require(pair["coefficient_algebra_sha256"] ==
            coefficient_algebra_sha256(),
            "pair coefficient algebra hash drift")
    require(pair["pair_custody_sha256"] == sha256_bytes(canonical_json({
        "run_nonce": pair["run_nonce"],
        "side_receipts": pair["side_receipts"],
        "worker_concurrency": pair["worker_concurrency"],
    })), "pair custody digest drift")
    require(pair["worker_concurrency"]["status"] ==
            "PASS_OVERLAPPING_DISTINCT_PIDS",
            "pair concurrency status drift")
    result = {}
    for side in ("f", "g"):
        item = pair["side_receipts"][side]
        receipt_path = (pair_path.parent / item["path"]).resolve()
        if pair_path.parent.resolve() not in receipt_path.parents:
            raise CustodyError("side receipt escapes pair directory")
        if sha256_path(receipt_path) != item["sha256"]:
            raise CustodyError("side receipt hash drift")
        payload, receipt = load_side_receipt(receipt_path, manifest_hash,
                                             preflight_hash, lease,
                                             lease_hash)
        require(receipt["payload_sha256"] == item["payload_sha256"],
                "pair payload hash drift")
        require(payload["jet_semantic_sha256"] == item["jet_semantic_sha256"],
                "pair semantic digest drift")
        result[side] = payload
    require(tuple(result["f"]["registry_names"]) ==
            tuple(result["g"]["registry_names"]),
            "pair registries disagree")
    return result["f"]["jet"], result["g"]["jet"], \
        tuple(result["f"]["registry_names"]), pair


def expected_collapsed_d21_band20(manifest, registry_names,
                                  hw_signs=(1, 1), add_target=True):
    relative = "directionb_tails_D21.pkl"
    path = ROOT / relative
    payload = _load_pickle_after_hash(path,
                                      manifest["input_sha256"][relative])
    require(payload["D"] == 21, "D21 reference bank depth drift")
    name_to_id = {name: index for index, name in enumerate(registry_names)}
    rows = {}
    for eta, _slot in BAND_TARGETS[20]:
        result = {}
        for monomial, coefficient in payload["byk"][20][eta].items():
            source_names = tuple(payload["vars"][index]
                                 for index in monomial)
            if not all(name in LOW_SUPPORT for name in source_names):
                continue
            mapped = tuple(sorted(name_to_id[name] for name in source_names))
            collapsed = collapse_r1_ring_element(coefficient, hw_signs)
            if collapsed:
                result[mapped] = cp_add(result.get(mapped, {}), collapsed)
                if not result[mapped]:
                    del result[mapped]
        if add_target and eta == 0:
            result = cv_add(result, cv_constant(cp_k3(42)))
        rows[(eta, 20)] = result
    return rows


def collapsed_d21_gate(rows, manifest, registry_names):
    """Literal structural band-20 equality with literal mutation refusal.

    The decision rests on Python structural equality of the canonical
    collapsed objects (registry-ordered variable monomials over exact
    ``RadicalCoefficient`` values).  SHA-256 digests are computed only as
    custody receipts and never decide the gate.
    """
    expected = expected_collapsed_d21_band20(manifest, registry_names)
    mutation_rows = {
        "HW1_negative": expected_collapsed_d21_band20(
            manifest, registry_names, (-1, 1)),
        "HW2_negative": expected_collapsed_d21_band20(
            manifest, registry_names, (1, -1)),
        "plus42_omitted": expected_collapsed_d21_band20(
            manifest, registry_names, (1, 1), add_target=False),
    }
    for name, mutated in sorted(mutation_rows.items()):
        if mutated == expected:
            raise CustodyError(
                "collapsed D21 mutation %s is not literally distinct "
                "from the reference" % name)
    if rows != expected:
        raise CustodyError(
            "exact collapsed D21 band20 literal equality failed")
    for name, mutated in sorted(mutation_rows.items()):
        if rows == mutated:
            raise CustodyError(
                "collapsed D21 band20 literally equals mutation %s" % name)
    actual_digest = semantic_rows_sha256(rows, registry_names)
    expected_digest = semantic_rows_sha256(expected, registry_names)
    mutation_digests = {
        name: semantic_rows_sha256(value, registry_names)
        for name, value in mutation_rows.items()
    }
    require(actual_digest == expected_digest,
            "receipt digests disagree after literal equality")
    require(len({expected_digest, *mutation_digests.values()}) == 4,
            "receipt digests fail to separate the mutations")
    return {
        "status": "PASS_EXACT_COLLAPSED_D21_BAND20_LITERAL_EQUALITY",
        "decision_basis": "LITERAL_STRUCTURAL_EQUALITY",
        "digests_are_receipts_only": True,
        "actual_semantic_sha256": actual_digest,
        "expected_semantic_sha256": expected_digest,
        "required_mutation_digests": mutation_digests,
        "all_mutations_literally_refused": True,
    }


def template_bridge_spec():
    one = COMMON.RadicalCoefficient.scalar(1)
    r = COMMON.RadicalCoefficient.generator("r3")
    A1 = COMMON.RadicalCoefficient.generator("A1")
    A2 = COMMON.RadicalCoefficient.generator("A2")
    a1 = COMMON.RadicalCoefficient.scalar(3) + r
    a2 = COMMON.RadicalCoefficient.scalar(3) - r
    b = COMMON.RadicalCoefficient.scalar(4)
    sm = COMMON.RadicalCoefficient.scalar(Fraction(7 ** 12, 2 ** 6))
    C = COMMON.RadicalCoefficient.scalar(243) * sm ** 3 * (2 * r) ** 4
    U = cp_w(4, 0, A1)
    V = cp_w(0, 4, A2)
    E = cp_add(cp_w(4, 0, (9 * one + 5 * r) * A1),
               cp_w(0, 4, (9 * one - 5 * r) * A2))
    inv_4_a1_minus_b = (r + one) * Fraction(1, 8)
    HM = cp_mul(cp_rc(-C * a1 ** 2 * inv_4_a1_minus_b), U)
    E5_1 = cp_add(cp_mul(cp_rc(4 * (a1 - b)), HM),
                  cp_mul(cp_rc(C * a1 ** 2), U))
    E5_2 = cp_add(cp_mul(cp_rc(4 * (a2 - b)), HM),
                  cp_mul(cp_rc(C * a2 ** 2), V))
    e5_2_factor = C * r * (r + one)
    require(not E5_1,
            "literal E5_1 does not vanish after HM reconstruction")
    require(E5_2 == cp_mul(cp_rc(e5_2_factor), E),
            "literal E5_2 is not the displayed unit multiple of E")
    s1F = cp_mul(cp_k3(Fraction(2 ** 8, 7 ** 16)), HM)
    E6 = cp_add(cp_mul(cp_k3(2 ** 24), cp_pow(HM, 3)),
                cp_mul(cp_k3(-(7 ** 48)), cp_pow(s1F, 3)))
    require(not E6,
            "literal E6 cube row does not vanish after s1F reconstruction")
    return {
        "projection_equations": [
            "E=(9+5*r3)*A1*W1^4+(9-5*r3)*A2*W2^4=0",
            "W1*W2*uW12-1=0",
        ],
        "one_unit_coordinate": "uW12",
        "HM_reconstruction":
            "-C*a1^2*A1*W1^4/(4*(a1-4))",
        "s1F_reconstruction": "(2^8/7^16)*HM",
        "C": "243*(7^12/2^6)^3*(2*r3)^4",
        "E_semantic_sha256": semantic_cp_sha256(E),
        "HM_semantic_sha256": semantic_cp_sha256(HM),
        "s1F_semantic_sha256": semantic_cp_sha256(s1F),
        "literal_replay": {
            "E5_1_identically_zero_after_HM_reconstruction": True,
            "E5_2_equals_unit_times_E": True,
            "E5_2_unit_factor_semantic_sha256": semantic_cp_sha256(
                cp_rc(e5_2_factor)),
            "E6_identically_zero_after_s1F_reconstruction": True,
        },
        "scope": "DISPLAYED_E5_E6_AND_ONE_W_PRODUCT_UNIT_ONLY",
        "full_template_claim": None,
    }


def evaluate_cp_mod(value, W1, W2, modulus, frame):
    total = 0
    for (power1, power2), coefficient in value.items():
        term = coefficient.specialize(modulus, frame)
        term = term * pow(W1, power1, modulus) % modulus
        term = term * pow(W2, power2, modulus) % modulus
        total = (total + term) % modulus
    return total


def evaluate_cvexpr_mod(expression, assignment, registry_names,
                        W1, W2, modulus, frame):
    total = 0
    for monomial, coefficient in expression.items():
        term = evaluate_cp_mod(coefficient, W1, W2, modulus, frame)
        for index in monomial:
            term = term * assignment[registry_names[index]] % modulus
        total = (total + term) % modulus
    return total


def template_bridge_modular_gate(W1, W2, uW12, modulus, frame):
    spec = template_bridge_spec()
    one = COMMON.RadicalCoefficient.scalar(1)
    r = COMMON.RadicalCoefficient.generator("r3")
    A1 = COMMON.RadicalCoefficient.generator("A1")
    A2 = COMMON.RadicalCoefficient.generator("A2")
    a1 = COMMON.RadicalCoefficient.scalar(3) + r
    a2 = COMMON.RadicalCoefficient.scalar(3) - r
    b = COMMON.RadicalCoefficient.scalar(4)
    sm = COMMON.RadicalCoefficient.scalar(Fraction(7 ** 12, 2 ** 6))
    C = COMMON.RadicalCoefficient.scalar(243) * sm ** 3 * (2 * r) ** 4
    E = cp_add(cp_w(4, 0, (9 * one + 5 * r) * A1),
               cp_w(0, 4, (9 * one - 5 * r) * A2))
    inv = (r + one) * Fraction(1, 8)
    HM = cp_mul(cp_rc(-C * a1 ** 2 * inv), cp_w(4, 0, A1))
    s1F = cp_mul(cp_k3(Fraction(2 ** 8, 7 ** 16)), HM)
    hm = evaluate_cp_mod(HM, W1, W2, modulus, frame)
    s1f = evaluate_cp_mod(s1F, W1, W2, modulus, frame)
    values = {
        "E": evaluate_cp_mod(E, W1, W2, modulus, frame),
        "unit": (W1 * W2 * uW12 - 1) % modulus,
        "E5_1": (4 * ((3 + frame.r3) - 4) * hm +
                   evaluate_cp_mod(cp_mul(cp_rc(C * a1 ** 2),
                                          cp_w(4, 0, A1)),
                                   W1, W2, modulus, frame)) % modulus,
        "E5_2": (4 * ((3 - frame.r3) - 4) * hm +
                   evaluate_cp_mod(cp_mul(cp_rc(C * a2 ** 2),
                                          cp_w(0, 4, A2)),
                                   W1, W2, modulus, frame)) % modulus,
        "E6": (pow(2, 24, modulus) * pow(hm, 3, modulus) -
                pow(7, 48, modulus) * pow(s1f, 3, modulus)) % modulus,
    }
    if any(values.values()) or not hm or not s1f:
        raise CustodyError("literal E/E5/E6/unit reconstruction gate failed")
    return {"status": "PASS_LITERAL_E5_E6_ONE_UNIT_RECONSTRUCTION",
            "values": values, "HM": hm, "s1F": s1f,
            "bridge_spec_sha256": sha256_bytes(canonical_json(spec))}


def registered_modular_replay(rows, registry_names, manifest):
    reports = []
    for prime in (105337, 105673):
        relative = "cases/d43_full_certificate_p%d.json" % prime
        path = ROOT / relative
        if sha256_path(path) != manifest["input_sha256"][relative]:
            raise CustodyError("registered certificate hash drift")
        point = json.loads(path.read_text())["point"]
        graph = point["graph_156"]
        assignment = {name: 0 for name in registry_names}
        for name, value in graph.items():
            source_name = BASE.GRAPH_TO_SOURCE.get(name, name)
            if source_name in assignment:
                assignment[source_name] = int(value) % prime
        parked = point["parked_28"]
        W1, W2 = parked["W1"], parked["W2"]
        frame = COMMON.REGISTERED_FRAMES[prime]
        COMMON.validate_registered_prime(prime, frame)
        residuals = {
            "%d,%d" % target: evaluate_cvexpr_mod(
                rows[target], assignment, registry_names,
                W1, W2, prime, frame)
            for target in TARGETS
        }
        nonzero = {target: value for target, value in residuals.items()
                   if value}
        if nonzero:
            raise CustodyError("registered modular all-row replay failed at "
                               "p=%d" % prime)
        unit = pow(W1 * W2 % prime, -1, prime)
        bridge = template_bridge_modular_gate(
            W1, W2, unit, prime, frame)
        reports.append({
            "prime": prime,
            "raw_J_residuals_zero": len(TARGETS),
            "template_bridge_reconstruction": bridge,
        })
    return reports


def validate_exact_inventory(rows):
    live = [target for target in TARGETS if rows[target]]
    zero = [target for target in TARGETS if not rows[target]]
    bands = {}
    for target in live:
        bands[target[1]] = bands.get(target[1], 0) + 1
    degrees = [len(monomial) for target in live
               for monomial in rows[target]]
    if len(live) != 29 or len(zero) != 155:
        raise CustodyError("exact live/zero inventory differs from 29/155")
    if bands != {20: 10, 30: 9, 40: 10}:
        raise CustodyError("exact live-band inventory drift")
    if max(degrees, default=0) > 2:
        raise CustodyError("exact tail degree exceeds two")
    return {"live_rows": len(live), "exact_zero_rows": len(zero),
            "live_bands": {str(key): value for key, value in sorted(bands.items())},
            "max_tail_degree": max(degrees, default=0),
            "exact_zero_targets": [list(target) for target in zero]}


def validate_cover(shards):
    seen = {}
    for shard_index, shard in enumerate(shards):
        for target, row in shard["rows"].items():
            if target in seen:
                raise CustodyError("duplicate target %r" % (target,))
            seen[target] = (shard_index, row)
    missing = set(TARGETS) - set(seen)
    extra = set(seen) - set(TARGETS)
    if missing or extra:
        raise CustodyError("184-cover mismatch")
    return {target: seen[target][1] for target in TARGETS}


def load_shard_receipt(receipt_path: Path, manifest_hash: str,
                       preflight_hash: str, pair_custody: str,
                       gate_hash: str, lease, lease_hash):
    receipt = json.loads(receipt_path.read_text())
    require(receipt["schema"] == SHARD_SCHEMA, "shard receipt schema drift")
    require(receipt["manifest_sha256"] == manifest_hash,
            "shard receipt manifest hash drift")
    require(receipt["preflight_receipt_sha256"] == preflight_hash,
            "shard receipt preflight hash drift")
    require(receipt["pair_custody_sha256"] == pair_custody,
            "shard receipt pair custody drift")
    require(receipt["pilot_gate_sha256"] == gate_hash,
            "shard receipt gate hash drift")
    require_lease_binding(receipt, lease, lease_hash, "shard receipt")
    payload_path = receipt_path.parent / receipt["payload"]
    payload = _load_pickle_after_hash(payload_path,
                                      receipt["payload_sha256"])
    require(payload["schema"] == SHARD_SCHEMA, "shard payload schema drift")
    require(payload["manifest_sha256"] == manifest_hash,
            "shard payload manifest hash drift")
    require(payload["preflight_receipt_sha256"] == preflight_hash,
            "shard payload preflight hash drift")
    require(payload["pair_custody_sha256"] == pair_custody,
            "shard payload pair custody drift")
    require(payload["pilot_gate_sha256"] == gate_hash,
            "shard payload gate hash drift")
    require_lease_binding(payload, lease, lease_hash, "shard payload")
    require(payload["semantic_sha256"] == semantic_rows_sha256(
        payload["rows"], payload["registry_names"]),
        "shard payload semantic digest drift")
    require(payload["semantic_sha256"] == receipt["semantic_sha256"],
            "shard payload/receipt semantic digest mismatch")
    require(tuple(payload["targets"]) == tuple(payload["rows"]),
            "shard payload target census drift")
    return payload


def conditional_emit_all(manifest_path: Path, preflight_path: Path,
                         lease_path: Path, pair_path: Path,
                         output_dir: Path):
    manifest, manifest_hash = load_manifest(manifest_path)
    assert_operational_registration(manifest)
    verify_operational_sources(manifest)
    run_dir = Path(os.environ.get("JOB_ROOT", ""))
    lease, lease_hash = load_run_lease(lease_path, run_dir)
    _preflight, preflight_hash = validate_preflight_receipt(
        preflight_path, manifest, manifest_hash, lease, lease_hash)
    jf, jg, names, pair = load_pair(pair_path, manifest_hash, preflight_hash,
                                    lease, lease_hash)
    band20 = selected_source_rows(jf, jg, BAND_TARGETS[20])
    gate = {
        "schema": GATE_SCHEMA,
        "status": "PENDING",
        "manifest_sha256": manifest_hash,
        "preflight_receipt_sha256": preflight_hash,
        "pair_sha256": sha256_path(pair_path),
        "pair_custody_sha256": pair["pair_custody_sha256"],
        "coefficient_algebra_sha256": coefficient_algebra_sha256(),
    }
    gate.update(lease_binding(lease, lease_hash))
    try:
        gate["regression"] = collapsed_d21_gate(band20, manifest, names)
    except Exception as error:
        gate["status"] = "FAIL_NO_CONTINUATION"
        gate["error"] = str(error)
        atomic_json(output_dir / "PILOT_GATE.json", gate)
        raise
    gate["status"] = "PASS_CONTINUE_SAME_MANIFEST_ALL184"
    atomic_json(output_dir / "PILOT_GATE.json", gate)
    gate_hash = sha256_path(output_dir / "PILOT_GATE.json")

    all_rows = {}
    shard_receipt_paths = []
    shard_dir = output_dir / "shards"
    for band in BANDS:
        rows = band20 if band == 20 else selected_source_rows(
            jf, jg, BAND_TARGETS[band])
        all_rows.update(rows)
        payload = {
            "schema": SHARD_SCHEMA,
            "status": "EXACT_A00PP_SOURCE_ROW_SHARD_COMPLETE",
            "manifest_sha256": manifest_hash,
            "preflight_receipt_sha256": preflight_hash,
            "pair_custody_sha256": pair["pair_custody_sha256"],
            "pilot_gate_sha256": gate_hash,
            "band": band,
            "targets": BAND_TARGETS[band],
            "registry_names": names,
            "rows": rows,
            "semantic_sha256": semantic_rows_sha256(rows, names),
        }
        payload.update(lease_binding(lease, lease_hash))
        path = shard_dir / ("band%02d.pkl" % band)
        atomic_pickle(path, payload)
        receipt = {key: payload[key] for key in (
            "schema", "status", "manifest_sha256",
            "preflight_receipt_sha256", "pair_custody_sha256",
            "pilot_gate_sha256", "band", "semantic_sha256",
            "run_nonce", "lease_sha256", "terminal_authority")}
        receipt.update({"payload": path.name,
                        "payload_sha256": sha256_path(path),
                        "targets": [list(target) for target in rows]})
        receipt_path = path.with_suffix(".pkl.receipt.json")
        atomic_json(receipt_path, receipt)
        shard_receipt_paths.append(receipt_path)
    shards = [load_shard_receipt(
        path, manifest_hash, preflight_hash, pair["pair_custody_sha256"],
        gate_hash, lease, lease_hash) for path in shard_receipt_paths]
    rows = validate_cover(shards)
    require(rows == {target: all_rows[target] for target in TARGETS},
            "reloaded shard cover is not literally the emitted rows")
    inventory = validate_exact_inventory(rows)
    bridge = template_bridge_spec()
    modular_replays = registered_modular_replay(rows, names, manifest)
    merged = {
        "schema": MERGE_SCHEMA,
        "status": "EXACT_A00PP_184_RAW_J_ROWS_MERGED_NO_SOLVE",
        "manifest_sha256": manifest_hash,
        "preflight_receipt_sha256": preflight_hash,
        "pair_custody_sha256": pair["pair_custody_sha256"],
        "pilot_gate_sha256": gate_hash,
        "registry_sha256": EXPECTED_REGISTRY_SHA256,
        "registry_names": names,
        "support": SUPPORT,
        "support_sha256": support_sha256(),
        "coefficient_algebra": COEFFICIENT_ALGEBRA,
        "coefficient_algebra_sha256": coefficient_algebra_sha256(),
        "targets": TARGETS,
        "rows": rows,
        "semantic_sha256": semantic_rows_sha256(rows, names),
        "exact_inventory": inventory,
        "template_bridge": bridge,
        "template_bridge_sha256": sha256_bytes(canonical_json(bridge)),
        "registered_modular_replays": modular_replays,
        "claim_boundary": manifest["claim_boundary"],
    }
    merged.update(lease_binding(lease, lease_hash))
    merge_path = output_dir / "d43_a00pp_exact_184_raw_J_rows.pkl"
    atomic_pickle(merge_path, merged)
    receipt = {
        "schema": MERGE_SCHEMA + ".receipt",
        "status": merged["status"],
        "manifest_sha256": manifest_hash,
        "preflight_receipt_sha256": preflight_hash,
        "pair_custody_sha256": pair["pair_custody_sha256"],
        "pilot_gate_sha256": gate_hash,
        "payload": merge_path.name,
        "payload_sha256": sha256_path(merge_path),
        "semantic_sha256": merged["semantic_sha256"],
        "exact_inventory": inventory,
        "template_bridge_sha256": merged["template_bridge_sha256"],
    }
    receipt.update(lease_binding(lease, lease_hash))
    atomic_json(output_dir / "MERGE_RECEIPT.json", receipt)
    return receipt


def finalize_candidate(manifest_path: Path, preflight_path: Path,
                       lease_path: Path, output_dir: Path,
                       _fail_stage=None):
    """Re-verify the complete payload chain and stage a non-authoritative
    finalize candidate.

    This command never writes a verdict, terminal marker, stage-complete
    value, or positive receipt.  The single authoritative terminal object is
    published later, once, by the job-contract terminal decision after all
    custody and archive gates.  ``_fail_stage`` is a hostile-test injection
    point; production callers never set it.
    """
    manifest, manifest_hash = load_manifest(manifest_path)
    assert_operational_registration(manifest)
    verify_operational_sources(manifest)
    run_dir = Path(os.environ.get("JOB_ROOT", ""))
    lease, lease_hash = load_run_lease(lease_path, run_dir)
    _preflight, preflight_hash = validate_preflight_receipt(
        preflight_path, manifest, manifest_hash, lease, lease_hash)
    require(_fail_stage != "after_preflight", "INJECTED_FAILURE:after_preflight")
    gate_path = output_dir / "PILOT_GATE.json"
    gate = json.loads(gate_path.read_text())
    require(gate["status"] == "PASS_CONTINUE_SAME_MANIFEST_ALL184",
            "pilot gate is not a continuation pass")
    require(gate["manifest_sha256"] == manifest_hash,
            "pilot gate manifest hash drift")
    require_lease_binding(gate, lease, lease_hash, "pilot gate")
    gate_hash = sha256_path(gate_path)
    require(_fail_stage != "after_gate", "INJECTED_FAILURE:after_gate")
    merge_receipt_path = output_dir / "MERGE_RECEIPT.json"
    merge_receipt = json.loads(merge_receipt_path.read_text())
    require(merge_receipt["schema"] == MERGE_SCHEMA + ".receipt",
            "merge receipt schema drift")
    require(merge_receipt["status"] ==
            "EXACT_A00PP_184_RAW_J_ROWS_MERGED_NO_SOLVE",
            "merge receipt status drift")
    require(merge_receipt["manifest_sha256"] == manifest_hash,
            "merge receipt manifest hash drift")
    require(merge_receipt["preflight_receipt_sha256"] == preflight_hash,
            "merge receipt preflight hash drift")
    require(merge_receipt["pilot_gate_sha256"] == gate_hash,
            "merge receipt gate hash drift")
    require_lease_binding(merge_receipt, lease, lease_hash, "merge receipt")
    require(_fail_stage != "after_merge_receipt",
            "INJECTED_FAILURE:after_merge_receipt")
    merge_path = output_dir / merge_receipt["payload"]
    merged = _load_pickle_after_hash(merge_path,
                                     merge_receipt["payload_sha256"])
    require(merged["schema"] == MERGE_SCHEMA, "merge payload schema drift")
    require(merged["status"] == merge_receipt["status"],
            "merge payload status drift")
    require(merged["manifest_sha256"] == manifest_hash,
            "merge payload manifest hash drift")
    require_lease_binding(merged, lease, lease_hash, "merge payload")
    require(merged["semantic_sha256"] == semantic_rows_sha256(
        merged["rows"], merged["registry_names"]),
        "merge payload semantic digest drift on recomputation")
    require(merged["semantic_sha256"] == merge_receipt["semantic_sha256"],
            "merge payload/receipt semantic digest mismatch")
    inventory = validate_exact_inventory(merged["rows"])
    require(inventory == merged["exact_inventory"],
            "merge payload inventory drift on recomputation")
    require(_fail_stage != "after_merge_payload",
            "INJECTED_FAILURE:after_merge_payload")
    candidate = {
        "schema": CANDIDATE_SCHEMA,
        "status": CANDIDATE_STATUS,
        "manifest_sha256": manifest_hash,
        "preflight_receipt_sha256": preflight_hash,
        "pilot_gate_sha256": gate_hash,
        "merge_receipt_sha256": sha256_path(merge_receipt_path),
        "merge_payload_sha256": merge_receipt["payload_sha256"],
        "semantic_sha256": merged["semantic_sha256"],
        "exact_inventory": inventory,
        "template_bridge_sha256": merged["template_bridge_sha256"],
        "claim_boundary": manifest["claim_boundary"],
        "utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }
    candidate.update(lease_binding(lease, lease_hash))
    require(_fail_stage != "before_candidate_write",
            "INJECTED_FAILURE:before_candidate_write")
    atomic_json(output_dir / "FINALIZE_CANDIDATE.json", candidate)
    return candidate


def print_registry():
    _orbits, names, registry_hash, pin42 = BASE.reconstruct_registry()
    require_registry(names, registry_hash, pin42)
    print(json.dumps({
        "schema": SCHEMA,
        "registry_variables": len(names),
        "registry_sha256": registry_hash,
        "support": list(SUPPORT),
        "support_sha256": support_sha256(),
        "pin42_names": list(pin42),
        "targets": len(TARGETS),
        "target_registry_sha256": target_registry_sha256(),
        "coefficient_algebra": COEFFICIENT_ALGEBRA,
        "coefficient_algebra_sha256": coefficient_algebra_sha256(),
        "template_bridge": template_bridge_spec(),
    }, indent=1, sort_keys=True))


def main():
    parser = argparse.ArgumentParser()
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("registry")
    build = commands.add_parser("build-side")
    build.add_argument("--manifest", type=Path, required=True)
    build.add_argument("--preflight-receipt", type=Path, required=True)
    build.add_argument("--lease", type=Path, required=True)
    build.add_argument("--side", choices=("f", "g"), required=True)
    build.add_argument("--output", type=Path, required=True)
    pair = commands.add_parser("assemble-pair")
    pair.add_argument("--manifest", type=Path, required=True)
    pair.add_argument("--preflight-receipt", type=Path, required=True)
    pair.add_argument("--lease", type=Path, required=True)
    pair.add_argument("--f-receipt", type=Path, required=True)
    pair.add_argument("--g-receipt", type=Path, required=True)
    pair.add_argument("--output", type=Path, required=True)
    emit = commands.add_parser("conditional-emit-all")
    emit.add_argument("--manifest", type=Path, required=True)
    emit.add_argument("--preflight-receipt", type=Path, required=True)
    emit.add_argument("--lease", type=Path, required=True)
    emit.add_argument("--pair", type=Path, required=True)
    emit.add_argument("--output-dir", type=Path, required=True)
    final = commands.add_parser("finalize-candidate")
    final.add_argument("--manifest", type=Path, required=True)
    final.add_argument("--preflight-receipt", type=Path, required=True)
    final.add_argument("--lease", type=Path, required=True)
    final.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    if args.command == "registry":
        print_registry()
    elif args.command == "build-side":
        print(json.dumps(build_side(args.manifest, args.preflight_receipt,
                                    args.lease, args.side, args.output),
                         sort_keys=True))
    elif args.command == "assemble-pair":
        print(json.dumps(assemble_pair(
            args.manifest, args.preflight_receipt, args.lease,
            args.f_receipt, args.g_receipt, args.output), sort_keys=True))
    elif args.command == "conditional-emit-all":
        print(json.dumps(conditional_emit_all(
            args.manifest, args.preflight_receipt, args.lease, args.pair,
            args.output_dir), sort_keys=True))
    elif args.command == "finalize-candidate":
        print(json.dumps(finalize_candidate(
            args.manifest, args.preflight_receipt, args.lease,
            args.output_dir), sort_keys=True))
    else:
        raise CustodyError("unknown command %r" % (args.command,))


if __name__ == "__main__":
    main()
