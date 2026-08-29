#!/usr/bin/env python3
"""Compile exact next-Fitting minor/factor censuses from frozen r2 archives."""

from __future__ import annotations

import argparse
from collections import deque
import hashlib
import itertools
from pathlib import Path
import tarfile


ARCHIVES = {
    "c8": ("ec13fb990a35f0a3c02da2bcbbfb3a99b21a8f3cae180e3a712a5431a3802c02", 9, 75),
    "q1": ("15b91c08c47bb933ce5d9231bf602d09c8e4fd290d466e2fb8fb5d07599c3a4d", 6, 36),
    "p": ("b3f9024711176a00c62460179b526d25748ef6a0258b24af7788538cbb0737ec", 9, 75),
    "c8_q1": ("fc773ba8745876fc1d95dc39e44f298e34b2dbc2bdc2056ab561491828b3211c", 6, 36),
    "c8p02": ("3f2db20b34a94ee5b63669e1c20c46cb2c2e52cede3ee90d03708f282373bc8f", 9, 75),
    "q1p02": ("62731094b8c25128ca8f69682fcc9a23046f0c96a4981ed1f89896ccab4598b5", 6, 36),
    "q1p03": ("3ff39d779654e8f0726e6084c25f77151416f36dcfb6a927c667efcc56c6a8c0", 6, 36),
    "triple02": ("09ad7d9e39c15b3dd9bf760cee7b7de6a04ae2a36aecd8aa53efa0a864f62e33", 6, 36),
    "triple03": ("ed93f709c86430b490096a02179fac1b1320dd8b50917db00c95ccce858c248f", 6, 36),
}
LABELS = {"c8": "C8", "q1": "Q1", "p": "P", "c8_q1": "C8_Q1", "c8p02": "C8P02", "q1p02": "Q1P02", "q1p03": "Q1P03", "triple02": "TRIPLE02", "triple03": "TRIPLE03"}
A_ROWS = (4, 7, 9, 11)
A_COLS = (1, 2, 4, 6, 7, 8, 9, 10)
B_ROWS = (1, 2, 3, 5, 6, 8, 10)
B_COLS = (3, 5)


def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def member_bytes(tf: tarfile.TarFile, top: str, relative: str) -> bytes:
    extracted = tf.extractfile(f"{top}/{relative}")
    if extracted is None:
        raise SystemExit(f"ARCHIVE_MEMBER_NOT_FILE:{relative}")
    return extracted.read()


def verify_evidence(tf: tarfile.TarFile, top: str) -> None:
    for line in member_bytes(tf, top, "EVIDENCE.sha256").decode().splitlines():
        expected, remote = line.split(None, 1)
        marker = f"/{top}/"
        if marker not in remote:
            raise SystemExit("EVIDENCE_PATH_SCOPE_FAILURE")
        relative = remote.split(marker, 1)[1]
        if sha_bytes(member_bytes(tf, top, relative)) != expected:
            raise SystemExit(f"EVIDENCE_SHA_MISMATCH:{relative}")


def archive_payload(path: Path, component: str) -> tuple[str, list[list[str]], int]:
    expected_sha, expected_rank, expected_nonzero = ARCHIVES[component]
    if sha256(path) != expected_sha:
        raise SystemExit("TERMINAL_ARCHIVE_SHA_MISMATCH")
    with tarfile.open(path, "r:gz") as tf:
        top = tf.getnames()[0].split("/", 1)[0]
        verify_evidence(tf, top)
        result = member_bytes(tf, top, "output/COMPONENT_RESULT.tsv").decode().splitlines()[-1].split("|")
        if result[0] != component or result[2] != "EXACT_RESIDUAL_CENSUS" or int(result[6]) != expected_rank:
            raise SystemExit("COMPONENT_RESULT_DISAGREEMENT")
        compiled = member_bytes(tf, top, f"output/compiled/{component}.sing").decode()
        marker = "matrix M[106][105]="
        if compiled.count(marker) != 1:
            raise SystemExit("COMPILED_RING_PREFIX_DISAGREEMENT")
        header = compiled.split(marker, 1)[0]
        label = LABELS[component]
        residual = member_bytes(tf, top, f"output/run/{label}_RESIDUAL_MATRIX.tsv").decode().splitlines()
    if residual[0] != "rows|11|cols|10" or len(residual) != 111:
        raise SystemExit("RESIDUAL_SHAPE_DISAGREEMENT")
    matrix = [["0" for _ in range(10)] for _ in range(11)]
    seen: set[tuple[int, int]] = set()
    for line in residual[1:]:
        i_s, j_s, value = line.split("|", 2)
        i, j = int(i_s), int(j_s)
        if not (1 <= i <= 11 and 1 <= j <= 10) or (i, j) in seen:
            raise SystemExit("RESIDUAL_INDEX_DISAGREEMENT")
        seen.add((i, j)); matrix[i - 1][j - 1] = value.replace(" ", "")
    nonzero = sum(value != "0" for row in matrix for value in row)
    if len(seen) != 110 or nonzero != expected_nonzero:
        raise SystemExit("RESIDUAL_SUPPORT_DISAGREEMENT")
    return header, matrix, expected_rank


