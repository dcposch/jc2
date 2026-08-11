"""Differential parity gate for the FLINT backend (lib/fastcoef.py).

Runs the full pipeline (SystemA generation -> Cascade3 -> two_chart) on
reg_9_24_c3 and open_8_28_c2 under JC_BACKEND=python and JC_BACKEND=flint and
asserts:
  * coefficient drop-ins (cadd/cmul/cscale/cneg) agree with the jc.py oracle
    on randomized inputs (int and Fraction values);
  * bracket under the flint backend equals the pure computation;
  * cascade internals agree exactly (status, elimination sequence, zeroed
    vars, log, final equation content);
  * every emitted .ms file (SystemA raw, cascade core at p=65521 and char 0,
    both two_chart leaves) is byte-identical across backends.

Skips (exit 0 with a message) if python-flint is not installed.
"""
import os
import random
import sys
import tempfile
from fractions import Fraction

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE, "lib"))
sys.path.insert(0, os.path.join(BASE, "cases"))

import fastcoef
import jc
from jc import SystemA, padd, pmul, pneg, dx, dy
from emit import CASES, FIX
from reduce3 import Cascade3
from chartelim import two_chart, leaf_to_msolve

CASES_UNDER_TEST = ["reg_9_24_c3", "open_8_28_c2"]


def _rcoef(rng, nv=8, nt=6, frac=False):
    c = {}
    for _ in range(rng.randint(0, nt)):
        m = tuple(sorted(rng.choices(range(nv), k=rng.randint(0, 3))))
        v = rng.randint(-9, 9)
        if v == 0:
            continue
        c[m] = Fraction(v, rng.randint(1, 7)) if frac else v
    return c


def test_coef_drop_ins():
    rng = random.Random(42)
    n = 0
    for frac in (False, True):
        for _ in range(250):
            c1, c2 = _rcoef(rng, frac=frac), _rcoef(rng, frac=frac)
            k = rng.randint(-5, 5)
            assert fastcoef.cadd(c1, c2) == jc.cadd(c1, c2)
            assert fastcoef.cmul(c1, c2) == jc.cmul(c1, c2)
            assert fastcoef.cneg(c1) == jc.cneg(c1)
            assert fastcoef.cscale(c1, k) == jc.cscale(c1, k)
            n += 4
    print(f"coef drop-in oracle OK ({n} checks)")


def test_bracket_fast():
    rng = random.Random(7)
    for _ in range(60):
        P = {(rng.randint(0, 4), rng.randint(0, 4)): _rcoef(rng, nt=4) or {(): 1}
             for _ in range(rng.randint(2, 5))}
        Q = {(rng.randint(0, 4), rng.randint(0, 4)): _rcoef(rng, nt=4) or {(): 1}
             for _ in range(rng.randint(2, 5))}
        pure = padd(pmul(dx(P), dy(Q)), pneg(pmul(dy(P), dx(Q))))
        assert fastcoef.bracket_fast(P, Q) == pure
    print("bracket_fast oracle OK (60 checks)")


def _pipeline(name, be, outdir):
    os.environ["JC_BACKEND"] = be
    spec = CASES[name]
    S = SystemA(name, spec["cornersP"], spec["cornersQ"], spec["rhs"],
                nonvanish="nonorigin", fix_ones=FIX[name])
    C = Cascade3(S)
    status = C.run()
    leafG, leafC, info = two_chart(C)
    emitted = {}
    S.write_msolve(os.path.join(outdir, "sysA.ms"), 65521)
    C.write_msolve(os.path.join(outdir, "core.p65521.ms"), 65521)
    C.write_msolve(os.path.join(outdir, "core.q.ms"), 0)
    leaf_to_msolve(leafG, os.path.join(outdir, "leafG.q.ms"), 0)
    leaf_to_msolve(leafC, os.path.join(outdir, "leafC.q.ms"), 0)
    for fn in sorted(os.listdir(outdir)):
        with open(os.path.join(outdir, fn), "rb") as f:
            emitted[fn] = f.read()
    return S, C, status, leafG, leafC, info, emitted


def test_pipeline_parity(name):
    with tempfile.TemporaryDirectory() as dp, tempfile.TemporaryDirectory() as df:
        Sp, Cp, stp, gp, cp, ip, ep = _pipeline(name, "python", dp)
        Sf, Cf, stf, gf, cf, if_, ef = _pipeline(name, "flint", df)
    assert Cp.backend == "python" and Cf.backend == "flint", "backend switch inert"
    assert Sp.equations == Sf.equations, f"{name}: SystemA equations differ"
    assert stp == stf, f"{name}: cascade status differs {stp}/{stf}"
    assert Cp.elim == Cf.elim, f"{name}: elimination sequence differs"
    assert Cp.zeroed == Cf.zeroed, f"{name}: zeroed vars differ"
    assert Cp.log == Cf.log, f"{name}: cascade log differs"
    assert Cp.eqs == Cf.eqs, f"{name}: core equations differ"
    assert ip == if_, f"{name}: two_chart pivot info differs"
    assert gp.eqs == gf.eqs and cp.eqs == cf.eqs, f"{name}: leaves differ"
    assert set(ep) == set(ef)
    for fn in ep:
        assert ep[fn] == ef[fn], f"{name}: emitted {fn} differs between backends"
    print(f"pipeline parity OK: {name} [{stp}; {len(ep)} emitted files "
          f"byte-identical; {len(Cp.elim)} elims]")


if __name__ == "__main__":
    prev = os.environ.get("JC_BACKEND")
    if not fastcoef.HAVE_FLINT:
        print("SKIP test_parity: python-flint not installed")
        sys.exit(0)
    try:
        test_coef_drop_ins()
        test_bracket_fast()
        for nm in CASES_UNDER_TEST:
            test_pipeline_parity(nm)
    finally:
        if prev is None:
            os.environ.pop("JC_BACKEND", None)
        else:
            os.environ["JC_BACKEND"] = prev
    print("ALL PARITY TESTS PASS")
