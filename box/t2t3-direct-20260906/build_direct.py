#!/usr/bin/env python3
"""Build the exact semantic T2+T3 presentations without circuit variables.

The earlier audited presentation adjoined one variable for each arithmetic
circuit node.  Every such row was ``X-expression`` with coefficient +1 and
only earlier graph variables in ``expression``.  This driver evaluates that
acyclic graph in the frozen source-coordinate ring and emits only the images
of the constraint rows.  It does *not* pivot any constraint variable.

All arithmetic is exact over Q (python-flint).  Each nonzero row is made
primitive integral once, then written from the same term iterator to an
exact-Q Singular input and to an aliased prime-field msolve input.  The
variable-independent canonical stream hash is custody that the two files
carry identical generators before coefficient reduction modulo p.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import resource
import time
from collections import Counter
from pathlib import Path

from flint import fmpq_mpoly, fmpq_mpoly_ctx


ROOT = Path(__file__).resolve().parents[2]
TERM = re.compile(r"^\((.*)\)\*tt\^(\d+)\*zz\^(\d+)$")
SITE = re.compile(r"_(\d+)_(\d+)$")
EXPECTED = {
    "99-delta2": {
        "input": ROOT / "box/char-degree-20260905/active-gauge/inputs/delta2_stage8.strongest.json",
        "input_sha256": "778eda933ee9b2acbad20f6dc862c25db94776cb25ffd5782646427a3b63e1ea",
        "semantic_count": 449,
        "semantic_sha256": "ee778e93b4293b9399761911d80dd71dd63b5fa95d21055cf50cd0db51428a4b",
        "k": 33, "D2": 55, "n2": 3, "D3": 145,
        "t2z": 40, "t2p": 15, "t3z": 105, "t3p": 40,
        "sep": "rho", "zsep": "Zrho", "lam2": "leader55", "zlam2": "Z55",
        "recurrence": ["t3eq", "t3_fq"],
        "raw_counts": {"T2_upper": 462, "T2_strict": 1263, "T2_face": 56,
                       "T3_recurrence": 1, "T3_strict": 2539,
                       "T3_face": 146, "inverse": 3},
        "nonzero_counts": {"T2_upper": 462, "T2_strict": 1263, "T2_face": 17,
                           "T3_recurrence": 1, "T3_strict": 962,
                           "T3_face": 46, "inverse": 3},
    },
    "99-delta52": {
        "input": ROOT / "box/char-degree-20260905/active-gauge/inputs/delta52_stage8.strongest.json",
        "input_sha256": "3f81dc99770d235099249a818a55b19f0c828d36109e30aa738995177f97dc46",
        "semantic_count": 447,
        "semantic_sha256": "20c0e973211f3417eca0284e725cbbc46f5ba698257a05f87e08cedff038fd9c",
        "k": 33, "D2": 55, "n2": 3, "D3": 145,
        "t2z": 40, "t2p": 15, "t3z": 105, "t3p": 40,
        "sep": "c", "zsep": "Zc", "lam2": "leader55", "zlam2": "Z55",
        "recurrence": ["t3eq", "t3_fq"],
        "raw_counts": {"T2_upper": 462, "T2_strict": 1263, "T2_face": 56,
                       "T3_recurrence": 1, "T3_strict": 2539,
                       "T3_face": 146, "inverse": 3},
        "nonzero_counts": {"T2_upper": 462, "T2_strict": 1263, "T2_face": 17,
                           "T3_recurrence": 1, "T3_strict": 962,
                           "T3_face": 46, "inverse": 3},
    },
    "108-free-mean": {
        "input": ROOT / "box/char-degree-20260905/d108/selected/meanfree_stage8_slimgb/d108_meanfree_stage8_strongfront.input.json",
        "input_sha256": "1c927d83aa4684ae91bfffc8d03500fbabb73a500faa222fa349a6d129a10814",
        "semantic_count": 507,
        "semantic_sha256": "4c8952648ab814be891a76e4b0fc8b2f650ccf0689ebfba882a96ac2a83f1ad4",
        "k": 36, "D2": 63, "n2": 4, "D3": 227,
        "t2z": 49, "t2p": 14, "t3z": 176, "t3p": 51,
        "sep": "c", "zsep": "Zc", "lam2": "leader63", "zlam2": "Z63",
        "recurrence": ["t3eq", "t3_fgq", "t3_fq2"],
        "raw_counts": {"source_residual": 14, "T2_upper": 461,
                       "T2_strict": 1128, "T2_face": 64,
                       "T3_recurrence": 1, "T3_strict": 5123,
                       "T3_face": 228, "inverse": 3},
        "nonzero_counts": {"source_residual": 14, "T2_upper": 461,
                           "T2_strict": 1128, "T2_face": 16,
                           "T3_recurrence": 1, "T3_strict": 1514,
                           "T3_face": 59, "inverse": 3},
    },
}


def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha_path(path: Path) -> str:
    return sha_bytes(path.read_bytes())


def seq_sha(values) -> str:
    digest = hashlib.sha256()
    for value in values:
        digest.update(str(value).encode())
        digest.update(b"\n")
    return digest.hexdigest()


def split_top(text: str):
    pieces = []
    start = depth = 0
    for index, character in enumerate(text):
        if character == "(":
            depth += 1
        elif character == ")":
            depth -= 1
            if depth < 0:
                raise ValueError("unbalanced source expression")
        elif character == "+" and depth == 0:
            pieces.append(text[start:index])
            start = index + 1
    if depth:
        raise ValueError("unbalanced source expression")
    pieces.append(text[start:])
    return [piece for piece in pieces if piece]


class DirectChart:
    PRIME = 1073741827
    MSOLVE_OFFSET_LIMIT = 2**31 - 1

    def __init__(self, tag: str, output: Path):
        self.started = time.monotonic()
        self.tag = tag
        self.spec = EXPECTED[tag]
        staged_input = Path(__file__).resolve().parent / "inputs" / self.spec["input"].name
        self.input = staged_input if staged_input.is_file() else self.spec["input"]
        if sha_path(self.input) != self.spec["input_sha256"]:
            raise RuntimeError("frozen source input SHA-256 mismatch")
        self.data = json.loads(self.input.read_text())
        self.output = output.resolve()
        self.output.mkdir(parents=True, exist_ok=True)
        if any(self.output.iterdir()):
            raise RuntimeError("output directory must be empty")

        if tag.startswith("99-"):
            expected_branch = "delta2" if tag.endswith("delta2") else "delta52"
            assert self.data["branch"] == expected_branch
            assert self.data["stage"] == 8 and self.data["field"] == "Q"
            assert self.data["residual_rows"] == []
            frozen_names = list(self.data["full_free_coordinates"])
            self.residuals = [value for _, value in self.data["residual_rows"]]
        else:
            assert self.data["k"] == 36 and self.data["target"] == 63
            frozen_names = list(self.data["names"])
            self.residuals = list(self.data["residual_strings"])

        semantic = sorted(set(frozen_names) | {self.spec["zsep"]})
        semantic += self.spec["recurrence"] + ["lambda3", "Z3"]
        assert len(semantic) == len(set(semantic)) == self.spec["semantic_count"]
        assert seq_sha(semantic) == self.spec["semantic_sha256"]
        self.semantic_names = semantic
        self.inverse_names = [self.spec["zlam2"], self.spec["zsep"], "Z3"]
        assert len(set(self.inverse_names)) == 3
        assert all(name in semantic for name in self.inverse_names)
        self.names = [name for name in semantic if name not in self.inverse_names]
        self.names += self.inverse_names
        self.aliases = [f"v{i}" for i in range(len(self.names))]
        self.index = {name: i for i, name in enumerate(self.names)}
        self.alias = dict(zip(self.names, self.aliases))
        self.ctx = fmpq_mpoly_ctx.get(tuple(self.names), ordering="degrevlex")
        self.gens = list(self.ctx.gens())
        self.zero = self.ctx.constant(0)
        self.one = self.ctx.constant(1)

        self.k = self.spec["k"]
        self.D2 = self.spec["D2"]
        self.n2 = self.spec["n2"]
        self.D3 = self.spec["D3"]
        self.defect = self.n2 * self.D2 - self.D3
        self.lead = 6 * self.k - 2 - self.D2
        self.qcap = self.lead + self.defect

        self.sites = [self.site(name) for name in self.names]
        assert all(r > 0 for r, _ in self.sites[:-3])
        assert self.sites[-3:] == [(0, 0)] * 3
        self.noninverse_count = len(self.names) - 3
        self.order_matrix, self.order_minor = self.make_order_matrix()

        self.raw_counts = Counter()
        self.zero_counts = Counter()
        self.emitted_counts = Counter()
        self.raw_label_sha = hashlib.sha256()
        self.emitted_label_sha = hashlib.sha256()
        self.canonical_sha = hashlib.sha256()
        self.generator_text_sha = hashlib.sha256()
        self.total_terms = 0
        self.max_terms = (0, "")
        self.max_total_degree = 0
        self.homogeneous_pair_count = 0
        self.nonhomogeneous_pair_count = 0
        self.nonhomogeneous_examples = []

        self.sing_path = self.output / f"{tag}.sing"
        self.ms_path = self.output / f"{tag}.ms"
        self.labels_path = self.output / f"{tag}.labels.tsv"
        self.variables_path = self.output / f"{tag}.variables.json"
        self.meta_path = self.output / f"{tag}.build.json"
        self.sing = self.sing_path.open("w", buffering=1024 * 1024)
        self.ms = self.ms_path.open("w", buffering=1024 * 1024)
        self.labels = self.labels_path.open("w", buffering=1024 * 1024)
        self.row_count = 0
        self.write_headers()

    def C(self, value):
        if isinstance(value, fmpq_mpoly):
            return value
        if isinstance(value, int):
            return self.ctx.constant(value)
        return fmpq_mpoly(str(value).replace("**", "^"), ctx=self.ctx)

    def var(self, name: str):
        return self.gens[self.index[name]]

    @staticmethod
    def add(*tables):
        out = {}
        for table, scalar in tables:
            for pos, value in table.items():
                term = value * scalar
                out[pos] = term if pos not in out else out[pos] + term
                if not out[pos]:
                    del out[pos]
        return out

    def shift(self, table, dr=0, dz=0, scalar=1, cap=None):
        scalar = self.C(scalar)
        return {
            (r + dr, z + dz): value * scalar
            for (r, z), value in table.items()
            if cap is None or r + dr <= cap
        }

    def mul(self, left, right, cap=None):
        out = {}
        for (r, z), a in left.items():
            for (s, w), b in right.items():
                if cap is not None and r + s > cap:
                    continue
                pos = (r + s, z + w)
                term = a * b
                out[pos] = term if pos not in out else out[pos] + term
                if not out[pos]:
                    del out[pos]
        return out

    def power(self, table, exponent, cap=None):
        answer = {(0, 0): self.one}
        base = table
        power = exponent
        while power:
            if power & 1:
                answer = self.mul(answer, base, cap)
            power //= 2
            if power:
                base = self.mul(base, base, cap)
        return answer

    @staticmethod
    def support_mul(left, right, cap=None):
        out = set()
        for r, z in left:
            for s, w in right:
                if cap is None or r + s <= cap:
                    out.add((r + s, z + w))
        return out

    def coefficient_mul(self, left, right, position):
        """One coefficient of a series product, with immediate cancellation."""
        target_r, target_z = position
        answer = self.zero
        # Iterate the smaller support; dictionary lookup avoids a full product
        # table and, critically, combines the six Q* summands coefficientwise.
        if len(left) > len(right):
            left, right = right, left
        for (r, z), value in left.items():
            mate = right.get((target_r - r, target_z - z))
            if mate is not None:
                answer += value * mate
        return answer

    @staticmethod
    def shifted_support(support, dr=0, dz=0, cap=None):
        return {
            (r + dr, z + dz) for r, z in support
            if cap is None or r + dr <= cap
        }

    def map_table(self, rows):
        out = {}
        for r, z, expression in rows:
            pos = (int(r), int(z))
            assert pos not in out
            value = self.C(expression)
            if value:
                out[pos] = value
        return out

    def string_table(self, text):
        out = {}
        for piece in split_top(text):
            match = TERM.fullmatch(piece)
            if not match:
                raise ValueError("unparsed normalized term: " + piece[:180])
            expression, r, z = match.groups()
            pos = (int(r), int(z))
            assert pos not in out
            value = self.C(expression)
            if value:
                out[pos] = value
        return out

    def source_series(self):
        if self.tag.startswith("99-"):
            maps = self.data["maps"]
            assert {"h3", "C2", "C3", "B2", "A3"} <= set(maps)
            h3 = self.map_table(maps["h3"])
            c2 = self.map_table(maps["C2"])
            c3 = self.map_table(maps["C3"])
            h = self.add((self.power(h3, 3), 1), (self.mul(c2, h3), 1), (c3, 1))
            D = self.map_table(maps["B2"])
            C = self.map_table(maps["A3"])
            assert (len(h), len(D), len(C)) == (178, 194, 201)
            expected = {24 + i: self.ctx.constant(math.comb(9, i)) for i in range(10)}
        else:
            h = self.string_table(self.data["h_expr"])
            D = self.string_table(self.data["D_expr"])
            C = self.string_table(self.data["C_expr"])
            assert (len(h), len(D), len(C)) == (185, 191, 197)
            expected = {28 + i: self.ctx.constant(math.comb(8, i)) for i in range(9)}
        actual = {z: value for (r, z), value in h.items() if r == 0}
        assert actual == expected
        return h, D, C

    def site(self, name: str):
        if name in self.inverse_names:
            return (0, 0)
        match = SITE.search(name)
        if match:
            return (int(match.group(1)), int(match.group(2)))
        if name == "E82":
            return (8, 2)
        targets = {
            "target_b": self.k, "target_a": 2 * self.k,
            "target_c": 3 * self.k, "target_d": 4 * self.k,
            "target_e": 6 * self.k,
        }
        if name in targets:
            return (targets[name], 0)
        if name == self.spec["lam2"]:
            return (self.lead + 2, self.D2)
        if name == "lambda3":
            return (self.n2 * (self.lead + 2) + self.defect, self.D3)
        if name == "t3eq":
            return (self.n2 * (self.lead + 2), 0)
        if name == "t3_fq":
            return (11, 0)
        if name == "t3_fgq":
            return (9, 0)
        if name == "t3_fq2":
            return (18, 0)
        conventions = {
            "u": (2, 0), "v": (1, 0), "rho": (3, 0), "c": (2, 0),
            "minor_a2": (3, 0), "minor_mean": (1, 0),
            "jet0": (1, 0), "jet1": (2, 0), "jet2": (3, 0),
        }
        return conventions.get(name, (1, 0))

    def make_order_matrix(self):
        """Two site rows followed by an identity completion.

        The matrix acts only on noninverse variables.  Its first two rows are
        r and z.  Every r is positive, so the block is global.  Omitting two
        identity rows at columns with a nonzero 2x2 site minor makes the square
        matrix full rank.  The three inverse variables form a final dp block.
        """
        n = self.noninverse_count
        rrow = [self.sites[i][0] for i in range(n)]
        zrow = [self.sites[i][1] for i in range(n)]
        omitted = None
        determinant = 0
        for i in range(n):
            for j in range(i + 1, n):
                determinant = rrow[i] * zrow[j] - rrow[j] * zrow[i]
                if determinant:
                    omitted = (i, j)
                    break
            if omitted:
                break
        if omitted is None:
            raise RuntimeError("site vectors have rank below two")
        rows = [rrow, zrow]
        for column in range(n):
            if column in omitted:
                continue
            row = [0] * n
            row[column] = 1
            rows.append(row)
        assert len(rows) == n
        flat = [entry for row in rows for entry in row]
        return flat, {
            "columns": [self.names[i] for i in omitted],
            "indices": list(omitted),
            "determinant": determinant,
        }

    def write_headers(self):
        n = self.noninverse_count
        matrix_text = ",".join(str(value) for value in self.order_matrix)
        self.sing.write(
            f"ring R=0,({','.join(self.names)}),(M({matrix_text}),dp(3));\n"
            "option(redSB);\n"
            "ideal I=\n"
        )
        self.ms.write(",".join(self.aliases) + "\n")
        self.ms.write(str(self.PRIME) + "\n")
        self.labels.write("emitted_index\tblock\tlabel\tterms\tprimitive_sha256\n")
        assert len(self.order_matrix) == n * n

    def raw_row(self, block: str, label: str, polynomial):
        self.raw_counts[block] += 1
        self.raw_label_sha.update(label.encode())
        self.raw_label_sha.update(b"\n")
        polynomial = self.C(polynomial)
        if not polynomial:
            self.zero_counts[block] += 1
            return
        self.emit_row(block, label, polynomial)

    def emit_row(self, block: str, label: str, polynomial):
        terms_count = len(polynomial)
        assert terms_count > 0
        denominator = 1
        first_pair = None
        pair_homogeneous = True
        total_degree = 0
        for monomial, coefficient in polynomial.terms():
            denominator = math.lcm(denominator, int(coefficient.denominator))
            rcharge = sum(exp * self.sites[i][0] for i, exp in enumerate(monomial) if exp)
            zcharge = sum(exp * self.sites[i][1] for i, exp in enumerate(monomial) if exp)
            pair = (rcharge, zcharge)
            if first_pair is None:
                first_pair = pair
            elif pair != first_pair:
                pair_homogeneous = False
            total_degree = max(total_degree, sum(monomial))
        common = 0
        first_integer = None
        for _, coefficient in polynomial.terms():
            integer = int(coefficient * denominator)
            if first_integer is None:
                first_integer = integer
            common = math.gcd(common, abs(integer))
        assert first_integer and common
        sign_scale = -1 if first_integer < 0 else 1

        if self.row_count:
            self.sing.write(",\n")
            self.ms.write(",\n")
        row_sha = hashlib.sha256()
        self.canonical_sha.update(b"GENERATOR\n")
        first = True
        for monomial, coefficient in polynomial.terms():
            integer = sign_scale * (int(coefficient * denominator) // common)
            assert integer
            sign = "-" if integer < 0 else ("" if first else "+")
            if integer > 0 and not first:
                sign = "+"
            magnitude = abs(integer)
            original_factors = []
            alias_factors = []
            support = []
            for index, exponent in enumerate(monomial):
                if not exponent:
                    continue
                support.append(f"{index}^{exponent}")
                if exponent == 1:
                    original_factors.append(self.names[index])
                    alias_factors.append(self.aliases[index])
                else:
                    original_factors.append(f"{self.names[index]}^{exponent}")
                    alias_factors.append(f"{self.aliases[index]}^{exponent}")
            original_body = "*".join(original_factors) or "1"
            alias_body = "*".join(alias_factors) or "1"
            if magnitude != 1:
                original_body = f"{magnitude}*{original_body}"
                alias_body = f"{magnitude}*{alias_body}"
            original_piece = sign + original_body
            alias_piece = sign + alias_body
            self.sing.write(original_piece)
            self.ms.write(alias_piece)
            encoded = original_piece.encode()
            self.generator_text_sha.update(encoded)
            row_sha.update(encoded)
            self.canonical_sha.update(f"{integer}:{','.join(support)}\n".encode())
            first = False
        self.generator_text_sha.update(b"\n")
        self.canonical_sha.update(b"END\n")

        self.row_count += 1
        self.emitted_counts[block] += 1
        self.emitted_label_sha.update(label.encode())
        self.emitted_label_sha.update(b"\n")
        self.total_terms += terms_count
        self.max_terms = max(self.max_terms, (terms_count, label))
        self.max_total_degree = max(self.max_total_degree, total_degree)
        if pair_homogeneous:
            self.homogeneous_pair_count += 1
        else:
            self.nonhomogeneous_pair_count += 1
            if len(self.nonhomogeneous_examples) < 8:
                self.nonhomogeneous_examples.append(label)
        self.labels.write(
            f"{self.row_count - 1}\t{block}\t{label}\t{terms_count}\t{row_sha.hexdigest()}\n"
        )
        if self.row_count % 100 == 0:
            print(
                f"EMIT_PROGRESS case={self.tag} rows={self.row_count} terms={self.total_terms} "
                f"block={block} rssKiB={resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}",
                flush=True,
            )

    def build(self):
        h, D, C = self.source_series()
        a, b, c, d = [self.var("target_" + letter) for letter in "abcd"]
        H = self.add((h, 1), ({(self.k, 0): b}, -self.C("1/6")))
        v = self.add(
            (D, 1),
            ({(2 * self.k - 1, 0): a / 3 + b * b / 18}, 1),
        )
        V = self.add(
            (C, 1),
            (self.shift(D, self.k), -b / 4),
            ({(3 * self.k - 1, 0): a * b / 12 + b**3 / 54 - c / 2}, 1),
        )
        assert min(r for r, _ in V) >= 1
        U = self.shift(V, -1, scalar=self.C("8/3"))
        Rraw = self.add((self.mul(v, v), 1), (self.mul(U, H), -1))
        print(
            f"BUILD_PROGRESS case={self.tag} phase=R support={len(Rraw)} "
            f"rssKiB={resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}", flush=True,
        )
        Rlow = {}
        for (r, z), value in sorted(Rraw.items()):
            if z >= self.k:
                self.raw_row("T2_upper", f"T2_Rhigh_{r}_{z}", value)
            else:
                Rlow[(r, z)] = value

        for index, expression in enumerate(self.residuals):
            self.raw_row("source_residual", f"source_residual_{index}", self.C(expression))

        HH = self.mul(H, H, self.qcap - min(r for r, _ in Rlow))
        vU = self.mul(v, U, self.qcap - 1)
        pp = d + b * c / 2 - (a + b * b / 4) ** 2 / 3
        support_RHH = self.support_mul(Rlow, HH, self.qcap)
        support_vUH = self.support_mul(vU, H, self.qcap - 1)
        support_vR = self.support_mul(v, Rlow, self.qcap - 1)
        support_UU = self.support_mul(U, U, self.qcap - 2)
        q_support = set(support_RHH)
        q_support |= self.shifted_support(support_vUH, 1, cap=self.qcap)
        q_support |= self.shifted_support(support_vR, 1, cap=self.qcap)
        q_support |= self.shifted_support(support_UU, 2, cap=self.qcap)
        q_support |= self.shifted_support(HH, 4 * self.k - 2, cap=self.qcap)
        q_support |= self.shifted_support(v, 4 * self.k - 1, cap=self.qcap)
        need = q_support | {(self.lead, z) for z in range(self.D2 + 1)}
        Qjet = {}
        for r, z in sorted(need):
            value = self.zero
            if (r, z) in support_RHH:
                value += self.coefficient_mul(Rlow, HH, (r, z)) * self.C("3/4")
            if (r - 1, z) in support_vUH:
                value += self.coefficient_mul(vU, H, (r - 1, z)) * self.C("-1/8")
            if (r - 1, z) in support_vR:
                value += self.coefficient_mul(v, Rlow, (r - 1, z))
            if (r - 2, z) in support_UU:
                value += self.coefficient_mul(U, U, (r - 2, z)) * self.C("-9/64")
            value += HH.get((r - (4 * self.k - 2), z), self.zero) * pp
            value += v.get((r - (4 * self.k - 1), z), self.zero) * pp
            if r < self.lead:
                self.raw_row("T2_strict", f"T2_strict_{r}_{z}", value)
                continue
            delta = r - self.lead
            if value:
                Qjet[(delta, z)] = value
            if delta == 0:
                if self.spec["t2z"] <= z <= self.D2:
                    target = math.comb(self.spec["t2p"], z - self.spec["t2z"]) * self.var(self.spec["lam2"])
                else:
                    target = self.zero
                self.raw_row("T2_face", f"T2_face_{z}", value - target)
            elif z > self.D2 - delta:
                self.raw_row("T2_support", f"T2_support_{delta}_{z}", value)
        print(
            f"BUILD_PROGRESS case={self.tag} phase=Q support={len(q_support)} jet={len(Qjet)} "
            f"rows={self.row_count} terms={self.total_terms} "
            f"rssKiB={resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}", flush=True,
        )

        ht = {pos: value for pos, value in h.items() if pos[0] <= self.defect}
        F = self.mul(self.mul(ht, ht, self.defect), ht, self.defect)
        G = self.mul(ht, ht, self.defect)
        Qsq = self.mul(Qjet, Qjet, self.defect)
        if self.n2 == 3:
            FG = self.mul(F, G, self.defect)
            FQ = self.mul(F, Qjet, self.defect - 11)
            T3 = self.add(
                (self.mul(Qsq, Qjet, self.defect), 1),
                (FG, self.var("t3eq")),
                (self.shift(FQ, 11, scalar=self.var("t3_fq")), 1),
            )
        else:
            Qfour = self.mul(Qsq, Qsq, self.defect)
            Gsq = self.mul(G, G, self.defect)
            FG2 = self.mul(F, Gsq, self.defect)
            FG = self.mul(F, G, self.defect - 9)
            FGQ = self.mul(FG, Qjet, self.defect - 9)
            FQ2 = self.mul(F, Qsq, self.defect - 18)
            T3 = self.add(
                (Qfour, 1),
                (FG2, self.var("t3eq")),
                (self.shift(FGQ, 9, scalar=self.var("t3_fgq")), 1),
                (self.shift(FQ2, 18, scalar=self.var("t3_fq2")), 1),
            )
        self.raw_row(
            "T3_recurrence", "T3_equality_coefficient",
            self.var("t3eq") + self.var(self.spec["lam2"]) ** self.n2,
        )
        for (r, z), value in sorted(T3.items()):
            if r < self.defect:
                self.raw_row("T3_strict", f"T3_strict_{r}_{z}", value)
        face_z = set(range(self.D3 + 1)) | {z for (r, z) in T3 if r == self.defect}
        for z in sorted(face_z):
            value = T3.get((self.defect, z), self.zero)
            if self.spec["t3z"] <= z <= self.D3:
                target = math.comb(self.spec["t3p"], z - self.spec["t3z"]) * self.var("lambda3")
            else:
                target = self.zero
            self.raw_row("T3_face", f"T3_face_{z}", value - target)
        self.raw_row("inverse", "inverse_T2", self.var(self.spec["zlam2"]) * self.var(self.spec["lam2"]) - 1)
        self.raw_row("inverse", "inverse_T3", self.var("Z3") * self.var("lambda3") - 1)
        self.raw_row("inverse", "inverse_separation", self.var(self.spec["zsep"]) * self.var(self.spec["sep"]) - 1)
        print(
            f"BUILD_PROGRESS case={self.tag} phase=T3 support={len(T3)} "
            f"rows={self.row_count} terms={self.total_terms} "
            f"rssKiB={resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}", flush=True,
        )
        self.finish(h, D, C, q_support, Qjet, F, G, T3)

    def finish(self, h, D, C, Q, Qjet, F, G, T3):
        actual_raw = {key: self.raw_counts[key] for key in self.spec["raw_counts"]}
        actual_nonzero = {key: self.emitted_counts[key] for key in self.spec["nonzero_counts"]}
        assert actual_raw == self.spec["raw_counts"], (actual_raw, self.spec["raw_counts"])
        assert self.raw_counts["T2_support"] == 0
        assert actual_nonzero == self.spec["nonzero_counts"], (actual_nonzero, self.spec["nonzero_counts"])
        assert self.row_count == sum(self.spec["nonzero_counts"].values())
        msolve_offset_safe = self.total_terms * len(self.names) < self.MSOLVE_OFFSET_LIMIT

        self.sing.write(
            ";\n"
            'print("ALL_ROWS_PARSED");\n'
            'print("BEGIN_STD");\n'
            "ideal G=std(I);\n"
            'print("END_STD");\n'
            'print("BEGIN_RESULT");\n'
            'print("REDUCE_ONE="+string(reduce(1,G)));\n'
            'print("DIMENSION="+string(dim(G)));\n'
            'print("BASIS_SIZE="+string(size(G)));\n'
            'print("END_RESULT");\n'
            "quit;\n"
        )
        self.ms.write("\n")
        self.sing.close()
        self.ms.close()
        self.labels.close()

        variable_records = [
            {
                "solver_index": i, "semantic_index": self.semantic_names.index(name),
                "name": name, "alias": self.aliases[i], "site_r": self.sites[i][0],
                "site_z": self.sites[i][1], "inverse_dp_block": i >= self.noninverse_count,
            }
            for i, name in enumerate(self.names)
        ]
        variable_payload = {
            "schema": "T2T3_DIRECT_VARIABLE_MAP/v1",
            "case": self.tag,
            "semantic_order": self.semantic_names,
            "solver_order": self.names,
            "records": variable_records,
        }
        self.variables_path.write_text(json.dumps(variable_payload, indent=2, sort_keys=True) + "\n")

        site_r = [r for r, _ in self.sites]
        site_z = [z for _, z in self.sites]
        meta = {
            "schema": "T2T3_DIRECT_BUILD/v1",
            "status": "EMITTED_EXACT_Q_AND_MODULAR_NOT_RUN",
            "case": self.tag,
            "field": "Q",
            "modular_prime": self.PRIME,
            "input": str(self.input.relative_to(ROOT)),
            "input_sha256": sha_path(self.input),
            "semantic_variable_count": len(self.semantic_names),
            "semantic_variable_order_sha256": seq_sha(self.semantic_names),
            "solver_variable_count": len(self.names),
            "solver_variable_order_sha256": seq_sha(self.names),
            "alias_order_sha256": seq_sha(self.aliases),
            "variable_map_file": self.variables_path.name,
            "variable_map_sha256": sha_path(self.variables_path),
            "inverse_dp_block": self.inverse_names,
            "order": {
                "singular": f"(M(two-site {self.noninverse_count}x{self.noninverse_count}),dp(3))",
                "classification": "global two-site matrix filtration; normalized ideal is not homogeneous",
                "first_row": "source/assigned t-depth r",
                "second_row": "source/assigned z-index",
                "identity_completion_omits": self.order_minor,
                "site_r_sha256": seq_sha(site_r),
                "site_z_sha256": seq_sha(site_z),
                "matrix_flat_sha256": seq_sha(self.order_matrix),
                "matrix_entries": len(self.order_matrix),
                "homogeneous_generator_count_under_site_pair": self.homogeneous_pair_count,
                "nonhomogeneous_generator_count_under_site_pair": self.nonhomogeneous_pair_count,
                "nonhomogeneous_examples": self.nonhomogeneous_examples,
                "warning": "The frozen data supply no preserved bigrading after beta=1, binomial faces, and localizers; these two vectors define only the requested computational weight order.",
            },
            "arithmetic": {
                "k": self.k, "D2": self.D2, "n2": self.n2,
                "D3": self.D3, "defect": self.defect,
                "T2_H_adic_lead": self.lead, "T2_physical_lead": self.lead + 2,
                "qcap": self.qcap,
            },
            "source_residual_count": len(self.residuals),
            "source_maps_composed_into_semantic_ring": True,
            "source_support_rows_preserved_via_frozen_affine_map": True,
            "graph_variables_emitted": 0,
            "constraint_variables_pivoted": 0,
            "raw_row_counts": dict(sorted(self.raw_counts.items())),
            "identically_zero_after_substitution": dict(sorted(self.zero_counts.items())),
            "emitted_nonzero_counts": dict(sorted(self.emitted_counts.items())),
            "raw_row_count": sum(self.raw_counts.values()),
            "emitted_generator_count": self.row_count,
            "raw_row_labels_sha256": self.raw_label_sha.hexdigest(),
            "emitted_row_labels_sha256": self.emitted_label_sha.hexdigest(),
            "canonical_primitive_generator_sequence_sha256": self.canonical_sha.hexdigest(),
            "original_name_generator_text_sha256": self.generator_text_sha.hexdigest(),
            "expanded_term_count": self.total_terms,
            "msolve_32bit_offset_product": self.total_terms * len(self.names),
            "msolve_32bit_offset_guard": self.MSOLVE_OFFSET_LIMIT,
            "msolve_32bit_offset_safe": msolve_offset_safe,
            "maximum_generator_terms": self.max_terms[0],
            "maximum_generator_label": self.max_terms[1],
            "maximum_total_degree": self.max_total_degree,
            "series_support": {"h": len(h), "D": len(D), "C": len(C), "Q": len(Q),
                               "Qjet": len(Qjet), "F": len(F), "G": len(G), "T3": len(T3)},
            "T2_target": f"{self.spec['lam2']}*z^{self.spec['t2z']}*(1+z)^{self.spec['t2p']}",
            "T3_target": f"lambda3*z^{self.spec['t3z']}*(1+z)^{self.spec['t3p']}",
            "localizers": [f"{self.spec['zlam2']}*{self.spec['lam2']}-1",
                           "Z3*lambda3-1", f"{self.spec['zsep']}*{self.spec['sep']}-1"],
            "T3_equality": f"t3eq+{self.spec['lam2']}^{self.n2}",
            "no_t_or_z_series_variables": True,
            "no_Jacobian_variable_or_tail_rows": True,
            "no_saturation": True,
            "primitive_integer_rows": True,
            "singular_file": self.sing_path.name,
            "singular_file_bytes": self.sing_path.stat().st_size,
            "singular_file_sha256": sha_path(self.sing_path),
            "msolve_file": self.ms_path.name,
            "msolve_file_bytes": self.ms_path.stat().st_size,
            "msolve_file_sha256": sha_path(self.ms_path),
            "labels_file": self.labels_path.name,
            "labels_file_sha256": sha_path(self.labels_path),
            "driver_sha256": sha_path(Path(__file__)),
            "build_wall_seconds": round(time.monotonic() - self.started, 3),
            "peak_RSS_KiB": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        }
        # python-flint exposes exponent sums as fmpz values.  They are exact
        # Python-int equivalents, but the stdlib JSON encoder does not know
        # that scalar type.
        self.meta_path.write_text(
            json.dumps(meta, indent=2, sort_keys=True, default=int) + "\n"
        )
        print(json.dumps(meta, indent=2, sort_keys=True, default=int), flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--case", required=True, choices=sorted(EXPECTED))
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    DirectChart(args.case, args.output).build()


if __name__ == "__main__":
    main()
