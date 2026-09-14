#!/usr/bin/env python3
"""Assemble bounded report from charged text plus new custody/decision sections."""
from pathlib import Path
B=Path(__file__).resolve().parent
charged=Path('/tmp/jc2-lane.01qCZg/inputs/char-degree-instrument-astra-20260905.md').read_text()
theorems=charged[charged.index('**2. '):charged.index('**7. ')]
start=theorems.index('There are two precise coordinate implementations.')
end=theorems.index('The numerical calculations,',start)
theorems=theorems[:start]+('The canonical implementation takes the monic approximate root of the target resultant before composition. The runs instead retain every permitted target monomial existentially; this is a necessary enlargement. Such a member is a family representative, not an independently certified canonical `T_i`.\n\n')+theorems[end:]
start=theorems.index('All five lower target coefficients remain.')
end=theorems.index('Write `q_pq=',start)
theorems=theorems[:start]+('All five lower target coefficients remain. Four are recovered with rational monic pivots from high y-coefficients, retaining every unselected row. The positive-degree rows leave `e0` free; only the canonical resultant construction determines it.\n\n')+theorems[end:]
start=theorems.index('At the whole-target band,')
end=theorems.index('Some high-degree cancellation rows',start)
theorems=theorems[:start]+theorems[end:]
start=theorems.index('For (1), the high h-coefficients give explicitly')
end=theorems.index('A necessary caution is',start)
theorems=theorems[:start]+('After eliminating the four high h-coefficients, Q is constant in h, including an identically canceled h-linear term. Thus the upper-bound-only system retains Delta, but exact attainment forces `lambda=0`, contradicting `Z lambda-1`. This is **PROVED-HERE: UNIT ON DELTA**, not a unit of the unrestricted chart. The fresh source-arithmetic control retains all four Delta parameters.\n\n')+theorems[end:]
parts=[(B/'report-intro.md').read_text(),theorems,(B/'report-implementation.md').read_text()]
finite=B/'report-finite.md'
parts.append(finite.read_text() if finite.exists() else '\n[FINITE TABLE TO BE INSERTED BEFORE SEAL]\n\n')
parts.append((B/'report-uniform.md').read_text())
close=B/'report-closeout.md'
parts.append(close.read_text() if close.exists() else '\n[TERMINATION RECEIPT TO BE INSERTED BEFORE SEAL]\n')
out='\n\n'.join(p.strip() for p in parts)+'\n'
(B/'report-draft.md').write_text(out)
print('draft_bytes',len(out.encode()))
