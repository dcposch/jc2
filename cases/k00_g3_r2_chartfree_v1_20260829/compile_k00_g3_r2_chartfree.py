#!/usr/bin/env python3
"""Build the exact desk-scale K00 grade-three rank-two obstruction packet."""

from __future__ import annotations

import argparse
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path
import re
import shutil
import subprocess


CASE_REL = "cases/k00_g3_r2_chartfree_v1_20260829"
ATLAS_REL = (
    "cases/max12_812_order2_u2_62_k00_grade7_fitting_atlas_v26_20260827/"
    "aws_box02_r2_held_compile/output/ATLAS_EXACT_POLYNOMIALS.json"
)
V27_BASIS_REL = (
    "cases/max12_812_order2_u2_62_k00_rank_compressed_atlas_v27_20260827/"
    "aws_r6a_r2_exact_base3/output/BASE3_R2_STANDARD_BASIS.txt"
)
V27_REVIEW_REL = "xmodel/k00-v27-base4-base3-base2-hostile-review-fable5-20260827.md"
DISCOVERY_REL = "xmodel/k00-chartfree-next-sol56-20260829.md"

PINNED = {
    ATLAS_REL: "d7ec6d18d58265421ff315fa00e38cd32992ac12f7d8166cf6c436e23bf06501",
    V27_BASIS_REL: "c8aa23e46f909e70c2c8d302ca67a415496df9a969f99817d2ef593f60f614c0",
    V27_REVIEW_REL: "738f46030a73fea2a06a8e3139ed9aa5e2001b72a579e459357af81f6801647a",
    DISCOVERY_REL: "ac843e4c3da54a60d96f8b15961f1d75ffb45ca7ebef1664d44c755fffb25d76",
}

BASIS_COMMIT = "92ebe92ad5986a47f01af9ed901260595dfed869"
STATUS = "PASS_K00_G3_R2_CHARTFREE_OBSTRUCTED_PRODUCER_EXPLICIT_CERTIFICATES"
EXPECTED_PRIOR = tuple(
    [f"d{i}_{j}" for i in range(6) for j in range(1, 6)]
    + ["k10_0", "k10_1", "k10_2"]
)
LEADING = tuple(f"d{i}_1" for i in range(6))
SECOND = tuple(f"d{i}_2" for i in range(6))
NEWEST = tuple([f"d{i}_6" for i in range(6)] + ["k10_3"])
DIAGNOSTIC = re.compile(r"(?mi)^\s*\?|// \*\*|warning|error occurred|K00_G3_FAIL=")


def fail(message: object) -> "None":
    raise RuntimeError(message)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def text_digest(value: str) -> str:
    return sha256((value.strip() + "\n").encode()).hexdigest()


def poly(item: object) -> str:
    if not isinstance(item, dict):
        fail("polynomial record is not an object")
    value = item.get("singular")
    if not isinstance(value, str) or not value:
        fail("missing exact Singular polynomial")
    return value


def determinant(matrix: str, rows: tuple[int, ...], cols: tuple[int, ...]) -> str:
    if len(rows) == 2 and len(cols) == 2:
        a, b = rows
        c, d = cols
        return f"({matrix}[{a},{c}]*{matrix}[{b},{d}]-{matrix}[{a},{d}]*{matrix}[{b},{c}])"
    if len(rows) == 3 and len(cols) == 3:
        a, b, c = rows
        i, j, k = cols
        return (
            f"({matrix}[{a},{i}]*{matrix}[{b},{j}]*{matrix}[{c},{k}]"
            f"+{matrix}[{a},{j}]*{matrix}[{b},{k}]*{matrix}[{c},{i}]"
            f"+{matrix}[{a},{k}]*{matrix}[{b},{i}]*{matrix}[{c},{j}]"
            f"-{matrix}[{a},{k}]*{matrix}[{b},{j}]*{matrix}[{c},{i}]"
            f"-{matrix}[{a},{j}]*{matrix}[{b},{i}]*{matrix}[{c},{k}]"
            f"-{matrix}[{a},{i}]*{matrix}[{b},{k}]*{matrix}[{c},{j}])"
        )
    fail(("unsupported determinant shape", rows, cols))


