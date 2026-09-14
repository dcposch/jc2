#!/usr/bin/env python3
"""Change only the exact-Q Gröbner algorithm in a complete emitted circuit."""
import argparse,hashlib,json
from pathlib import Path
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--source',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args()
    source=a.source.read_bytes();text=source.decode();old='ideal SB=std(I);';new='ideal SB=slimgb(I);'
    assert text.count(old)==1 and 'ALL_ROWS_PARSED' in text and 'BEGIN_CONTROLS' in text
    changed=text.replace(old,new);assert changed.replace(new,old)==text
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(changed)
    record={'source':str(a.source),'source_sha256':hashlib.sha256(source).hexdigest(),
      'script_sha256':hashlib.sha256(changed.encode()).hexdigest(),'change':{'from':old,'to':new},
      'all_equation_ring_and_control_text_unchanged':True,'field':'Q'}
    a.out.with_suffix('.variant.json').write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
    print(json.dumps(record,sort_keys=True))
if __name__=='__main__':main()
