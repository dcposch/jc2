#!/usr/bin/env python3
"""Cheap exact viability gate for full-q transported-FIRST nilpotence."""

from hashlib import sha256
import importlib.util
import os
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
PARENT_PATH = HERE / "replay_v89h10_allq_mod_f_unitriangular_functional_v1.py"
PARENT_SHA256 = "4ff99ca9b7d8539aa369b65a953da63dc731d12ba3faf4184678fe8d0b6b9524"
assert sha256(PARENT_PATH.read_bytes()).hexdigest() == PARENT_SHA256
spec = importlib.util.spec_from_file_location("td6_v89h10q_parent", PARENT_PATH)
p = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = p
spec.loader.exec_module(p)

h5, h6, v87, v85 = p.h5, p.h6, p.v87, p.v85
QPoly, E3 = p.QPoly, p.E3


def main():
    outdir = Path(os.environ["TD6_OUTPUT_DIR"]).resolve()
    outdir.mkdir(parents=True, exist_ok=True)
    assert os.environ.get("AWS_RUN_TAG", "").startswith(
        "td6_v89h10q_allq_transported_nilpotence_quick_"
    )
    print("producer=TD6-V89H10Q-ALLQ-TRANSPORTED-NILPOTENCE-QUICK")
    print(f"parent_sha256={PARENT_SHA256}")
    print("raw_qprime_basis_replay_skipped=true")
    print("P12_compile_and_division_skipped=true", flush=True)

    events, bands, seen = v87.build_bands()
    first = v87.compile_first(bands)
    assert events == 2 and len(first) == 38
    assert set(seen) == set(p.ALLOWED_Q)
    assert all(seen[exponent] == 1 for exponent in p.ALLOWED_Q)
    sources = [v87.source_polynomial(row, rhs) for _, row, rhs in first]
    _, raw_common = v87.assert_denominators_allowed(sources)
    print(f"raw_FIRST_common_denominator=({raw_common})")
    print("literal_allq_FIRST_rebuilt=true", flush=True)

    specialized = h6.specialize_first(first)
    pivots = h5.base_pivot_columns(specialized)
    A0 = [
        [row.get(pivot, QPoly()).constant() for pivot in pivots]
        for _, row, _ in specialized
    ]
    A = [
        [row.get(pivot, QPoly()) for pivot in pivots]
        for _, row, _ in specialized
    ]
    inverse_A0 = h5.inverse_constant_matrix(A0)
    B = h5.matmul_constant_q(inverse_A0, A)
    identity = p.identity_matrix(38)
    N = [
        [B[i][j] - identity[i][j] for j in range(38)]
        for i in range(38)
    ]
    n_sha, n_entries, n_terms, n_degree = p.matrix_stats(N)
    assert n_degree <= 1
    print(f"N_sha256={n_sha}")
    print(f"N_nonzero_entries={n_entries}")
    print(f"N_q_terms={n_terms}")
    print(f"N_max_total_q_degree={n_degree}", flush=True)

    inverse = identity
    power = identity
    records = [
        "power\tsha256\tnonzero_entries\tq_terms\tmax_total_q_degree"
    ]
    nilpotence_index = None
    for exponent in range(1, 39):
        power = h5.matmul_q(power, N)
        digest, entries, terms, degree = p.matrix_stats(power)
        records.append(
            f"{exponent}\t{digest}\t{entries}\t{terms}\t{degree}"
        )
        print(
            f"N_power={exponent};sha256={digest};entries={entries};"
            f"q_terms={terms};max_q_degree={degree}",
            flush=True,
        )
        if not entries:
            nilpotence_index = exponent
            break
        inverse = p.add_scaled_matrix(
            inverse, power, -1 if exponent & 1 else 1
        )
    telemetry = "\n".join(records) + "\n"
    (outdir / "ALLQ_QUICK_NILPOTENCE_TELEMETRY.tsv").write_text(telemetry)
    telemetry_sha = sha256(telemetry.encode()).hexdigest()
    print(f"nilpotence_telemetry_sha256={telemetry_sha}")
    print(f"nilpotence_index={nilpotence_index}", flush=True)
    if nilpotence_index is None:
        print("transported_allq_N_nilpotent=false")
        print("P12_functional_claim=false")
        print("TD6-V89H10Q-ALLQ-TRANSPORTED-NILPOTENCE-QUICK NONNILPOTENT-PASS")
        v85.restore_base_qd_state()
        return

    assert h5.is_identity(h5.matmul_q(B, inverse))
    assert h5.is_identity(h5.matmul_q(inverse, B))
    inverse_sha, inverse_terms = h5.write_qmatrix(
        outdir / "ALLQ_QUICK_RELATIVE_PIVOT_INVERSE.tsv", inverse
    )
    print("transported_allq_N_nilpotent=true")
    print("relative_pivot_inverse_two_sided=true")
    print(f"relative_pivot_inverse_sha256={inverse_sha}")
    print(f"relative_pivot_inverse_terms={inverse_terms}")
    print("P12_functional_claim=false")
    print("TD6-V89H10Q-ALLQ-TRANSPORTED-NILPOTENCE-QUICK PASS")
    v85.restore_base_qd_state()


if __name__ == "__main__":
    main()