def assignments(name: str, matrix: str, rank: int) -> tuple[list[str], list[dict]]:
    lines = [f"ideal {name};"]
    labels: list[dict] = []
    index = 0
    for rows in combinations(range(1, 8), rank):
        for cols in combinations(range(1, 8), rank):
            index += 1
            lines.append(f"{name}[{index}]={determinant(matrix, rows, cols)};")
            labels.append({
                "literal_index": index,
                "rows_one_based": list(rows),
                "columns_one_based": list(cols),
            })
    expected = 441 if rank == 2 else 1225
    if index != expected:
        fail(("literal determinant census mismatch", name, index, expected))
    return lines, labels


def validate_inputs(root: Path) -> tuple[dict, list[dict], list[dict], list[dict]]:
    for relative, expected in PINNED.items():
        path = root / relative
        if not path.is_file() or digest(path) != expected:
            fail(("pinned input mismatch", relative))
    atlas = json.loads((root / ATLAS_REL).read_text())
    if tuple(atlas.get("ring_variables", ())) != EXPECTED_PRIOR:
        fail("prior ring variable order mismatch")
    if tuple(atlas.get("honest_newest_variables", ())) != NEWEST:
        fail("newest-variable order mismatch")
    matrix = atlas.get("A")
    if not isinstance(matrix, list) or len(matrix) != 7 or any(
        not isinstance(row, list) or len(row) != 7 for row in matrix
    ):
        fail("A shape mismatch")
    literal = atlas.get("P6_literal_rows_through_grade6")
    if not isinstance(literal, list) or len(literal) != 49:
        fail("literal prior-row census mismatch")
    p3 = [item for item in literal if item.get("Lambda_grade") == 3]
    if len(p3) != 7 or [item.get("row") for item in p3] != list(range(1, 8)):
        fail("grade-three source-label mismatch")
    p3_polys = [item.get("poly") for item in p3]
    nonzero = atlas.get("P6_nonzero_generators_plus_F10")
    if not isinstance(nonzero, list) or p3_polys != nonzero[6:13]:
        fail("grade-three labelled rows differ from frozen nonzero slice")
    b = list(atlas.get("Q1_to_Q6", ())) + [atlas.get("F10")]
    if len(b) != 7 or any(poly(item) == "0" for item in b):
        fail("B source mismatch")
    for row in matrix:
        for item in row:
            poly(item)
    for item in p3_polys + b:
        poly(item)
    return atlas, p3, p3_polys, b


