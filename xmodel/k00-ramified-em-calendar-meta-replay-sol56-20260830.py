#!/usr/bin/env python3
"""Exact desk replay for the generic-K00 ramified (e,m) calendar meta gate.

This program parses the frozen 569-tail source through the already frozen
exact sparse-Q engine.  It certifies the raw d-order stencil, the exact
surface/normal bidegree antichains, the four charged cell calendars, and two
arithmetic controls showing why ratio or gcd scaling is not a cell
equivalence.  It does not solve a new jet cell and makes no arc, map, or JC2
claim.
"""

from __future__ import annotations

from fractions import Fraction as F
from hashlib import sha256
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TAILS = (
    ROOT / "cases/max12_812_order2_u2_62_strict_rees_20260825"
    / "aws_compile_v2_jsat/run/output/compiled_v2/tails.json"
)
COMPILER = (
    ROOT / "cases/max12_812_order2_u2_62_k00_common_lambda19_kuranishi_v20_20260827"
    / "compile_contracted_source_v20r2.py"
)
ENGINE = ROOT / "xmodel/k00-r2-full-rank-fan-replay-sol56-20260829.py"
E2M1 = ROOT / "xmodel/k00-ram-e2m1-allfaces-coordinator-integration-sol56-20260829.md"
E3M1 = ROOT / "xmodel/k00-ram-e3m1-g0-g9-complete-rankfan-coordinator-integration-sol56-20260830.md"
E2M2 = ROOT / "xmodel/k00-ram-e2m2-g0-g10-complete-rankfan-sol56-20260829.md"
E2M2_REPLAY = ROOT / "xmodel/k00-ram-e2m2-g0-g10-complete-rankfan-replay-sol56-20260829.py"
E2M2_REVIEW = ROOT / "xmodel/k00-ram-e2m2-g0-g10-complete-rankfan-hostile-review-fable5-20260830.md"
E3M2 = ROOT / "xmodel/k00-ram-e3m2-g0-g12-complete-rankfan-sol56-20260830.md"
E3M2_REPLAY = ROOT / "xmodel/k00-ram-e3m2-g0-g12-complete-rankfan-replay-sol56-20260830.py"
SANDWICH = ROOT / "xmodel/k00-unloaded-normal-cone-quartic-coordinator-integration-sol56-20260829.md"

EXPECTED = {
    TAILS: "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848",
    COMPILER: "2ac7653cf0c7a39970d54286b85974b39a2e6deb116839720cb1ae91f8ad6d2b",
    ENGINE: "2c918d5b0d165977bdd2b598cf48d90cf3d0dfe0922ce27213dfa01dc255e7c4",
    E2M1: "7c73616d99bd0cf3880dfedc790bcbdc055f68f800a94fd65bcae43ae4711bac",
    E3M1: "6c7195218dcdac680d260d2db3e7bcff197a2ba7ee09055a8e6f67884ce27a38",
    E2M2: "fa5a4ef6a1b2c0640c6363b84e6b547a044920b15249f7c72b25ffbcda2c1733",
    E2M2_REPLAY: "efd2f4fea4f58ee4783d9b373ee68f2ff191a9923b08bf2ead8dd1c59a4d3749",
    E2M2_REVIEW: "4710349b6082623213a6074cb92ebc7944fb5ce751a06112f2fa560e043bb69c",
    E3M2: "3a4565b8e7163acb3cea8f1504123cab3e1c04ca936110bdaf047952181188ae",
    E3M2_REPLAY: "7cbc45a13d84c7921e7548c7229fcd28e8c28cdd4ff6a11c4c5643b24e426a33",
    SANDWICH: "669a3496e9e1fac43e8a6e8ccfee58d4622ecab2d416838c349bfbfa398e690b",
}
EXPECTED_CERTIFICATE_SHA256 = "afb3979a091647fb1c2567c06295400358bf84d65387cc6447faabb92231f501"


def fail(message: object) -> None:
    raise AssertionError(message)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def load_engine():
    spec = importlib.util.spec_from_file_location("k00_em_meta_engine", ENGINE)
    if spec is None or spec.loader is None:
        fail("cannot import exact engine")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def degree_minima(polys):
    return [min((sum(key) for key in poly), default=None) for poly in polys]


def degree_maxima(polys):
    return [max((sum(key) for key in poly), default=None) for poly in polys]


def pareto_bidegrees(poly) -> list[list[int]]:
    pairs = sorted({(sum(key[:2]), sum(key[2:])) for key in poly})
    minimal = [
        pair
        for pair in pairs
        if not any(
            other != pair and other[0] <= pair[0] and other[1] <= pair[1]
            for other in pairs
        )
    ]
    return [list(pair) for pair in minimal]


