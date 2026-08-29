#!/usr/bin/env python3
"""Exact stdlib replay for the ramified e=2,m=1 K00 cell through G7.

This reconstructs the frozen 569-tail source, corrects the omitted cubic in
the earlier K10/G7 sharpness check, and proves point-set emptiness by two
successive complete rank fans.  It uses exact rational/Gaussian arithmetic,
writes no files, and invokes no CAS or network service.
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
VALUATIVE = ROOT / "xmodel/k00-v20r2-valuative-comparison-v1-sol56-20260829.md"
G3_PROMOTION = ROOT / "xmodel/k00-rank5-rankle1-coordinator-integration-sol56-20260829.md"
PREFIX_REPORT = ROOT / "xmodel/k00-ram-e2m1-g5-prefix-certificate-sol56-20260829.md"
PREFIX_REPLAY = ROOT / "xmodel/k00-ram-e2m1-g5-prefix-replay-sol56-20260829.py"

EXPECTED = {
    TAILS: "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848",
    COMPILER: "2ac7653cf0c7a39970d54286b85974b39a2e6deb116839720cb1ae91f8ad6d2b",
    ENGINE: "2c918d5b0d165977bdd2b598cf48d90cf3d0dfe0922ce27213dfa01dc255e7c4",
    VALUATIVE: "98fb38535405f1cc853dd4d430e26876a84f6f97c538f862f18a0446c0c97ecf",
    G3_PROMOTION: "d453b9563d8f6cc23319d6bc0d8edce8a83f657b9e3a60cb244b00f181459860",
    PREFIX_REPORT: "a6fd11f1c6d5b32cc2e497722245cbe7381356ffdbba02c6db050ad5fe67ced0",
    PREFIX_REPLAY: "b4fd505d0345b21a2978f06ff63cb0c9fcacd9d7226d7accaa0b2ab489b210ea",
}

EXPECTED_CERTIFICATE_SHA256 = "9a8e19ab5fc95b4039206029a33923dc7f080ed332e4788e465467296e72850c"


def fail(message: object) -> None:
    raise AssertionError(message)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def load_engine():
    spec = importlib.util.spec_from_file_location("k00_exact_engine_g7", ENGINE)
    if spec is None or spec.loader is None:
        fail("cannot import exact engine")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def assert_zero(poly, label: str) -> None:
    if poly:
        fail((label, len(poly), next(iter(poly.items()))))


def assert_equal(module, ring, left, right, label: str) -> None:
    module.assert_equal(left, right, ring, label)


def directional(module, ring, poly, point, direction):
    out = ring.const()
    for index in range(6):
        out = ring.add(
            out,
            ring.mul(
                module.eval_dpoly(module.dderivative(poly, index), point, ring),
                direction[index],
            ),
        )
    return out


def second_half(module, ring, poly, point, direction):
    out = ring.const()
    for i in range(6):
        first = module.dderivative(poly, i)
        for j in range(6):
            out = ring.add(
                out,
                ring.mul(
                    ring.mul(
                        module.eval_dpoly(
                            module.dderivative(first, j), point, ring
                        ),
                        direction[i],
                    ),
                    direction[j],
                ),
            )
    return ring.scale(out, F(1, 2))


def map_poly(module, source_ring, target_ring, poly, images):
    """Evaluate a sparse GPoly under arbitrary polynomial images."""
    out = target_ring.const()
    for key, coefficient in poly.items():
        term = target_ring.const(coefficient)
        for name, exponent in zip(source_ring.names, key):
            if exponent:
                term = target_ring.mul(
                    term, target_ring.power(images[name], exponent)
                )
        out = target_ring.add(out, term)
    return out


def determinant3(ring, matrix):
    terms = (
        ((0, 1, 2), 1), ((1, 2, 0), 1), ((2, 0, 1), 1),
        ((2, 1, 0), -1), ((1, 0, 2), -1), ((0, 2, 1), -1),
    )
    out = ring.const()
    for permutation, sign in terms:
        term = ring.const(sign)
        for row, column in enumerate(permutation):
            term = ring.mul(term, matrix[row][column])
        out = ring.add(out, term)
    return out


def qstring(value: F) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def poly_object(poly):
    answer = []
    for key in sorted(poly):
        real, imag = poly[key]
        answer.append([list(key), qstring(real), qstring(imag)])
    return answer


def dpoly_object(poly):
    return [[list(key), qstring(poly[key])] for key in sorted(poly)]


def evaluate_rational(poly, ring, values: dict[str, F]):
    real = F(0)
    imag = F(0)
    for key, coefficient in poly.items():
        factor = F(1)
        for name, exponent in zip(ring.names, key):
            factor *= values.get(name, F(0)) ** exponent
        real += coefficient[0] * factor
        imag += coefficient[1] * factor
    return real, imag


def mu_vector(ring, s, t):
    return [
        ring.mul(s, s),
        ring.scale(ring.mul(s, t), F(1, 8)),
        ring.scale(ring.mul(t, t), 16),
        ring.const(), ring.const(), ring.const(),
    ]


def surface_vector(ring, s, t):
    """The exact unloaded singular surface D(S,T)."""
    return [
        ring.add(ring.scale(s, 2), ring.mul(s, s)),
        ring.scale(ring.mul(ring.add(ring.const(1), s), t), F(1, 8)),
        ring.add(s, ring.scale(ring.mul(t, t), 16)),
        t, s, ring.scale(t, 2),
    ]


def source_series(module, ring, rows, loads, coefficients, k0=None, k1=None):
    dseries = []
    for entries in coefficients:
        series = module.series_zero(8)
        for grade, value in entries.items():
            series[grade] = value
        dseries.append(series)
    equations = [module.eval_dpoly_series(row, dseries, ring) for row in rows]
    if k0 is not None:
        load_series = [
            module.eval_dpoly_series(row, dseries, ring) for row in loads["K10"]
        ]
        for row in range(7):
            for grade in range(4, 8):
                source_grade = grade - 4
                if load_series[row][source_grade]:
                    equations[row][grade] = ring.add(
                        equations[row][grade],
                        ring.mul(k0, load_series[row][source_grade]),
                    )
                if k1 is not None and source_grade >= 1 and load_series[row][source_grade - 1]:
                    equations[row][grade] = ring.add(
                        equations[row][grade],
                        ring.mul(k1, load_series[row][source_grade - 1]),
                    )
    return equations


def main() -> None:
    for path, expected in EXPECTED.items():
        if digest(path) != expected:
            fail(("custody", path))
    if sha256(TAILS.read_bytes() + b"\n").hexdigest() == EXPECTED[TAILS]:
        fail("custody mutation did not fire")

    module = load_engine()
    rows, loads, term_count = module.reconstruct_rows()
    if term_count != 569:
        fail(("tail census", term_count))
    quadrics = [module.dhom(row, 2) for row in rows]
    cubics = [module.dhom(row, 3) for row in rows]
    m4 = [module.dhom(row, 2) for row in loads["K10"]]
    a10_cubic = [module.dhom(row, 3) for row in loads["K10"]]

    # The unloaded source vanishes identically on this exact two-plane.
    surface_ring = module.Ring(("S", "T"))
    S, T = (surface_ring.var(name) for name in surface_ring.names)
    surface = surface_vector(surface_ring, S, T)
    for row_index, row in enumerate(rows):
        assert_zero(
            module.eval_dpoly(row, surface, surface_ring),
            f"unloaded surface row {row_index + 1}",
        )
    wrong_surface = list(surface)
    wrong_surface[2] = surface_ring.add(S, surface_ring.scale(surface_ring.mul(T, T), 15))
    if not any(module.eval_dpoly(row, wrong_surface, surface_ring) for row in rows):
        fail("surface coefficient mutation is invisible")

    # Erratum: literal K10/G7 includes the cubic A10^[3](ell).
    err_ring = module.Ring(("s", "t", "a", "b"))
    ev = {name: err_ring.var(name) for name in err_ring.names}
    ex = module.old_plane(err_ring, ev["s"], ev["t"])
    emu = mu_vector(err_ring, ev["s"], ev["t"])
    eplane = module.old_plane(err_ring, ev["a"], ev["b"])
    eu = [err_ring.add(emu[i], eplane[i]) for i in range(6)]
    corrected_load = []
    omitted_cubic = []
    for row_index in range(7):
        assert_zero(
            module.eval_dpoly(m4[row_index], ex, err_ring),
            f"K10 G6 row {row_index + 1}",
        )
        old_term = directional(module, err_ring, m4[row_index], ex, eu)
        cubic_term = module.eval_dpoly(a10_cubic[row_index], ex, err_ring)
        literal = err_ring.add(old_term, cubic_term)
        half_shift = [err_ring.sub(eu[i], err_ring.scale(emu[i], F(1, 2))) for i in range(6)]
        assert_equal(
            module, err_ring, literal,
            directional(module, err_ring, m4[row_index], ex, half_shift),
            f"corrected K10 G7 row {row_index + 1}",
        )
        corrected_load.append(literal)
        omitted_cubic.append(old_term)
    err_witness = {"s": F(1), "t": F(0), "a": F(0), "b": F(0)}
    if evaluate_rational(omitted_cubic[1], err_ring, err_witness) != (F(5, 32768), F(0)):
        fail("old omitted-cubic witness drift")
    if evaluate_rational(corrected_load[1], err_ring, err_witness) != (F(5, 65536), F(0)):
        fail("literal K10 G7 witness drift")
    if omitted_cubic == corrected_load:
        fail("omitted A10 cubic mutation is invisible")

    # First fan: G5 over the reduced G4 cone w=cone(a,b,p,q).
    g5_ring = module.Ring(("s", "t", "a", "b", "p", "q", "X", "Y"))
    gv = {name: g5_ring.var(name) for name in g5_ring.names}
    gx = module.old_plane(g5_ring, gv["s"], gv["t"])
    gw = module.cone_vector(g5_ring, gv["a"], gv["b"], gv["p"], gv["q"])
    alpha = [
        module.eval_dpoly(module.dderivative(row, 5), gw, g5_ring)
        for row in quadrics
    ]
    beta = [
        module.eval_dpoly(module.dderivative(row, 0), gw, g5_ring)
        for row in quadrics
    ]
    n5 = [second_half(module, g5_ring, cubics[i], gx, gw) for i in range(7)]
    g5 = [
        g5_ring.add(
            g5_ring.add(n5[i], g5_ring.mul(alpha[i], gv["X"])),
            g5_ring.mul(beta[i], gv["Y"]),
        )
        for i in range(7)
    ]
    g5_mu = mu_vector(g5_ring, gv["s"], gv["t"])
    g5_u = [g5_ring.add(g5_mu[i], gw[i]) for i in range(6)]
    g5_v = module.vector_with_ab(
        g5_ring, gv["X"], gv["Y"],
        g5_ring.const(), g5_ring.const(), g5_ring.const(), g5_ring.const(),
    )
    g5_source = source_series(
        module, g5_ring, rows, loads,
        [{1: gx[i], 2: g5_u[i], 3: g5_v[i]} for i in range(6)],
    )
    for row_index in range(7):
        for grade in range(5):
            assert_zero(
                g5_source[row_index][grade],
                f"direct reduced-cone row {row_index + 1} G{grade}",
            )
        assert_equal(
            module, g5_ring, g5_source[row_index][5], g5[row_index],
            f"direct literal G5 row {row_index + 1}",
        )
    avec = (0, 16, 0, -4, 0, 1)
    bvec = (1, 0, -4, 0, 2, 0)
    for row_index, quadric in enumerate(quadrics):
        for column in range(6):
            actual = module.eval_dpoly(
                module.dderivative(quadric, column), gw, g5_ring
            )
            expected = g5_ring.linear(
                (avec[column], alpha[row_index]),
                (bvec[column], beta[row_index]),
            )
            assert_equal(
                module, g5_ring, actual, expected,
                f"G5 coefficient factor row {row_index + 1} col {column}",
            )
    delta = g5_ring.add(
        g5_ring.mul(gv["p"], gv["p"]),
        g5_ring.scale(g5_ring.mul(gv["q"], gv["q"]), 64),
    )
    cform = g5_ring.add(
        g5_ring.mul(
            gv["t"],
            g5_ring.sub(
                g5_ring.scale(g5_ring.mul(gv["q"], gv["q"]), 64),
                g5_ring.mul(gv["p"], gv["p"]),
            ),
        ),
        g5_ring.scale(g5_ring.mul(g5_ring.mul(gv["s"], gv["p"]), gv["q"]), 2),
    )
    eform = g5_ring.sub(
        g5_ring.mul(
            gv["s"],
            g5_ring.sub(
                g5_ring.scale(g5_ring.mul(gv["q"], gv["q"]), 64),
                g5_ring.mul(gv["p"], gv["p"]),
            ),
        ),
        g5_ring.scale(g5_ring.mul(g5_ring.mul(gv["t"], gv["p"]), gv["q"]), 128),
    )
    augmented = determinant3(
        g5_ring, [[alpha[i], beta[i], n5[i]] for i in range(3)]
    )
    assert_equal(
        module, g5_ring, augmented,
        g5_ring.scale(g5_ring.mul(delta, cform), F(27, 2**35)),
        "G5 augmented determinant",
    )
    assert_equal(module, g5_ring, n5[3], g5_ring.scale(eform, F(3, 2**15)), "G5 row4")
    assert_zero(g5_ring.add(g5_ring.add(g5[4], g5[0], F(3, 128)), g5[2], F(1, 8)), "G5 S5")
    assert_zero(g5[5], "G5 row6 retained zero")
    assert_zero(g5_ring.add(g5_ring.add(g5[6], g5[0], F(1, 512)), g5[2], F(1, 128)), "G5 S7")
    rank2_det = g5_ring.sub(
        g5_ring.mul(
            g5_ring.scale(g5_ring.mul(gv["p"], gv["q"]), 2),
            g5_ring.scale(g5_ring.mul(gv["p"], gv["q"]), -128),
        ),
        g5_ring.power(
            g5_ring.sub(
                g5_ring.scale(g5_ring.mul(gv["q"], gv["q"]), 64),
                g5_ring.mul(gv["p"], gv["p"]),
            ),
            2,
        ),
    )
    assert_equal(module, g5_ring, rank2_det, g5_ring.scale(g5_ring.mul(delta, delta), -1), "G5 rank2 determinant")
    wrong_delta = g5_ring.add(
        g5_ring.mul(gv["p"], gv["p"]),
        g5_ring.scale(g5_ring.mul(gv["q"], gv["q"]), 63),
    )
    if rank2_det == g5_ring.scale(g5_ring.mul(wrong_delta, wrong_delta), -1):
        fail("rank-fan coefficient mutation is invisible")

    # Rank-one G5 branches are exactly parameterized and survive G5.
    for sign in (1, -1):
        br = module.Ring(("t", "a", "b", "q", "X"))
        bv = {name: br.var(name) for name in br.names}
        images = {
            "s": br.scale(bv["t"], module.g(0, 8 * sign)),
            "t": bv["t"], "a": bv["a"], "b": bv["b"],
            "p": br.scale(bv["q"], module.g(0, 8 * sign)),
            "q": bv["q"], "X": bv["X"],
            "Y": br.add(
                br.scale(bv["X"], module.g(0, 8 * sign)),
                br.scale(br.mul(bv["t"], bv["q"]), -128),
            ),
        }
        for row_index, poly in enumerate(g5):
            assert_zero(
                map_poly(module, g5_ring, br, poly, images),
                f"G5 rank1 sign {sign} row {row_index + 1}",
            )
        wrong_images = dict(images)
        wrong_images["Y"] = br.add(
            br.scale(bv["X"], module.g(0, -8 * sign)),
            br.scale(br.mul(bv["t"], bv["q"]), -128),
        )
        if all(
            not map_poly(module, g5_ring, br, poly, wrong_images)
            for poly in g5
        ):
            fail(("rank-one sign mutation is invisible", sign))

    rank0_images = {name: gv[name] for name in g5_ring.names}
    rank0_images["p"] = g5_ring.const()
    rank0_images["q"] = g5_ring.const()
    for row_index, poly in enumerate(g5):
        assert_zero(
            map_poly(module, g5_ring, g5_ring, poly, rank0_images),
            f"G5 rank0 row {row_index + 1}",
        )

    # The two G5 rank-one branches die at G6; labelled zero rows are retained.
    rank1_g6_rows = {}
    for sign in (1, -1):
        names = (
            "t", "q", "a", "b", "rho", "y1", "y2", "y3", "y4",
            *(f"z{i}" for i in range(6)),
        )
        ring = module.Ring(names)
        v = {name: ring.var(name) for name in names}
        s = ring.scale(v["t"], module.g(0, 8 * sign))
        p = ring.scale(v["q"], module.g(0, 8 * sign))
        x = module.old_plane(ring, s, v["t"])
        mu = mu_vector(ring, s, v["t"])
        plane2 = module.old_plane(ring, v["a"], v["b"])
        transverse = module.cone_vector(ring, ring.const(), ring.const(), p, v["q"])
        u = [ring.add(ring.add(mu[i], plane2[i]), transverse[i]) for i in range(6)]
        nu3 = [
            ring.scale(ring.mul(s, v["a"]), 2),
            ring.scale(
                ring.add(ring.mul(s, v["b"]), ring.mul(v["a"], v["t"])),
                F(1, 8),
            ),
            ring.scale(ring.mul(v["t"], v["b"]), 32),
            ring.const(), ring.const(), ring.const(),
        ]
        aval = v["rho"]
        bval = ring.add(
            ring.scale(aval, module.g(0, 8 * sign)),
            ring.scale(ring.mul(v["t"], v["q"]), -128),
        )
        normal3 = module.vector_with_ab(
            ring, aval, bval, v["y1"], v["y2"], v["y3"], v["y4"]
        )
        d3 = [ring.add(nu3[i], normal3[i]) for i in range(6)]
        d4 = [v[f"z{i}"] for i in range(6)]
        equations = source_series(
            module, ring, rows, loads,
            [{1: x[i], 2: u[i], 3: d3[i], 4: d4[i]} for i in range(6)],
        )
        for row_index in range(7):
            for grade in range(6):
                assert_zero(
                    equations[row_index][grade],
                    f"rank1 sign {sign} row {row_index + 1} G{grade}",
                )
        g6 = [equations[i][6] for i in range(7)]
        s5 = ring.add(ring.add(g6[4], g6[0], F(3, 128)), g6[2], F(1, 8))
        s7 = ring.add(ring.add(g6[6], g6[0], F(1, 512)), g6[2], F(1, 128))
        q3 = ring.power(v["q"], 3)
        assert_equal(module, ring, s5, ring.scale(q3, F(-1, 16)), f"rank1 sign {sign} G6 S5")
        assert_equal(module, ring, g6[5], ring.scale(q3, module.g(0, F(sign, 32))), f"rank1 sign {sign} G6 row6")
        assert_equal(module, ring, s7, ring.scale(q3, F(1, 128)), f"rank1 sign {sign} G6 S7")
        rank1_g6_rows[str(sign)] = [poly_object(poly) for poly in g6]

    # On the G5-rank-zero plane, G6 is a fresh exact Q-cone after centering.
    center_names = (
        "s", "t", "a", "b", *(f"r{i}" for i in range(6)),
        *(f"z{i}" for i in range(6)),
    )
    center_ring = module.Ring(center_names)
    cv = {name: center_ring.var(name) for name in center_names}
    cx = module.old_plane(center_ring, cv["s"], cv["t"])
    cmu = mu_vector(center_ring, cv["s"], cv["t"])
    cplane = module.old_plane(center_ring, cv["a"], cv["b"])
    cu = [center_ring.add(cmu[i], cplane[i]) for i in range(6)]
    cnu3 = [
        center_ring.scale(center_ring.mul(cv["s"], cv["a"]), 2),
        center_ring.scale(
            center_ring.add(
                center_ring.mul(cv["s"], cv["b"]),
                center_ring.mul(cv["a"], cv["t"]),
            ),
            F(1, 8),
        ),
        center_ring.scale(center_ring.mul(cv["t"], cv["b"]), 32),
        center_ring.const(), center_ring.const(), center_ring.const(),
    ]
    cr = [cv[f"r{i}"] for i in range(6)]
    cz = [cv[f"z{i}"] for i in range(6)]
    cd3 = [center_ring.add(cnu3[i], cr[i]) for i in range(6)]
    centered = source_series(
        module, center_ring, rows, loads,
        [{1: cx[i], 2: cu[i], 3: cd3[i], 4: cz[i]} for i in range(6)],
    )
    for row_index in range(7):
        for grade in range(6):
            assert_zero(centered[row_index][grade], f"centered row {row_index + 1} G{grade}")
        assert_equal(
            module, center_ring, centered[row_index][6],
            module.eval_dpoly(quadrics[row_index], cr, center_ring),
            f"centered G6=Q(r) row {row_index + 1}",
        )

    # Parameterize the reduced G6 cone, absorb its plane part into the exact
    # surface, and extract the literal corrected G7 equations.
    g7_names = (
        "s", "t", "a", "b", "c", "d", "p", "q",
        *(f"z{i}" for i in range(6)), "k", "k1",
    )
    g7_ring = module.Ring(g7_names)
    hv = {name: g7_ring.var(name) for name in g7_names}
    hx = module.old_plane(g7_ring, hv["s"], hv["t"])
    hmu = mu_vector(g7_ring, hv["s"], hv["t"])
    hplane2 = module.old_plane(g7_ring, hv["a"], hv["b"])
    hu = [g7_ring.add(hmu[i], hplane2[i]) for i in range(6)]
    hnu3 = [
        g7_ring.add(
            g7_ring.scale(g7_ring.mul(hv["s"], hv["a"]), 2),
            g7_ring.scale(hv["c"], 2),
        ),
        g7_ring.add(
            g7_ring.scale(
                g7_ring.add(
                    g7_ring.mul(hv["s"], hv["b"]),
                    g7_ring.mul(hv["a"], hv["t"]),
                ), F(1, 8),
            ),
            g7_ring.scale(hv["d"], F(1, 8)),
        ),
        g7_ring.add(g7_ring.scale(g7_ring.mul(hv["t"], hv["b"]), 32), hv["c"]),
        hv["d"], hv["c"], g7_ring.scale(hv["d"], 2),
    ]
    hr = module.cone_vector(
        g7_ring, g7_ring.const(), g7_ring.const(), hv["p"], hv["q"]
    )
    hd3 = [g7_ring.add(hnu3[i], hr[i]) for i in range(6)]
    hnu4 = [
        g7_ring.add(
            g7_ring.mul(hv["a"], hv["a"]),
            g7_ring.scale(g7_ring.mul(hv["s"], hv["c"]), 2),
        ),
        g7_ring.scale(
            g7_ring.add(
                g7_ring.add(
                    g7_ring.mul(hv["s"], hv["d"]),
                    g7_ring.mul(hv["a"], hv["b"]),
                ),
                g7_ring.mul(hv["c"], hv["t"]),
            ), F(1, 8),
        ),
        g7_ring.add(
            g7_ring.scale(g7_ring.mul(hv["b"], hv["b"]), 16),
            g7_ring.scale(g7_ring.mul(hv["t"], hv["d"]), 32),
        ),
        g7_ring.const(), g7_ring.const(), g7_ring.const(),
    ]
    hz = [hv[f"z{i}"] for i in range(6)]
    hd4 = [g7_ring.add(hnu4[i], hz[i]) for i in range(6)]
    heq = source_series(
        module, g7_ring, rows, loads,
        [{1: hx[i], 2: hu[i], 3: hd3[i], 4: hd4[i]} for i in range(6)],
        hv["k"], hv["k1"],
    )
    hload = []
    halpha = []
    hbeta = []
    hn = []
    for row_index in range(7):
        for grade in range(7):
            assert_zero(heq[row_index][grade], f"G6-cone row {row_index + 1} G{grade}")
        load = g7_ring.add(
            directional(module, g7_ring, m4[row_index], hx, hu),
            module.eval_dpoly(a10_cubic[row_index], hx, g7_ring),
        )
        normal = second_half(module, g7_ring, cubics[row_index], hx, hr)
        coefficient = directional(module, g7_ring, quadrics[row_index], hr, hz)
        expected = g7_ring.add(
            g7_ring.add(coefficient, normal), g7_ring.mul(hv["k"], load)
        )
        assert_equal(module, g7_ring, heq[row_index][7], expected, f"literal G7 row {row_index + 1}")
        if g7_ring.depends_on(heq[row_index][7], "k1"):
            fail(("spurious k1 at G7", row_index + 1))
        hload.append(load)
        hn.append(normal)
        halpha.append(module.eval_dpoly(module.dderivative(quadrics[row_index], 5), hr, g7_ring))
        hbeta.append(module.eval_dpoly(module.dderivative(quadrics[row_index], 0), hr, g7_ring))

    hdelta = g7_ring.add(
        g7_ring.mul(hv["p"], hv["p"]),
        g7_ring.scale(g7_ring.mul(hv["q"], hv["q"]), 64),
    )
    hc = g7_ring.add(
        g7_ring.mul(
            hv["t"],
            g7_ring.sub(
                g7_ring.scale(g7_ring.mul(hv["q"], hv["q"]), 64),
                g7_ring.mul(hv["p"], hv["p"]),
            ),
        ),
        g7_ring.scale(g7_ring.mul(g7_ring.mul(hv["s"], hv["p"]), hv["q"]), 2),
    )
    he = g7_ring.sub(
        g7_ring.mul(
            hv["s"],
            g7_ring.sub(
                g7_ring.scale(g7_ring.mul(hv["q"], hv["q"]), 64),
                g7_ring.mul(hv["p"], hv["p"]),
            ),
        ),
        g7_ring.scale(g7_ring.mul(g7_ring.mul(hv["t"], hv["p"]), hv["q"]), 128),
    )
    g7_augmented = determinant3(
        g7_ring,
        [[halpha[i], hbeta[i], g7_ring.add(hn[i], g7_ring.mul(hv["k"], hload[i]))] for i in range(3)],
    )
    assert_equal(
        module, g7_ring, g7_augmented,
        g7_ring.scale(g7_ring.mul(hdelta, hc), F(27, 2**35)),
        "G7 augmented determinant including K10",
    )
    assert_equal(module, g7_ring, heq[3][7], g7_ring.scale(he, F(3, 2**15)), "G7 row4")
    assert_zero(g7_ring.add(g7_ring.add(heq[4][7], heq[0][7], F(3, 128)), heq[2][7], F(1, 8)), "G7 S5")
    assert_zero(heq[5][7], "G7 row6 retained zero")
    assert_zero(g7_ring.add(g7_ring.add(heq[6][7], heq[0][7], F(1, 512)), heq[2][7], F(1, 128)), "G7 S7")

    rank1_terminals = {}
    for sign in (1, -1):
        combo = g7_ring.add(heq[1][7], heq[0][7], module.g(0, F(sign, 2)))
        specialized = g7_ring.replace_by_scaled_var(
            combo,
            {
                "p": (module.g(0, 8 * sign), "q"),
                "s": (module.g(0, 8 * sign), "t"),
            },
        )
        terminal = g7_ring.monomial(
            {"t": 3, "k": 1}, module.g(0, F(-5 * sign, 16))
        )
        assert_equal(module, g7_ring, specialized, terminal, f"G7 rank1 terminal sign {sign}")
        rank1_terminals[str(sign)] = poly_object(terminal)

    expected_w1 = g7_ring.scale(
        g7_ring.mul(
            hv["t"],
            g7_ring.sub(
                g7_ring.scale(g7_ring.mul(hv["s"], hv["s"]), 3),
                g7_ring.scale(g7_ring.mul(hv["t"], hv["t"]), 64),
            ),
        ), F(5, 4096),
    )
    expected_w2 = g7_ring.scale(
        g7_ring.mul(
            hv["s"],
            g7_ring.sub(
                g7_ring.mul(hv["s"], hv["s"]),
                g7_ring.scale(g7_ring.mul(hv["t"], hv["t"]), 192),
            ),
        ), F(5, 65536),
    )
    assert_equal(module, g7_ring, hload[0], expected_w1, "rank0 G7 K10 row1")
    assert_equal(module, g7_ring, hload[1], expected_w2, "rank0 G7 K10 row2")
    for load in hload:
        if g7_ring.depends_on(load, "a") or g7_ring.depends_on(load, "b"):
            fail("K10 surface cubic spuriously depends on second surface coefficient")

    certificate = {
        "type": "K00-V20R2-RAM-E2-M1-G7-EMPTY-CERT/v1",
        "source": {path.name: expected for path, expected in EXPECTED.items()},
        "orders": {"Lambda": 2, "d": 1, "k10": 0, "k6": 1, "k2": 1,
                   "mu2": 1, "mu4": 1, "mu6": 1, "Jdet": 0},
        "open": ["(s,t)!=(0,0)", "k10[0]!=0"],
        "raw_g4_quadrics": [dpoly_object(poly) for poly in quadrics],
        "erratum": {
            "old_row2": "5/32768", "cubic_row2": "-5/65536",
            "literal_row2": "5/65536",
            "identity": "DM4(ell)[u]+A10^[3](ell)=DM4(ell)[u-mu/2]",
        },
        "g5": {
            "rows": [poly_object(poly) for poly in g5],
            "delta": poly_object(delta), "C": poly_object(cform), "E": poly_object(eform),
            "rank2": "C=E=0 and det=-delta^2 force s=t=0",
            "rank1": "p=+/-8*i*q; E gives s=+/-8*i*t; exact affine solution; G6 kills",
            "rank0": "p=q=0; all seven labelled G5 rows are zero",
        },
        "g5_rank1_g6_rows": rank1_g6_rows,
        "centered_g6": [poly_object(centered[i][6]) for i in range(7)],
        "g7": {
            "rows": [poly_object(heq[i][7]) for i in range(7)],
            "loads": [poly_object(poly) for poly in hload],
            "delta": poly_object(hdelta), "C": poly_object(hc), "E": poly_object(he),
            "rank1_terminals": rank1_terminals,
            "rank0_cubics": [poly_object(expected_w1), poly_object(expected_w2)],
        },
        "conclusion": "EMPTY_ON_D(k10[0])_INTERSECT_(D(s)_UNION_D(t))_THROUGH_G7",
        "attainment": False,
    }
    cert_bytes = (
        json.dumps(certificate, sort_keys=True, separators=(",", ":")) + "\n"
    ).encode()
    cert_sha = sha256(cert_bytes).hexdigest()
    if EXPECTED_CERTIFICATE_SHA256 != "PENDING" and cert_sha != EXPECTED_CERTIFICATE_SHA256:
        fail(("certificate digest", cert_sha))

    print("K00_RAM_E2M1_G7_RANKFAN_REPLAY=PASS")
    print(f"TAIL_TERMS={term_count}")
    print("UNLOADED_SINGULAR_SURFACE=EXACT")
    print("K10_G7_ERRATUM=DM4(ell)[u]+A10_CUBIC(ell)=DM4(ell)[u-mu/2]")
    print("K10_G7_ROW2_WITNESS=5/65536;OMITTED_CUBIC_MUTATION=5/32768")
    print("G5_RANK2=EMPTY;G5_RANK1=EMPTY_AT_G6;G5_RANK0=ALL_SEVEN_ROWS_ZERO")
    print("G6_CENTERED=Q(r);G6_RANK2=EMPTY_AT_G7;G6_RANK1=EMPTY_AT_G7;G6_RANK0=EMPTY_AT_G7")
    print("CELL_STATUS=EMPTY_THROUGH_G7_ON_EXACT_SOURCE_OPENS")
    print(f"CERTIFICATE_BYTES={len(cert_bytes)}")
    print(f"CERTIFICATE_SHA256={cert_sha}")
    print("MUTATIONS=CUSTODY,SURFACE_16_TO_15,OMIT_A10_CUBIC,DELTA_64_TO_63,RANK1_SIGN,ZERO_ROW_REACTIVATION")


if __name__ == "__main__":
    main()
