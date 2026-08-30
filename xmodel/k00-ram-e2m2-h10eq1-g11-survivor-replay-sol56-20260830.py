#!/usr/bin/env python3
"""Exact stdlib replay for the e=2,m=2, ord(k10)=1 G11 boundary.

The replay reconstructs the literal V20R2 source, extracts G11 without
shifting a prior coefficient formula, verifies the complete fresh-n=5
reduced rank fan at G11, and checks two literal G0--G11 survivor fixtures.

All conclusions concern field-valued finite jets.  No formal arc, source
reachability, polynomial map, or Jacobian-conjecture conclusion is made.
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
ENGINE = ROOT / "xmodel/k00-r2-full-rank-fan-replay-sol56-20260829.py"
BASE_REPLAY = ROOT / "xmodel/k00-ram-e2m2-g0-g10-complete-rankfan-replay-sol56-20260829.py"
BASE_REPORT = ROOT / "xmodel/k00-ram-e2m2-g0-g10-complete-rankfan-sol56-20260829.md"
BASE_REVIEW = ROOT / "xmodel/k00-ram-e2m2-g0-g10-complete-rankfan-hostile-review-fable5-20260830.md"
META_REPORT = ROOT / "xmodel/k00-ramified-em-calendar-finite-type-gate-sol56-20260830.md"

EXPECTED = {
    TAILS: "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848",
    ENGINE: "2c918d5b0d165977bdd2b598cf48d90cf3d0dfe0922ce27213dfa01dc255e7c4",
    BASE_REPLAY: "efd2f4fea4f58ee4783d9b373ee68f2ff191a9923b08bf2ead8dd1c59a4d3749",
    BASE_REPORT: "fa5a4ef6a1b2c0640c6363b84e6b547a044920b15249f7c72b25ffbcda2c1733",
    BASE_REVIEW: "4710349b6082623213a6074cb92ebc7944fb5ce751a06112f2fa560e043bb69c",
    META_REPORT: "9a94cd3bc58c04331b430f66d6fbabaa41ccee1eebcb4f18315e514fc0850c65",
}
EXPECTED_CERTIFICATE_SHA256 = "d83eeb1db7e7d092eaa5cb23016e73ebcf72835024300d679316121a9518d817"


def fail(message: object) -> None:
    raise AssertionError(message)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        fail(("cannot import", path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def assert_zero(poly, label: str) -> None:
    if poly:
        fail((label, len(poly), next(iter(poly.items()))))


def assert_equal(module, ring, left, right, label: str) -> None:
    module.assert_equal(left, right, ring, label)


def qstring(value: F) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def poly_object(poly):
    answer = []
    for key in sorted(poly):
        real, imag = poly[key]
        answer.append([list(key), qstring(real), qstring(imag)])
    return answer


def bilinear_hessian(module, ring, poly, point, left, right):
    out = ring.const()
    for first_index in range(6):
        first = module.dderivative(poly, first_index)
        for second_index in range(6):
            coefficient = module.eval_dpoly(
                module.dderivative(first, second_index), point, ring
            )
            out = ring.add(
                out,
                ring.mul(
                    ring.mul(coefficient, left[first_index]),
                    right[second_index],
                ),
            )
    return out


def surface_load_rows(base, module, ring, m4, a10_cubic, s, t):
    ell = module.old_plane(ring, s, t)
    mu = base.mu_vector(ring, s, t)
    rows = []
    for row_index in range(7):
        rows.append(
            ring.add(
                base.directional(module, ring, m4[row_index], ell, mu),
                module.eval_dpoly(a10_cubic[row_index], ell, ring),
            )
        )
    return rows


def literal_general_g11(
    base, module, rows, loads, quadrics, cubics, m4, a10_cubic
):
    """Re-extract the n=4 G11 coefficient with every capable slot retained."""

    names = (
        "s", "t", "alpha", "beta", "p", "q", "kap", "k2",
        *(f"n5_{index}" for index in range(6)),
        *(f"n6_{index}" for index in range(6)),
        *(f"n7_{index}" for index in range(6)),
    )
    ring = module.Ring(names)
    value = {name: ring.var(name) for name in names}
    dseries = base.surface_series(
        module,
        ring,
        {2: value["s"], 3: value["alpha"]},
        {2: value["t"], 3: value["beta"]},
        12,
    )
    n4 = module.cone_vector(
        ring, ring.const(), ring.const(), value["p"], value["q"]
    )
    n5 = [value[f"n5_{index}"] for index in range(6)]
    n6 = [value[f"n6_{index}"] for index in range(6)]
    n7 = [value[f"n7_{index}"] for index in range(6)]
    base.add_normal(ring, dseries, 4, n4)
    base.add_normal(ring, dseries, 5, n5)
    base.add_normal(ring, dseries, 6, n6)
    base.add_normal(ring, dseries, 7, n7)
    source, _ = base.literal_e2_source(
        module,
        rows,
        loads["K10"],
        dseries,
        (ring.const(), value["kap"], value["k2"]),
        ring,
    )

    ell2 = module.old_plane(ring, value["s"], value["t"])
    ell3 = module.old_plane(ring, value["alpha"], value["beta"])
    wrows = surface_load_rows(
        base, module, ring, m4, a10_cubic, value["s"], value["t"]
    )
    term_counts = []
    for row_index in range(7):
        load_row = ring.add(
            base.directional(module, ring, m4[row_index], ell2, n4),
            wrows[row_index],
        )
        expected = ring.add(
            base.directional(module, ring, quadrics[row_index], n4, n7),
            ring.add(
                base.directional(module, ring, quadrics[row_index], n5, n6),
                ring.add(
                    bilinear_hessian(
                        module, ring, cubics[row_index], ell2, n4, n5
                    ),
                    ring.add(
                        base.second_half(
                            module, ring, cubics[row_index], ell3, n4
                        ),
                        ring.mul(value["kap"], load_row),
                    ),
                ),
            ),
        )
        assert_equal(
            module,
            ring,
            source[row_index][11],
            expected,
            f"literal general n4 G11 row {row_index + 1}",
        )
        if ring.depends_on(source[row_index][11], "k2"):
            fail(("spurious k10[2] at G11", row_index + 1))
        term_counts.append(len(source[row_index][11]))
    return {
        "retained": "S2,T2,S3,T3,N4,N5,N6,N7,k10[1],k10[2]",
        "k10_2_absent": True,
        "row_term_counts": term_counts,
        "formula": (
            "DQ(N4)[N7]+DQ(N5)[N6]+D2R3(ell2)[N4,N5]+"
            "1/2D2R3(ell3)[N4,N4]+k10[1](DM4(ell2)[N4]+W(S2,T2))"
        ),
    }


def fresh_n5_g11_fan(base, module, rows, loads, quadrics, m4, a10_cubic):
    """Complete reduced rank fan for the fresh n=5 cone at G10/G11."""

    names = (
        "s", "t", "alpha", "beta", "p", "q", "A", "B", "kap", "k2",
        "y1", "y2", "y3", "y4",
        *(f"n7_{index}" for index in range(6)),
    )
    ring = module.Ring(names)
    value = {name: ring.var(name) for name in names}
    dseries = base.surface_series(
        module,
        ring,
        {2: value["s"], 3: value["alpha"]},
        {2: value["t"], 3: value["beta"]},
        12,
    )
    w = module.cone_vector(
        ring, ring.const(), ring.const(), value["p"], value["q"]
    )
    tangent = module.vector_with_ab(
        ring,
        value["A"], value["B"],
        value["y1"], value["y2"], value["y3"], value["y4"],
    )
    n7 = [value[f"n7_{index}"] for index in range(6)]
    base.add_normal(ring, dseries, 5, w)
    base.add_normal(ring, dseries, 6, tangent)
    base.add_normal(ring, dseries, 7, n7)
    source, _ = base.literal_e2_source(
        module,
        rows,
        loads["K10"],
        dseries,
        (ring.const(), value["kap"], value["k2"]),
        ring,
    )
    wrows = surface_load_rows(
        base, module, ring, m4, a10_cubic, value["s"], value["t"]
    )
    for row_index in range(7):
        assert_equal(
            module,
            ring,
            source[row_index][10],
            module.eval_dpoly(quadrics[row_index], w, ring),
            f"fresh n5 G10 row {row_index + 1}",
        )
        expected = ring.add(
            base.directional(module, ring, quadrics[row_index], w, tangent),
            ring.mul(value["kap"], wrows[row_index]),
        )
        assert_equal(
            module,
            ring,
            source[row_index][11],
            expected,
            f"fresh n5 literal G11 row {row_index + 1}",
        )
        for absent in ("alpha", "beta", "k2", *(f"n7_{i}" for i in range(6))):
            if ring.depends_on(source[row_index][11], absent):
                fail(("spurious fresh-n5 G11 dependence", row_index + 1, absent))
        assert_zero(source[row_index][10], f"fresh n5 cone support row {row_index + 1}")

    expected_w1 = ring.scale(
        ring.mul(
            value["t"],
            ring.sub(
                ring.scale(ring.mul(value["s"], value["s"]), 3),
                ring.scale(ring.mul(value["t"], value["t"]), 64),
            ),
        ),
        F(5, 4096),
    )
    expected_w2 = ring.scale(
        ring.mul(
            value["s"],
            ring.sub(
                ring.mul(value["s"], value["s"]),
                ring.scale(ring.mul(value["t"], value["t"]), 192),
            ),
        ),
        F(5, 65536),
    )
    assert_equal(module, ring, wrows[0], expected_w1, "fresh n5 W1")
    assert_equal(module, ring, wrows[1], expected_w2, "fresh n5 W2")
    for index, factor in ((2, F(-1, 8)), (4, F(-1, 128)), (6, F(-1, 1024))):
        assert_equal(
            module, ring, wrows[index], ring.scale(expected_w1, factor),
            f"fresh n5 W row {index + 1}",
        )
    assert_zero(wrows[3], "fresh n5 W4")
    assert_zero(wrows[5], "fresh n5 W6")
    for index, factor in ((2, F(-1, 8)), (4, F(-1, 128)), (6, F(-1, 1024))):
        assert_equal(
            module,
            ring,
            source[index][11],
            ring.scale(source[0][11], factor),
            f"fresh n5 full G11 row {index + 1} pattern",
        )
    assert_zero(source[3][11], "fresh n5 full G11 row4")
    assert_zero(source[5][11], "fresh n5 full G11 row6")

    delta = ring.add(
        ring.mul(value["p"], value["p"]),
        ring.scale(ring.mul(value["q"], value["q"]), 64),
    )
    u_rhs = ring.scale(ring.mul(value["kap"], expected_w1), F(-1024, 3))
    v_rhs = ring.scale(ring.mul(value["kap"], expected_w2), F(-16384, 3))
    anum = ring.add(
        ring.mul(value["p"], u_rhs), ring.mul(value["q"], v_rhs)
    )
    bnum = ring.add(
        ring.scale(ring.mul(value["q"], u_rhs), -64),
        ring.mul(value["p"], v_rhs),
    )
    assert_equal(
        module,
        ring,
        ring.sub(ring.mul(value["p"], anum), ring.mul(value["q"], bnum)),
        ring.mul(delta, u_rhs),
        "fresh n5 rank2 matrix inverse A equation",
    )
    assert_equal(
        module,
        ring,
        ring.add(
            ring.scale(ring.mul(value["q"], anum), 64),
            ring.mul(value["p"], bnum),
        ),
        ring.mul(delta, v_rhs),
        "fresh n5 rank2 matrix inverse B equation",
    )

    rank1 = {}
    for sign in (1, -1):
        replacements = {"p": (module.g(0, 8 * sign), "q")}
        specialized_w1 = ring.replace_by_scaled_var(expected_w1, replacements)
        specialized_w2 = ring.replace_by_scaled_var(expected_w2, replacements)
        compatibility = ring.add(
            specialized_w2,
            specialized_w1,
            module.g(0, F(sign, 2)),
        )
        wall = ring.scale(
            ring.power(
                ring.add(
                    value["s"],
                    ring.scale(value["t"], module.g(0, 8 * sign)),
                ),
                3,
            ),
            F(5, 65536),
        )
        assert_equal(
            module, ring, compatibility, wall,
            f"fresh n5 rank1 sign {sign} cubic wall",
        )
        wrong_wall = ring.scale(
            ring.power(
                ring.sub(
                    value["s"],
                    ring.scale(value["t"], module.g(0, 8 * sign)),
                ),
                3,
            ),
            F(5, 65536),
        )
        if compatibility == wrong_wall:
            fail(("rank-one wall-sign mutation invisible", sign))
        rank1[str(sign)] = poly_object(wall)

    return {
        "G10": "Q(w)",
        "G11": "DQ(w)[v]+k10[1]*W(s,t)",
        "W1": poly_object(expected_w1),
        "W2": poly_object(expected_w2),
        "delta": poly_object(delta),
        "rank2": "SURVIVES; unique (A,B) after inverting Delta",
        "rank1_walls": rank1,
        "rank1": "SURVIVES exactly on s=-epsilon*8*i*t on reduced support",
        "rank0": "DEAD on k10[1]!=0 and (s,t)!=(0,0)",
    }


def fixture_source(base, module, rows, loads, kind: str, mutation: bool = False):
    ring = module.Ring(())
    if kind == "n5_rank2":
        dseries = base.surface_series(
            module, ring, {2: ring.const(1)}, {2: ring.const()}, 12
        )
        n5 = module.cone_vector(
            ring, ring.const(), ring.const(), ring.const(1), ring.const()
        )
        bvalue = F(-5, 13) if mutation else F(-5, 12)
        n6 = module.vector_with_ab(
            ring,
            ring.const(), ring.const(bvalue),
            ring.const(), ring.const(), ring.const(), ring.const(),
        )
        base.add_normal(ring, dseries, 5, n5)
        base.add_normal(ring, dseries, 6, n6)
    elif kind in ("n4_rank1_plus", "n4_rank1_minus"):
        sign = 1 if kind.endswith("plus") else -1
        dseries = base.surface_series(
            module,
            ring,
            {2: ring.const(module.g(0, 8 * sign))},
            {2: ring.const(1)},
            12,
        )
        n4 = module.cone_vector(
            ring,
            ring.const(), ring.const(),
            ring.const(module.g(0, 8 * sign)), ring.const(1),
        )
        y1 = F(0) if mutation else F(5, 72)
        n5 = module.vector_with_ab(
            ring,
            ring.const(), ring.const(),
            ring.const(y1), ring.const(), ring.const(), ring.const(),
        )
        n6 = module.vector_with_ab(
            ring,
            ring.const(), ring.const(-128),
            ring.const(), ring.const(), ring.const(), ring.const(),
        )
        n7 = module.vector_with_ab(
            ring,
            ring.const(), ring.const(F(320, 9)),
            ring.const(), ring.const(), ring.const(), ring.const(),
        )
        base.add_normal(ring, dseries, 4, n4)
        base.add_normal(ring, dseries, 5, n5)
        base.add_normal(ring, dseries, 6, n6)
        base.add_normal(ring, dseries, 7, n7)
    else:
        fail(("unknown fixture", kind))
    return base.literal_e2_source(
        module,
        rows,
        loads["K10"],
        dseries,
        (ring.const(), ring.const(1)),
        ring,
    )[0]


def survivor_fixtures(base, module, rows, loads):
    results = {}
    for kind in ("n5_rank2", "n4_rank1_plus", "n4_rank1_minus"):
        source = fixture_source(base, module, rows, loads, kind)
        for row_index in range(7):
            for grade in range(12):
                assert_zero(
                    source[row_index][grade],
                    f"{kind} row {row_index + 1} G{grade}",
                )
        wrong = fixture_source(base, module, rows, loads, kind, mutation=True)
        if all(not wrong[row_index][11] for row_index in range(7)):
            fail(("fixture mutation invisible", kind))
        results[kind] = "G0_G11_PASS"
    return results


def main() -> None:
    for path, expected in EXPECTED.items():
        actual = digest(path)
        if actual != expected:
            fail(("custody", path, actual, expected))
    base = load_module(BASE_REPLAY, "k00_e2m2_g10_base")
    module = base.load_engine()
    rows, loads, term_count = module.reconstruct_rows()
    if term_count != 569:
        fail(("tail census", term_count))
    quadrics = [module.dhom(row, 2) for row in rows]
    cubics = [module.dhom(row, 3) for row in rows]
    m4 = [module.dhom(row, 2) for row in loads["K10"]]
    a10_cubic = [module.dhom(row, 3) for row in loads["K10"]]

    general = literal_general_g11(
        base, module, rows, loads, quadrics, cubics, m4, a10_cubic
    )
    n5_fan = fresh_n5_g11_fan(
        base, module, rows, loads, quadrics, m4, a10_cubic
    )
    fixtures = survivor_fixtures(base, module, rows, loads)

    certificate = {
        "type": "K00-RAM-E2M2-H10EQ1-G11-SURVIVOR/v1",
        "basis": "0d7544ebd5cb12def6bac892646010301098be3c",
        "source": {path.name: expected for path, expected in EXPECTED.items()},
        "tail_terms": term_count,
        "field": "algebraic closure of characteristic zero; Gaussian charts",
        "normalization": "Lambda=tau^2; C6=1; ord(d)=2; ord(k10)=1",
        "opens": ["k10[1]!=0", "Jdet[0]!=0", "d[2]!=0"],
        "general_g11": general,
        "fresh_n5_fan": n5_fan,
        "fixtures": fixtures,
        "conclusion": "G11_POINT_SET_NONEMPTY;FIRST_UNRESOLVED_GATE_G12",
        "nonclaims": [
            "formal arc", "lifting", "source reachability", "polynomial map", "JC2"
        ],
        "mutations": [
            "custody", "rank1_wall_sign", "n5_B_-5/12_to_-5/13",
            "n4_y1_5/72_to_0",
        ],
    }
    cert_bytes = (
        json.dumps(certificate, sort_keys=True, separators=(",", ":")) + "\n"
    ).encode()
    cert_sha = sha256(cert_bytes).hexdigest()
    if EXPECTED_CERTIFICATE_SHA256 != "PENDING" and cert_sha != EXPECTED_CERTIFICATE_SHA256:
        fail(("certificate digest", cert_sha, EXPECTED_CERTIFICATE_SHA256))

    print("K00_RAM_E2M2_H10EQ1_G11_SURVIVOR_REPLAY=PASS")
    print(f"TAIL_TERMS={term_count}")
    print("GENERAL_G11=LITERAL_N4_FORMULA;ALL_CAPABLE_SLOTS_RETAINED;K10_2_ABSENT")
    print("N4_RANK1=G11_SURVIVOR_BOTH_SIGNS")
    print("N5_G11=RANK2_SURVIVES;RANK1_SURVIVES_ON_OPPOSITE_WALL;RANK0_DEAD")
    print("FIXTURE_N5=S2=1;T2=0;P5=1;Q5=0;A6=0;B6=-5/12")
    print("FIXTURE_N4=S2=EPS*8i;T2=1;Y1_5=5/72;B6=-128;B7=320/9")
    print("CELL_STATUS=POINT_SET_NONEMPTY_THROUGH_G11;FORMAL_ARC_OPEN")
    print(f"CERTIFICATE_BYTES={len(cert_bytes)}")
    print(f"CERTIFICATE_SHA256={cert_sha}")
    print("MUTATIONS=CUSTODY,WALL_SIGN,N5_B,N4_Y1")


if __name__ == "__main__":
    main()
