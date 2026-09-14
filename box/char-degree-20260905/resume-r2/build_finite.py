#!/usr/bin/env python3
import json,math
from pathlib import Path
B=Path(__file__).resolve().parent
a=json.loads((B/'audit-99.json').read_text())
b=json.loads((B/'audit-d108-custody.json').read_text())
def cell(r,client):
 status=r['status']
 assert 'BOUND' in status,status
 label='M' if 'MEMORY' in status else 'T'
 rc=r['cas_rc'] if client==99 else r['returncode']
 wall=r['total_wall_seconds'] if client==99 else r['wall_seconds']
 rss=r.get('rss_kib') if client==99 else r.get('observed_RSS_HWM_KiB')
 shown='—' if rss is None else '≥'+str(math.floor(rss/1048576*100)/100)
 return f'{label}{rc}; {wall:.1f}; {shown}'
rows=[]
for stage in range(9):
 rs=[next(r for r in a['records'] if r['stage']==stage and r['branch']==br) for br in ('delta2','delta52')]
 ds=[next(r for r in b['stages'] if r['stage']==stage and ('frozen' in r['variant'])==frozen) for frozen in (True,False)]
 rows.append('| '+str(stage)+' | '+' | '.join([cell(r,99) for r in rs]+[cell(r,108) for r in ds])+' |')
table='\n'.join(rows)
stats=[]
for title,rs,client in [('99 delta2',[r for r in a['records'] if r['branch']=='delta2'],99),('99 delta5/2',[r for r in a['records'] if r['branch']=='delta52'],99),('108 mean zero',[r for r in b['stages'] if 'frozen' in r['variant']],108),('108 free mean',[r for r in b['stages'] if 'free-mean' in r['variant']],108)]:
 gs=[r['ordered_generator_count'] if client==99 else r['ring_generator_count'] for r in rs]
 qs=[r['counts']['Q'] if client==99 else r['row_counts']['Q'] for r in rs]
 stats.append(f'{title}: {min(gs)}–{max(gs)} generators, {min(qs)}–{max(qs)} characteristic Q rows')
sel=[]
for r in b['selected']:
 x=r['result'];assert 'BOUND' in x['status'],x['status']
 rss=r.get('observed_RSS_HWM_KiB');shown='not captured' if rss is None else f'observed HWM ≥{math.floor(rss/1048576*100)/100} GiB'
 sel.append(f"`{r['case']}`: rc{x['returncode']}, {x['elapsed_seconds']:.3f}s, {shown}, OPEN")
text=f'''**8. Reissued finite schedule and decision table.** All36 main circuit attempts reached complete emission and `ALL_ROWS_PARSED`. None reached a complete accepted result/control block. Each cell is **status+rc; recorded elapsed seconds; RSS GiB**: T=COMPUTE-BOUND OPEN, M=MEMORY-BOUND OPEN. Both clients' times include emitter/build overhead; build times are separately retained. A dash means RSS was not captured. An inequality is the observed `/proc` VmHWM through the last sample, rounded downward, hence only a lower bound on final peak RSS. The 16 GiB address-space caps are not substituted for RSS.

| Stage | 99 delta2 | 99 delta5/2 | D108 mean-zero restriction | D108 repaired free mean |
|---:|---|---|---|---|
{table}

Every stage's script, input, emitter, source-map, ordered-ring and output SHA-256 is bound in [99 custody](/home/ubuntu/jc2/box/char-degree-20260905/resume-r2/audit-99.json) and [D108 custody](/home/ubuntu/jc2/box/char-degree-20260905/resume-r2/audit-d108-custody.json). These retain exact row counts, localizer strings, ring order and target checks. Ring/block sizes are: {'; '.join(stats)}. A zero residual-source-row count after graph elimination does not mean original source conditions were dropped; their images and rational pivots are separately audited.

Selected stage8 alternatives also remained OPEN. The 99 delta2 `slimgb` run ended rc1 at1200.467s; the delta5/2 active-front run ended rc1 at1801.169s; the delta5/2 remainder run failed for memory at1215.298s. Their peak RSS was not captured. D108 {'; '.join(sel)}. No selected run supplies a branch kill or proper ideal.

The final historical inventory is [status-catalog-final.json](/home/ubuntu/jc2/box/char-degree-20260905/resume-r2/status-catalog-final.json). It includes the older normalized/active/construction attempts and quarantined startup failures. Stale `RUNNING`, `EXPANDING_FULL_CHARACTERISTIC`, or `EMITTED_NOT_DECIDED` metadata is reconciled against the final process inventory; it proves no solver completion. Some legacy `CAS_ERROR_OPEN` records are memory failures during construction, not parser failures. No control result or administrative `CLOSED` receipt is promoted to a production verdict.

Fresh emitter and all-production-ring inverse controls pass. The independent [final strict reader](/home/ubuntu/jc2/box/char-degree-20260905/resume-r2/strict-acceptance-production-final.json) binds39 actual production outputs: **34 time-bound,5 memory-bound, zero complete clean unit/proper candidates**. Its controls reject incomplete markers, wrong control vectors, and a real malformed Singular script that exits rc0. Production inline controls never completed after the bounded Gröbner calls, so acceptance stops at OPEN.

**Per-client verdict:** (99,66) delta2 — **compute-bound OPEN**; (99,66) delta5/2 — **compute-bound OPEN**; D108 delta3 — **compute-bound OPEN**, including the coverage-repaired free-mean chart. No independent unit replay or coordinate extraction was triggered because no production unit or proper candidate existed. If a complete validated ideal had been proper, the charged typing would be **PROPER — EXACT-Q-PROPER-AUGMENTED-IDEAL: an existential nondegenerate necessary-chart survivor over Qbar**, even without extracted coordinates. That event did not occur here.

'''
(B/'report-finite.md').write_text(text)
print('finite_bytes',len(text.encode()))
