#!/usr/bin/env python3
"""Independent whole-row checker for a jc2.d125-physical-literal/v1 stream.

Never imports exporter.py.  Every expected object is rebuilt by a different
route: direct rectangular support enumeration; all-pairs P x Q Jacobian
convolution (not a forced-Q lookup); jet/pin rows read from actual integer
powers of (Y + X^-1) (not math.comb); explicit cubic guard; explicit envelope.
Then EVERY JSON line and EVERY Singular line is compared.  Changed-object
controls re-synchronise the footer so a hash-only checker would accept them.
"""
import argparse, hashlib, json, os, re, resource, sys, time
from collections import Counter
from fractions import Fraction

def canonical(obj):
    return (json.dumps(obj, sort_keys=True, separators=(",", ":")) + "\n").encode()

class Fail(Exception):
    pass

def need(ok, msg):
    if not ok:
        raise Fail(msg)

def cdiv(a, b):  # ceil for ints, b>0
    return -((-a) // b)

SCHEMA = "jc2.d125-physical-literal/v1"
BUILDER_PIN = "a8092908c9f4916306e24fdeca622426f8e6be09ab4f3d0d19e7488e05eca2f9"
SOURCE_PINS = {
    "d125-client-interface-astra-20260906.md": "0c5270a432a6336c17c4693034e36cb496f139c3267843e3ac06628ec8c4b255",
    "d125-source-contract-gate-fable5-20260906.md": "a802587179b6f105bb47555ceb0e6a1d20c94c68a76c6ac4a26bbea1fce7b4e4",
    "d125-triangular-source-normalization-astra-20260906.md": "8ea55aaf26acbd4992aee9d14cce8712fda1c7590cd876ee974194c76bb3ad9e",
}
# Reviewed source contract (client interface + normalization): (D,U,h)=(75,15,3),(125,25,5);
# normalized caps deg_v P<=60 with [v^60]P=a*u^15, deg_v Q<=100 with [v^100]Q=b*u^25; five pins; target 1/5.
D125_SPEC = {"name": "D125", "mode": "normalized", "target": ["1", "5"],
    "sides": {"P": {"degree": 75, "weight_cap": 15, "terminal_h": 3, "vertical_cap": 60, "guard": [15, 60]},
              "Q": {"degree": 125, "weight_cap": 25, "terminal_h": 5, "vertical_cap": 100, "guard": [25, 100]}},
    "pins": [["P", 3, 4, "1", "1"], ["P", 15, 21, "1", "1"], ["Q", 1, 1, "-1", "1"],
             ["Q", 13, 18, "-3", "1"], ["Q", 25, 35, "-9", "5"]]}
TOY_SPEC = {"name": "TOY_NOT_D125", "mode": "original", "target": ["1", "5"],
    "sides": {"P": {"degree": 3, "weight_cap": 5, "terminal_h": 0, "vertical_cap": 2, "guard": [1, 2]},
              "Q": {"degree": 4, "weight_cap": 8, "terminal_h": 1, "vertical_cap": 2, "guard": [2, 2]}},
    "pins": [["P", 3, 3, "1", "1"], ["P", -2, -1, "2", "3"], ["Q", 8, 8, "-1", "1"],
             ["Q", -1, 0, "-3", "1"], ["Q", 2, 3, "-9", "5"]]}

# ---------------------------------------------------------------- expected objects
def rect_support(side, normalized):
    D, U, V = side["degree"], side["weight_cap"], side["vertical_cap"]
    gi, gj = side["guard"]
    S = []
    for i in range(D + 1):
        for j in range(D + 1):
            if i + j > D or 5 * i - j > U:
                continue
            if normalized and (j > V or (j == V and i != gi)):
                continue
            S.append((i, j))
    S.sort(key=lambda ij: (5 * ij[0] - ij[1], ij[0]))
    need((gi, gj) in S and gi + gj == D, "guard endpoint not on support/degree boundary")
    return S

def power_table(jmax):
    """(Y + X^-1)^j as {(xexp, yexp): int}, by repeated multiplication."""
    tab = [{(0, 0): 1}]
    for _ in range(jmax):
        nxt = {}
        for (a, b), c in tab[-1].items():
            nxt[(a, b + 1)] = nxt.get((a, b + 1), 0) + c
            nxt[(a - 1, b)] = nxt.get((a - 1, b), 0) + c
        tab.append(nxt)
    return tab

class Expected:
    def __init__(self, spec, auth_obj):
        self.spec = spec
        normalized = spec["mode"] == "normalized"
        self.S = {s: rect_support(spec["sides"][s], normalized) for s in ("P", "Q")}
        self.records, self.ids = [], {"P": {}, "Q": {}}
        for s in ("P", "Q"):
            for (i, j) in self.S[s]:
                idx = len(self.records)
                self.ids[s][(i, j)] = idx
                self.records.append({"type": "variable", "id": idx, "side": s, "name": f"{s}_u{i}_v{j}",
                                     "source_exponent": [i, j], "public_name": f"{s}_{5*i-j}_{i}",
                                     "additive_constant": (i == 0 and j == 0)})
        self.zid = len(self.records)
        self.records.append({"type": "variable", "id": self.zid, "side": "guard", "name": "Z_degree_guard"})
        self.nvar = len(self.records)
        self.names = [r["name"] for r in self.records]
        jmax = max(j for s in ("P", "Q") for (_, j) in self.S[s])
        self.tab = power_table(jmax)
        self.auth_sha = hashlib.sha256(canonical(auth_obj)).hexdigest() if auth_obj is not None else None
        self.header = {"type": "header", "schema": SCHEMA, "coefficient_field": "Q", "global_order": "dp",
            "spec": spec, "source_hashes": SOURCE_PINS, "builder_sha256": BUILDER_PIN,
            "variable_count": self.nvar, "production_authority_canonical_sha256": self.auth_sha,
            "source_counts": {s: len(self.S[s]) for s in ("P", "Q")},
            "normalized_equivalence_status": "PROVISIONAL_UNLICENSED" if normalized else "NOT_REQUIRED",
            "zero_policy": "all envelope and original linear rows retained",
            "constants_policy": "both source additive constants retained",
            "semantics": "ALL ordinary coefficients of J(P,Q)-1/5 plus every jet, pin, guard; no solve"}
        self.build_conv()

    def band_row(self, side, ell, k):
        out = []
        if k < 0:
            return out
        for (i, j) in self.S[side]:
            if 5 * i - j != ell:
                continue
            c = self.tab[j].get((k - j, k), 0)   # coeff of X^(ell+k) Y^k in X^(5i)(Y+X^-1)^j
            if c:
                out.append((Fraction(c), (self.ids[side][(i, j)],)))
        return out

    def build_conv(self):
        conv = {}
        for (i, j) in self.S["P"]:
            pid = self.ids["P"][(i, j)]
            for (k, s) in self.S["Q"]:
                det = i * s - j * k
                if det:
                    slot = (i + k - 1, j + s - 1)
                    d = conv.setdefault(slot, {})
                    key = (pid, self.ids["Q"][(k, s)])
                    need(key not in d, "duplicate bilinear monomial in convolution")
                    d[key] = Fraction(det)
        self.conv = conv
        sp, sq = self.spec["sides"]["P"], self.spec["sides"]["Q"]
        Imax = max(i for i, _ in self.S["P"]) + max(i for i, _ in self.S["Q"]) - 1
        Jmax = max(j for _, j in self.S["P"]) + max(j for _, j in self.S["Q"]) - 1
        degb = sp["degree"] + sq["degree"] - 2
        wb = sp["weight_cap"] + sq["weight_cap"] - 4
        self.envelope = [(I, J) for I in range(Imax + 1)
                         for J in range(max(0, 5 * I - wb), min(degb - I, Jmax) + 1)]
        env = set(self.envelope)
        need(all(slot in env for slot in conv), "nonzero convolution slot outside envelope")
        self.env_bounds = {"I_max": Imax, "J_max": Jmax, "degree_bound": degb, "weight_bound": wb,
                           "slots": len(self.envelope), "nonzero_slots": len(conv)}

    def rows(self):
        spec = self.spec
        for s in ("P", "Q"):
            d = spec["sides"][s]
            for ell in range(-d["degree"], d["weight_cap"] + 1):
                r = max(0, cdiv(5 * ell - d["terminal_h"], 12))
                for k in range(r):
                    yield ("jet", f"jet_{s}_ell{ell}_order{k}", self.band_row(s, ell, k),
                           {"side": s, "ell": ell, "order": k})
        for n, (s, ell, power, num, den) in enumerate(spec["pins"]):
            terms = self.band_row(s, ell, power - ell)
            val = Fraction(int(num), int(den))
            if val:
                terms.append((-val, ()))
            yield ("pin", f"pin_{n}_{s}_ell{ell}_t{power}", terms,
                   {"side": s, "ell": ell, "t_power": power, "target": [num, den]})
        target = Fraction(int(spec["target"][0]), int(spec["target"][1]))
        for (I, J) in self.envelope:
            terms = [(c, key) for key, c in self.conv.get((I, J), {}).items()]
            if (I, J) == (0, 0) and target:
                terms.append((-target, ()))
            yield ("physical_J", f"J_u{I}_v{J}", terms, {"output_exponent": [I, J]})
        gids = (self.ids["P"][tuple(spec["sides"]["P"]["guard"])],
                self.ids["Q"][tuple(spec["sides"]["Q"]["guard"])], self.zid)
        yield ("degree_guard", "original_degree_guard", [(Fraction(1), gids), (Fraction(-1), ())],
               {"original_degrees": [spec["sides"]["P"]["degree"], spec["sides"]["Q"]["degree"]]})

# ---------------------------------------------------------------- JSON verification
INT_RE = re.compile(r"-?(0|[1-9][0-9]*)\Z")

def decode_terms(terms, nvar):
    out = {}
    for t in terms:
        need(isinstance(t, list) and len(t) == 3, "term shape")
        n, d, ids = t
        need(isinstance(n, str) and isinstance(d, str) and INT_RE.match(n) and INT_RE.match(d), "term literal")
        n, d = int(n), int(d)
        need(n != 0 and d > 0, "zero term or bad denominator")
        from math import gcd
        need(gcd(abs(n), d) == 1, "unreduced fraction")
        need(isinstance(ids, list) and all(type(i) is int and 0 <= i < nvar for i in ids), "term ids")
        key = tuple(ids)
        need(key not in out, "duplicate monomial in row")
        out[key] = Fraction(n, d)
    return out

def verify_json(lines, E, stats):
    """lines: iterator of bytes lines. Raises Fail with semantic reason on first defect."""
    digest = hashlib.sha256()
    def nxt(what):
        line = next(lines, None)
        need(line is not None and line.endswith(b"\n"), f"stream truncated before {what}")
        obj = json.loads(line)
        need(canonical(obj) == line, f"non-canonical encoding at {what}")
        return line, obj
    line, header = nxt("header")
    need(header == E.header, "header contract drift")
    digest.update(line)
    for rec in E.records:
        line, obj = nxt(f"variable {rec['id']}")
        need(obj == rec, f"variable record drift at id {rec['id']}")
        digest.update(line)
    counts, zero, terms, used = Counter(), Counter(), Counter(), set()
    order_ok = True
    first_zero_physical = None
    for kind, label, exp_terms, meta in E.rows():
        line, obj = nxt(f"row {label}")
        need(obj.get("type") == "row", f"row type at {label}")
        need(obj.get("label") == label, f"row label mismatch: expected {label}, got {obj.get('label')}")
        need(obj.get("kind") == kind, f"row kind at {label}")
        extra = {k: v for k, v in obj.items() if k not in ("type", "label", "kind", "terms")}
        need(extra == meta, f"row metadata at {label}")
        actual = decode_terms(obj["terms"], E.nvar)
        expected = {key: c for c, key in exp_terms}
        need(actual == expected, f"coefficient/monomial mismatch in row {label}")
        if [tuple(t[2]) for t in obj["terms"]] != [key for _, key in exp_terms]:
            order_ok = False
        digest.update(line)
        counts[kind] += 1
        zero[kind] += not obj["terms"]
        terms[kind] += len(obj["terms"])
        for key in actual:
            used.update(key)
        if kind == "physical_J" and not obj["terms"] and first_zero_physical is None:
            first_zero_physical = label
    line, footer = nxt("footer")
    need(footer.get("type") == "footer", "footer missing (extra row or wrong record)")
    need(footer.get("complete") is True, "footer complete flag not true")
    need(footer.get("variable_count") == E.nvar, "footer variable_count")
    need(footer.get("row_counts") == dict(counts), "footer row_counts")
    need(footer.get("zero_row_counts") == dict(zero), "footer zero_row_counts")
    need(footer.get("term_counts") == dict(terms), "footer term_counts")
    unused = [i for i in range(E.nvar) if i not in used]
    need(footer.get("unused_variable_ids") == unused, "footer unused_variable_ids")
    need(set(footer) == {"type", "complete", "prefix_sha256", "variable_count", "row_counts",
                         "zero_row_counts", "term_counts", "unused_variable_ids"}, "footer keys")
    need(footer.get("prefix_sha256") == digest.hexdigest(), "prefix digest")
    need(next(lines, None) is None, "trailing bytes after footer")
    stats.update({"row_counts": dict(counts), "zero_row_counts": dict(zero), "term_counts": dict(terms),
                  "unused_variable_ids": unused, "unused_variable_names": [E.names[i] for i in unused],
                  "prefix_sha256": digest.hexdigest(), "term_order_identical": order_ok,
                  "first_zero_physical_row": first_zero_physical, "variable_count": E.nvar})
    return footer

# ---------------------------------------------------------------- Singular verification
ATOM_RE = re.compile(r"\((-?(?:0|[1-9][0-9]*))/([1-9][0-9]*)\)((?:\*[A-Za-z_][A-Za-z0-9_]*)*)\Z")
LABEL_RE = re.compile(r"// ([A-Za-z0-9_\-]+)\Z")
RING_RE = re.compile(r"ring R=0,\(([A-Za-z0-9_,]*)\),dp;\Z")

def verify_sing(lines, json_rows, names, prefix_sha):
    """json_rows: list of (label, [(nstr,dstr,ids_tuple)...]) taken from the validated JSON."""
    name_id = {n: i for i, n in enumerate(names)}
    def nxt(what):
        raw = next(lines, None)
        need(raw is not None and raw.endswith(b"\n"), f"Singular file truncated before {what}")
        need(all(32 <= b < 127 for b in raw[:-1]), f"non-printable byte at {what}")
        return raw[:-1].decode("ascii")
    need(nxt("banner") == "// IMPORT ONLY: no standard basis or solve", "Singular banner")
    m = RING_RE.match(nxt("ring"))
    need(m is not None, "ring line grammar")
    ring_names = m.group(1).split(",")
    need(ring_names == names, "ring variable list differs from JSON variable map (names/order/count)")
    need(len(set(ring_names)) == len(ring_names), "duplicate ring variable")
    need(nxt("ideal") == "ideal I=", "ideal header")
    last = len(json_rows) - 1
    atoms_total = 0
    for idx, (label, jterms) in enumerate(json_rows):
        m = LABEL_RE.match(nxt(f"label {label}"))
        need(m is not None and m.group(1) == label, f"Singular row label mismatch at row {idx} ({label})")
        poly = nxt(f"polynomial {label}")
        term = ";" if idx == last else ","
        need(poly.endswith(term), f"row terminator at {label}")
        poly = poly[:-1]
        got = []
        if poly == "0":
            pass
        else:
            for atom in poly.split("+"):
                am = ATOM_RE.match(atom)
                need(am is not None, f"atom grammar violation at {label}: {atom[:40]!r}")
                n, d, factors = am.groups()
                ids = tuple(name_id[f] for f in factors.split("*")[1:]) if factors else ()
                got.append((n, d, ids))
                atoms_total += 1
        gd = {ids: (n, d) for n, d, ids in got}
        need(len(gd) == len(got), f"duplicate Singular monomial at {label}")
        jd = {ids: (n, d) for n, d, ids in jterms}
        need(gd == jd, f"Singular polynomial differs from JSON row {label}")
        need(got == list(jterms), f"Singular term order differs from JSON row {label}")
    need(nxt("complete marker") == "// COMPLETE prefix_sha256=" + prefix_sha, "COMPLETE marker/digest")
    need(nxt("print") == 'print("D125_IMPORT_ONLY_NO_SOLVE");', "print marker")
    need(nxt("quit") == "quit;", "quit line")
    need(next(lines, None) is None, "bytes after quit")
    return atoms_total

# ---------------------------------------------------------------- controls
def resync_footer(lines):
    """Recompute footer counts/digest from mutated content (keeps 'complete' flag as set)."""
    out = []
    digest = hashlib.sha256()
    counts, zero, terms, used = Counter(), Counter(), Counter(), set()
    nvar = 0
    footer_idx = None
    for i, line in enumerate(lines):
        obj = json.loads(line)
        if obj.get("type") == "footer":
            footer_idx = i
            break
        if obj.get("type") == "variable":
            nvar += 1
        if obj.get("type") == "row":
            k = obj["kind"]; counts[k] += 1; zero[k] += not obj["terms"]; terms[k] += len(obj["terms"])
            for t in obj["terms"]:
                used.update(t[2])
        digest.update(line)
        out.append(line)
    if footer_idx is None:
        return out
    footer = json.loads(lines[footer_idx])
    footer.update({"prefix_sha256": digest.hexdigest(), "variable_count": nvar, "row_counts": dict(counts),
                   "zero_row_counts": dict(zero), "term_counts": dict(terms),
                   "unused_variable_ids": [i for i in range(nvar) if i not in used]})
    out.append(canonical(footer))
    out.extend(lines[footer_idx + 1:])
    return out

def edit_record(lines, pred, change):
    for i, line in enumerate(lines):
        obj = json.loads(line)
        if pred(obj):
            change(obj)
            lines[i] = canonical(obj)
            return i
    raise RuntimeError("control target absent")

def find_index(lines, pred):
    for i, line in enumerate(lines):
        if pred(json.loads(line)):
            return i
    raise RuntimeError("control target absent")

def json_controls(base, first_zero):
    def C(name, mutate, resync=True):
        def thunk():
            L = list(base); mutate(L)
            return resync_footer(L) if resync else L
        return name, thunk
    yield C("coefficient_sign_flip", lambda L: edit_record(L,
        lambda r: r.get("kind") == "physical_J" and any(len(t[2]) == 2 for t in r["terms"]),
        lambda r: r["terms"][0].__setitem__(0, str(-int(r["terms"][0][0])))))
    def bump_bilinear(r):
        t = next(t for t in r["terms"] if len(t[2]) == 2)
        t[0] = str(2 * int(t[0]))
    yield C("determinant_plus_one", lambda L: edit_record(L,
        lambda r: r.get("kind") == "physical_J" and any(len(t[2]) == 2 for t in r["terms"]), bump_bilinear))
    yield C("guard_row_removed", lambda L: L.__delitem__(find_index(L, lambda r: r.get("label") == "original_degree_guard")))
    yield C("guard_constant_removed", lambda L: edit_record(L, lambda r: r.get("label") == "original_degree_guard",
        lambda r: r["terms"].pop()))
    yield C("target_constant_removed", lambda L: edit_record(L, lambda r: r.get("label") == "J_u0_v0",
        lambda r: r["terms"].__setitem__(slice(None), [t for t in r["terms"] if t[2]])))
    yield C("target_sign_flipped", lambda L: edit_record(L, lambda r: r.get("label") == "J_u0_v0",
        lambda r: r["terms"].__setitem__(-1, ["1", "5", []])))
    yield C("pin_value_changed", lambda L: edit_record(L, lambda r: r.get("label", "").startswith("pin_4_"),
        lambda r: r["terms"].__setitem__(-1, ["7", "5", []])))
    yield C("jet_binomial_changed", lambda L: edit_record(L, lambda r: r.get("kind") == "jet" and len(r["terms"]) > 1,
        lambda r: r["terms"][1].__setitem__(0, str(int(r["terms"][1][0]) + 1))))
    yield C("variable_exponent_swapped", lambda L: edit_record(L, lambda r: r.get("type") == "variable" and r.get("id") == 1,
        lambda r: r.__setitem__("source_exponent", list(reversed(r["source_exponent"])))))
    yield C("variable_name_changed", lambda L: edit_record(L, lambda r: r.get("type") == "variable" and r.get("id") == 2,
        lambda r: r.__setitem__("name", r["name"] + "x")))
    yield C("footer_complete_false", lambda L: edit_record(L, lambda r: r.get("type") == "footer",
        lambda r: r.__setitem__("complete", False)))
    yield C("footer_removed", lambda L: L.pop(), resync=False)
    yield C("trailing_line_after_footer", lambda L: L.append(b'{"type":"note"}\n'))
    yield C("trailing_partial_bytes", lambda L: L.append(b"X"))
    if first_zero:
        yield C("zero_row_omitted", lambda L: L.__delitem__(find_index(L, lambda r: r.get("label") == first_zero)))
    yield C("last_physical_row_omitted", lambda L: L.__delitem__(
        max(i for i, l in enumerate(L) if json.loads(l).get("kind") == "physical_J")))
    yield C("header_field_changed", lambda L: edit_record(L, lambda r: r.get("type") == "header",
        lambda r: r.__setitem__("coefficient_field", "Fp")))

def sing_controls(base, first_zero):
    def idx_of_label(L, label):
        key = ("// " + label + "\n").encode()
        for i, l in enumerate(L):
            if l == key:
                return i
        raise RuntimeError("label absent")
    def C(name, mutate):
        def thunk():
            L = list(base); mutate(L); return L
        return name, thunk
    def flip(L):
        i = idx_of_label(L, "J_u0_v1") + 1
        need(L[i].startswith(b"("), "control target")
        L[i] = (b"(-" + L[i][1:]) if not L[i].startswith(b"(-") else (b"(" + L[i][2:])
    yield C("sing_sign_flip", flip)
    def drop_guard(L):
        i = idx_of_label(L, "original_degree_guard")
        del L[i:i + 2]
        L[i - 1] = L[i - 1][:-2] + b";\n"   # previous row now terminates the ideal
    yield C("sing_guard_removed", drop_guard)
    def drop_target(L):
        i = idx_of_label(L, "J_u0_v0") + 1
        atoms = L[i][:-2].decode().split("+")
        atoms = [a for a in atoms if "*" in a]
        L[i] = ("+".join(atoms) + L[i][-2:].decode()).encode()
    yield C("sing_target_removed", drop_target)
    def rename_ring(L):
        L[1] = L[1].replace(b"P_u0_v0,", b"P_u0_w0,", 1)
    yield C("sing_ring_variable_renamed", rename_ring)
    def swap_ring(L):
        head, rest = L[1].split(b"(", 1)
        body, tail = rest.split(b")", 1)
        names = body.split(b",")
        names[3], names[4] = names[4], names[3]
        L[1] = head + b"(" + b",".join(names) + b")" + tail
    yield C("sing_ring_order_swapped", swap_ring)
    def wrong_order_desc(L):
        L[1] = L[1].replace(b"),dp;", b"),lp;")
    yield C("sing_order_lp", wrong_order_desc)
    def drop_complete(L):
        i = next(i for i, l in enumerate(L) if l.startswith(b"// COMPLETE"))
        del L[i]
    yield C("sing_complete_marker_removed", drop_complete)
    def hidden_command(L):
        i = next(i for i, l in enumerate(L) if l == b"quit;\n")
        L.insert(i, b"ideal J=std(I);\n")
    yield C("sing_hidden_command_before_quit", hidden_command)
    def hidden_in_atom(L):
        i = idx_of_label(L, "J_u0_v1") + 1
        L[i] = L[i][:-2] + b"+(1/1)*P_u0_v1*Q_u1_v0;ideal J=std(I)" + L[i][-2:]
    yield C("sing_command_inside_polynomial", hidden_in_atom)
    yield C("sing_trailing_text", lambda L: L.append(b"std(I);\n"))
    if first_zero:
        def drop_zero(L):
            i = idx_of_label(L, first_zero)
            need(L[i + 1] == b"0,\n", "zero-row control shape")
            del L[i:i + 2]
        yield C("sing_zero_row_omitted", drop_zero)
    def poly_line_split(L):
        i = idx_of_label(L, "J_u0_v1") + 1
        L[i:i + 1] = [L[i][:-2] + b"\n", L[i][-2:]]
    yield C("sing_polynomial_line_split", poly_line_split)

# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--spec", choices=["d125", "toy"], required=True)
    ap.add_argument("--jsonl", required=True)
    ap.add_argument("--sing", required=True)
    ap.add_argument("--authority")
    ap.add_argument("--out", required=True)
    ap.add_argument("--as-bytes", type=int, default=8 * 1024 ** 3)
    ap.add_argument("--soft-deadline", type=float, default=480.0)
    ap.add_argument("--skip-controls", action="store_true")
    a = ap.parse_args()
    resource.setrlimit(resource.RLIMIT_AS, (a.as_bytes, a.as_bytes))
    t0 = time.monotonic()
    R = {"schema": "d125-full-stream-gate-fable5/independent-check/v1", "spec": a.spec,
         "checker_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
         "inputs": {}, "stages": {}, "json_controls": [], "sing_controls": [], "status": "RUNNING"}
    def flush():
        R["elapsed_seconds"] = time.monotonic() - t0
        R["max_rss_kib_self"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        with open(a.out, "w") as f:
            json.dump(R, f, indent=1, sort_keys=True); f.write("\n"); f.flush(); os.fsync(f.fileno())
    for path in (a.jsonl, a.sing):
        data = open(path, "rb").read()
        R["inputs"][path] = {"bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}
    auth = json.load(open(a.authority)) if a.authority else None
    if a.authority:
        R["inputs"][a.authority] = {"sha256": hashlib.sha256(open(a.authority, "rb").read()).hexdigest()}
    spec = D125_SPEC if a.spec == "d125" else TOY_SPEC
    try:
        E = Expected(spec, auth)
        R["stages"]["expected"] = {"source_counts": {s: len(E.S[s]) for s in ("P", "Q")}, "variable_count": E.nvar,
            "envelope": E.env_bounds, "expected_rows": sum(1 for _ in E.rows()),
            "authority_canonical_sha256": E.auth_sha, "seconds": time.monotonic() - t0}
        flush()
        json_lines = open(a.jsonl, "rb").read().splitlines(keepends=True)
        st = {}
        footer = verify_json(iter(json_lines), E, st)
        R["stages"]["json_whole_row"] = {"verdict": "PASS", "lines": len(json_lines), **st, "seconds": time.monotonic() - t0}
        flush()
        # validated JSON rows for the Singular comparison
        jrows = []
        for line in json_lines:
            obj = json.loads(line)
            if obj.get("type") == "row":
                jrows.append((obj["label"], [(t[0], t[1], tuple(t[2])) for t in obj["terms"]]))
        sing_lines = open(a.sing, "rb").read().splitlines(keepends=True)
        atoms = verify_sing(iter(sing_lines), jrows, E.names, st["prefix_sha256"])
        R["stages"]["singular_whole_row"] = {"verdict": "PASS", "lines": len(sing_lines), "atoms": atoms,
                                             "rows": len(jrows), "seconds": time.monotonic() - t0}
        flush()
        if not a.skip_controls:
            def built(name, thunk, bucket):
                try:
                    return thunk()
                except Exception as e:
                    bucket.append({"control": name, "result": "NOT_CONSTRUCTED", "reason": repr(e)[:120]}); flush()
                    return None
            for name, thunk in json_controls(json_lines, st["first_zero_physical_row"]):
                L = built(name, thunk, R["json_controls"])
                if L is None:
                    continue
                if time.monotonic() - t0 > a.soft_deadline:
                    R["json_controls"].append({"control": name, "result": "SKIPPED_SOFT_DEADLINE"}); continue
                try:
                    verify_json(iter(L), E, {})
                    R["json_controls"].append({"control": name, "result": "SURVIVED"})
                except Fail as e:
                    R["json_controls"].append({"control": name, "result": "REJECTED", "reason": str(e)})
                except Exception as e:
                    R["json_controls"].append({"control": name, "result": "REJECTED_EXC", "reason": repr(e)[:200]})
                flush()
            for name, thunk in sing_controls(sing_lines, st["first_zero_physical_row"]):
                L = built(name, thunk, R["sing_controls"])
                if L is None:
                    continue
                if time.monotonic() - t0 > a.soft_deadline:
                    R["sing_controls"].append({"control": name, "result": "SKIPPED_SOFT_DEADLINE"}); continue
                try:
                    verify_sing(iter(L), jrows, E.names, st["prefix_sha256"])
                    R["sing_controls"].append({"control": name, "result": "SURVIVED"})
                except Fail as e:
                    R["sing_controls"].append({"control": name, "result": "REJECTED", "reason": str(e)})
                except Exception as e:
                    R["sing_controls"].append({"control": name, "result": "REJECTED_EXC", "reason": repr(e)[:200]})
                flush()
        survived = [c["control"] for c in R["json_controls"] + R["sing_controls"] if c["result"] == "SURVIVED"]
        R["status"] = "PASS" if not survived else "CONTROL_SURVIVED"
        R["survived_controls"] = survived
    except Fail as e:
        R["status"] = "FAIL"; R["failure"] = str(e)
    flush()
    print(json.dumps({"status": R["status"], "failure": R.get("failure"), "elapsed": R["elapsed_seconds"]}))
    return 0 if R["status"] == "PASS" else 1

if __name__ == "__main__":
    sys.exit(main())
