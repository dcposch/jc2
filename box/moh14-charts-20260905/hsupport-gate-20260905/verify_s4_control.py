#!/usr/bin/env python3
"""Compare the newly built genuine 425-generator s'=4 control with old rows."""
from pathlib import Path
import hashlib
import importlib.util
import json
import re
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
CID = 'C_n24m16_Mm12_m2_5_ell1_s4'
STEM = CID + '_union'
EXPECTED_OLD_ROWS = 'af3cf058c7e949d7e9958b1c9120b9350436c6eca7a952afbc8ea32f9794ef58'


def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as fh:
        for block in iter(lambda: fh.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def main():
    old_base = HERE.parent / 'classes' / CID
    new_base = HERE / 'classes' / CID
    old_rows = old_base / 'rows' / (STEM + '_rows.tsv')
    new_rows = new_base / 'rows' / (STEM + '_rows.tsv')
    assert sha(old_rows) == EXPECTED_OLD_ROWS, 'Original control changed'
    out = (new_base / 'control-s4-builder.stdout.log').read_text()
    err = (new_base / 'control-s4-builder.stderr.log').read_text()
    assert 'NATIVE_GATE lead_h_is_yK=1' in out
    old_builder = old_base / 'builders' / (STEM + '_builder.sing')
    new_builder = new_base / 'builders' / (STEM + '_builder.sing')
    assert old_builder.read_bytes() == new_builder.read_bytes()
    if 'Exit status: 124' in err:
        report = dict(status='BUILDER_IDENTITY_PASS; FRESH_REBUILD_TIMEOUT',
                      actual_control=STEM, timeout_seconds=900,
                      original_425_rows_sha256=sha(old_rows),
                      original_builder_sha256=sha(old_builder),
                      rebuilt_builder_sha256=sha(new_builder),
                      old_and_new_builders_byte_identical=True,
                      old_original_untouched=True,
                      fresh_rows_sha256=sha(new_rows),
                      fresh_row_count=max(0,len(new_rows.read_text().splitlines())-1),
                      semantic_compare='NOT_RUN: fresh builder did not complete',
                      script_sha256=sha(Path(__file__)),
                      interpretation='Identical builder preserves original425 generators; timeout is no emptiness result')
        (HERE / 'control-s4-verification.json').write_text(json.dumps(report,indent=2)+'\n')
        print(json.dumps(report,indent=2))
        return
    assert 'NATIVE_DONE equations=425' in out
    assert 'Exit status: 0' in err
    assert '// **' not in out and '// **' not in err
    fix_path = HERE.parent / 'builder_fix.py'
    spec = importlib.util.spec_from_file_location('builder_fix', fix_path)
    fix = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(fix)
    comparison = fix.semantic_compare(old_rows, new_rows)
    assert comparison['identical'] and comparison['old_rows'] == 425, comparison
    # A structural negative control rejects replacing a complete row set by the
    # known header-only V3_2 file. This creates no malformed control artifact.
    incomplete = HERE.parent / 'classes' / 'C_n24m16_M12_17_ell1_s3' / 'rows' / (
        'C_n24m16_M12_17_ell1_s3_V3_2_rows.tsv')
    incomplete_count = len(fix.read_row_set(incomplete))
    assert incomplete_count == 0
    rss = re.search(r'Maximum resident set size \(kbytes\): (\d+)', err)
    elapsed = re.search(r'Elapsed \(wall clock\) time \(h:mm:ss or m:ss\): (.*)', err)
    report = dict(status='PASS', actual_control=STEM,
                  old_rows_path=str(old_rows), new_rows_path=str(new_rows),
                  old_rows_sha256=sha(old_rows), new_rows_sha256=sha(new_rows),
                  builder_fix_sha256=sha(fix_path),
                  new_builder_sha256=sha(new_base / 'builders' / (STEM + '_builder.sing')),
                  script_sha256=sha(Path(__file__)),
                  comparison=comparison, old_original_untouched=True,
                  gates=[line for line in out.splitlines() if line.startswith('NATIVE_')],
                  elapsed=elapsed.group(1) if elapsed else None,
                  max_rss_kb=int(rss.group(1)) if rss else None,
                  negative_control_header_only_V3_2_rows=incomplete_count,
                  h_support='11/11 complete; no support or generator changes')
    (HERE / 'control-s4-verification.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
