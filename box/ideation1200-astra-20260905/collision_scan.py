#!/usr/bin/env python3
"""Run the canonical collision engine with an additional explicit blind denylist.
No running moh14-msolve content may be scanned even if its receipt completes.
"""
from pathlib import Path
import importlib.util
import sys
ROOT=Path(__file__).resolve().parents[2]
report=ROOT/'xmodel/ideation-20260905T1200Z-astra.md'
spec=importlib.util.spec_from_file_location('open_collision_astra',ROOT/'ops/open_collision.py')
mod=importlib.util.module_from_spec(spec);sys.modules[spec.name]=mod;spec.loader.exec_module(mod)
questions=mod.extract_raised_opens(report.read_text())
corpus=tuple(p for p in mod.banked_corpus(ROOT,report)
             if not p.name.startswith('moh14-msolve-sol56')
             and not p.name.startswith('ideation-20260905T1200Z-'))
if len(questions)!=4:
    raise RuntimeError(f'Expected four explicit raised OPENs, found {len(questions)}')
if any(p.name.startswith(('moh14-msolve-sol56','ideation-20260905T1200Z-')) for p in corpus):
    raise RuntimeError('Blind denylist failed')
collisions=mod.find_collisions(questions,corpus,ROOT,max_candidates=1000)
print(mod.render_collisions(questions,collisions),end='')
print(f'\nCorpus: {len(corpus)} canonical banked files after the explicit denylist; {len(questions)} raised OPENs. Same-round and moh14-msolve content excluded before reads.')
