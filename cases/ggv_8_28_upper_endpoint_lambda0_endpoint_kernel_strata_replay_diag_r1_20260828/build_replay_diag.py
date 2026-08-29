#!/usr/bin/env python3
"""Instrument the two frozen r6 quotient scripts without changing their math."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
import tarfile


ARCHIVE_SHA256 = "cfd2c020b204beecaca5b60ee062aed8a1fe274a399c2ebda93d0d300a00c0f4"
TAG = "ggv_lambda0_endpoint_strata_p_r6_20260828T140500Z_r6a"
INPUTS = {
    "C8P_BRANCH_02": (
        f"{TAG}/output/compiled/branches/c8p_branch_02.sing",
        "bed61e93582dfefab3ffa5da5ea43a527887572c2c4b602e2249a2f251ccc076",
    ),
    "TRIPLE_BRANCH_02": (
        f"{TAG}/output/compiled/branches/triple_branch_02.sing",
        "e1c50b669a90e3c5a8a6984d34e13365600b11d19b9be5fbabc673edc7e9c021",
    ),
}
EXPECTED_OUTPUTS = {
    "C8P_BRANCH_02": "edbdc4851427feba7310787bb270f1048e0504cae3afc0dc348f53ecd520d8f1",
    "TRIPLE_BRANCH_02": "5575e15b819614f8485d4ec34e5d54a1f7a3a4717e211f4d7c5a5291098cbdbd",
}
OLD = "matrix replay=M*N; int replay_zero=(size(module(replay))==0);"
NEW_TEMPLATE = r'''matrix replay=M*N;
int replay_size_zero=(size(module(replay))==0);
int replay_nonzero_entries=0; int replay_i; int replay_j;
string replay_diag_file="{label}_REPLAY_DIAGNOSTIC.tsv";
for(replay_i=1;replay_i<=nrows(replay);replay_i=replay_i+1){{ for(replay_j=1;replay_j<=ncols(replay);replay_j=replay_j+1){{ if(replay[replay_i,replay_j]!=0){{ replay_nonzero_entries=replay_nonzero_entries+1; write(replay_diag_file,string(replay_i)+"|"+string(replay_j)+"|"+string(replay[replay_i,replay_j])); }} }} }}
int replay_zero=(replay_nonzero_entries==0);
matrix N_MUT=N; N_MUT[1,1]=N_MUT[1,1]+1;
matrix replay_mut=M*N_MUT; int mutation_nonzero_entries=0;
for(replay_i=1;replay_i<=nrows(replay_mut);replay_i=replay_i+1){{ for(replay_j=1;replay_j<=ncols(replay_mut);replay_j=replay_j+1){{ if(replay_mut[replay_i,replay_j]!=0){{ mutation_nonzero_entries=mutation_nonzero_entries+1; }} }} }}
int mutation_zero=(mutation_nonzero_entries==0);
print("ORIGINAL_SIZE_MODULE_REPLAY_ZERO="+string(replay_size_zero));
print("ENTRYWISE_REPLAY_ZERO="+string(replay_zero));
print("ENTRYWISE_REPLAY_NONZERO_ENTRIES="+string(replay_nonzero_entries));
print("MUTATION_PIVOT_NONZERO="+string(replay_mut[1,1]!=0));
print("MUTATION_REPLAY_ZERO="+string(mutation_zero));
print("MUTATION_REPLAY_NONZERO_ENTRIES="+string(mutation_nonzero_entries));
if((replay_size_zero==0) && replay_zero && (replay_mut[1,1]!=0) && (mutation_nonzero_entries>0)){{ print("REPLAY_MARKER_MUTATION_CONTROL_PASS={label}"); }}
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
            name = label.lower() + "_diag.sing"
            (args.output_dir / name).write_text(result)
            manifest.append(f"{label}|{expected_input}|{output_sha}|{name}")
            print(f"DIAGNOSTIC_SCRIPT_SHA256_{label}={output_sha}")
    (args.output_dir / "DIAGNOSTIC_MANIFEST.tsv").write_text("\n".join(manifest) + "\n")
    print("REPLAY_DIAGNOSTIC_BUILD_PASS")


if __name__ == "__main__":
    main()