def common_source(atlas: dict, p3_polys: list[dict], b: list[dict]) -> tuple[list[str], dict]:
    i3a_lines, i3a_labels = assignments("I3ALIT", "A0", 3)
    i3e_lines, i3e_labels = assignments("I3ELIT", "E3", 3)
    i3em_lines, _ = assignments("I3EMUTLIT", "E3M", 3)
    i2_lines, i2_labels = assignments("I2LIT", "A0", 2)
    ring = ",".join(EXPECTED_PRIOR)
    matrix_a = ",".join(f"({poly(item)})" for row in atlas["A"] for item in row)
    zero_images: list[str] = []
    for name in EXPECTED_PRIOR:
        zero_images.append(name if name in LEADING else "0")
    lines = [
        f"ring R=0,({ring}),dp;",
        f"matrix A[7][7]={matrix_a};",
        "ideal B=" + ",".join(f"({poly(item)})" for item in b) + ";",
        "ideal P3=" + ",".join(f"({poly(item)})" for item in p3_polys) + ";",
        "matrix C[7][6]; int i; int j; int k; int secondbad=0; int affinebad=0; poly cc; poly rr;",
        (
            "for (i=1;i<=7;i++) { for (j=1;j<=6;j++) { "
            "C[i,j]=diff(P3[i],var(2+5*(j-1))); "
            "for (k=1;k<=6;k++) { if (diff(C[i,j],var(2+5*(k-1)))!=0) { secondbad++; } } "
            "} cc=P3[i]; for (j=1;j<=6;j++) { cc=subst(cc,var(2+5*(j-1)),0); } "
            "rr=P3[i]-cc; for (j=1;j<=6;j++) { rr=rr-C[i,j]*var(2+5*(j-1)); } "
            "if (rr!=0) { affinebad++; } }"
        ),
        "ring S=0,(" + ",".join(LEADING) + "),dp;",
        "map zero=R," + ",".join(zero_images) + ";",
        "matrix A0=zero(A); matrix C0=zero(C); ideal B0=zero(B); ideal c3=zero(P3);",
        "int mismatch=0; for (i=1;i<=7;i++) { for (j=1;j<=6;j++) { if (C0[i,j]!=A0[i,j]) { mismatch++; } } }",
        "matrix E3[7][7]; for (i=1;i<=7;i++) { for (j=1;j<=6;j++) { E3[i,j]=C0[i,j]; } E3[i,7]=c3[i]; }",
    ]
    lines.extend(i3a_lines)
    lines.extend(i3e_lines)
    lines.extend(i2_lines)
    lines.extend([
        "if ((ncols(I3ALIT)!=1225)||(ncols(I3ELIT)!=1225)||(ncols(I2LIT)!=441)) { print(\"K00_G3_FAIL=LITERAL_NCOLS\"); quit; }",
        "if ((size(I3ALIT)!=813)||(size(I3ELIT)!=813)||(size(I2LIT)!=351)) { print(\"K00_G3_FAIL=LITERAL_NONZERO_CENSUS\"); quit; }",
        "ideal Hraw; for (i=1;i<=7;i++) { Hraw[i]=B0[i]; }",
        "for (i=1;i<=1225;i++) { Hraw[7+i]=I3ALIT[i]; Hraw[1232+i]=I3ELIT[i]; }",
        "if ((ncols(Hraw)!=2457)||(size(Hraw)!=1633)) { print(\"K00_G3_FAIL=HRAW_CENSUS\"); quit; }",
        "string i3aidx=\"\"; string i3eidx=\"\"; string i2idx=\"\"; int i3anz=0; int i3enz=0; int i2nz=0;",
        "for (i=1;i<=1225;i++) { if (I3ALIT[i]!=0) { i3anz++; i3aidx=i3aidx+string(i)+\",\"; } if (I3ELIT[i]!=0) { i3enz++; i3eidx=i3eidx+string(i)+\",\"; } }",
        "ideal Q4; for (i=1;i<=441;i++) { if (I2LIT[i]!=0) { i2nz++; i2idx=i2idx+string(i)+\",\"; Q4[i2nz]=I2LIT[i]^4; } }",
        "if ((i3anz!=813)||(i3enz!=813)||(i2nz!=351)||(ncols(Q4)!=351)) { print(\"K00_G3_FAIL=NONZERO_LABEL_MAP\"); quit; }",
        "matrix CM=C0; CM[1,1]=CM[1,1]+1; int cmismatch=0; for (i=1;i<=7;i++){for(j=1;j<=6;j++){if(CM[i,j]!=A0[i,j]){cmismatch++;}}}",
        "matrix E3M=E3; E3M[1,7]=E3M[1,7]+d5_1^3;",
    ])
    lines.extend(i3em_lines)
    lines.extend([
        "int c3changed=0; int c3first=0; for(i=1;i<=1225;i++){if(I3EMUTLIT[i]!=I3ELIT[i]){c3changed++;if(c3first==0){c3first=i;}}}",
    ])
    label_seed = {
        "i3a": i3a_labels,
        "i3e": i3e_labels,
        "i2a": i2_labels,
    }
    return lines, label_seed


def count_matrix_nonzero_lines(prefix: str, matrix: str) -> list[str]:
    return [
        f"int {prefix}=0;",
        f"for(i=1;i<=nrows({matrix});i++){{for(j=1;j<=ncols({matrix});j++){{if({matrix}[i,j]!=0){{{prefix}++;}}}}}}",
    ]