def matching(rows: tuple[int, ...], cols: tuple[int, ...], support: set[tuple[int, int]]) -> bool:
    match: dict[int, int] = {}
    def augment(row: int, visited: set[int]) -> bool:
        for col in cols:
            if (row, col) not in support or col in visited:
                continue
            visited.add(col)
            if col not in match or augment(match[col], visited):
                match[col] = row; return True
        return False
    return all(augment(row, set()) for row in rows)


def matrix_declaration(matrix: list[list[str]]) -> str:
    return "matrix R[11][10]=\n" + ",\n".join(value for row in matrix for value in row) + ";\n"


def factor_block(poly: str, index: str, raw_file: str, factor_file: str, gcd_name: str) -> list[str]:
    return [
        f'write({raw_file},"{index}|"+string({poly}));',
        f'if({poly}!=0){{ {gcd_name}=gcd({gcd_name},{poly}); list FF=factorize({poly}); write({factor_file},"{index}|"+string(FF)); kill FF; }}',
    ]


def rank9_script(header: str, matrix: list[list[str]], label: str) -> str:
    support = {(i + 1, j + 1) for i, row in enumerate(matrix) for j, value in enumerate(row) if value != "0"}
    row_sets = list(itertools.combinations(range(1, 12), 9))
    col_sets = list(itertools.combinations(range(1, 11), 9))
    structural = sum(matching(rows, cols, support) for rows in row_sets for cols in col_sets)
    if structural != 172:
        raise SystemExit("RANK9_STRUCTURAL_CENSUS_DISAGREEMENT")
    lines = [header, matrix_declaration(matrix), f'string RAWFILE="{label}_RAW_SIGNED_9X9_MINORS.tsv";', f'string FACFILE="{label}_RAW_9X9_FACTORS.tsv";', 'write(RAWFILE,"slot|rows|cols|polynomial");', 'write(FACFILE,"slot|factorize_literal");', 'int residual_rank=rank(R); if(residual_rank!=9){ print("FATAL_RESIDUAL_RANK_DISAGREEMENT"); quit; }', "poly RUNNING_GCD=0; int raw_slots=0; int algebraic_nonzero=0; int structural_matchable=0;"]
    slot = 0
    for rows in row_sets:
        for cols in col_sets:
            slot += 1
            entries = [f"R[{i},{j}]" for i in rows for j in cols]
            matchable = matching(rows, cols, support)
            lines.extend([
                f"matrix S[9][9]={','.join(entries)}; poly D=det(S); raw_slots=raw_slots+1;",
                f'write(RAWFILE,"{slot:04d}|{",".join(map(str, rows))}|{",".join(map(str, cols))}|"+string(D));',
                f"structural_matchable=structural_matchable+{int(matchable)};",
                'if(D!=0){ algebraic_nonzero=algebraic_nonzero+1; RUNNING_GCD=gcd(RUNNING_GCD,D); list FF=factorize(D); write(FACFILE,"'+f'{slot:04d}'+ '|"+string(FF)); kill FF; }',
                "kill S; kill D;",
            ])
    lines.extend([
        'write(FACFILE,"COMMON_GCD|"+string(RUNNING_GCD)); list GF=factorize(RUNNING_GCD); write(FACFILE,"COMMON_GCD_FACTORS|"+string(GF));',
        'print("RESIDUAL_RANK="+string(residual_rank));', 'print("RAW_MINOR_SLOT_COUNT="+string(raw_slots));',
        'print("STRUCTURALLY_MATCHABLE_SLOT_COUNT="+string(structural_matchable));', 'print("ALGEBRAIC_NONZERO_MINOR_COUNT="+string(algebraic_nonzero));',
        'print("RAW_MINOR_COMMON_GCD="+string(RUNNING_GCD));', 'if(raw_slots!=550 || structural_matchable!=172){ print("FATAL_RAW_SLOT_CENSUS"); quit; }',
        'print("MINOR_FACTOR_CENSUS_COMPLETE=1");', 'quit;', ''
    ])
    return "\n".join(lines)


