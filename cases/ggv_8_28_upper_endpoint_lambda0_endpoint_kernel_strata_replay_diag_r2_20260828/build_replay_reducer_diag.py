#!/usr/bin/env python3
"""Test quotient-ideal normal forms on both frozen failed r6 replays."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
import tarfile


ARCHIVE_SHA256 = "cfd2c020b204beecaca5b60ee062aed8a1fe274a399c2ebda93d0d300a00c0f4"
TAG = "ggv_lambda0_endpoint_strata_p_r6_20260828T140500Z_r6a"
INPUTS = {
    "C8P_BRANCH_02": (f"{TAG}/output/compiled/branches/c8p_branch_02.sing", "bed61e93582dfefab3ffa5da5ea43a527887572c2c4b602e2249a2f251ccc076"),
    "TRIPLE_BRANCH_02": (f"{TAG}/output/compiled/branches/triple_branch_02.sing", "e1c50b669a90e3c5a8a6984d34e13365600b11d19b9be5fbabc673edc7e9c021"),
}
EXPECTED_OUTPUTS = {
    "C8P_BRANCH_02": "08bdc93c56b6e7ed8ab313413e9fd22af2eda098ef14814a9f6d68bbc8a46cf6",
    "TRIPLE_BRANCH_02": "1feba464ee914d93935d4ef4165be7d260044940c6c28cb632f662b8cf7066ea",
}
OLD = "matrix replay=M*N; int replay_zero=(size(module(replay))==0);"
NEW_TEMPLATE = r'''matrix replay=M*N;
int replay_size_zero=(size(module(replay))==0);
ideal replay_qideal=ideal(basering); ideal replay_qsb=std(replay_qideal);
int replay_raw_nonzero_entries=0; int replay_reduced_nonzero_entries=0;
int replay_i; int replay_j; poly replay_nf;
string replay_raw_file="{label}_REPLAY_RAW_NONZERO.tsv";
string replay_nf_file="{label}_REPLAY_REDUCED_NONZERO.tsv";
for(replay_i=1;replay_i<=nrows(replay);replay_i=replay_i+1){{ for(replay_j=1;replay_j<=ncols(replay);replay_j=replay_j+1){{ if(replay[replay_i,replay_j]!=0){{ replay_raw_nonzero_entries=replay_raw_nonzero_entries+1; write(replay_raw_file,string(replay_i)+"|"+string(replay_j)+"|"+string(replay[replay_i,replay_j])); }} replay_nf=reduce(replay[replay_i,replay_j],replay_qsb); if(replay_nf!=0){{ replay_reduced_nonzero_entries=replay_reduced_nonzero_entries+1; write(replay_nf_file,string(replay_i)+"|"+string(replay_j)+"|"+string(replay_nf)); }} }} }}
int replay_zero=(replay_reduced_nonzero_entries==0);
matrix N_MUT=N; N_MUT[1,1]=N_MUT[1,1]+1;
matrix replay_mut=M*N_MUT;
int mutation_raw_nonzero_entries=0; int mutation_reduced_nonzero_entries=0;
for(replay_i=1;replay_i<=nrows(replay_mut);replay_i=replay_i+1){{ for(replay_j=1;replay_j<=ncols(replay_mut);replay_j=replay_j+1){{ if(replay_mut[replay_i,replay_j]!=0){{ mutation_raw_nonzero_entries=mutation_raw_nonzero_entries+1; }} replay_nf=reduce(replay_mut[replay_i,replay_j],replay_qsb); if(replay_nf!=0){{ mutation_reduced_nonzero_entries=mutation_reduced_nonzero_entries+1; }} }} }}
poly mutation_pivot_nf=reduce(replay_mut[1,1],replay_qsb);
print("ORIGINAL_SIZE_MODULE_REPLAY_ZERO="+string(replay_size_zero));
print("RAW_ENTRYWISE_REPLAY_ZERO="+string(replay_raw_nonzero_entries==0));
print("RAW_ENTRYWISE_REPLAY_NONZERO_ENTRIES="+string(replay_raw_nonzero_entries));
print("QIDEAL_REDUCED_REPLAY_ZERO="+string(replay_zero));
print("QIDEAL_REDUCED_REPLAY_NONZERO_ENTRIES="+string(replay_reduced_nonzero_entries));
print("MUTATION_RAW_REPLAY_ZERO="+string(mutation_raw_nonzero_entries==0));
print("MUTATION_QIDEAL_REDUCED_PIVOT_NONZERO="+string(mutation_pivot_nf!=0));
print("MUTATION_QIDEAL_REDUCED_REPLAY_ZERO="+string(mutation_reduced_nonzero_entries==0));
print("MUTATION_QIDEAL_REDUCED_NONZERO_ENTRIES="+string(mutation_reduced_nonzero_entries));
if((replay_size_zero==0) && (replay_raw_nonzero_entries>0) && replay_zero && (mutation_pivot_nf!=0) && (mutation_reduced_nonzero_entries>0)){{ print("REPLAY_REDUCER_MUTATION_CONTROL_PASS={label}"); }}
'''


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--archive", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    archive = args.archive.resolve()
    if sha(archive.read_bytes()) != ARCHIVE_SHA256:
        raise SystemExit("R6_RESULT_ARCHIVE_DRIFT")
    args.output_dir.mkdir(parents=True, exist_ok=True)
    manifest = ["label|input_sha256|output_sha256|script"]
    with tarfile.open(archive, "r:gz") as bundle:
        for label, (member, expected_input) in INPUTS.items():
            handle = bundle.extractfile(member)
            if handle is None:
                raise SystemExit(f"MISSING_ARCHIVE_MEMBER:{label}")
            raw = handle.read()
            if sha(raw) != expected_input:
                raise SystemExit(f"INPUT_SCRIPT_DRIFT:{label}")
            text = raw.decode()
            if text.count(OLD) != 1:
                raise SystemExit(f"REPLAY_MARKER_SITE_DRIFT:{label}")
            result = text.replace(OLD, NEW_TEMPLATE.format(label=label))
            output_sha = sha(result.encode())
            frozen = EXPECTED_OUTPUTS[label]
            if frozen != "TO_BE_FROZEN" and output_sha != frozen:
                raise SystemExit(f"DIAGNOSTIC_SCRIPT_HASH_DISAGREEMENT:{label}:{output_sha}")
            name = label.lower() + "_reducer_diag.sing"
            (args.output_dir / name).write_text(result)
            manifest.append(f"{label}|{expected_input}|{output_sha}|{name}")
            print(f"REDUCER_DIAGNOSTIC_SCRIPT_SHA256_{label}={output_sha}")
    (args.output_dir / "DIAGNOSTIC_MANIFEST.tsv").write_text("\n".join(manifest) + "\n")
    print("REPLAY_REDUCER_DIAGNOSTIC_BUILD_PASS")


if __name__ == "__main__":
    main()