def producer_source(common: list[str]) -> str:
    lines = list(common)
    lines.extend([
        "matrix TH; ideal GH=liftstd(Hraw,TH);",
        "matrix HR=matrix(Hraw)*TH-matrix(GH); int hresbad=0; for(i=1;i<=nrows(HR);i++){for(j=1;j<=ncols(HR);j++){if(HR[i,j]!=0){hresbad++;}}}",
        "ideal HFRESH=std(Hraw); ideal GHMOD=reduce(GH,HFRESH); ideal HFMOD=reduce(HFRESH,GH); int basisbad=0; for(i=1;i<=ncols(GHMOD);i++){if(GHMOD[i]!=0){basisbad++;}} for(i=1;i<=ncols(HFMOD);i++){if(HFMOD[i]!=0){basisbad++;}}",
        "if ((hresbad!=0)||(basisbad!=0)||(reduce(1,GH)!=1)||(dim(GH)!=2)||(ncols(GH)!=20)) { print(\"K00_G3_FAIL=TRACKED_H_BASIS\"); quit; }",
        "matrix CQ=lift(GH,Q4); matrix QR=matrix(GH)*CQ-matrix(Q4); int qresbad=0; for(i=1;i<=nrows(QR);i++){for(j=1;j<=ncols(QR);j++){if(QR[i,j]!=0){qresbad++;}}}",
        "if (qresbad!=0) { print(\"K00_G3_FAIL=Q4_CERTIFICATES\"); quit; }",
        "int unresolved; int u1=0; int u2=0; int u3=0; int u4=0;",
        "for(i=1;i<=441;i++){if(I2LIT[i]!=0){if(reduce(I2LIT[i],GH)!=0){u1++;}if(reduce(I2LIT[i]^2,GH)!=0){u2++;}if(reduce(I2LIT[i]^3,GH)!=0){u3++;}if(reduce(I2LIT[i]^4,GH)!=0){u4++;}}}",
        "if ((u1!=291)||(u2!=60)||(u3!=36)||(u4!=0)) { print(\"K00_G3_FAIL=POWER_PROFILE\"); quit; }",
        "int thri=0; int thci=0; for(i=1;i<=nrows(TH);i++){for(j=1;j<=ncols(TH);j++){if((thri==0)&&(TH[i,j]!=0)){thri=i;thci=j;}}}",
        "matrix THM=TH; THM[thri,thci]=THM[thri,thci]+1; matrix THMR=matrix(Hraw)*THM-matrix(GH); int thmutbad=0; for(i=1;i<=nrows(THMR);i++){for(j=1;j<=ncols(THMR);j++){if(THMR[i,j]!=0){thmutbad++;}}}",
        "int cqri=0; int cqci=0; for(i=1;i<=nrows(CQ);i++){for(j=1;j<=ncols(CQ);j++){if((cqri==0)&&(CQ[i,j]!=0)){cqri=i;cqci=j;}}}",
        "matrix CQM=CQ; CQM[cqri,cqci]=CQM[cqri,cqci]+1; matrix CQMR=matrix(GH)*CQM-matrix(Q4); int cqmutbad=0; for(i=1;i<=nrows(CQMR);i++){for(j=1;j<=ncols(CQMR);j++){if(CQMR[i,j]!=0){cqmutbad++;}}}",
        "ideal Q4M=Q4; Q4M[1]=Q4M[1]+1; matrix QTMR=matrix(GH)*CQ-matrix(Q4M); int qtmutbad=0; for(i=1;i<=nrows(QTMR);i++){for(j=1;j<=ncols(QTMR);j++){if(QTMR[i,j]!=0){qtmutbad++;}}}",
        "ideal HUNIT=Hraw,1; ideal KNOWN=d0_1; if ((thmutbad==0)||(cqmutbad==0)||(qtmutbad==0)||(cmismatch==0)||(c3changed==0)||(reduce(1,std(HUNIT))!=0)||(reduce(1,std(KNOWN))==0)) { print(\"K00_G3_FAIL=MUTATION_OR_CONTROL\"); quit; }",
    ])
    lines.extend(count_matrix_nonzero_lines("thnz", "TH"))
    lines.extend(count_matrix_nonzero_lines("cqnz", "CQ"))
    lines.extend([
        f'print("K00_G3_R2_CHARTFREE={STATUS}");',
        'print("SECOND_DERIVATIVE_BAD="+string(secondbad));',
        'print("AFFINE_RECONSTRUCTION_BAD="+string(affinebad));',
        'print("C_A_MISMATCH="+string(mismatch));',
        'print("I3A_NONZERO="+string(i3anz)); print("I3E_NONZERO="+string(i3enz)); print("I2_NONZERO="+string(i2nz));',
        'print("HRAW_NCOLS="+string(ncols(Hraw))); print("HRAW_SIZE="+string(size(Hraw)));',
        'print("H_BASIS_NCOLS="+string(ncols(GH))); print("H_DIM="+string(dim(GH)));',
        'print("POWER_PROFILE="+string(u1)+","+string(u2)+","+string(u3)+","+string(u4));',
        'print("TH_SHAPE="+string(nrows(TH))+"x"+string(ncols(TH))); print("TH_NONZERO="+string(thnz));',
        'print("CQ_SHAPE="+string(nrows(CQ))+"x"+string(ncols(CQ))); print("CQ_NONZERO="+string(cqnz));',
        'print("C3_MUTATION_CHANGED="+string(c3changed)); print("C3_MUTATION_FIRST="+string(c3first));',
        'print("TH_MUTATION="+string(thri)+","+string(thci)); print("CQ_MUTATION="+string(cqri)+","+string(cqci));',
        'print("I3A_NONZERO_LITERAL_INDICES="+i3aidx); print("I3E_NONZERO_LITERAL_INDICES="+i3eidx); print("I2_NONZERO_LITERAL_INDICES="+i2idx);',
        'print("BEGIN_H_BASIS"); print(string(GH)); print("END_H_BASIS");',
        'print("BEGIN_HRAW_TO_H"); print(string(TH)); print("END_HRAW_TO_H");',
        'print("BEGIN_H_TO_Q4"); print(string(CQ)); print("END_H_TO_Q4");',
        "quit;",
    ])
    return "\n".join(lines) + "\n"


