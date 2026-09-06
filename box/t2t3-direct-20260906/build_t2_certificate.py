#!/usr/bin/env python3
"""Emit a literal T2 certificate subset of the direct T2+T3 presentation.

The subset consists of the frozen source residuals, every T2 upper row, the
complete attained T2 face, and all three production localizers.  It never
pivots a semantic variable.  Hence UNIT for this smaller ideal is an exact
certificate that the complete direct ideal is UNIT; NONUNIT has no force for
the complete ideal.

This focused builder computes the face coefficients directly and does not
expand or serialize the omitted strict/T3 rows.  All selected rows go through
the exact same primitive-integer emitter as ``build_direct.py``.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import resource
import time
from pathlib import Path

from build_direct import DirectChart, EXPECTED, seq_sha, sha_path


class T2Certificate(DirectChart):
    def __init__(self, tag: str, output: Path, face_indices: list[int] | None = None):
        self.face_indices = list(range(EXPECTED[tag]["D2"] + 1)) if face_indices is None else sorted(set(face_indices))
        if not self.face_indices or self.face_indices[0] < 0 or self.face_indices[-1] > EXPECTED[tag]["D2"]:
            raise ValueError("face indices must be a nonempty subset of 0..D2")
        self.complete_face = self.face_indices == list(range(EXPECTED[tag]["D2"] + 1))
        super().__init__(tag, output)

    def build(self):
        h, D, C = self.source_series()
        a, b, c, d = [self.var("target_" + letter) for letter in "abcd"]
        H = self.add((h, 1), ({(self.k, 0): b}, -self.C("1/6")))
        v = self.add(
            (D, 1),
            ({(2 * self.k - 1, 0): a / 3 + b * b / 18}, 1),
        )
        V = self.add(
            (C, 1),
            (self.shift(D, self.k), -b / 4),
            ({(3 * self.k - 1, 0): a * b / 12 + b**3 / 54 - c / 2}, 1),
        )
        assert min(r for r, _ in V) >= 1
        U = self.shift(V, -1, scalar=self.C("8/3"))
        Rraw = self.add((self.mul(v, v), 1), (self.mul(U, H), -1))
        Rlow = {}
        for (r, z), value in sorted(Rraw.items()):
            if z >= self.k:
                self.raw_row("T2_upper", f"T2_Rhigh_{r}_{z}", value)
            else:
                Rlow[(r, z)] = value

        for index, expression in enumerate(self.residuals):
            self.raw_row("source_residual", f"source_residual_{index}", self.C(expression))

        # These are exactly the six summands of Q_* in build_direct.py.  Only
        # the complete attained face r=lead is evaluated here.
        HH = self.mul(H, H, self.qcap - min(r for r, _ in Rlow))
        vU = self.mul(v, U, self.qcap - 1)
        pp = d + b * c / 2 - (a + b * b / 4) ** 2 / 3
        for z in self.face_indices:
            r = self.lead
            value = self.coefficient_mul(Rlow, HH, (r, z)) * self.C("3/4")
            value += self.coefficient_mul(vU, H, (r - 1, z)) * self.C("-1/8")
            value += self.coefficient_mul(v, Rlow, (r - 1, z))
            value += self.coefficient_mul(U, U, (r - 2, z)) * self.C("-9/64")
            value += HH.get((r - (4 * self.k - 2), z), self.zero) * pp
            value += v.get((r - (4 * self.k - 1), z), self.zero) * pp
            if self.spec["t2z"] <= z <= self.D2:
                target = self.C(math.comb(self.spec["t2p"], z - self.spec["t2z"]))
                target *= self.var(self.spec["lam2"])
            else:
                target = self.zero
            self.raw_row("T2_face", f"T2_face_{z}", value - target)

        self.raw_row(
            "inverse", "inverse_T2",
            self.var(self.spec["zlam2"]) * self.var(self.spec["lam2"]) - 1,
        )
        self.raw_row("inverse", "inverse_T3", self.var("Z3") * self.var("lambda3") - 1)
        self.raw_row(
            "inverse", "inverse_separation",
            self.var(self.spec["zsep"]) * self.var(self.spec["sep"]) - 1,
        )
        self.finish_certificate(h, D, C)

    def finish_certificate(self, h, D, C):
        expected_upper = self.spec["nonzero_counts"]["T2_upper"]
        expected_face = self.spec["nonzero_counts"]["T2_face"]
        expected_residual = self.spec["nonzero_counts"].get("source_residual", 0)
        assert self.raw_counts["T2_upper"] == self.spec["raw_counts"]["T2_upper"]
        assert self.raw_counts["T2_face"] == len(self.face_indices)
        assert self.emitted_counts["T2_upper"] == expected_upper
        if self.complete_face:
            assert self.emitted_counts["T2_face"] == expected_face
        assert self.emitted_counts["source_residual"] == expected_residual
        assert self.emitted_counts["inverse"] == 3
        assert self.row_count == (
            expected_upper + self.emitted_counts["T2_face"] + expected_residual + 3
        )

        self.sing.write(
            ";\n"
            'print("ALL_ROWS_PARSED");\n'
            'print("BEGIN_STD");\n'
            "ideal G=std(I);\n"
            'print("END_STD");\n'
            'print("BEGIN_RESULT");\n'
            'print("REDUCE_ONE="+string(reduce(1,G)));\n'
            'print("DIMENSION="+string(dim(G)));\n'
            'print("BASIS_SIZE="+string(size(G)));\n'
            'print("END_RESULT");\n'
            "quit;\n"
        )
        self.ms.write("\n")
        self.sing.close()
        self.ms.close()
        self.labels.close()

        variable_payload = {
            "schema": "T2T3_DIRECT_VARIABLE_MAP/v1",
            "case": self.tag,
            "semantic_order": self.semantic_names,
            "solver_order": self.names,
            "records": [
                {
                    "solver_index": i,
                    "semantic_index": self.semantic_names.index(name),
                    "name": name,
                    "alias": self.aliases[i],
                    "site_r": self.sites[i][0],
                    "site_z": self.sites[i][1],
                    "inverse_dp_block": i >= self.noninverse_count,
                }
                for i, name in enumerate(self.names)
            ],
        }
        self.variables_path.write_text(json.dumps(variable_payload, indent=2, sort_keys=True) + "\n")
        meta = {
            "schema": (
                "T2T3_DIRECT_T2_CERTIFICATE/v1" if self.complete_face
                else "T2T3_DIRECT_T2_FACE_SUBSET/v1"
            ),
            "status": "EMITTED_EXACT_Q_AND_MODULAR_NOT_RUN",
            "case": self.tag,
            "classification_scope": (
                "literal full-direct-ideal generator subset; UNIT is conclusive for the full ideal, "
                "NONUNIT is inconclusive"
            ),
            "selected_blocks": [
                "source_residual", "T2_upper",
                "T2_face" if self.complete_face else "T2_face_subset", "inverse",
            ],
            "omitted_blocks": ["T2_strict", "T3_recurrence", "T3_strict", "T3_face"],
            "selected_T2_face_indices": self.face_indices,
            "complete_T2_face": self.complete_face,
            "field": "Q",
            "modular_prime": self.PRIME,
            "input": str(self.input),
            "input_sha256": sha_path(self.input),
            "semantic_variable_count": len(self.semantic_names),
            "semantic_variable_order_sha256": seq_sha(self.semantic_names),
            "solver_variable_count": len(self.names),
            "solver_variable_order_sha256": seq_sha(self.names),
            "alias_order_sha256": seq_sha(self.aliases),
            "graph_variables_emitted": 0,
            "constraint_variables_pivoted": 0,
            "raw_row_counts": dict(sorted(self.raw_counts.items())),
            "identically_zero_after_substitution": dict(sorted(self.zero_counts.items())),
            "emitted_nonzero_counts": dict(sorted(self.emitted_counts.items())),
            "emitted_generator_count": self.row_count,
            "raw_row_labels_sha256": self.raw_label_sha.hexdigest(),
            "emitted_row_labels_sha256": self.emitted_label_sha.hexdigest(),
            "canonical_primitive_generator_sequence_sha256": self.canonical_sha.hexdigest(),
            "original_name_generator_text_sha256": self.generator_text_sha.hexdigest(),
            "expanded_term_count": self.total_terms,
            "msolve_32bit_offset_product": self.total_terms * len(self.names),
            "msolve_32bit_offset_guard": self.MSOLVE_OFFSET_LIMIT,
            "msolve_32bit_offset_safe": self.total_terms * len(self.names) < self.MSOLVE_OFFSET_LIMIT,
            "maximum_generator_terms": self.max_terms[0],
            "maximum_generator_label": self.max_terms[1],
            "maximum_total_degree": self.max_total_degree,
            "order": {
                "singular": f"(M(two-site {self.noninverse_count}x{self.noninverse_count}),dp(3))",
                "matrix_flat_sha256": seq_sha(self.order_matrix),
                "identity_completion_omits": self.order_minor,
                "classification": "global two-site matrix filtration; normalized rows need not be bihomogeneous",
            },
            "T2_target": f"{self.spec['lam2']}*z^{self.spec['t2z']}*(1+z)^{self.spec['t2p']}",
            "localizers": [
                f"{self.spec['zlam2']}*{self.spec['lam2']}-1",
                "Z3*lambda3-1",
                f"{self.spec['zsep']}*{self.spec['sep']}-1",
            ],
            "source_support_rows_preserved_via_frozen_affine_map": True,
            "no_Jacobian_variable_or_tail_rows": True,
            "primitive_integer_rows": True,
            "singular_file": self.sing_path.name,
            "singular_file_bytes": self.sing_path.stat().st_size,
            "singular_file_sha256": sha_path(self.sing_path),
            "msolve_file": self.ms_path.name,
            "msolve_file_bytes": self.ms_path.stat().st_size,
            "msolve_file_sha256": sha_path(self.ms_path),
            "labels_file": self.labels_path.name,
            "labels_file_sha256": sha_path(self.labels_path),
            "variable_map_file": self.variables_path.name,
            "variable_map_sha256": sha_path(self.variables_path),
            "driver_sha256": sha_path(Path(__file__)),
            "shared_emitter_driver_sha256": sha_path(Path(__file__).with_name("build_direct.py")),
            "build_wall_seconds": round(time.monotonic() - self.started, 3),
            "peak_RSS_KiB": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        }
        # Some exact exponent totals arrive from python-flint as fmpz scalars.
        self.meta_path.write_text(
            json.dumps(meta, indent=2, sort_keys=True, default=int) + "\n"
        )
        print(json.dumps(meta, indent=2, sort_keys=True, default=int), flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--case", required=True, choices=sorted(EXPECTED))
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument(
        "--face-z", action="append", type=int,
        help="emit only this T2 face index (repeatable); default is the complete face",
    )
    args = parser.parse_args()
    T2Certificate(args.case, args.output, args.face_z).build()


if __name__ == "__main__":
    main()
