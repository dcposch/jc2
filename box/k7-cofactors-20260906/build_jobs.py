#!/usr/bin/env python3
"""Build exact-Q Singular certificate jobs from frozen integral .ms charts.

The conversion is deliberately syntax-only: it preserves the alias and
generator order from the source and restores the recorded tower-weight order.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


CHARTS = (
    "K7_B9_Q0",
    "K7_B9_Q1",
    "K7_B10_Q0",
    "K7_B10_Q1",
    "K7_B11_Q0",
    "K7_B11_Q1",
    "K7_B12_Q0",
)

EXPECTED = {
    "K7_B9_Q0": (72, 241, "15b4b715767a72e152f340dda11354af380897f6670d6370f0542841cdb4c275"),
    "K7_B9_Q1": (71, 235, "09002c7229da517ca0d809f925873aeb94d44650467bd6addf71268aacbb7934"),
    "K7_B10_Q0": (79, 261, "273a1a0f65308af6019c3b8986fa921c76d4e27da30d0b675afc532bc3f3d434"),
    "K7_B10_Q1": (78, 255, "a49433e9834c4fa7a76a89aef50e7f3852ee0e26ff1d665bc1c8516dc390f97d"),
    "K7_B11_Q0": (86, 281, "e8e57139c2292f0535226e7fb8fc2fac90b459685e939b825abec31531b2367e"),
    "K7_B11_Q1": (85, 275, "42f96a5f916e94457887e933cb8cb3f8656537e1547e719e30851075990fd4f1"),
    "K7_B12_Q0": (93, 301, "3a3821db1511fa96096f627d5d5ed23b1b60a2c95022f33dfb90791a4c60561d"),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_ms(path: Path) -> tuple[list[str], list[str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if len(lines) < 3 or lines[1].strip() != "0":
        raise ValueError(f"{path}: expected characteristic-zero msolve input")
    variables = [v.strip() for v in lines[0].split(",") if v.strip()]
    body = "\n".join(lines[2:]).strip()
    if body.endswith(","):
        body = body[:-1]
    generators = [g.strip() for g in body.split(",\n") if g.strip()]
    return variables, generators


def prelude(stem: str, source: Path, variables: list[str], generators: list[str], weights: list[int]) -> list[str]:
    digest = sha256(source)
    order = f"wp({','.join(map(str, weights))})"
    return [
        "option(redSB); short=0;",
        f"// chart={stem}",
        f"// source={source.resolve()}",
        f"// source_sha256={digest}",
        "// generator_order=one-based source order, unchanged",
        f"// monomial_order={order}",
        f"ring R=0,({','.join(variables)}),{order};",
        "ideal I=",
        ",\n".join(generators) + ";",
        f'print("CERT__CHART {stem}");',
        f'print("CERT__SOURCE_SHA256 {digest}");',
        f'print("CERT__ORDER {order}");',
        'print("CERT__NVARS "+string(nvars(basering)));',
        'print("CERT__NGEN "+string(size(I)));',
    ]


def std_job(lines: list[str]) -> str:
    return "\n".join(lines + [
        "int t=timer; option(prot); ideal G=std(I); option(noprot);",
        'print("CERT__SECONDS "+string(timer-t));',
        'print("CERT__GB_SIZE "+string(size(G)));',
        'print("CERT__UNIT "+string(size(G)==1 && G[1]==1));',
        'print("CERT__GB_BEGIN"); print(G); print("CERT__GB_END");',
        "quit;",
    ]) + "\n"


def lift_job(lines: list[str]) -> str:
    return "\n".join(lines + [
        "int t=timer; option(prot); matrix T; ideal G=liftstd(I,T); option(noprot);",
        'print("CERT__SECONDS "+string(timer-t));',
        'print("CERT__GB_SIZE "+string(size(G)));',
        "int UNITCONST=(size(G)==1 && deg(G[1])==0);",
        "number UNITCOEF; if (UNITCONST) { UNITCOEF=leadcoef(G[1]); T=(1/UNITCOEF)*T; G=ideal(1); }",
        'print("CERT__UNIT "+string(size(G)==1 && G[1]==1));',
        "matrix C=matrix(I)*T;",
        'print("CERT__INPROCESS_CHECK "+string(ncols(C)==1 && C[1,1]==1));',
        'print("CERT__COFACTORS_BEGIN");',
        'int i; for (i=1; i<=nrows(T); i++) { if (T[i,1]!=0) { print("CERT__COFACTOR "+string(i)+" "+string(T[i,1])); } }',
        'print("CERT__COFACTORS_END");',
        "quit;",
    ]) + "\n"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("source_root", type=Path)
    ap.add_argument("output_root", type=Path)
    args = ap.parse_args()
    jobs = args.output_root / "jobs"
    jobs.mkdir(parents=True, exist_ok=True)
    manifest: list[dict[str, object]] = []
    for stem in CHARTS:
        source = args.source_root / f"{stem}_p0.ms"
        meta_path = args.source_root / f"{stem}_p0.json"
        variables, generators = parse_ms(source)
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        weights = meta["weights"]
        want_nv, want_ng, want_sha = EXPECTED[stem]
        assert (len(variables), len(generators), sha256(source)) == (want_nv, want_ng, want_sha)
        assert len(weights) == len(variables)
        base = prelude(stem, source, variables, generators, weights)
        std_path = jobs / f"{stem}_std.sing"
        lift_path = jobs / f"{stem}_liftstd.sing"
        std_path.write_text(std_job(base), encoding="utf-8")
        lift_path.write_text(lift_job(base), encoding="utf-8")
        manifest.append({
            "chart": stem,
            "source": str(source.resolve()),
            "source_sha256": want_sha,
            "nvars": want_nv,
            "ngens": want_ng,
            "generator_order": "one-based source order, unchanged",
            "monomial_order": f"wp({','.join(map(str, weights))})",
            "std_script_sha256": sha256(std_path),
            "liftstd_script_sha256": sha256(lift_path),
        })
    (args.output_root / "jobs-manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