def extract_section(stdout: str, name: str) -> str:
    start = f"BEGIN_{name}\n"
    end = f"\nEND_{name}\n"
    if stdout.count(start) != 1 or stdout.count(end) != 1:
        fail(("missing or duplicate producer section", name))
    payload = stdout.split(start, 1)[1].split(end, 1)[0].strip()
    if not payload:
        fail(("empty producer section", name))
    return payload + "\n"


def marker(stdout: str, name: str) -> str:
    found = re.findall(rf"(?m)^{re.escape(name)}=(.*)$", stdout)
    if len(found) != 1:
        fail(("missing or duplicate marker", name, len(found)))
    return found[0].strip()


def parse_indices(value: str, expected: int) -> list[int]:
    if not value.endswith(","):
        fail("nonzero-index marker lacks terminal comma")
    parts = value[:-1].split(",") if value[:-1] else []
    result = [int(item) for item in parts]
    if len(result) != expected or result != sorted(set(result)):
        fail(("nonzero-index map mismatch", len(result), expected))
    return result


def run_singular(executable: str, script: Path) -> tuple[str, str]:
    completed = subprocess.run(
        [executable, "-q", str(script)],
        cwd=script.parent,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=60,
    )
    if completed.returncode or completed.stderr or not completed.stdout.strip() or DIAGNOSTIC.search(completed.stdout):
        fail(("Singular failure", script.name, completed.returncode, completed.stderr[-2000:], completed.stdout[-4000:]))
    return completed.stdout, completed.stderr


