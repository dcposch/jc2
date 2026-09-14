#!/usr/bin/env python3
"""Worker-only replay of hash-bound graph producer plus independent pivot typing."""
import hashlib
import json
import runpy
import math
from pathlib import Path
from flint import fmpq_mpoly_ctx

root = Path(__file__).resolve().parent
driver = root / "box/t2t3-chain-20260906/acyclic_graph_audit.py"
assert hashlib.sha256(driver.read_bytes()).hexdigest() == "bc83ab1560f418038c7cc26cca003c45fb51ac8745ef2ae4cb5d257438ba6ca4"
ns = runpy.run_path(str(driver))
rows, graph = ns["rows"], ns["graph"]
pivots = [pivot for _, _, kind, pivot in rows if pivot is not None]
assert len(pivots) == len(set(pivots)) == len(graph) == 7136
assert set(pivots) == set(graph)
assert all((kind == "graph") == (pivot is not None) for _, _, kind, pivot in rows)
assert all(label.startswith("def_") for label, _, kind, _ in rows if kind == "graph")
assert not set(graph).intersection(ns["source"] + ["t3eq", "t3_fq", "lambda3", "Z3"])
assert len(rows) - len(pivots) == 4470
result = dict(ns["record"])
result.update(
    independent_pivot_type_check=True,
    unique_pivots_exactly_graph_variables=True,
    constraint_rows_pivoted=0,
    semantic_variables_pivoted=0,
    original_driver_sha256=hashlib.sha256(driver.read_bytes()).hexdigest(),
    replay_driver_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
)
(root / "graph-replay.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
print("INDEPENDENT_GRAPH_TYPE_AUDIT=PASS", flush=True)

# Independently evaluate three original constraint expressions via their
# local polynomial contexts, recursively substituting only graph definitions.
semantic = ns["source"] + ["t3eq", "t3_fq", "lambda3", "Z3"]
inverse = ["Z55", "Zrho", "Z3"]
names = [name for name in semantic if name not in inverse] + inverse
ctx = fmpq_mpoly_ctx.get(tuple(names), ordering="degrevlex")
cache = dict(zip(names, ctx.gens()))
definitions = {pivot: i for i, (_, _, _, pivot) in enumerate(rows) if pivot}

def image_of(name):
    if name not in cache:
        i = definitions[name]
        polynomial, local_ctx, local_index = ns["parsed"][i]
        rhs = -(polynomial - local_ctx.gens()[local_index[name]])
        args = [ctx.constant(0) if v == name else image_of(v)
                for v in sorted(local_index, key=local_index.get)]
        cache[name] = rhs.compose(*args, ctx=ctx)
    return cache[name]

def primitive_sha(polynomial):
    denominator = 1
    for _, c in polynomial.terms():
        denominator = math.lcm(denominator, int(c.denominator))
    common = 0
    first = None
    for _, c in polynomial.terms():
        n = int(c * denominator)
        if first is None:
            first = n
        common = math.gcd(common, abs(n))
    scale = -1 if first < 0 else 1
    digest = hashlib.sha256()
    for j, (mon, c) in enumerate(polynomial.terms()):
        n = scale * (int(c * denominator) // common)
        factors = [names[i] + (f"^{e}" if e != 1 else "")
                   for i, e in enumerate(mon) if e]
        term = "*".join(factors) or "1"
        if abs(n) != 1:
            term = f"{abs(n)}*" + term
        term = ("-" if n < 0 else ("+" if j else "")) + term
        digest.update(term.encode())
    return digest.hexdigest()

upper = [i for i, row in enumerate(rows) if row[2] == "T2_upper"]
samples = []
for index in [0, 231, 461]:
    i = upper[index]
    polynomial, local_ctx, local_index = ns["parsed"][i]
    image = polynomial.compose(*(image_of(v) for v in sorted(local_index, key=local_index.get)), ctx=ctx)
    assert image
    samples.append({"upper_index": index, "label": rows[i][0],
                    "terms": len(image), "primitive_sha256": primitive_sha(image)})
samples += [{"label": name, "terms": 2,
             "primitive_sha256": primitive_sha(ctx.gens()[names.index(z)] * ctx.gens()[names.index(v)] - 1)}
            for name, z, v in [("inverse_T2", "Z55", "leader55"),
                               ("inverse_T3", "Z3", "lambda3"),
                               ("inverse_separation", "Zrho", "rho")]]
(root / "graph-generator-samples.json").write_text(json.dumps(samples, indent=2) + "\n")
print("INDEPENDENT_GRAPH_CONSTRAINT_SAMPLE_HASHES=PASS", flush=True)
