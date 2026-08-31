#!/usr/bin/env python3
"""Exact even-conductor 30--40 delta-sequence/S4 replay.

Pins the already written (PROVISIONAL) arithmetic core and the
delta-sequence-to-braid / V4->S4->S3 counter.  Extends the complete
even-conductor ladder through conductor 40.  The packets' own
parametrization is the even ladder C in {30,32,34,36,38,40}, not the
two-term obstruction guess {34,40}.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys


PINNED_CORE_SHA256 = "a076e204121e1ed291edab8a94b09a9832afd3f04fda2a10cd94d36e5397258a"
PINNED_NEXT_SHA256 = "e01c7815a9ef3be93305ae54d7cdc2747e0e11909f9185031fd2762c4605367b"
CORE_PATH = Path(__file__).with_name("block_descent_a1_genus_ladder_s4_replay.py")
NEXT_PATH = Path(__file__).with_name("block_descent_a1_genus_ladder_next_s4_replay.py")

PUBLISHED_CONDUCTOR_14 = (
    (6, 4, 11),
    (8, 3),
    (8, 6, 3),
    (9, 6, 5),
    (10, 4, 7),
    (12, 8, 3),
    (12, 8, 6, 3),
    (15, 2),
    (15, 6, 2),
    (15, 10, 2),
)

PARENT_CONDUCTOR_28 = (
    (8, 5),
    (8, 6, 17),
    (10, 6, 13),
    (10, 8, 5),
    (12, 8, 10, 13),
    (14, 4, 17),
    (18, 4, 13),
    (20, 8, 5),
    (20, 8, 10, 5),
    (29, 2),
)

EXPECTED_CENSUSES = {
    30: (
        (7, 6),
        (8, 6, 19),
        (9, 6, 13),
        (10, 6, 15),
        (11, 4),
        (12, 8, 10, 15),
        (12, 8, 14, 11),
        (12, 9, 7),
        (14, 4, 19),
        (14, 6, 7),
        (15, 6, 10),
        (15, 10, 6),
        (16, 3),
        (16, 6, 3),
        (16, 12, 3),
        (16, 12, 6, 3),
        (18, 4, 15),
        (18, 12, 9, 7),
        (18, 12, 15, 4),
        (21, 6, 7),
        (22, 4, 11),
        (24, 16, 3),
        (24, 16, 6, 3),
        (24, 16, 12, 3),
        (24, 16, 12, 6, 3),
        (27, 6, 4),
        (27, 18, 6, 4),
        (31, 2),
    ),
    32: (
        (8, 6, 21),
        (9, 5),
        (9, 6, 14),
        (10, 6, 17),
        (10, 8, 9),
        (12, 8, 9),
        (12, 8, 10, 17),
        (12, 8, 14, 13),
        (12, 8, 18, 9),
        (12, 9, 8),
        (14, 4, 21),
        (14, 6, 9),
        (15, 6, 11),
        (15, 9, 5),
        (17, 3),
        (18, 4, 17),
        (18, 12, 5),
        (18, 12, 8, 9),
        (18, 12, 9, 8),
        (18, 12, 10, 5),
        (18, 12, 15, 5),
        (20, 8, 10, 9),
        (21, 6, 8),
        (21, 14, 4),
        (22, 4, 13),
        (25, 10, 4),
        (33, 2),
        (33, 6, 2),
        (33, 22, 2),
    ),
    34: (
        (8, 6, 23),
        (10, 6, 19),
        (12, 8, 10, 19),
        (12, 8, 14, 15),
        (14, 4, 23),
        (15, 10, 7),
        (18, 4, 19),
        (20, 8, 7),
        (20, 8, 14, 7),
        (22, 4, 15),
        (35, 2),
        (35, 10, 2),
        (35, 14, 2),
    ),
    36: (
        (9, 6, 16),
        (10, 6, 21),
        (10, 8, 13),
        (12, 8, 14, 17),
        (12, 8, 18, 13),
        (12, 9, 10),
        (13, 4),
        (14, 4, 25),
        (14, 6, 13),
        (15, 6, 13),
        (16, 6, 9),
        (16, 12, 6, 9),
        (18, 4, 21),
        (18, 12, 8, 13),
        (18, 12, 9, 10),
        (18, 12, 10, 9),
        (18, 12, 21, 4),
        (19, 3),
        (20, 8, 10, 13),
        (21, 6, 10),
        (22, 4, 17),
        (24, 16, 6, 9),
        (24, 16, 12, 6, 9),
        (26, 4, 13),
        (33, 6, 4),
        (37, 2),
    ),
    38: (
        (9, 6, 17),
        (10, 6, 23),
        (10, 8, 15),
        (12, 8, 11),
        (12, 8, 14, 19),
        (12, 8, 18, 15),
        (12, 8, 22, 11),
        (12, 9, 11),
        (14, 4, 27),
        (14, 6, 15),
        (15, 6, 14),
        (15, 9, 8),
        (15, 10, 8),
        (16, 6, 11),
        (16, 12, 6, 11),
        (18, 4, 23),
        (18, 12, 8, 15),
        (18, 12, 9, 11),
        (18, 12, 10, 11),
        (18, 12, 15, 8),
        (20, 3),
        (20, 6, 3),
        (20, 8, 10, 15),
        (20, 8, 14, 11),
        (20, 12, 3),
        (20, 12, 6, 3),
        (20, 15, 3),
        (21, 6, 11),
        (21, 14, 5),
        (22, 4, 19),
        (24, 16, 6, 11),
        (24, 16, 12, 6, 11),
        (26, 4, 15),
        (27, 6, 8),
        (27, 18, 6, 8),
        (30, 20, 3),
        (30, 20, 6, 3),
        (30, 20, 15, 3),
        (39, 2),
        (39, 6, 2),
        (39, 26, 2),
    ),
    40: (
        (10, 6, 25),
        (10, 8, 17),
        (11, 5),
        (12, 8, 14, 21),
        (12, 8, 18, 17),
        (14, 6, 17),
        (18, 4, 25),
        (18, 12, 8, 17),
        (20, 8, 9),
        (20, 8, 10, 17),
        (20, 8, 18, 9),
        (22, 4, 21),
        (25, 10, 6),
        (26, 4, 17),
        (41, 2),
    ),
}

EXPECTED_POSITIVE_COUNTS = {
    "(12, 8, 10, 15)": 72,
    "(12, 9, 7)": 24,
    "(16, 3)": 24,
    "(16, 6, 3)": 72,
    "(16, 12, 3)": 168,
    "(16, 12, 6, 3)": 360,
    "(18, 4, 15)": 72,
    "(18, 12, 9, 7)": 72,
    "(18, 12, 15, 4)": 24,
    "(24, 16, 3)": 168,
    "(24, 16, 6, 3)": 360,
    "(24, 16, 12, 3)": 744,
    "(24, 16, 12, 6, 3)": 1512,
    "(27, 6, 4)": 72,
    "(27, 18, 6, 4)": 936,
    "(8, 6, 21)": 72,
    "(9, 6, 14)": 144,
    "(12, 8, 9)": 168,
    "(12, 8, 18, 9)": 360,
    "(12, 9, 8)": 384,
    "(18, 12, 8, 9)": 72,
    "(18, 12, 9, 8)": 432,
    "(21, 6, 8)": 24,
    "(12, 8, 14, 15)": 72,
    "(9, 6, 16)": 72,
    "(12, 9, 10)": 168,
    "(16, 6, 9)": 72,
    "(16, 12, 6, 9)": 360,
    "(18, 4, 21)": 72,
    "(18, 12, 9, 10)": 792,
    "(18, 12, 21, 4)": 24,
    "(24, 16, 6, 9)": 360,
    "(24, 16, 12, 6, 9)": 1512,
    "(33, 6, 4)": 24,
    "(12, 8, 18, 15)": 360,
    "(12, 9, 11)": 24,
    "(15, 9, 8)": 24,
    "(18, 12, 8, 15)": 72,
    "(18, 12, 9, 11)": 72,
    "(18, 12, 15, 8)": 24,
    "(20, 3)": 24,
    "(20, 6, 3)": 72,
    "(20, 12, 3)": 24,
    "(20, 12, 6, 3)": 72,
    "(20, 15, 3)": 24,
    "(27, 6, 8)": 72,
    "(27, 18, 6, 8)": 936,
    "(30, 20, 3)": 72,
    "(30, 20, 6, 3)": 72,
    "(30, 20, 15, 3)": 72,
    "(12, 8, 14, 21)": 72,
    "(20, 8, 9)": 24,
    "(20, 8, 18, 9)": 72,
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def load_pinned_next():
    core_source = CORE_PATH.read_bytes()
    next_source = NEXT_PATH.read_bytes()
    require(hashlib.sha256(core_source).hexdigest() == PINNED_CORE_SHA256, "pinned genus-ladder core")
    require(hashlib.sha256(next_source).hexdigest() == PINNED_NEXT_SHA256, "pinned genus-ladder next compiler")
    specification = importlib.util.spec_from_file_location("_pinned_genus_ladder_next", NEXT_PATH)
    require(specification is not None and specification.loader is not None, "next import specification")
    module = importlib.util.module_from_spec(specification)
    sys.modules[specification.name] = module
    specification.loader.exec_module(module)
    return module


NEXT = load_pinned_next()
CORE = NEXT.CORE


def alexander_sign_vectors(sequence: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    """All independent signs when r1<=12; both global orientations otherwise.

    The 16-to-26-strand Burau product at t=-1 is the local-runtime cost.
    Colouring still exhausts every 2^h sign vector on every row.
    """

    stages = len(sequence) - 1
    if sequence[1] <= 12:
        return NEXT.sign_vectors(stages)
    return ((1,) * stages, (-1,) * stages)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutate-drop-freeness", action="store_true")
    parser.add_argument("--mutate-framing", action="store_true")
    parser.add_argument("--mutate-quotient", action="store_true")
    parser.add_argument("--mutate-promote-exclusion", action="store_true")
    arguments = parser.parse_args()

    if arguments.mutate_framing:
        NEXT.writhe = lambda word: 0
    if arguments.mutate_quotient:
        NEXT.AFFINE_CONJUGATION[(0, 1)] = (0, 0, 0)

    drop_freeness = arguments.mutate_drop_freeness
    published = CORE.delta_sequences_with_conductor(14, drop_freeness, False)
    require(published == PUBLISHED_CONDUCTOR_14, "published conductor-14 example reproduced")

    parent_28 = CORE.delta_sequences_with_conductor(28, drop_freeness, False)
    require(parent_28 == PARENT_CONDUCTOR_28, "parent conductor-28 census reproduced")

    conductors = (30, 32, 34, 36, 38, 40)
    censuses = {
        conductor: CORE.delta_sequences_with_conductor(conductor, drop_freeness, False)
        for conductor in conductors
    }
    require(censuses == EXPECTED_CENSUSES, "exact recursive delta-sequence censuses at 30--40")
    require(sum(len(sequences) for sequences in censuses.values()) == 152, "152 reduced rows")
    require(
        all(CORE.is_delta_sequence(sequence, drop_freeness=False, drop_ordering=False) for sequences in censuses.values() for sequence in sequences),
        "every enumerated row satisfies the exact reduced axioms",
    )
    require(
        all(CORE.delta_sequence_conductor(sequence) == conductor for conductor, sequences in censuses.items() for sequence in sequences),
        "conductor reconstruction matches the target",
    )

    old_two_cable = CORE.two_cable_of_two_braid_word(3, 7)
    new_strands, new_two_cable = NEXT.compile_delta_sequence((6, 4, 7))
    require(new_strands == 4 and new_two_cable == old_two_cable, "winding-two compiler specialization")

    compiler_controls: dict[str, dict[str, int]] = {}
    all_rows = tuple(sequence for conductor in conductors for sequence in censuses[conductor])
    for sequence in all_rows:
        expected_determinant = NEXT.recursive_alexander_determinant(sequence)
        sign_count = 0
        for signs in alexander_sign_vectors(sequence):
            strands, word = NEXT.compile_delta_sequence(sequence, signs)
            require(strands == sequence[1], "compiled strand count equals r1")
            require(
                CORE.cycle_lengths(CORE.strand_permutation(strands, word)) == (strands,),
                "compiled braid closes to one knot",
            )
            require(
                NEXT.braid_alexander_determinant(strands, word) == expected_determinant,
                "recursive Alexander determinant",
            )
            sign_count += 1
        compiler_controls[str(sequence)] = {
            "alexander_sign_variants": sign_count,
            "strands": sequence[1],
            "alexander_determinant": expected_determinant,
        }

    full_alexander_controls: dict[str, int] = {}
    full_control_signs = {
        (16, 3): NEXT.sign_vectors(1),
        (11, 4): NEXT.sign_vectors(1),
        (20, 8, 9): ((1, 1),),
    }
    for sequence, selected_signs in full_control_signs.items():
        expected = NEXT.recursive_alexander_polynomial(sequence)
        for signs in selected_signs:
            strands, word = NEXT.compile_delta_sequence(sequence, signs)
            expected_numerator = expected * (CORE.ONE - CORE.Laurent.monomial(strands))
            require(
                CORE.unit_normalized(CORE.alexander_numerator(strands, word))
                == CORE.unit_normalized(expected_numerator),
                "full recursive cable Alexander polynomial",
            )
        full_alexander_controls[str(sequence)] = len(selected_signs)

    parent_28_counts: dict[str, int] = {}
    for sequence in parent_28:
        strands, word = NEXT.compile_delta_sequence(sequence)
        full, _, _ = NEXT.lifted_full_s4_colorings(strands, word)
        parent_28_counts[str(sequence)] = full
    require(set(parent_28_counts.values()) == {0}, "parent conductor-28 remains all-zero")

    direct_controls: dict[str, int] = {}
    for sequence in all_rows:
        if sequence[1] > 4:
            continue
        strands, word = NEXT.compile_delta_sequence(sequence)
        lifted, _, _ = NEXT.lifted_full_s4_colorings(strands, word, validate_groups=True)
        direct = CORE.full_s4_colorings(strands, word)
        require(lifted == direct, "V4/S3 counter equals direct 6^n counter")
        direct_controls[str(sequence)] = direct

    unique_c34 = (12, 8, 14, 15)
    c34_strands, c34_word = NEXT.compile_delta_sequence(unique_c34)
    c34_full, c34_fox, c34_lifts = NEXT.lifted_full_s4_colorings(
        c34_strands, c34_word, validate_groups=True
    )
    require(c34_full == 72 and c34_fox == 9 and c34_lifts == 96, "C=34 unique survivor group-validated")

    counts: dict[str, dict[str, object]] = {}
    for conductor, sequences in censuses.items():
        for sequence in sequences:
            variants: dict[str, dict[str, int]] = {}
            for signs in NEXT.sign_vectors(len(sequence) - 1):
                strands, word = NEXT.compile_delta_sequence(sequence, signs)
                full, fox, lifts = NEXT.lifted_full_s4_colorings(strands, word)
                variants["".join("+" if sign > 0 else "-" for sign in signs)] = {
                    "full_S4": full,
                    "fox_colorings": fox,
                    "nonconstant_S4_lifts": lifts,
                }
            counts[str(sequence)] = {
                "conductor": conductor,
                "strands": sequence[1],
                "variants": variants,
            }

    observed_positive_counts = {}
    for sequence in all_rows:
        key = str(sequence)
        positive = "+" * (len(sequence) - 1)
        full = counts[key]["variants"][positive]["full_S4"]
        if full:
            observed_positive_counts[key] = full
    require(observed_positive_counts == EXPECTED_POSITIVE_COUNTS, "frozen 30--40 survivor census")
    require(
        all(len({variant["full_S4"] for variant in row["variants"].values()}) == 1 for row in counts.values()),
        "all independent sign variants have the same count",
    )

    survivors = {
        sequence: sorted(sign for sign, data in row["variants"].items() if data["full_S4"])
        for sequence, row in counts.items()
        if any(data["full_S4"] for data in row["variants"].values())
    }

    if arguments.mutate_promote_exclusion:
        require(
            not any(
                row["conductor"] in (34, 40)
                and any(variant["full_S4"] for variant in row["variants"].values())
                for row in counts.values()
            ),
            "false 10+6k complete-exclusion at 34 and 40",
        )

    payload = {
        "status": "PASS-A1-GENUS-LADDER-C34-C40-S4-CENSUS",
        "pinned_core_sha256": PINNED_CORE_SHA256,
        "pinned_next_sha256": PINNED_NEXT_SHA256,
        "targets_from_packet_parametrization": [30, 32, 34, 36, 38, 40],
        "obstruction_progression_candidates": [34, 40],
        "complete_exclusion_at_34": False,
        "complete_exclusion_at_40": False,
        "published_conductor_14_example_reproduced": True,
        "parent_conductor_28_all_zero": True,
        "conductors": list(conductors),
        "censuses": {
            str(conductor): [list(sequence) for sequence in sequences]
            for conductor, sequences in censuses.items()
        },
        "compiler_controls": compiler_controls,
        "full_alexander_polynomial_controls": full_alexander_controls,
        "direct_counter_controls": direct_controls,
        "c34_unique_survivor_group_validated": {
            "sequence": [12, 8, 14, 15],
            "full_S4": c34_full,
            "fox_colorings": c34_fox,
            "nonconstant_S4_lifts": c34_lifts,
        },
        "all_family_criterion": {
            "quotient": "nonconstant Fox 3-coloring rho",
            "lift_space": "affine F2 solution space L_rho",
            "four_nonfull_lifts": "the four S3 complements in S4",
            "full_S4_iff": "some |L_rho| > 4",
            "labeled_count": "sum_rho (|L_rho|-4)",
        },
        "counts": counts,
        "survivors": survivors,
        "positive_counts": observed_positive_counts,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    print(json.dumps(payload, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