def replay_source(
    common: list[str], basis: str, transform: str, qcert: str, expected_indices: dict[str, str]
) -> str:
    lines = list(common)
    lines.extend([
        f"ideal GH={basis.strip()}; ideal GHCERT=std(GH);",
        f"matrix TH[2457][20]={transform.strip()};",
        f"matrix CQ[20][351]={qcert.strip()};",
        "if ((i3aidx!=\"" + expected_indices["i3a"] + "\")||(i3eidx!=\"" + expected_indices["i3e"] + "\")||(i2idx!=\"" + expected_indices["i2"] + "\")) { print(\"K00_G3_FAIL=REPLAY_LABEL_MAP\"); quit; }",
        "matrix HR=matrix(Hraw)*TH-matrix(GH); int hresbad=0; for(i=1;i<=nrows(HR);i++){for(j=1;j<=ncols(HR);j++){if(HR[i,j]!=0){hresbad++;}}}",
        "matrix QR=matrix(GH)*CQ-matrix(Q4); int qresbad=0; for(i=1;i<=nrows(QR);i++){for(j=1;j<=ncols(QR);j++){if(QR[i,j]!=0){qresbad++;}}}",
        "ideal HFRESH=std(Hraw); ideal GHMOD=reduce(GHCERT,HFRESH); ideal HFMOD=reduce(HFRESH,GHCERT); int basisbad=0; for(i=1;i<=ncols(GHMOD);i++){if(GHMOD[i]!=0){basisbad++;}} for(i=1;i<=ncols(HFMOD);i++){if(HFMOD[i]!=0){basisbad++;}}",
        "int u1=0; int u2=0; int u3=0; int u4=0; for(i=1;i<=441;i++){if(I2LIT[i]!=0){if(reduce(I2LIT[i],GHCERT)!=0){u1++;}if(reduce(I2LIT[i]^2,GHCERT)!=0){u2++;}if(reduce(I2LIT[i]^3,GHCERT)!=0){u3++;}if(reduce(I2LIT[i]^4,GHCERT)!=0){u4++;}}}",
        "int thri=0; int thci=0; for(i=1;i<=nrows(TH);i++){for(j=1;j<=ncols(TH);j++){if((thri==0)&&(TH[i,j]!=0)){thri=i;thci=j;}}} matrix THM=TH; THM[thri,thci]=THM[thri,thci]+1; matrix THMR=matrix(Hraw)*THM-matrix(GH); int thmutbad=0; for(i=1;i<=nrows(THMR);i++){for(j=1;j<=ncols(THMR);j++){if(THMR[i,j]!=0){thmutbad++;}}}",
        "int cqri=0; int cqci=0; for(i=1;i<=nrows(CQ);i++){for(j=1;j<=ncols(CQ);j++){if((cqri==0)&&(CQ[i,j]!=0)){cqri=i;cqci=j;}}} matrix CQM=CQ; CQM[cqri,cqci]=CQM[cqri,cqci]+1; matrix CQMR=matrix(GH)*CQM-matrix(Q4); int cqmutbad=0; for(i=1;i<=nrows(CQMR);i++){for(j=1;j<=ncols(CQMR);j++){if(CQMR[i,j]!=0){cqmutbad++;}}}",
        "ideal Q4M=Q4; Q4M[1]=Q4M[1]+1; matrix QTMR=matrix(GH)*CQ-matrix(Q4M); int qtmutbad=0; for(i=1;i<=nrows(QTMR);i++){for(j=1;j<=ncols(QTMR);j++){if(QTMR[i,j]!=0){qtmutbad++;}}}",
        "ideal HUNIT=Hraw,1; ideal KNOWN=d0_1; if ((secondbad!=0)||(affinebad!=0)||(mismatch!=0)||(hresbad!=0)||(qresbad!=0)||(basisbad!=0)||(u1!=291)||(u2!=60)||(u3!=36)||(u4!=0)||(thmutbad==0)||(cqmutbad==0)||(qtmutbad==0)||(cmismatch==0)||(c3changed==0)||(reduce(1,GHCERT)!=1)||(dim(GHCERT)!=2)||(reduce(1,std(HUNIT))!=0)||(reduce(1,std(KNOWN))==0)) { print(\"K00_G3_FAIL=REPLAY_EXACT_CHECK\"); quit; }",
        f'print("K00_G3_R2_CHARTFREE_REPLAY={STATUS}");',
        'print("REPLAY_AFFINE=0,0,0"); print("REPLAY_CENSUS=2457,1633,351"); print("REPLAY_POWER_PROFILE=291,60,36,0"); print("REPLAY_CERTIFICATES=EXACT_TWO_STAGE"); print("REPLAY_MUTATIONS=PASS");',
        "quit;",
    ])
    return "\n".join(lines) + "\n"


