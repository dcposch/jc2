"""Name the surviving sibling tower of each ALIVE row: full leaf ledger + I_M, I_m."""
import sys, json, itertools
from fractions import Fraction as Q
from math import gcd
sys.path.insert(0, '/home/ubuntu/jc2/box/t3-residue-20260906')
from exact_contact import tower, all_flat
from t3_closure import Closure, lcmn, ROSTER

rows = {json.loads(l)['row_id']: json.loads(l) for l in open(ROSTER)}
out = {}
for rid in sys.argv[1:]:
    T = tower(rows[rid]['source']); n, m, s = T['n'], T['m'], T['s']
    best_global = None
    for c in all_flat(T):
        dtrue = {}
        for i, (z, orb, ix) in c['pattern'].items():
            gg = 0
            for r in ([z] if z > 0 else [])+list(orb): gg = gcd(gg, r)
            dtrue[i] = T['d'][i]//gg
        dtrue[s] = T['d'][s]//gcd(T['d'][s]-T['V'][s], T['V'][s])
        sib = [l for l in c['leaves'] if l['kind'] == 'major-sibling']
        base_IM = c['IM'] - sum(l['IM_each']*l['copies'] for l in sib)
        pools = []; ok = True
        for l in sib:
            i = l['level']; rho = int(l['rho'])
            W0 = n - T['M'][i]; L = lcmn([T['delta'][j].denominator for j in range(i, s+1)])
            C = Closure(n, m, m//dtrue[i], dtrue[i], True, True, True, False, None)
            R = C.run(rho, l['kappa'], W0, L)
            if not R: ok = False; break
            pools.append([(a, b, w, l['copies'], i, l['mult'], rho) for a, (b, w) in R.items()])
        if not ok: continue
        for combo in itertools.product(*pools) if pools else [()]:
            IM = base_IM + sum(a*k for a, b, w, k, i, mu, rr in combo)
            Im = c['Im'] + sum(b*k for a, b, w, k, i, mu, rr in combo)
            if IM.denominator != 1 or IM < Im: continue
            cand = (IM-Im, IM, Im, c, combo)
            if best_global is None or cand[:3] < best_global[:3]: best_global = cand
    if best_global is None:
        print(f"=== {rid}: NO SURVIVOR"); out[rid] = None; continue
    mg, IM, Im, c, combo = best_global
    print(f"=== {rid} ({n},{m}) s={s}  minimal-margin survivor:  I_M={IM}  I_m={Im}  margin={mg}")
    print(f"    level pattern p_i = pi^z prod(pi^A_i - c)^r :  "
          + "; ".join(f"i={i}: z={z}, orbits={list(o)}, tower-class#{ix} (A_{i}={T['A'][i]}, lo_{i}={T['lo'][i]})"
                      for i, (z, o, ix) in sorted(c['pattern'].items(), reverse=True)))
    for l in sorted(c['leaves'], key=lambda L: (-L['level'], L['kind'])):
        if l['kind'] == 'major-sibling': continue
        print("    leaf level %s %-12s mult=%s rho_f=%s copies=%s delta=%s%s" % (l["level"], l["kind"], l["mult"], l["rho"], l["copies"], l["delta"], ("  I_M each=%s"%l["IM_each"]) if "IM_each" in l else ""))


    for a, b, w, k, i, mu, rr in combo:
        print(f"    SIBLING TOWER level {i}, root multiplicity {mu}, rho_f={rr}, x{k} conjugates:")
        print(f"       dI_M={a} each, dI_m={b} each   {w}")
    out[rid] = dict(row=rid, n=n, m=m, IM=str(IM), Im=str(Im), margin=str(mg),
                    pattern={str(i): [z, list(o), ix] for i, (z, o, ix) in c['pattern'].items()},
                    leaves=[{k: str(v) for k, v in L.items()} for L in c['leaves']
                            if L['kind'] != 'major-sibling'],
                    sibling_towers=[dict(level=i, mult=mu, rho=rr, copies=k,
                                         dIM_each=str(a), dIm_each=str(b), tower=w)
                                    for a, b, w, k, i, mu, rr in combo])
json.dump(out, open('/home/ubuntu/jc2/box/t3-residue-20260906/t3_witnesses.json', 'w'), indent=1)
