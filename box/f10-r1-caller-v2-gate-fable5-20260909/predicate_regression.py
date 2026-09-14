"""Metadata-only regression of v2 caller predicates. No import/run of dispatch_batch.py, probe, checker,
precision, CAPRUN or any math. Predicates are EXTRACTED from the v2 source by AST and exec'd in isolation
against dictionary fixtures. No fork, no signal, no /proc scan. RLIMIT_AS 64 MiB, SIGALRM 10 s."""
import ast, copy, hashlib, json, resource, signal, sys, datetime
resource.setrlimit(resource.RLIMIT_AS, (64*1024*1024, 64*1024*1024))
signal.alarm(10)
INP = '/tmp/jc2-lane.y92awu/inputs/'
SRC = open(INP+'dispatch_batch.py').read()
tree = ast.parse(SRC)
tele = json.load(open(INP+'dummy-descendant.telemetry.json'))
run_fn = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'run')
main_fn = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'main')

def names(node): return {n.id for n in ast.walk(node) if isinstance(n, ast.Name)}
# --- locate the dummy branch: if defect: ... elif name=='dummy-descendant': ... else: ...
defect_if = next(s for s in run_fn.body if isinstance(s, ast.If) and isinstance(s.test, ast.Name) and s.test.id == 'defect')
dummy_if = defect_if.orelse[0]
assert isinstance(dummy_if, ast.If) and ast.get_source_segment(SRC, dummy_if.test) == "name=='dummy-descendant'"
dummy_stmts = [s for s in dummy_if.body if not (names(s) & {'ROOT', 'lines', 'namespace'})]
skipped = [ast.get_source_segment(SRC, s).splitlines()[0][:60] for s in dummy_if.body if names(s) & {'ROOT', 'lines', 'namespace'}]
dummy_code = compile(ast.Module(body=dummy_stmts, type_ignores=[]), 'dummy-branch', 'exec')
# --- admission block and post-return require, DEADLINE constant
math_if = next(s for s in run_fn.body if isinstance(s, ast.If) and ast.get_source_segment(SRC, s.test) == 'mathematical')
admission_code = compile(ast.Module(body=math_if.body, type_ignores=[]), 'admission', 'exec')
post_stmt = next(s for s in run_fn.body if isinstance(s, ast.Expr) and 'NONDECISION' in ast.get_source_segment(SRC, s))
post_code = compile(ast.Module(body=[post_stmt], type_ignores=[]), 'postreturn', 'exec')
deadline_assign = next(s for s in tree.body if isinstance(s, ast.Assign) and isinstance(s.targets[0], ast.Name) and s.targets[0].id == 'DEADLINE')
DEADLINE = eval(compile(ast.Expression(deadline_assign.value), 'deadline', 'eval'), {'datetime': datetime})
# ordering facts by line number
record_write = next(s for s in run_fn.body if 'dispatch.json' in ast.get_source_segment(SRC, s))
rc0_line = [n.lineno for n in ast.walk(defect_if.orelse[0]) if isinstance(n, ast.Call) and 'no retry' in ast.get_source_segment(SRC, n)]
returned_assign = [n for n in ast.walk(run_fn) if isinstance(n, ast.Assign) and isinstance(n.targets[0], ast.Name) and n.targets[0].id == 'returned']
wait_line = [n.lineno for n in ast.walk(run_fn) if isinstance(n, ast.Assign) and 'process.wait()' in ast.get_source_segment(SRC, n)]
hard_init = [s for s in run_fn.body if isinstance(s, ast.Assign) and isinstance(s.targets[0], ast.Name) and s.targets[0].id == 'hard']

class Rej(Exception): pass
def require(ok, reason):
    if not ok: raise Rej(reason)
def dummy(t, rc=125, rss=33554432):
    ns = {'require': require, 'telemetry': t, 'rc': rc, 'rss': rss}
    try: exec(dummy_code, ns); return 'PASS'
    except Rej as e: return 'FAIL:' + str(e)
    except Exception as e: return 'EXC:' + type(e).__name__
def admission(now, first_math, wall):
    ns = {'require': require, 'DEADLINE': DEADLINE, 'first_math': first_math, 'wall': wall,
          'time': type('T', (), {'time': staticmethod(lambda: now)}), 'min': min}
    try: exec(admission_code, ns); return ('PASS', ns['hard'], ns['first_math'])
    except Rej as e: return ('FAIL:' + str(e), None, None)
def post(mathematical, returned, hard):
    ns = {'require': require, 'mathematical': mathematical, 'returned': returned, 'hard': hard}
    try: exec(post_code, ns); return 'PASS'
    except Rej as e: return 'FAIL:' + str(e)
    except Exception as e: return 'EXC:' + type(e).__name__