def build_labels(
    atlas: dict,
    p3: list[dict],
    b: list[dict],
    seed: dict,
    nonzero: dict[str, list[int]],
) -> dict:
    for key in ("i3a", "i3e", "i2a"):
        nz = set(nonzero[key])
        for item in seed[key]:
            item["zero"] = item["literal_index"] not in nz
    qcolumn = {literal: column for column, literal in enumerate(nonzero["i2a"], 1)}
    for item in seed["i2a"]:
        item["q4_certificate_column"] = qcolumn.get(item["literal_index"])
    hraw = {
        "B": [
            {
                "raw_h_index": index,
                "name": f"B{index}",
                "singular_text_sha256": text_digest(poly(item)),
            }
            for index, item in enumerate(b, 1)
        ],
        "I3A": [],
        "I3E3": [],
    }
    for item in seed["i3a"]:
        item["raw_h_index"] = 7 + item["literal_index"]
        hraw["I3A"].append(item)
    for item in seed["i3e"]:
        item["raw_h_index"] = 1232 + item["literal_index"]
        hraw["I3E3"].append(item)
    return {
        "format": "K00-G3-R2-CHARTFREE-LABELS/v1",
        "basis_commit": BASIS_COMMIT,
        "ring_variables": list(EXPECTED_PRIOR),
        "leading_variables": list(LEADING),
        "second_shell_variables": list(SECOND),
        "newest_variables_for_A": list(NEWEST),
        "A_entries": [
            {
                "row": row + 1,
                "column": col + 1,
                "newest_variable": NEWEST[col],
                "singular_text_sha256": text_digest(poly(atlas["A"][row][col])),
            }
            for row in range(7)
            for col in range(7)
        ],
        "P3_rows": [
            {
                "Lambda_grade": item["Lambda_grade"],
                "row": item["row"],
                "singular_text_sha256": text_digest(poly(item["poly"])),
            }
            for item in p3
        ],
        "Hraw": hraw,
        "I2A": seed["i2a"],
        "ordering": {
            "literal_minors": "lexicographic row subset then lexicographic column subset",
            "Hraw": "B1..B7, 1225 literal I3(A), 1225 literal I3(E3)",
            "q4_columns": "nonzero literal I2(A) in increasing literal_index",
        },
        "counts": {
            "Hraw_ncols": 2457,
            "Hraw_nonzero": 1633,
            "I3A_literal": 1225,
            "I3A_nonzero": 813,
            "I3E3_literal": 1225,
            "I3E3_nonzero": 813,
            "I2A_literal": 441,
            "I2A_nonzero": 351,
            "I2A_zero": 90,
        },
    }


