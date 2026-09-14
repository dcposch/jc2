#!/usr/bin/env python3
"""Worker-only measured construction, no solve. Physical coordinates X=x,W=y-x."""
import argparse
import ast
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import re
import resource
import socket
import time
from fractions import Fraction

SOURCE_SHA = "778eda933ee9b2acbad20f6dc862c25db94776cb25ffd5782646427a3b63e1ea"
P = 1073741827


def check(ok, why):
    if not ok:
        raise ValueError(why)


def guard():
    check(platform.system() == "Linux", "Linux worker required")
    check(Path("/sys/class/dmi/id/sys_vendor").read_text().strip() == "Amazon EC2", "EC2 required")
    check(socket.gethostname() == "ip-172-30-0-56", "Wrong allocated worker")
    check(os.environ.get("JC2_REGISTERED_JOB") == "factored-jacobian-pilot-astra-20260906", "Registered job required")


def main():
    guard()
    from flint import fmpq_mpoly_ctx, fmpq_mpoly, fmpz_mod_mpoly_ctx
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["scalar", "modular", "exact"], required=True)
    parser.add_argument("--cap", type=int, default=-1)
    parser.add_argument("--source", default="delta2_stage8.strongest.json")
    parser.add_argument("--out", required=True)
    parser.add_argument("--row-limit", type=int, default=0)
    parser.add_argument("--hash-rows", action="store_true")
    args = parser.parse_args()
    start = time.monotonic()
    raw = Path(args.source).read_bytes()
    check(hashlib.sha256(raw).hexdigest() == SOURCE_SHA, "Source hash drift")
    data = json.loads(raw)
    expressions = [str(term[2]) for key in ("h3", "C2", "C3", "B2", "A3") for term in data["maps"][key]]
    names = sorted(set(re.findall(r"\b[A-Za-z_][A-Za-z_0-9]*\b", " ".join(expressions))) | {"target_a", "target_b"})
    check(set(names) <= set(data["full_free_coordinates"]), "Unknown semantic name")
    removed = sorted(set(data["full_free_coordinates"]) - set(names))
    ctx = None
    if args.mode == "exact":
        ctx = fmpq_mpoly_ctx.get(tuple(names), ordering="degrevlex")
    elif args.mode == "modular":
        ctx = fmpz_mod_mpoly_ctx.get(tuple(names), P, ordering="degrevlex")
    const = (lambda n: n % P) if ctx is None else ctx.constant
    zero, one = const(0), const(1)
    if args.mode == "scalar":
        values = {n: 1 + int.from_bytes(hashlib.sha256(("factored-jacobian:" + n).encode()).digest(), "big") % (P - 1) for n in names}
    else:
        values = dict(zip(names, ctx.gens()))
    parse_cache = {}

    def numeric(node):
        if isinstance(node, ast.Constant): return Fraction(node.value)
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub): return -numeric(node.operand)
        if isinstance(node, ast.BinOp):
            a, b = numeric(node.left), numeric(node.right)
            if isinstance(node.op, ast.Add): return a+b
            if isinstance(node.op, ast.Sub): return a-b
            if isinstance(node.op, ast.Mult): return a*b
            if isinstance(node.op, ast.Div): return a/b
            if isinstance(node.op, ast.Pow): return a**int(b)
        raise ValueError("Non-numeric denominator")

    def ev(node):
        if isinstance(node, ast.Constant) and type(node.value) is int:
            return const(node.value)
        if isinstance(node, ast.Name):
            return values[node.id]
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
            return -ev(node.operand)
        if isinstance(node, ast.BinOp):
            a = ev(node.left)
            if isinstance(node.op, ast.Pow):
                check(isinstance(node.right, ast.Constant) and type(node.right.value) is int and node.right.value >= 0, "Noninteger exponent")
                return a**node.right.value
            b = ev(node.right)
            if isinstance(node.op, ast.Add): return a + b
            if isinstance(node.op, ast.Sub): return a - b
            if isinstance(node.op, ast.Mult): return a * b
            if isinstance(node.op, ast.Div):
                check(not any(isinstance(t, ast.Name) for t in ast.walk(node.right)), "Parameter denominator")
                den = numeric(node.right)
                if args.mode == "exact": return a * den.denominator / den.numerator
                return a * const(den.denominator * pow(den.numerator, -1, P) % P)
        raise ValueError(ast.dump(node))

    def parse(expression):
        expression = str(expression)
        if expression not in parse_cache:
            parse_cache[expression] = ev(ast.parse(expression.replace("^", "**"), mode="eval").body)
            if args.mode == "scalar": parse_cache[expression] %= P
        return parse_cache[expression]

    def clean(value):
        return value % P if args.mode == "scalar" else value

    def add(*tables):
        out = {}
        for table, scalar in tables:
            for pos, value in table.items():
                out[pos] = clean(out.get(pos, zero) + scalar * value)
                if not out[pos]: del out[pos]
        return out

    def mul(left, right, cap=None):
        out = {}
        for (i, j), a in left.items():
            for (k, l), b in right.items():
                if cap is not None and i+j+k+l > cap: continue
                pos = (i+k, j+l)
                out[pos] = clean(out.get(pos, zero) + a*b)
                if not out[pos]: del out[pos]
        return out

    def diff(table, col):
        out = {}
        for pos, value in table.items():
            if pos[col]:
                target = list(pos); target[col] -= 1
                out[tuple(target)] = clean(value * pos[col])
        return out

    def bracket(left, right, cap=None):
        return add((mul(diff(left, 0), diff(right, 1), cap), one),
                   (mul(diff(left, 1), diff(right, 0), cap), -one))

    def load_table(key, degree):
        out = {}
        for r, z, expression in data["maps"][key]:
            r, z = int(r), int(z)
            check(r+z <= degree, "Negative physical exponent")
            # For low-J rows, degree cap+2 source jets suffice.
            if args.cap >= 0 and degree-r > args.cap+2: continue
            pos = (degree-r-z, z)
            check(pos not in out, "Duplicate physical monomial")
            value = parse(expression)
            if value: out[pos] = value
        return out

    def table_stats(table):
        if args.mode == "scalar":
            return {"physical_support": len(table), "max_physical_degree": max((sum(p) for p in table), default=-1)}
        return {"physical_support": len(table), "literal_terms": sum(len(v) for v in table.values()),
                "max_semantic_degree": max((int(v.total_degree()) for v in table.values()), default=-1),
                "max_coefficient_terms": max((len(v) for v in table.values()), default=0),
                "max_physical_degree": max((sum(p) for p in table), default=-1)}

    def event(phase, **kwargs):
        print(json.dumps({"phase": phase, "wall": round(time.monotonic()-start, 6),
                          "rss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, **kwargs}, sort_keys=True), flush=True)

    h3, c2, c3 = load_table("h3", 11), load_table("C2", 22), load_table("C3", 33)
    cap_source = None if args.cap < 0 else args.cap+2
    h = add((mul(mul(h3, h3, cap_source), h3, cap_source), one), (mul(c2, h3, cap_source), one), (c3, one))
    D, C = load_table("B2", 65), load_table("A3", 98)
    source_stats = {"h": table_stats(h), "D": table_stats(D), "C": table_stats(C)}
    event("source", semantic_variables=len(names), removed_source_coordinates=removed, stats=source_stats)
    a, b = values["target_a"], values["target_b"]
    two_inv = parse("1/2"); three_inv = parse("1/3")
    A = add((D, parse("3/2")), (h, b*two_inv), ({(0,0): a*two_inv}, one))
    B = add((h, const(2)), ({(0,0): -b*three_inv}, one))
    cap = None if args.cap < 0 else args.cap
    hd = bracket(h, D, cap); event("bracket_hd", stats=table_stats(hd))
    ch = bracket(C, h, cap); event("bracket_ch", stats=table_stats(ch))
    cd = bracket(C, D, cap); event("bracket_cd", stats=table_stats(cd))
    support = set(cd)
    for left, right in ((A, hd), (B, ch)):
        support.update((i+k,j+l) for i,j in left for k,l in right if cap is None or i+j+k+l <= cap)
    event("output_support", candidate_rows=len(support))
    rows_path = Path(args.out + ".rows.tsv")
    stream = hashlib.sha256()
    count = terms = max_degree = 0
    max_terms, max_label = 0, None
    constants = None
    per_degree = {}
    Jscalar = {}
    with rows_path.open("w") as fh:
        fh.write("X_power\tW_power\tliteral_terms\tsemantic_degree\tsha256\n")
        for pos in sorted(support, key=lambda q: (sum(q), q)):
            out = cd.get(pos, zero)
            for left, right in ((A, hd), (B, ch)):
                for (i,j), value in left.items():
                    mate = right.get((pos[0]-i,pos[1]-j))
                    if mate is not None: out += value*mate
            out = clean(out)
            if not out: continue
            if args.mode == "scalar":
                Jscalar[pos] = out
                nterms, degree = 1, 0
                payload = str(out).encode()
            else:
                nterms, degree = len(out), int(out.total_degree())
                payload = str(out).encode() if args.hash_rows else f"{nterms}:{degree}".encode()
            if pos == (0,0): constants = {"terms": nterms, "degree": degree, "digest": hashlib.sha256(payload).hexdigest()}
            fh.write(f"{pos[0]}\t{pos[1]}\t{nterms}\t{degree}\t{hashlib.sha256(payload).hexdigest()}\n")
            stream.update(f"{pos[0]},{pos[1]}:".encode()+payload+b"\n")
            count += 1; terms += nterms; max_degree = max(max_degree, degree)
            per_degree[sum(pos)] = per_degree.get(sum(pos), 0)+1
            if nterms > max_terms: max_terms, max_label = nterms, pos
            if count % 100 == 0: event("rows", rows=count, terms=terms, last_degree=sum(pos))
            if args.row_limit and count >= args.row_limit: break
    # Independent scalar direct F/G control, also verifies the sign/orientation.
    direct_check = "NOT_RUN"
    if args.mode == "scalar":
        F = add((mul(mul(h,h,cap_source),h,cap_source),one),
                (mul(add((D,parse("3/2")),({(0,0):a*two_inv},one)),h,cap_source),one),(C,one))
        G = add((mul(h,h,cap_source),one),(h,-b*three_inv),(D,one))
        direct = bracket(F,G,cap)
        check(direct == Jscalar, "Factored/direct scalar mismatch")
        check(any(v for pos,v in direct.items()), "Trivial zero Jacobian control")
        direct_check = "PASS"
    out = {"mode":args.mode,"prime":None if args.mode=="exact" else P,"cap":args.cap,
           "complete": not bool(args.row_limit),"host":socket.gethostname(),"source_sha256":SOURCE_SHA,
           "semantic_variables_without_Zj":len(names),"semantic_variables_with_Zj":len(names)+1,
           "coordinate_order":names,"removed_source_coordinates":removed,"source_stats":source_stats,
           "candidate_support_rows":len(support),"nonzero_coefficient_rows_including_constant":count,
           "literal_terms_without_inverse":terms,"maximum_semantic_degree":max_degree,
           "maximum_row_terms":max_terms,"maximum_row_label":max_label,"constant_J":constants,
           "rows_per_physical_degree":per_degree,"source_to_factored_direct_scalar_check":direct_check,
           "row_hash_scope":"literal polynomial text" if args.hash_rows else "measurement metadata only, not a polynomial certificate",
           "row_stream_sha256":stream.hexdigest(),"row_metadata_sha256":hashlib.sha256(rows_path.read_bytes()).hexdigest(),
           "wall_seconds":time.monotonic()-start,"peak_rss_kib":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
           "scope":"Representation measurement only; no ideal solve or properness claim"}
    Path(args.out+".json").write_text(json.dumps(out,sort_keys=True,indent=2)+"\n")
    event("complete",report=args.out+".json", rows=count, terms=terms)


if __name__ == "__main__":
    main()
