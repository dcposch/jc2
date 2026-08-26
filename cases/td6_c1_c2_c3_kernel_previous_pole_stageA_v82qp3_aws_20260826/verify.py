#!/usr/bin/env python3
"""Lightweight custody/string verifier for the frozen V82 Stage-A package."""

from hashlib import sha256
from pathlib import Path


HERE = Path(__file__).resolve().parent
Q_TABLE_SHA = "b1b1f6980b03fb5ea4695ba82eb3fc628db410e1fc7932161c2a1ca29352cb30"
Q_KERNEL_SHA = "ef4d3be85c40e12582c80963eb36e9e3ff843ec4c239679d0060ff873c4905bb"
D_TABLE_SHA = "2c0e79ec04b6e8cfc4da5ca71454e2b27aac9ad2fa20a13a97b3066947f76400"
Q_SOURCE_SHA = "cc7717b46d667726d0b4b51b51027b19dfbbb3823104018fca4a912af6eb6579"
D_SOURCE_SHA = "1a23ceca70fa65b7907e301972356db899b28f1a5ff7e91f52d397fede2b24a6"


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def require(text, *markers):
    for marker in markers:
        assert marker in text, marker


def main():
    for host in ("r6d", "box03"):
        q = HERE / "evidence" / host / "q"
        assert digest(q / "source.tar.gz") == Q_SOURCE_SHA
        assert digest(q / "output" / "PREVIOUS_POLE_CONORMAL.tsv") == Q_TABLE_SHA
        assert digest(q / "output" / "PREVIOUS_POLE_KERNEL.exact.tsv") == Q_KERNEL_SHA
        assert len((q / "output" / "PREVIOUS_POLE_CONORMAL.tsv").read_text().splitlines()) == 1
        assert len((q / "output" / "PREVIOUS_POLE_KERNEL.exact.tsv").read_text().splitlines()) == 22
        require(
            (q / "stdout").read_text(),
            "previous_pole_all_q_rank=38/94",
            "previous_pole_all_q_dependent_count=1",
            "previous_pole_all_q_pivot_source_replay=true",
            "PREVIOUS_POLE_conormal_coordinate_count=0",
            "PREVIOUS_POLE_conormal_rank=0/22",
            "PREVIOUS_POLE_conormal_kernel_dimension=22",
            "PREVIOUS_POLE_denominator_factor=(1, [])",
            f"PREVIOUS_POLE_conormal_sha256={Q_TABLE_SHA}",
            f"PREVIOUS_POLE_kernel_sha256={Q_KERNEL_SHA}",
            "previous_pole_all_q_full_family_parameterization=true",
        )

        roots = list((HERE / "evidence" / host).glob("td6_v82p3_dead_previous_pole_*"))
        assert len(roots) == 1
        root = roots[0]
        assert digest(root / "source.tar.gz") == D_SOURCE_SHA
        for level, raw_count, raw_sha in (
            (10, 1115, "86e61fc847d09005e00be42eb6cda44312a50ffb4b396ac9195ddaedfeeadfb6"),
            (15, 980, "90e13af111cdda4febadd57ccb6a583b650d5ccca25c473775bb68603e0b99b2"),
        ):
            lane = root / "lanes" / f"d{level}"
            assert (lane / "rc").read_text() == "0\n"
            table = lane / "evidence" / f"D{level}_PREVIOUS_POLE_CONORMAL.tsv"
            assert digest(table) == D_TABLE_SHA
            assert len(table.read_text().splitlines()) == 1
            require(
                (lane / "stdout").read_text(),
                "axisjet_composition_boundary_preflight=true",
                "source_center=(C,V,U);symbolic=true",
                "transport_conormal_exact_zero=true",
                "transport_original_3470_pivot_rows_replayed=true",
                "first_conormal_exact_zero=true",
                "first_raw_source_omission_control=true",
                f"previous_pole_raw_axis_entries={raw_count};sha256={raw_sha}",
                "previous_pole_rank=38/94",
                "previous_pole_dependent_count=0",
                "previous_pole_axis_conormal_rank=0/1",
                "previous_pole_axis_conormal_coordinate_count=0",
                "previous_pole_axis_denominator_factor=(1, [])",
                f"previous_pole_axis_table_sha256={D_TABLE_SHA}",
                "all_previous_pole_pivot_source_combinations_replayed=true",
                "TD6-A3-KERNEL-DEAD-PREVIOUS-POLE-SHARD-V82P3 PASS",
            )

    assert (
        HERE / "evidence" / "r6d" / "q" / "output" / "PREVIOUS_POLE_CONORMAL.tsv"
    ).read_bytes() == (
        HERE / "evidence" / "box03" / "q" / "output" / "PREVIOUS_POLE_CONORMAL.tsv"
    ).read_bytes()
    print("TD6-V82-STAGE-A-QPREV-DIM24-VERIFY PASS")


if __name__ == "__main__":
    main()

