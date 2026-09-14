#!/usr/bin/env python3
"""Read-only audit of existing G-containing receivers, using no child V value.

The proof of G coverage is a separate source dependency. This checks that its
fixed (n,m,M_last,ell) inventory is present in the saved emitted charts and
that the printed parameterized polynomial setup has exactly that metadata.
It writes only this lane's report artifact.
"""
from fractions import Fraction
from math import floor, gcd
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
BASE = ROOT / "box/moh14-charts-20260905/hsupport-gate-20260905/source-complete"


def terms(expr):
    return {tuple(sorted(t.strip().split("*"))) for t in expr.split("+")}


def expected_terms(mons, prefix, monic=0):
    out = {("y^%d" % monic,)} if monic else set()
    for b, a in mons:
        factors = ["%s_%d_%d" % (prefix, b, a)]
        if b:
            factors.append("x" if b == 1 else "x^%d" % b)
        if a:
            factors.append("y" if a == 1 else "y^%d" % a)
        out.add(tuple(sorted(factors)))
    return out or {("0",)}


def main():
    manifest = BASE / "classes_manifest.json"
    classes = json.loads(manifest.read_text())
    results = []
    for cls in classes:
        cid = cls["class_id"]
        n, m, mt, ell = cls["n_prime"], cls["m_prime"], cls["M_prime"][-1], cls["ell"]
        K = gcd(n, m)
        e, q = n // K, m // K
        d = Fraction(ell + 1, n - mt - 1)
        stems = [row["stem"] for row in cls["rows"]] + [cid + "_union"]
        for stem in stems:
            meta_path = BASE / "classes" / cid / "meta" / (stem + ".json")
            saved = json.loads(meta_path.read_text())
            meta = saved["meta"]
            assert saved["sat"] == meta["saturation_factor"] == "c"
            assert meta["omega"] == "1"
            assert meta["top_face_factored"] == "y^%d" % K
            assert meta["partition"] == []
            assert all(g in ("P -> P - const(alpha_%d)" % e,
                             "Q -> Q - const(beta_%d)" % q) for g in meta["gauges"])
            blocks = [("h", 1, "h", meta["h_inventory"])]
            blocks += [("AA%d" % i, i, "A%d" % i, mons)
                       for i, mons in sorted((int(k), v) for k, v in meta["alpha_inventories"].items())]
            blocks += [("BB%d" % i, i, "B%d" % i, mons)
                       for i, mons in sorted((int(k), v) for k, v in meta["beta_inventories"].items())]
            builder = BASE / "classes" / cid / "builders" / (stem + "_builder.sing")
            text = builder.read_text()
            setup = dict(re.findall(r"^poly (h|AA\d+|BB\d+) = (.*);$", text, re.M))
            report = []
            for name, deficit, prefix, mons in blocks:
                own = set(map(tuple, mons))
                G = {(b, a) for a in range(K) for b in range(floor(d * (deficit * K - a)) + 1)}
                if name in ("AA%d" % e, "BB%d" % q):
                    G.discard((0, 0))
                assert G <= own, (stem, name, sorted(G - own))
                assert terms(setup[name]) == expected_terms(own, prefix, K if name == "h" else 0)
                report.append(dict(block=name, G_size=len(G), chart_size=len(own), G_contained=True))
            results.append(dict(stem=stem, n=n, m=m, M_last=mt, ell=ell, d=str(d),
                                no_child_V_read=True, terminal_translation_only=True,
                                blocks=report, meta_sha256=hashlib.sha256(meta_path.read_bytes()).hexdigest(),
                                builder_sha256=hashlib.sha256(builder.read_bytes()).hexdigest()))
    payload = dict(status="PASS", count_type="DETERMINED", classes=len(classes),
                   charts=len(results), blocks=sum(len(r["blocks"]) for r in results),
                   scope="saved emitted inventories and setup; source coverage theorem is a separate dependency",
                   manifest_sha256=hashlib.sha256(manifest.read_bytes()).hexdigest(), results=results)
    (HERE / "receiver-support-audit.json").write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps({k: v for k, v in payload.items() if k != "results"}, indent=2))


if __name__ == "__main__":
    main()