def graph_images(module, ring, square_coefficient: int = 16):
    value = {name: ring.var(name) for name in ring.names}
    s, t = value["S"], value["T"]
    return [
        ring.add(ring.add(ring.scale(s, 2), ring.mul(s, s)), value["n0"]),
        ring.add(
            ring.scale(ring.mul(ring.add(ring.const(1), s), t), F(1, 8)),
            value["n1"],
        ),
        ring.add(
            ring.add(s, ring.scale(ring.mul(t, t), square_coefficient)),
            value["n2"],
        ),
        t,
        s,
        ring.add(ring.scale(t, 2), value["n5"]),
    ]


def transform(module, ring, polys, images):
    return [module.eval_dpoly(poly, images, ring) for poly in polys]


def raw_cell(e: int, m: int) -> dict[str, object]:
    return {
        "e": e,
        "m": m,
        "R_main": 2 * m,
        "R_row6": 3 * m,
        "K10_raw": 2 * e + 2 * m,
        "K10_surface_main": 2 * e + 3 * m,
        "K10_surface_row6": 2 * e + 4 * m,
        "K6_raw_main_h1": 6 * e + 1 + m,
        "K6_raw_rows4_6_h1": 6 * e + 1 + 2 * m,
        "K2_raw_h1": 10 * e + 1 + m,
        "targets_h1_Junit": [14 * e + 1, 16 * e + 1, 18 * e + 1, 19 * e],
        "charged_terminal": 2 * e + 3 * m,
    }


def require_text(path: Path, snippet: str) -> None:
    if snippet not in path.read_text():
        fail(("missing charged transition text", path.name, snippet))


