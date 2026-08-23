#!/usr/bin/env python3
"""Fail-closed consolidation of the recovered D43 algebraization gates."""

import argparse
import hashlib
import json
import os
import pickle


HERE = os.path.dirname(os.path.abspath(__file__))
BANDS = tuple(range(6, 43, 2))


def sha256_path(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for block in iter(lambda: handle.read(8 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def load(path):
    with open(path) as handle:
        return json.load(handle)


def run(root, out_path):
    audit_paths = {
        p: os.path.join(root, "d43_integral_recovery_audit_p%d.json" % p)
        for p in (105337, 105673)
    }
    audits = {p: load(path) for p, path in audit_paths.items()}
    for p, audit in audits.items():
        assert int(audit["prime"]) == p
        assert audit["ideal"]["rows"] == 218
        assert audit["ideal"]["variables"] == 184
        assert audit["gates"]["parked_rows"] == "34/34"
        assert audit["gates"]["old_graph_rows"] == "95/95"
        assert audit["gates"]["late_graph_rows"] == "89/89"

    trace_path = os.path.join(root, "d43_nf_trace_p105337.json")
    trace = load(trace_path)
    assert trace["rows"] == 184
    assert trace["membership_identities_replayed"] == "184/184"
    assert trace["checkpoint_rows_dictionary_exact"] == "184/184"

    lift_path = os.path.join(root, "d43_char0_lift_p105337.json")
    lift = load(lift_path)
    jacobian = lift["assembled_special_fiber_jacobian"]
    assert jacobian["full_combined_rank"] == 131
    assert jacobian["zariski_tangent_dimension"] == 53
    assert jacobian["unit_minor"]["determinant_mod_p"] == 810
    assert lift["source_model"]["correction_solvable"]
    assert lift["source_model"]["p2_replay"][
        "all_184_source_rows_zero_mod_p2"]

    local_path = os.path.join(root, "d43_local_fiber_p105337.json")
    local = load(local_path)
    passing = [record for record in local["bands"] if record["pass"]]
    failing = [record for record in local["bands"] if not record["pass"]]
    assert passing and passing[-1]["band"] == 32
    assert len(failing) == 1 and failing[0]["band"] == 34
    assert failing[0]["normal_form"]["nonzero"] is None

    schemas = {}
    checkpoint_hashes = {}
    for p in (105337, 105673):
        schemas[str(p)] = {}
        checkpoint_hashes[str(p)] = {}
        for band in BANDS:
            path = os.path.join(
                root, "d43red",
                "d43red_p%d_a00pp_band%d.pkl" % (p, band))
            with open(path, "rb") as handle:
                payload = pickle.load(handle)
            keys = sorted(payload)
            assert keys == ["band", "fiber", "gbvars", "prime", "rows"]
            schemas[str(p)][str(band)] = keys
            checkpoint_hashes[str(p)][str(band)] = sha256_path(path)
    trace_fields_present = any(
        any("trace" in key.lower() for key in keys)
        for by_band in schemas.values() for keys in by_band.values())
    assert not trace_fields_present

    result = {
        "status": "STAGE 2 OPEN",
        "prime": 105337,
        "scope": "residue-A, B=84, D43 full 218-row presentation",
        "recovered_modular_model": {
            "status": "PASS",
            "primes": [105337, 105673],
            "variables": 184,
            "rows": 218,
            "blocks": {"parked": 34, "old_graph": 95,
                       "late_graph": 89},
            "audit_paths": audit_paths,
            "audit_sha256": {str(p): sha256_path(path)
                              for p, path in audit_paths.items()},
            "checkpoint_payload_keys": schemas,
            "checkpoint_trace_fields_present": trace_fields_present,
            "checkpoint_sha256": checkpoint_hashes,
        },
        "source_to_nf_mod_p": {
            "status": "PASS",
            "rows": trace["rows"],
            "raw_terms_after_grouping": trace["raw_terms_after_grouping"],
            "nf_terms": trace["nf_terms"],
            "trace_quotient_terms": trace["trace_quotient_terms"],
            "identities": trace["membership_identities_replayed"],
            "checkpoint_matches": trace[
                "checkpoint_rows_dictionary_exact"],
            "aggregate_trace_sha256": trace[
                "aggregate_trace_sha256"],
            "certificate": trace_path,
            "certificate_sha256": sha256_path(trace_path),
        },
        "common_integral_model": {
            "status": "NOT CERTIFIED",
            "positive": {
                "coefficient_radicals_hensel_lifted": True,
                "pristine_184_row_source_model_over_Zp": True,
                "source_model_p2_correction": "SOLVABLE",
                "mod_p_source_to_D23_NF_membership": "184/184",
            },
            "missing": [
                "a common integral or Z_p 34-row parked presentation derived from the source model",
                "integral/Z_p membership of the 509 D23 reducers in those parked generators",
                "integral/Z_p raw-to-NF identities; the recovered and regenerated traces stop over F_p",
                "an all-218-row p^2 replay in one common 184-coordinate integral presentation",
            ],
            "forbidden_promotion":
                "least-residue lifts of the prime-specialized parked/NF coefficients would define an unverified model",
        },
        "special_fiber_linear_data": {
            "jacobian_rank": 131,
            "tangent_dimension": 53,
            "unit_minor_determinant_mod_p": 810,
            "certificate": lift_path,
            "certificate_sha256": sha256_path(lift_path),
        },
        "dimension_generation_flatness": {
            "status": "NOT CERTIFIED",
            "fixed_parked_graph_fiber": {
                "ambient_variables": 156,
                "full_jacobian_rank": 111,
                "bandwise_local_generation_passed_through_band": 32,
                "passed_prefix_rank": passing[-1]["prefix_rank"],
                "first_inconclusive_band": 34,
                "dependent_rows": failing[0]["dependent_rows_checked"],
                "normal_form_result": "TIMEOUT; no nonzero remainder returned",
                "timeout_seconds": failing[0]["normal_form"][
                    "timeout_seconds"],
                "certificate": local_path,
                "certificate_sha256": sha256_path(local_path),
            },
            "local_dimension_53": None,
            "selected_131_generate_218_locally": None,
            "p_flatness": None,
            "standard_smooth": False,
        },
        "conclusion": {
            "source_point_reaches_p2": True,
            "assembled_218_point_reaches_p2": None,
            "Zp_point": None,
            "characteristic_zero_D43_point": None,
            "stage_2_cleared": False,
            "stacks_02H6_applicable": False,
        },
        "next_move": [
            "re-emit the D23/D25 parked system over the source radical number ring (or Z_p) with reducer-to-parked traces",
            "then run the bandwise local membership proof in the 14-free parked cell; if band 34 remains expensive, move to a non-origin point on that cell/component",
            "only after localized generation, deduce the 53-dimensional complete intersection and p-flatness and invoke formal smoothness",
        ],
    }
    with open(out_path, "w") as handle:
        json.dump(result, handle, indent=1, sort_keys=True)
        handle.write("\n")
    print("D43 integral gate: modular fidelity PASS; integral/local smooth gates OPEN -> %s" %
          out_path, flush=True)
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=HERE)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    run(args.root, args.out)


if __name__ == "__main__":
    main()