def permutation_sign(categories: list[str]) -> int:
    inversions = sum(categories[i] == "B" and categories[j] == "A" for i in range(len(categories)) for j in range(i + 1, len(categories)))
    return -1 if inversions % 2 else 1


def rank6_script(header: str, matrix: list[list[str]], label: str, slot_path: Path) -> str:
    a_rows, a_cols, b_rows, b_cols = set(A_ROWS), set(A_COLS), set(B_ROWS), set(B_COLS)
    for i in range(1, 12):
        for j in range(1, 11):
            allowed = (i in a_rows and j in a_cols) or (i in b_rows and j in b_cols)
            if not allowed and matrix[i - 1][j - 1] != "0":
                raise SystemExit("RANK6_OFF_BLOCK_NONZERO")
    a_col_sets = list(itertools.combinations(A_COLS, 4))
    b_row_sets = list(itertools.combinations(B_ROWS, 2))
    a_index = {value: index for index, value in enumerate(a_col_sets, 1)}
    b_index = {value: index for index, value in enumerate(b_row_sets, 1)}
    candidates: list[tuple[int, int, int, int, tuple[int, ...], tuple[int, ...]]] = []
    slot_lines = ["slot|rows|cols|classification|sign|a_minor|b_minor"]
    slot = 0
    for rows in itertools.combinations(range(1, 12), 6):
        for cols in itertools.combinations(range(1, 11), 6):
            slot += 1
            a_cs = tuple(col for col in cols if col in a_cols)
            b_rs = tuple(row for row in rows if row in b_rows)
            is_candidate = a_rows.issubset(rows) and b_cols.issubset(cols) and len(a_cs) == 4 and len(b_rs) == 2
            if is_candidate:
                sign = permutation_sign(["A" if row in a_rows else "B" for row in rows]) * permutation_sign(["A" if col in a_cols else "B" for col in cols])
                ai, bi = a_index[a_cs], b_index[b_rs]
                candidates.append((slot, sign, ai, bi, rows, cols))
                slot_lines.append(f"{slot}|{','.join(map(str, rows))}|{','.join(map(str, cols))}|SIGNED_BLOCK_PRODUCT|{sign}|{ai}|{bi}")
            else:
                slot_lines.append(f"{slot}|{','.join(map(str, rows))}|{','.join(map(str, cols))}|STRUCTURAL_ZERO|0|0|0")
    if slot != 97020 or len(candidates) != 1470:
        raise SystemExit("RANK6_FORMAL_SLOT_CENSUS_DISAGREEMENT")
    slot_path.write_text("\n".join(slot_lines) + "\n")
    a_entries = [f"R[{i},{j}]" for i in A_ROWS for j in A_COLS]
    b_entries = [f"R[{i},{j}]" for i in B_ROWS for j in B_COLS]
    lines = [header, matrix_declaration(matrix), f"matrix BA[4][8]={','.join(a_entries)};", f"matrix BB[7][2]={','.join(b_entries)};", 'int offblock_nonzero=0;', f'string ARAW="{label}_RAW_SIGNED_4X4_BLOCK_A_MINORS.tsv";', f'string BRAW="{label}_RAW_SIGNED_2X2_BLOCK_B_MINORS.tsv";', f'string AFAC="{label}_RAW_4X4_BLOCK_A_FACTORS.tsv";', f'string BFAC="{label}_RAW_2X2_BLOCK_B_FACTORS.tsv";', f'string PRODUCTS="{label}_SIGNED_I6_CANDIDATE_PRODUCTS.tsv";', 'write(ARAW,"index|cols|polynomial"); write(BRAW,"index|rows|polynomial"); write(AFAC,"index|factorize_literal"); write(BFAC,"index|factorize_literal"); write(PRODUCTS,"slot|sign|a_minor|b_minor|polynomial");']
    for i in range(1, 12):
        for j in range(1, 11):
            if not ((i in a_rows and j in a_cols) or (i in b_rows and j in b_cols)):
                lines.append(f"if(R[{i},{j}]!=0){{ offblock_nonzero=offblock_nonzero+1; }}")
    lines.extend(['int rank_a=rank(BA); int rank_b=rank(BB); int residual_rank=rank(R);', 'if(offblock_nonzero!=0 || rank_a!=4 || rank_b!=2 || residual_rank!=6){ print("FATAL_BLOCK_OR_RANK_REPLAY"); quit; }', 'poly GCD_A=0; poly GCD_B=0;'])
    for ai, cols in enumerate(a_col_sets, 1):
        entries = [f"R[{i},{j}]" for i in A_ROWS for j in cols]
        name = f"DA{ai:02d}"
        lines.extend([f"matrix SA[4][4]={','.join(entries)}; poly {name}=det(SA);", f'write(ARAW,"{ai:02d}|{",".join(map(str, cols))}|"+string({name}));', f'if({name}!=0){{ GCD_A=gcd(GCD_A,{name}); list FF=factorize({name}); write(AFAC,"{ai:02d}|"+string(FF)); kill FF; }}', "kill SA;"])
    for bi, rows in enumerate(b_row_sets, 1):
        entries = [f"R[{i},{j}]" for i in rows for j in B_COLS]
        name = f"DB{bi:02d}"
        lines.extend([f"matrix SB[2][2]={','.join(entries)}; poly {name}=det(SB);", f'write(BRAW,"{bi:02d}|{",".join(map(str, rows))}|"+string({name}));', f'if({name}!=0){{ GCD_B=gcd(GCD_B,{name}); list FF=factorize({name}); write(BFAC,"{bi:02d}|"+string(FF)); kill FF; }}', "kill SB;"])
    for formal_slot, sign, ai, bi, _, _ in candidates:
        sign_prefix = "-" if sign < 0 else ""
        lines.append(f'write(PRODUCTS,"{formal_slot}|{sign}|{ai}|{bi}|"+string({sign_prefix}DA{ai:02d}*DB{bi:02d}));')
    lines.extend(['write(AFAC,"COMMON_GCD|"+string(GCD_A)); write(BFAC,"COMMON_GCD|"+string(GCD_B));', 'list GFA=factorize(GCD_A); list GFB=factorize(GCD_B); write(AFAC,"COMMON_GCD_FACTORS|"+string(GFA)); write(BFAC,"COMMON_GCD_FACTORS|"+string(GFB));', 'print("RESIDUAL_RANK="+string(residual_rank)); print("BLOCK_A_RANK="+string(rank_a)); print("BLOCK_B_RANK="+string(rank_b)); print("OFFBLOCK_NONZERO="+string(offblock_nonzero));', 'print("BLOCK_A_RAW_MINOR_COUNT=70"); print("BLOCK_B_RAW_MINOR_COUNT=21"); print("FORMAL_I6_SLOT_COUNT=97020"); print("FORMAL_I6_STRUCTURAL_ZERO_COUNT=95550"); print("FORMAL_I6_SIGNED_PRODUCT_COUNT=1470");', 'print("BLOCK_A_COMMON_GCD="+string(GCD_A)); print("BLOCK_B_COMMON_GCD="+string(GCD_B)); print("BLOCK_FITTING_IDENTITY_REPLAY=1"); print("MINOR_FACTOR_CENSUS_COMPLETE=1"); quit;', ''])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--component", choices=sorted(ARCHIVES), required=True)
    parser.add_argument("--archive", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    header, matrix, rank = archive_payload(args.archive, args.component)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    label = LABELS[args.component]
    slot_path = args.output_dir / f"{label}_FORMAL_I6_SLOTS.tsv"
    if rank == 9:
        content = rank9_script(header, matrix, label)
    else:
        content = rank6_script(header, matrix, label, slot_path)
    script_path = args.output_dir / f"{args.component}_minors.sing"
    script_path.write_text(content)
    parse = content.split("string RAWFILE=", 1)[0] if rank == 9 else content.split("int offblock_nonzero=", 1)[0]
    (args.output_dir / f"{args.component}_parse.sing").write_text(parse + f'print("MINOR_MATRIX_PARSE_PASS={label}");\nquit;\n')
    (args.output_dir / "BUILD_MANIFEST.tsv").write_text(f"component|label|rank|archive_sha256|script_sha256\n{args.component}|{label}|{rank}|{sha256(args.archive)}|{sha_bytes(content.encode())}\n")
    print(f"COMPONENT={args.component}"); print(f"LABEL={label}"); print(f"RESIDUAL_RANK={rank}"); print("TERMINAL_EVIDENCE_REPLAY_PASS=1"); print("MINOR_CENSUS_BUILD_PASS")


if __name__ == "__main__":
    main()