out = []
def row(label, got, want):
    ok = (got == 'PASS') if want == 'PASS' else (got != 'PASS' and got.startswith('FAIL'))
    out.append(f"{'ok ' if ok else 'BAD'} | {label:58s} | want {want:4s} | got {got}")
    return ok
allok = True
def T(label, got, want):
    global allok; allok &= row(label, got, want)
def mut(f):
    t = copy.deepcopy(tele); f(t); return t
ev = lambda t: t['identity_checks']
# ---- D: dummy branch fixtures
T('ACTUAL pinned telemetry', dummy(tele), 'PASS')
T('EMPTY identity_checks', dummy(mut(lambda t: t.update(identity_checks=[]))), 'FAIL')
T('delete before-term-send SENT', dummy(mut(lambda t: ev(t).pop(1))), 'FAIL')
T('delete kill pair', dummy(mut(lambda t: t.update(identity_checks=ev(t)[:2]))), 'FAIL')
T('reorder: SENT before MATCH', dummy(mut(lambda t: t.update(identity_checks=[ev(t)[1], ev(t)[0]] + ev(t)[2:]))), 'FAIL')
T('reorder: kill pair before term pair', dummy(mut(lambda t: t.update(identity_checks=ev(t)[2:] + ev(t)[:2]))), 'FAIL')
T('extra fifth SENT', dummy(mut(lambda t: ev(t).append(dict(ev(t)[3])))), 'FAIL')
T('before-term MISMATCH', dummy(mut(lambda t: ev(t)[0].update(result='MISMATCH'))), 'FAIL')
T('before-kill NOT_FOUND', dummy(mut(lambda t: ev(t)[2].update(result='NOT_FOUND'))), 'FAIL')
T('kill-send GROUP_GONE', dummy(mut(lambda t: ev(t)[3].update(result='GROUP_GONE'))), 'FAIL')
T('wrong signal term=9', dummy(mut(lambda t: ev(t)[1].update(signal=9))), 'FAIL')
T('signal "15" string', dummy(mut(lambda t: ev(t)[1].update(signal='15'))), 'FAIL')
T('signal 15.0 float (== passes, type must fail)', dummy(mut(lambda t: ev(t)[1].update(signal=15.0))), 'FAIL')
T('signal 9.0 float on kill-send', dummy(mut(lambda t: ev(t)[3].update(signal=9.0))), 'FAIL')
T('signal True bool', dummy(mut(lambda t: ev(t)[1].update(signal=True))), 'FAIL')
T('renamed stage before-kill -> before-kil', dummy(mut(lambda t: ev(t)[2].update(stage='before-kil'))), 'FAIL')
T('MATCH foreign observed_pid 9999', dummy(mut(lambda t: ev(t)[2].update(observed_pid=9999))), 'FAIL')
T('MATCH foreign observed_pgid 9999', dummy(mut(lambda t: ev(t)[0].update(observed_pgid=9999))), 'FAIL')
T('MATCH foreign start identity', dummy(mut(lambda t: ev(t)[2].update(observed_start_identity='boot=x;start_ticks=1'))), 'FAIL')
T('MATCH missing observed_pid key', dummy(mut(lambda t: ev(t)[0].pop('observed_pid'))), 'FAIL')
T('top-level pid != pgid (leader not group leader)', dummy(mut(lambda t: t.update(pid=2627))), 'FAIL')
T('status NORMAL_EXIT with rc125/rss', dummy(mut(lambda t: t.update(status='NORMAL_EXIT'))), 'FAIL')
T('resource cpu', dummy(mut(lambda t: t.update(resource='cpu'))), 'FAIL')
T('rc 0 instead of 125', dummy(tele, rc=0), 'FAIL')
T('cleanup_complete false', dummy(mut(lambda t: t['termination'].update(cleanup_complete=False))), 'FAIL')
T('max RSS not above cap', dummy(mut(lambda t: t.update(max_observed_group_rss_bytes=33554432))), 'FAIL')
# ---- B/D: timing fixtures
fm = DEADLINE - 3600.0           # first_math an hour before the absolute deadline -> hard = first_math+360
st, hard, fm2 = admission(fm, None, 60)
T('first math admission (first_math None -> set)', st, 'PASS'); allok &= (hard == fm + 360 and fm2 == fm)
out.append(f"    stored hard == first_math+360: {hard == fm+360}; DEADLINE == 2026-09-09T13:35Z: {DEADLINE == datetime.datetime(2026,9,9,13,35,tzinfo=datetime.timezone.utc).timestamp()}")
st2, hard2, _ = admission(fm + 200, fm, 30)
T('later stage keeps SAME stored hard (no refresh)', st2, 'PASS'); allok &= (hard2 == hard)
out.append(f"    second-stage hard identical to first: {hard2 == hard}")
fm3 = DEADLINE - 100.0
st3, hard3, _ = admission(fm3, None, 60)
T('absolute 13:35 governs when first_math+360 is later', 'FAIL:' if hard3 is None else ('PASS' if hard3 == DEADLINE else 'FAIL:hard'), 'PASS')
T('admission now+wall+15 == hard (equal, strict <)', admission(hard - 60 - 15, fm, 60)[0], 'FAIL')
T('admission now+wall+15 == hard-0.001', admission(hard - 60 - 15 - 0.001, fm, 60)[0], 'PASS')
T('admission with only +2 s room (old margin)', admission(hard - 30 - 2, fm, 30)[0], 'FAIL')
T('admission with +14 s room', admission(hard - 30 - 14, fm, 30)[0], 'FAIL')
T('post-return: returned == stored hard, rc 0', post(True, hard, hard), 'FAIL')
T('post-return: returned = hard + 0.001, rc 0', post(True, hard + 0.001, hard), 'FAIL')
T('post-return: returned = hard - 0.001', post(True, hard - 0.001, hard), 'PASS')
T('post-return: returned = hard + 300 (late)', post(True, hard + 300, hard), 'FAIL')
T('post-return: non-mathematical stage, hard None', post(False, hard + 999, None), 'PASS')
T('post-return: refreshed cutoff would NOT be used (returned vs original)', post(True, hard + 5, hard), 'FAIL')
# ordering facts
out.append(f"    line order: process.wait {wait_line} < returned= {[n.lineno for n in returned_assign]} < dispatch.json write {record_write.lineno} < NONDECISION require {post_stmt.lineno} < rc==0 accept {rc0_line}")
allok &= wait_line[0] < returned_assign[0].lineno < record_write.lineno < post_stmt.lineno < rc0_line[0]
allok &= len(hard_init) == 1 and ast.get_source_segment(SRC, hard_init[0]) == 'hard = None'
out.append(f"    'hard = None' initialised once before the mathematical block: {len(hard_init)==1}; post require does not reference rc: {'rc' not in names(post_stmt)}")
out.append(f"    skipped dummy-branch statements (need uncharged stdout file): {skipped}")
# ---- helper pin constants from main(): compare against charged bytes
pins = {}
for n in ast.walk(main_fn):
    if isinstance(n, ast.Compare) and isinstance(n.left, ast.Call) and getattr(n.left.func, 'id', '') == 'digest':
        arg = ast.get_source_segment(SRC, n.left.args[0]); pins[arg] = n.comparators[0].value