def write_manifest(output: Path) -> None:
    members = sorted(path for path in output.iterdir() if path.name != "MANIFEST.sha256")
    lines = [f"{digest(path)}  {path.name}" for path in members]
    (output / "MANIFEST.sha256").write_text("\n".join(lines) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    output = args.output.resolve()
    if output.exists():
        fail(("output already exists", str(output)))
    singular = shutil.which("Singular")
    if singular is None:
        fail("Singular is unavailable")
    atlas, p3, p3_polys, b = validate_inputs(root)
    common, label_seed = common_source(atlas, p3_polys, b)
    output.mkdir(parents=True, exist_ok=False)
    producer = output / "producer.sing"
    producer.write_text(producer_source(common))
    stdout, stderr = run_singular(singular, producer)
    (output / "producer.stdout").write_text(stdout)
    (output / "producer.stderr").write_text(stderr)
    if marker(stdout, "K00_G3_R2_CHARTFREE") != STATUS:
        fail("producer status mismatch")
    expected_markers = {
        "SECOND_DERIVATIVE_BAD": "0",
        "AFFINE_RECONSTRUCTION_BAD": "0",
        "C_A_MISMATCH": "0",
        "I3A_NONZERO": "813",
        "I3E_NONZERO": "813",
        "I2_NONZERO": "351",
        "HRAW_NCOLS": "2457",
        "HRAW_SIZE": "1633",
        "H_BASIS_NCOLS": "20",
        "H_DIM": "2",
        "POWER_PROFILE": "291,60,36,0",
        "TH_SHAPE": "2457x20",
        "TH_NONZERO": "123",
        "CQ_SHAPE": "20x351",
        "CQ_NONZERO": "2434",
    }
    for name, expected in expected_markers.items():
        actual = marker(stdout, name)
        if actual != expected:
            fail(("producer marker mismatch", name, actual, expected))
    index_text = {
        "i3a": marker(stdout, "I3A_NONZERO_LITERAL_INDICES"),
        "i3e": marker(stdout, "I3E_NONZERO_LITERAL_INDICES"),
        "i2": marker(stdout, "I2_NONZERO_LITERAL_INDICES"),
    }
    nonzero = {
        "i3a": parse_indices(index_text["i3a"], 813),
        "i3e": parse_indices(index_text["i3e"], 813),
        "i2a": parse_indices(index_text["i2"], 351),
    }
    basis = extract_section(stdout, "H_BASIS")
    transform = extract_section(stdout, "HRAW_TO_H")
    qcert = extract_section(stdout, "H_TO_Q4")
    (output / "H_BASIS.txt").write_text(basis)
    (output / "HRAW_TO_H.matrix").write_text(transform)
    (output / "H_TO_Q4.matrix").write_text(qcert)
    (output / "I2_NONZERO_LITERAL_INDICES.txt").write_text(index_text["i2"] + "\n")
    labels = build_labels(atlas, p3, b, label_seed, nonzero)
    (output / "SOURCE_LABELS.json").write_text(
        json.dumps(labels, sort_keys=True, indent=2) + "\n"
    )
    replay = output / "replay.sing"
    replay.write_text(replay_source(common, basis, transform, qcert, index_text))
    replay_stdout, replay_stderr = run_singular(singular, replay)
    (output / "replay.stdout").write_text(replay_stdout)
    (output / "replay.stderr").write_text(replay_stderr)
    if marker(replay_stdout, "K00_G3_R2_CHARTFREE_REPLAY") != STATUS:
        fail("replay status mismatch")
    required_replay = {
        "REPLAY_AFFINE": "0,0,0",
        "REPLAY_CENSUS": "2457,1633,351",
        "REPLAY_POWER_PROFILE": "291,60,36,0",
        "REPLAY_CERTIFICATES": "EXACT_TWO_STAGE",
        "REPLAY_MUTATIONS": "PASS",
    }
    for name, expected in required_replay.items():
        if marker(replay_stdout, name) != expected:
            fail(("replay marker mismatch", name))
    artifacts = {}
    for name in (
        "producer.sing",
        "producer.stdout",
        "producer.stderr",
        "H_BASIS.txt",
        "HRAW_TO_H.matrix",
        "H_TO_Q4.matrix",
        "I2_NONZERO_LITERAL_INDICES.txt",
        "SOURCE_LABELS.json",
        "replay.sing",
        "replay.stdout",
        "replay.stderr",
    ):
        path = output / name
        artifacts[name] = {"sha256": digest(path), "bytes": path.stat().st_size}
    result = {
        "status": STATUS,
        "basis_commit": BASIS_COMMIT,
        "source_hashes": PINNED,
        "certificate_type": "explicit_two_stage_Hraw_to_H_and_H_to_all_q4",
        "same_code_family_replay_not_independent": True,
        "affine_checks": {
            "second_derivative_bad": 0,
            "affine_reconstruction_bad": 0,
            "C_equals_A_first_six_bad": 0,
        },
        "counts": labels["counts"] | {
            "H_basis": 20,
            "H_dimension": 2,
            "Hraw_to_H_matrix_shape": [2457, 20],
            "Hraw_to_H_nonzero": 123,
            "H_to_q4_matrix_shape": [20, 351],
            "H_to_q4_nonzero": 2434,
        },
        "power_unresolved_profile": {"1": 291, "2": 60, "3": 36, "4": 0},
        "mathematical_scope": "NO_RANK_EXACT_TWO_LEADING_POINT_LIFTS_THROUGH_LITERAL_LAMBDA_GRADE_THREE",
        "full_P6_consequence": "EVERY_I2_MINOR_CHART_IS_SET_THEORETICALLY_EMPTY_PENDING_INDEPENDENT_PROMOTION_REVIEW",
        "counterexample_claim": False,
        "jc2_claim": False,
        "mutations": {
            "C_entry": "PASS",
            "c3_entry": "PASS",
            "Hraw_to_H_coefficient": "PASS",
            "H_to_q4_coefficient": "PASS",
            "q4_target": "PASS",
            "forced_unit": "PASS",
            "known_proper": "PASS",
        },
        "artifacts": artifacts,
    }
    (output / "RESULT.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    write_manifest(output)
    print(STATUS)


if __name__ == "__main__":
    main()
