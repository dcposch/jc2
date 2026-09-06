#!/usr/bin/env python3
"""Independently evaluate the delta-2 top T2 face modulo the screen prime."""
from __future__ import annotations

import hashlib
import shutil
import tempfile
from pathlib import Path

from flint import nmod_mpoly, nmod_mpoly_ctx

from build_direct import DirectChart


class Probe(DirectChart):
    def C(self, value):
        if isinstance(value, nmod_mpoly):
            return value
        if isinstance(value, int):
            return self.ctx.constant(value)
        return nmod_mpoly(str(value).replace("**", "^"), ctx=self.ctx)


def main():
    scratch = Path(tempfile.mkdtemp(prefix="t2top-mod-"))
    try:
        chart = Probe("99-delta2", scratch)
        chart.sing.close()
        chart.ms.close()
        chart.labels.close()
        chart.ctx = nmod_mpoly_ctx.get(
            tuple(chart.names), modulus=chart.PRIME, ordering="degrevlex"
        )
        chart.gens = list(chart.ctx.gens())
        chart.zero = chart.ctx.constant(0)
        chart.one = chart.ctx.constant(1)

        h, D, C = chart.source_series()
        a, b, c, d = [chart.var("target_" + letter) for letter in "abcd"]
        H = chart.add((h, 1), ({(chart.k, 0): b}, -chart.C("1/6")))
        v = chart.add(
            (D, 1),
            ({(2 * chart.k - 1, 0): a / 3 + b * b / 18}, 1),
        )
        V = chart.add(
            (C, 1),
            (chart.shift(D, chart.k), -b / 4),
            ({(3 * chart.k - 1, 0): a * b / 12 + b**3 / 54 - c / 2}, 1),
        )
        U = chart.shift(V, -1, scalar=chart.C("8/3"))
        Rraw = chart.add((chart.mul(v, v), 1), (chart.mul(U, H), -1))
        Rlow = {pos: value for pos, value in Rraw.items() if pos[1] < chart.k}
        HH = chart.mul(H, H, chart.qcap - min(r for r, _ in Rlow))
        vU = chart.mul(v, U, chart.qcap - 1)
        pp = d + b * c / 2 - (a + b * b / 4) ** 2 / 3
        r, z = chart.lead, chart.D2
        value = chart.coefficient_mul(Rlow, HH, (r, z)) * chart.C("3/4")
        value += chart.coefficient_mul(vU, H, (r - 1, z)) * chart.C("-1/8")
        value += chart.coefficient_mul(v, Rlow, (r - 1, z))
        value += chart.coefficient_mul(U, U, (r - 2, z)) * chart.C("-9/64")
        value += HH.get((r - (4 * chart.k - 2), z), chart.zero) * pp
        value += v.get((r - (4 * chart.k - 1), z), chart.zero) * pp
        face = value - chart.var(chart.spec["lam2"])
        rendered = str(face)
        print(f"PRIME={chart.PRIME}")
        print(f"FACE_INDEX={z}")
        print(f"Q_COEFFICIENT_ZERO={int(not value)}")
        print(f"FACE_TERMS={len(face)}")
        print(f"FACE_TEXT_SHA256={hashlib.sha256(rendered.encode()).hexdigest()}")
        if len(face) <= 20:
            print("FACE=" + rendered)
    finally:
        shutil.rmtree(scratch)


if __name__ == "__main__":
    main()