def sha(b): return hashlib.sha256(b).hexdigest()
for key, fname in [("ROOT/'precision.py'", 'precision.py'), ("ROOT/'checker.py'", 'checker.py'), ("ROOT/'execution_gate.py'", 'execution_gate.py')]:
    b = open(INP + fname, 'rb').read()
    T(f'pin {fname} == charged bytes', 'PASS' if sha(b) == pins[key] else 'FAIL:pin', 'PASS')
    T(f'pin {fname} vs one appended byte', 'FAIL:changed' if sha(b + b'\n') != pins[key] else 'PASS', 'FAIL')
    T(f'pin {fname} vs one flipped byte', 'FAIL:changed' if sha(b[:100] + bytes([b[100] ^ 1]) + b[101:]) != pins[key] else 'PASS', 'FAIL')
reg = json.load(open(INP + 'REGISTRATION.disabled.json'))
T('probe pin == REGISTRATION probe_sha256 == prior-gate 02913a1c', 'PASS' if pins["ROOT/'probe.py'"] == reg['probe_sha256'] == '02913a1caf8cb5ebe2ec7c404ede0247a1954baee3751af8b2645496f6b6e1a7' else 'FAIL:', 'PASS')
T('precision pin == REGISTRATION precision_sha256', 'PASS' if pins["ROOT/'precision.py'"] == reg['precision_sha256'] else 'FAIL:', 'PASS')
T('REGISTRATION caller pin == charged dispatch_batch.py', 'PASS' if reg['caller_sha256_for_root_external_preflight'] == sha(open(INP+'dispatch_batch.py','rb').read()) else 'FAIL:', 'PASS')
T('REGISTRATION enabled=false, dispatch_authorized=false', 'PASS' if reg['enabled'] is False and reg['dispatch_authorized'] is False else 'FAIL:', 'PASS')
T('no dispatch_batch.py self-pin in main()', 'PASS' if not any('dispatch_batch' in k for k in pins) else 'FAIL:', 'PASS')
out.append(f"    main() pin keys: {sorted(pins)}")
print('\n'.join(out)); print('ALL_OK' if allok else 'SOME_BAD'); print(f"rows={len([l for l in out if l[:3] in ('ok ','BAD')])}")