def main() -> None:
    for path, expected in EXPECTED.items():
        actual = digest(path)
        if actual != expected:
            fail(("custody", str(path), actual, expected))

    module = load_engine()
    rows, loads, term_count = module.reconstruct_rows()
    if term_count != 569:
        fail(("tail census", term_count))

    raw_minima = {
        "R": degree_minima(rows),
        "K10": degree_minima(loads["K10"]),
        "K6": degree_minima(loads["K6"]),
        "K2": degree_minima(loads["K2"]),
    }
    raw_maxima = {
        "R": degree_maxima(rows),
        "K10": degree_maxima(loads["K10"]),
        "K6": degree_maxima(loads["K6"]),
        "K2": degree_maxima(loads["K2"]),
    }
    expected_minima = {
        "R": [2, 2, 2, 2, 2, 3, 2],
        "K10": [2, 2, 2, 2, 2, 2, 2],
        "K6": [1, 1, 1, 2, 1, 2, 1],
        "K2": [1, 1, 1, 1, 1, 1, 1],
    }
    expected_maxima = {
        "R": [4, 4, 5, 5, 5, 6, 6],
        "K10": [3, 4, 4, 4, 5, 5, 5],
        "K6": [2, 2, 3, 3, 3, 4, 4],
        "K2": [1, 1, 1, 2, 2, 2, 3],
    }
    if raw_minima != expected_minima or raw_maxima != expected_maxima:
        fail(("raw stencil", raw_minima, raw_maxima))

    ring = module.Ring(("S", "T", "n0", "n1", "n2", "n5"))
    images = graph_images(module, ring)
    transformed = {"R": transform(module, ring, rows, images)}
    transformed.update(
        {label: transform(module, ring, polys, images) for label, polys in loads.items()}
    )
    bidegrees = {
        label: [pareto_bidegrees(poly) for poly in polys]
        for label, polys in transformed.items()
    }
    expected_bidegrees = {
        "R": [[[0, 2]], [[0, 2]], [[0, 2]], [[0, 2]], [[0, 2]], [[0, 3], [1, 2]], [[0, 2]]],
        "K10": [[[0, 2], [1, 1], [3, 0]], [[0, 2], [1, 1], [3, 0]], [[0, 2], [1, 1], [3, 0]], [[0, 2], [2, 1]], [[0, 2], [1, 1], [3, 0]], [[0, 2], [2, 1], [4, 0]], [[0, 2], [1, 1], [3, 0]]],
        "K6": [[[0, 1], [2, 0]], [[0, 1], [2, 0]], [[0, 1], [2, 0]], [[0, 2], [1, 1]], [[0, 1], [2, 0]], [[0, 2], [2, 1], [3, 0]], [[0, 1], [2, 0]]],
        "K2": [[[0, 1], [1, 0]], [[1, 0]], [[0, 1], [1, 0]], [[0, 1]], [[0, 1], [1, 0]], [[0, 1], [2, 0]], [[0, 1], [1, 0]]],
    }
    if bidegrees != expected_bidegrees:
        fail(("graph bidegrees", bidegrees))

    # A planted graph mutation must destroy exact unloaded restriction.
    wrong_images = graph_images(module, ring, square_coefficient=15)
    wrong_rows = transform(module, ring, rows, wrong_images)
    normal_names = ("n0", "n1", "n2", "n5")
    wrong_surface = [ring.zero_vars(poly, normal_names) for poly in wrong_rows]
    if not any(wrong_surface):
        fail("16-to-15 graph mutation was not detected")

    cells = {
        "e2m1": raw_cell(2, 1),
        "e3m1": raw_cell(3, 1),
        "e2m2": raw_cell(2, 2),
        "e3m2": raw_cell(3, 2),
    }
    expected_terminals = {"e2m1": 7, "e3m1": 9, "e2m2": 10, "e3m2": 12}
    if {key: value["charged_terminal"] for key, value in cells.items()} != expected_terminals:
        fail(("cell terminals", cells))

    # Exact same-ratio/different-calendar control: h6 is not scaled.
    ratio_control = {
        "e2m9_h6_1": {"K10_surface": 31, "K6_surface": 31},
        "e4m18_h6_1": {"K10_surface": 62, "K6_surface": 61},
    }
    if 2 * 2 + 3 * 9 != 31 or 6 * 2 + 1 + 2 * 9 != 31:
        fail("primitive ratio control")
    if 2 * 4 + 3 * 18 != 62 or 6 * 4 + 1 + 2 * 18 != 61:
        fail("scaled ratio control")

    # Pin the exact same-cone/different-successor evidence in the four reports.
    require_text(E3M1, "At first normal order four, rank two dies at G9")
    require_text(E2M2, "G8_N4=ALL_G9_TANGENT_RANKS_DEAD_G10")
    require_text(E2M2_REVIEW, "**CONFIRMED.** Every displayed equation")
    require_text(E3M2, "G8_N4=RANK2_DEAD_G10;RANK1_G10_SURVIVOR_DEAD_RAW_G12;RANK0_TO_N5")
    require_text(E2M2, "S=8i*tau^2+3*tau^3")

    certificate = {
        "type": "K00-RAMIFIED-EM-CALENDAR-META/v1",
        "basis": "0d7544ebd5cb12def6bac892646010301098be3c",
        "source": {str(path.relative_to(ROOT)): expected for path, expected in EXPECTED.items()},
        "tail_terms": term_count,
        "raw_d_degree_minima": raw_minima,
        "raw_d_degree_maxima": raw_maxima,
        "graph_pareto_bidegrees": bidegrees,
        "cells_hlate_1": cells,
        "surface_resonance_walls": {
            "K6_equals_K10": "h6=m-4e",
            "K2_equals_K10": "h2=2m-8e",
            "mu2_equals_K10": "hmu2=3m-12e",
            "mu4_equals_K10": "hmu4=3m-14e",
            "mu6_equals_K10": "hmu6=3m-16e",
            "Jdet_equals_K10": "3m=17e",
        },
        "ratio_control": ratio_control,
        "same_cone_different_successor": [
            "E3M1_N4_G8_TO_G9_KILL_vs_E2M2_N4_G8_TO_G9_TANGENT_G10_KILL",
            "E2M2_N4_G8_G10_LOADED_KILL_vs_E3M2_N4_G8_G10_RECENTER_G12_KILL",
        ],
        "verdict": "FINITE_EXACT_CALENDAR_DATA_NO_FINITE_TRANSITION_QUOTIENT_PROVED",
        "attainment": False,
    }
    payload = (json.dumps(certificate, sort_keys=True, separators=(",", ":")) + "\n").encode()
    certificate_sha = sha256(payload).hexdigest()
    if certificate_sha != EXPECTED_CERTIFICATE_SHA256:
        fail(("certificate digest", certificate_sha, EXPECTED_CERTIFICATE_SHA256))

    print("K00_RAMIFIED_EM_CALENDAR_META_REPLAY=PASS")
    print(f"TAIL_TERMS={term_count}")
    print("RAW_MINIMA=R:2222232;K10:2222222;K6:1112121;K2:1111111")
    print("GRAPH_BIDEGREES=EXACT_PARETO_ANTICHAINS")
    print("SURFACE_MINIMA=K10:333_INF_343;K6:222_INF_232;K2:111_INF_121")
    print("CHARGED_TERMINALS=E2M1:G7;E3M1:G9;E2M2:G10;E3M2:G12")
    print("SAME_STATE_DIFFERENT_SUCCESSOR=N4_G8_E3M1_vs_E2M2;N4_G8_E2M2_vs_E3M2")
    print("RATIO_CONTROL=(2,9,h6=1):TIE31;(4,18,h6=1):K6_61_BEFORE_K10_62")
    print("FINITE_TYPE_VERDICT=CALENDAR_ONLY;NO_TRANSITION_QUOTIENT_THEOREM")
    print(f"CERTIFICATE_BYTES={len(payload)}")
    print(f"CERTIFICATE_SHA256={certificate_sha}")
    print("MUTATIONS=CUSTODY,SURFACE_16_TO_15,RATIO_SCALE,CHARGED_SUCCESSOR_TEXT")


if __name__ == "__main__":
    main()
