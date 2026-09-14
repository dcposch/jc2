#!/usr/bin/env python3
"""Exact-Q attained-T2/T3 defect chart, with audited Q-star projection.

The frozen stage-8 inputs are affine source charts: every source equation has
already been solved by a nonzero rational leader and the saved residual ideal
is zero (except for the explicitly retained D108 residuals).  This driver
composes those source maps, forms the depressed cubic identity used by the
charged characteristic-degree backend, and retains exactly the T2 rows needed
to define its defect jet and the complete T3 rows through its attained face.

All further eliminations performed here have a nonzero *rational* coefficient.
The output therefore is an isomorphic polynomial-ring graph projection, not a
specialization.  Its Singular file uses the exact field Q and integer-primitive
rows.  No Jacobian row and no saturation are used.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import resource
import time
from collections import defaultdict
from pathlib import Path

from flint import fmpq_mpoly, fmpq_mpoly_ctx


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
CASES = {
    "99-delta2": ROOT / "box/char-degree-20260905/active-gauge/inputs/delta2_stage8.strongest.json",
    "99-delta52": ROOT / "box/char-degree-20260905/active-gauge/inputs/delta52_stage8.strongest.json",
    "108-free-mean": ROOT / "box/char-degree-20260905/d108/selected/meanfree_stage8_slimgb/d108_meanfree_stage8_strongfront.input.json",
}
IDENT = re.compile(r"\b[A-Za-z_]\w*\b")
TERM = re.compile(r"^\((.*)\)\*tt\^(\d+)\*zz\^(\d+)$")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def seqsha(items) -> str:
    return hashlib.sha256("".join(str(x) + "\n" for x in items).encode()).hexdigest()


def split_top(text: str):
    ans = []
    start = depth = 0
    for i, ch in enumerate(text):
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        elif ch == "+" and depth == 0:
            ans.append(text[start:i])
            start = i + 1
    ans.append(text[start:])
    return [x for x in ans if x]


class Chart:
    def __init__(self, tag: str):
        self.tag = tag
        self.path = CASES[tag]
        self.data = json.loads(self.path.read_text())
        if tag.startswith("99"):
            self.k, self.n, self.m = 33, 99, 66
            self.D2, self.n2, self.D3 = 55, 3, 145
            self.t2_face = (40, 15)
            self.t3_face = (105, 40)
            self.sep = "rho" if tag == "99-delta2" else "c"
            source_names = list(self.data["full_free_coordinates"])
            self.source_residual_text = [v for _, v in self.data["residual_rows"]]
            self.h_kind = "maps"
        else:
            self.k, self.n, self.m = 36, 108, 72
            self.D2, self.n2, self.D3 = 63, 4, 227
            self.t2_face = (49, 14)
            self.t3_face = (176, 51)
            self.sep = "c"
            source_names = list(self.data["names"])
            self.source_residual_text = list(self.data["residual_strings"])
            self.h_kind = "strings"
        self.defect = self.n2 * self.D2 - self.D3
        self.lead = 6 * self.k - 2 - self.D2
        self.lam2 = "leader55" if self.D2 == 55 else "leader63"
        self.zlam2 = "Z55" if self.D2 == 55 else "Z63"
        self.lam3 = "leader145" if self.D3 == 145 else "leader227"
        self.zlam3 = "Z145" if self.D3 == 145 else "Z227"
        self.zsep = "Zrho" if self.sep == "rho" else "Zc"
        self.rec_names = ["rec_fq"] if self.n2 == 3 else ["rec_fgq", "rec_fq2"]
        # Preserve the frozen order, then append genuinely new chart variables.
        self.names = list(source_names)
        for name in [self.zsep, self.lam3, self.zlam3, *self.rec_names]:
            if name not in self.names:
                self.names.append(name)
        assert len(self.names) == len(set(self.names))
        self.ctx = fmpq_mpoly_ctx.get(self.names, ordering="degrevlex")
        self.gens = list(self.ctx.gens())
        self.index = {n: i for i, n in enumerate(self.names)}
        self.zero = self.ctx.constant(0)
        self.one = self.ctx.constant(1)
        self.pivot_images = {}
        self.pivot_order = []
        self.solved = set()
        self.pivots = []
        self.raw_counts = defaultdict(int)
        self.zero_counts = defaultdict(int)
        self.core = []
        self.compose_calls = 0
        self.compose_seconds = 0.0
        self.protected = {
            self.sep, self.zsep, self.lam2, self.zlam2, self.lam3, self.zlam3
        }

    def C(self, value):
        if isinstance(value, fmpq_mpoly):
            return value
        if isinstance(value, int):
            return self.ctx.constant(value)
        text = str(value).replace("**", "^")
        return fmpq_mpoly(text, ctx=self.ctx)

    def var(self, name):
        return self.gens[self.index[name]]

    @staticmethod
    def add(*series):
        out = {}
        for tab, scale in series:
            for pos, value in tab.items():
                got = out.get(pos)
                value = value * scale
                out[pos] = value if got is None else got + value
                if not out[pos]:
                    del out[pos]
        return out

    def shift(self, tab, dt=0, dz=0, scale=1, cap=None):
        scale = self.C(scale)
        return {
            (r + dt, z + dz): v * scale
            for (r, z), v in tab.items()
            if cap is None or r + dt <= cap
        }

    def mul(self, left, right, cap):
        out = {}
        for (r, z), a in left.items():
            for (s, w), b in right.items():
                if r + s > cap:
                    continue
                pos = (r + s, z + w)
                value = a * b
                out[pos] = value if pos not in out else out[pos] + value
                if not out[pos]:
                    del out[pos]
        return out

    def power(self, tab, exponent, cap):
        out = {(0, 0): self.one}
        base = tab
        n = exponent
        while n:
            if n & 1:
                out = self.mul(out, base, cap)
            n //= 2
            if n:
                base = self.mul(base, base, cap)
        return out

    def map_table(self, rows):
        return {(int(r), int(z)): self.C(v) for r, z, v in rows if self.C(v)}

    def string_table(self, text):
        out = {}
        for term in split_top(text):
            match = TERM.match(term)
            if not match:
                raise ValueError("unparsed normalized term: " + term[:180])
            value, r, z = match.groups()
            pos = (int(r), int(z))
            got = out.get(pos)
            value = self.C(value)
            out[pos] = value if got is None else got + value
            if not out[pos]:
                del out[pos]
        return out

    def source_series(self):
        if self.h_kind == "maps":
            maps = self.data["maps"]
            base = self.map_table(maps["h3"])
            h = self.add(
                (self.power(base, 3, self.k), 1),
                (self.mul(self.map_table(maps["C2"]), base, self.k), 1),
                (self.map_table(maps["C3"]), 1),
            )
            D = self.map_table(maps["B2"])
            C = self.map_table(maps["A3"])
        else:
            h = self.string_table(self.data["h_expr"])
            D = self.string_table(self.data["D_expr"])
            C = self.string_table(self.data["C_expr"])
        return h, D, C

    def reduce_poly(self, poly):
        if not self.solved or not poly:
            return poly
        t0 = time.monotonic()
        ans = poly
        # Every pivot image is free of earlier pivot variables.  Applying the
        # graph in chronological order therefore resolves it recursively.  A
        # one-variable dictionary substitution is far leaner than asking FLINT
        # to compose a 450-entry identity map for every coefficient row.
        degrees = ans.degrees()
        for idx in self.pivot_order:
            # `to_dict()` dominates this projection for the multi-million-term
            # R rows.  FLINT's degree vector answers the absence question
            # without materializing that dictionary.
            if degrees[idx] <= 0:
                continue
            terms = ans.to_dict()
            grouped = {}
            for mon, coefficient in terms.items():
                exponent = mon[idx]
                base = list(mon)
                base[idx] = 0
                bucket = grouped.setdefault(exponent, {})
                key = tuple(base)
                bucket[key] = bucket.get(key, 0) + coefficient
            ans = self.zero
            image = self.pivot_images[idx]
            powers = {0: self.one}
            for exponent in sorted(grouped):
                if exponent not in powers:
                    powers[exponent] = image**exponent
                ans += self.ctx.from_dict(grouped[exponent]) * powers[exponent]
            degrees = ans.degrees()
        self.compose_calls += 1
        self.compose_seconds += time.monotonic() - t0
        return ans

    def unit_candidates(self, poly):
        terms = poly.to_dict()
        candidates = []
        for exponent, coefficient in terms.items():
            if sum(exponent) != 1:
                continue
            idx = exponent.index(1)
            name = self.names[idx]
            if idx in self.solved or name in self.protected:
                continue
            if any(exp[idx] for exp in terms if exp != exponent):
                continue
            # Prefer outer coefficient variables, then all other affine ones.
            pref = 0 if name.startswith(("A3c_", "B2c_")) else 1
            candidates.append((pref, name, idx, coefficient))
        return sorted(candidates)

    def install_pivot(self, label, block, poly, candidate):
        _, name, idx, coefficient = candidate
        mon = [0] * len(self.names)
        mon[idx] = 1
        rest = poly - self.ctx.from_dict({tuple(mon): coefficient})
        image = -rest / coefficient
        # FLINT reports degree -1 for the zero polynomial and 0 when a
        # nonzero image is independent of this variable.
        assert image.degrees()[idx] <= 0
        self.pivot_images[idx] = image
        self.pivot_order.append(idx)
        self.solved.add(idx)
        self.pivots.append({
            "label": label,
            "block": block,
            "variable": name,
            "coefficient": str(coefficient),
            "row_terms": len(poly.to_dict()),
            "image_terms": len(image.to_dict()),
            "image_sha256": hashlib.sha256(str(image).encode()).hexdigest(),
        })

    def row(self, block, label, poly, allow_pivot=True):
        self.raw_counts[block] += 1
        if self.raw_counts[block] % 25 == 0:
            print(
                f"ROW_PROGRESS {self.tag} {block}={self.raw_counts[block]} "
                f"pivots={len(self.pivots)} core={len(self.core)} "
                f"rssKiB={resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}",
                flush=True,
            )
        poly = self.reduce_poly(poly)
        if not poly:
            self.zero_counts[block] += 1
            return
        candidates = self.unit_candidates(poly) if allow_pivot else []
        if candidates:
            self.install_pivot(label, block, poly, candidates[0])
        else:
            self.core.append((block, label, poly))

    def repivot_core(self):
        while True:
            changed = False
            pending = self.core
            self.core = []
            for block, label, raw in pending:
                poly = self.reduce_poly(raw)
                if not poly:
                    self.zero_counts[block] += 1
                    continue
                candidates = self.unit_candidates(poly)
                if candidates:
                    self.install_pivot(label, block, poly, candidates[0])
                    changed = True
                else:
                    self.core.append((block, label, poly))
            if not changed:
                break

    def build(self):
        started = time.monotonic()
        h, D, C = self.source_series()
        a, b, c, d, e = [self.var("target_" + x) for x in "abcde"]
        H = self.add((h, 1), ({(self.k, 0): b}, -self.C("1/6")))
        vv = self.add(
            (D, 1),
            ({(2 * self.k - 1, 0): a / 3 + b * b / 18}, 1),
        )
        V = self.add(
            (C, 1),
            (self.shift(D, self.k), -b / 4),
            ({(3 * self.k - 1, 0): a * b / 12 + b**3 / 54 - c / 2}, 1),
        )
        assert all(r >= 1 for r, _ in V)
        U = self.shift(V, -1, scale=self.C("8/3"))
        rcap = 4 * self.k - 2
        Rraw = self.add(
            (self.power(vv, 2, rcap), 1),
            (self.mul(U, H, rcap), -1),
        )
        print(f"PROGRESS {self.tag} source/Rraw support={len(h)}/{len(D)}/{len(C)}/{len(Rraw)} rssKiB={resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}", flush=True)
        RR = {}
        # Within a t-layer, descend in z.  Multiplication by the fixed monic
        # top of H is then genuinely triangular: the new highest-z source
        # coordinate is removed before it can contaminate a lower row.
        for (r, z), value in sorted(Rraw.items(), key=lambda item: (item[0][0], -item[0][1])):
            if z >= self.k:
                self.row("T2_upper", f"T2_upper_t{r}_z{z}", value)
            else:
                RR[(r, z)] = value
        # Source residuals belong to the frozen affine chart.  For 99 they are
        # empty; D108 has 14 genuine equations and they must survive projection.
        for i, text in enumerate(self.source_residual_text):
            self.row("source_residual", f"source_residual_{i}", self.C(text))
        print(f"PROGRESS {self.tag} upper rows={self.raw_counts['T2_upper']} pivots={len(self.pivots)} core={len(self.core)}", flush=True)

        qcap = self.lead + self.defect
        aa = a + b * b / 4
        dd = d + b * c / 2
        pp = dd - aa * aa / 3
        qq = e + c * c / 4 - aa * dd / 3 + 2 * aa**3 / 27
        HH = self.power(H, 2, qcap)
        Qrow = self.add(
            (self.mul(RR, HH, qcap), self.C("3/4")),
            (self.shift(self.mul(self.mul(vv, U, qcap), H, qcap), 1, cap=qcap), self.C("-1/8")),
            (self.shift(self.mul(vv, RR, qcap), 1, cap=qcap), 1),
            (self.shift(self.power(U, 2, qcap), 2, cap=qcap), self.C("-9/64")),
            (self.shift(HH, 4 * self.k - 2, scale=pp, cap=qcap), 1),
            (self.shift(vv, 4 * self.k - 1, scale=pp, cap=qcap), 1),
            ({(6 * self.k - 2, 0): qq}, 1),
        )
        # Above-degree rows and the entire attained homogeneous face.  Terms
        # below the face are retained as the actual Q defect jet.
        by_t = defaultdict(dict)
        for (r, z), value in Qrow.items():
            by_t[r][z] = value
        for r in sorted(x for x in by_t if x < self.lead):
            for z, value in sorted(by_t[r].items(), reverse=True):
                self.row("T2_above", f"T2_above_t{r}_z{z}", value)
        lam2 = self.var(self.lam2)
        z0, power = self.t2_face
        topzs = set(by_t.get(self.lead, {})) | set(range(z0, z0 + power + 1))
        for z in sorted(topzs, reverse=True):
            target = lam2 * math.comb(power, z - z0) if z0 <= z <= z0 + power else self.zero
            self.row("T2_face", f"T2_face_t{self.lead}_z{z}", by_t.get(self.lead, {}).get(z, self.zero) - target)
        self.repivot_core()
        print(f"PROGRESS {self.tag} T2 rows={sum(v for k,v in self.raw_counts.items() if k.startswith('T2'))} pivots={len(self.pivots)} core={len(self.core)}", flush=True)

        # Normalize all ingredients only after the complete T2 graph has been
        # solved.  Simultaneous graph images have been kept recursively resolved.
        Q = {}
        for (r, z), value in Qrow.items():
            if self.lead <= r <= qcap:
                value = self.reduce_poly(value)
                if value:
                    Q[(r - self.lead, z)] = value
        F = self.add((self.power(h, 3, self.defect), 1), (self.shift(C, 1, cap=self.defect), 1))
        G = self.add((self.power(h, 2, self.defect), 1), (self.shift(D, 1, cap=self.defect), 1))
        F = {pos: value for pos, v in F.items() if (value := self.reduce_poly(v))}
        G = {pos: value for pos, v in G.items() if (value := self.reduce_poly(v))}

        # Proposition 3.1 standard support: only the listed terms can reach the
        # defect window.  The equality coefficient is removed by its unit
        # leader equation (c_eq=-lambda2^n2); passive later terms stay free.
        if self.n2 == 3:
            T3 = self.add(
                (self.power(Q, 3, self.defect), 1),
                (self.mul(F, G, self.defect), -(lam2**3)),
                (self.shift(self.mul(F, Q, self.defect), 11, scale=self.var("rec_fq"), cap=self.defect), 1),
            )
        else:
            T3 = self.add(
                (self.power(Q, 4, self.defect), 1),
                (self.mul(F, self.power(G, 2, self.defect), self.defect), -(lam2**4)),
                (self.shift(self.mul(self.mul(F, G, self.defect), Q, self.defect), 9, scale=self.var("rec_fgq"), cap=self.defect), 1),
                (self.shift(self.mul(F, self.power(Q, 2, self.defect), self.defect), 18, scale=self.var("rec_fq2"), cap=self.defect), 1),
            )
        by_t3 = defaultdict(dict)
        for (r, z), value in T3.items():
            by_t3[r][z] = value
        for r in sorted(x for x in by_t3 if x < self.defect):
            for z, value in sorted(by_t3[r].items(), reverse=True):
                self.row("T3_above", f"T3_above_t{r}_z{z}", value)
        lam3 = self.var(self.lam3)
        z0, power = self.t3_face
        topzs = set(by_t3.get(self.defect, {})) | set(range(z0, z0 + power + 1))
        for z in sorted(topzs, reverse=True):
            target = lam3 * math.comb(power, z - z0) if z0 <= z <= z0 + power else self.zero
            self.row("T3_face", f"T3_face_t{self.defect}_z{z}", by_t3.get(self.defect, {}).get(z, self.zero) - target)
        self.repivot_core()
        print(f"PROGRESS {self.tag} T3 rows={self.raw_counts['T3_above']+self.raw_counts['T3_face']} pivots={len(self.pivots)} core={len(self.core)}", flush=True)

        # Localizations are not candidates for graph pivots.
        for block, label, poly in [
            ("inverse", "inverse_separation", self.var(self.zsep) * self.var(self.sep) - 1),
            ("inverse", "inverse_T2_leader", self.var(self.zlam2) * lam2 - 1),
            ("inverse", "inverse_T3_leader", self.var(self.zlam3) * lam3 - 1),
        ]:
            self.raw_counts[block] += 1
            self.core.append((block, label, self.reduce_poly(poly)))
        # Final reduction catches pivots installed late in the T3 block.
        final = []
        for block, label, value in self.core:
            value = self.reduce_poly(value)
            if value:
                final.append((block, label, value))
            else:
                self.zero_counts[block] += 1
        self.core = final
        self.assert_graph()
        self.emit(started, h, D, C, Q, F, G, T3)

    def assert_graph(self):
        free = set(range(len(self.names))) - self.solved
        for idx in self.solved:
            resolved = self.reduce_poly(self.pivot_images[idx])
            degrees = resolved.degrees()
            assert degrees[idx] <= 0
            assert not any(degrees[j] for j in self.solved)
        for _, _, row in self.core:
            degrees = row.degrees()
            assert not any(degrees[j] for j in self.solved)
            assert any(degrees[j] for j in free) or row.total_degree() == 0

    def active_indices(self):
        active = set()
        for _, _, row in self.core:
            for exponent in row.to_dict():
                active.update(i for i, degree in enumerate(exponent) if degree)
        return sorted(active)

    def primitive_string(self, poly, active):
        terms = poly.to_dict()
        denominator = 1
        for value in terms.values():
            denominator = math.lcm(denominator, int(value.denominator))
        integers = {mon: int(value * denominator) for mon, value in terms.items()}
        common = 0
        for value in integers.values():
            common = math.gcd(common, abs(value))
        common = common or 1
        integers = {mon: value // common for mon, value in integers.items()}
        # Deterministic descending exponent order; signs are explicit.
        pieces = []
        for mon in sorted(integers, reverse=True):
            coefficient = integers[mon]
            factors = []
            for idx in active:
                exponent = mon[idx]
                if exponent == 1:
                    factors.append(self.names[idx])
                elif exponent > 1:
                    factors.append(f"{self.names[idx]}^{exponent}")
            body = "*".join(factors) or "1"
            sign = "+" if coefficient >= 0 else "-"
            magnitude = abs(coefficient)
            term = body if magnitude == 1 else f"{magnitude}*{body}"
            pieces.append(sign + term)
        text = "".join(pieces)
        return text[1:] if text.startswith("+") else text

    def emit(self, started, h, D, C, Q, F, G, T3):
        active = self.active_indices()
        active_names = [self.names[i] for i in active]
        assert len(active_names) < 100, (self.tag, len(active_names), active_names)
        row_text = [self.primitive_string(poly, active) for _, _, poly in self.core]
        labels = [label for _, label, _ in self.core]
        blocks = [block for block, _, _ in self.core]
        outbase = HERE / ("small-" + self.tag)
        singular = [
            f"ring R=0,({','.join(active_names)}),dp;",
            "option(redSB);",
            'print("ALL_ROWS_PARSED");',
            "ideal I=" + ",\n".join(row_text) + ";",
            'print("BEGIN_GB");',
            "ideal SB=std(I);",
            'print("END_GB");',
            'print("BEGIN_RESULT");',
            "print(reduce(1,SB));print(dim(SB));print(size(SB));",
            'print("END_RESULT");',
            # Positive/negative inverse controls are independent of production.
            f"ideal n2={self.lam2},{self.zlam2}*{self.lam2}-1;",
            f"ideal p2={self.lam2}-1,{self.zlam2}*{self.lam2}-1;",
            f"ideal n3={self.lam3},{self.zlam3}*{self.lam3}-1;",
            f"ideal p3={self.lam3}-1,{self.zlam3}*{self.lam3}-1;",
            f"ideal ns={self.sep},{self.zsep}*{self.sep}-1;",
            f"ideal ps={self.sep}-1,{self.zsep}*{self.sep}-1;",
            'print("BEGIN_CONTROLS");',
            "print(reduce(1,std(n2)));print(reduce(1,std(p2)));",
            "print(reduce(1,std(n3)));print(reduce(1,std(p3)));",
            "print(reduce(1,std(ns)));print(reduce(1,std(ps)));",
            'print("END_CONTROLS");quit;',
        ]
        script = "\n".join(singular) + "\n"
        outbase.with_suffix(".sing").write_text(script)
        image_digest = seqsha(
            f"{self.names[i]}\t{self.reduce_poly(self.pivot_images[i])}" for i in sorted(self.solved)
        )
        meta = {
            "status": "EMITTED_EXACT_Q_NOT_RUN",
            "case": self.tag,
            "field": "Q",
            "input": str(self.path.relative_to(ROOT)),
            "input_sha256": sha(self.path),
            "source_generator_count": len(self.data.get("full_free_coordinates", self.data.get("names"))),
            "source_residual_count": len(self.source_residual_text),
            "source_chart_lift": "frozen saved rational-pivot maps; zero residual for 99, 14 residual rows retained for D108",
            "new_generator_order": self.names,
            "new_generator_order_sha256": seqsha(self.names),
            "arithmetic": {
                "n": self.n, "m": self.m, "k": self.k, "D2": self.D2,
                "n2": self.n2, "D3": self.D3, "defect": self.defect,
                "T2_H_adic_leader_depth": self.lead,
            },
            "T2_target": f"{self.lam2}*z^{self.t2_face[0]}*(1+z)^{self.t2_face[1]}",
            "T3_target": f"{self.lam3}*z^{self.t3_face[0]}*(1+z)^{self.t3_face[1]}",
            "T3_active_standard_terms": (["Q^3", "F*G", "F*Q"] if self.n2 == 3 else ["Q^4", "F*G^2", "F*G*Q", "F*Q^2"]),
            "raw_row_counts": dict(self.raw_counts),
            "identically_zero_row_counts": dict(self.zero_counts),
            "rational_unit_pivots": len(self.pivots),
            "pivot_blocks": {b: sum(p["block"] == b for p in self.pivots) for b in sorted(set(p["block"] for p in self.pivots))},
            "pivot_ledger": self.pivots,
            "resolved_graph_images_sha256": image_digest,
            "resolved_graph_images_checked_no_solved_variables": True,
            "core_generator_count": len(active_names),
            "core_generator_order": active_names,
            "core_generator_order_sha256": seqsha(active_names),
            "core_row_count": len(self.core),
            "core_row_labels": labels,
            "core_row_blocks": blocks,
            "core_rows_sha256": seqsha(row_text),
            "series_support": {"h": len(h), "D": len(D), "C": len(C), "Q_defect": len(Q), "F_defect": len(F), "G_defect": len(G), "T3": len(T3)},
            "compose_calls": self.compose_calls,
            "compose_seconds": round(self.compose_seconds, 3),
            "build_wall_seconds": round(time.monotonic() - started, 3),
            "peak_RSS_KiB": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            "singular_script": outbase.with_suffix(".sing").name,
            "singular_script_bytes": len(script.encode()),
            "singular_script_sha256": hashlib.sha256(script.encode()).hexdigest(),
            "no_raw_Jacobian_rows": True,
            "no_saturation": True,
            "integer_primitive_serialization": True,
        }
        outbase.with_suffix(".json").write_text(json.dumps(meta, indent=2, sort_keys=True) + "\n")
        print(json.dumps({k: meta[k] for k in ["case", "raw_row_counts", "rational_unit_pivots", "core_generator_count", "core_row_count", "series_support", "build_wall_seconds", "peak_RSS_KiB"]}, indent=2), flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--case", choices=CASES, required=True)
    args = parser.parse_args()
    Chart(args.case).build()


if __name__ == "__main__":
    main()
