#!/usr/bin/env python3
"""D43 family compiler, step 0: the full-live window build at D = 43.

Exactly the 6.T / build_tails25.py build (directionb_strike.dsys_tails
pattern) with D = 43: generators through absolute level 32+42 = 74,
VDEG_CAP = 43 (var-degree <= slot => exact, sentinel asserted), frees =
KEEP7 (dead-stretch) + ALL P-side tails tf*/tg* through level 74;
B-side frozen (pinned 0).  PIN42 is applied downstream at load
(load_nolog_rows convention: drop monomials containing level-42 tails),
identical to the D21/D25 chains.

RESUME-SAFE: each cumulative per-orbit jet product is checkpointed to
ckpt43/jet_<side>_<NN>_<orbit>.pkl (atomic os.replace); on restart the
finished orbits are loaded and the build continues.  The registry name
list is hashed into every checkpoint and re-asserted on load (the
var-index keys reference R1.VARS order).

Banks <here>/directionb_tails_D43.pkl with {"byk","vars","D"}.
Consumer-side gates (sol-round6 sec 2.3 pattern + the D43 spec
xmodel/sol-xside-spec.md sect 6): odd rows 25..41 == 0, eta supports,
frontier census, Row-24 digest replay, POST41 first-occurrence census
at Row 42 -- run by the consumer (d43_reduce.py), not here.

NOTE (x-side): this bank is the PURE-Y build.  Row 42 is banked here as
its pure-y part [t^42]E_y; the exact level-42 x-side correction
42*S_M*G_M*(3a-2b)*p^4*p' (sol-xside-spec.md (3.5), EXACT DERIVATION)
is appended by the consumer with (alpha, beta) as explicit independent
variables (fail-closed under CONJECTURE X-SIDE-30).
"""
import sys, os, time, pickle, gc, hashlib
gc.disable()          # pure refcount workload (dicts of tuples/K3)
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import r1_experiment as R1
import directionb_strike as D

DD = 43
CK = os.path.join(HERE, "ckpt43")
os.makedirs(CK, exist_ok=True)
OUT = os.path.join(HERE, "directionb_tails_D43.pkl")

t0 = time.time()
# dry pass: collect the template free names
D.fresh_registry()
R1.VDEG_CAP = DD
R1.build_generators(32 + DD)
names = [v["name"] for v in R1.VARS]
keep = tuple(n for n in names
             if n in D.KEEP7 or n[:2] in ("tf", "tg"))
print("free vars (%d): %s" % (len(keep), " ".join(keep)), flush=True)

# frozen registry (build_frozen pattern, inlined so the two gm_jet2
# sides can be checkpointed per orbit via the seed parameter)
D.fresh_registry()
R1.PINS = {n: R1.RZERO for n in names if n not in keep}
R1.VDEG_CAP = DD
orbs = R1.build_generators(32 + DD)
names2 = [v["name"] for v in R1.VARS]
REG_HASH = hashlib.sha256(repr(names2).encode()).hexdigest()
print("registry: %d vars, hash %s" % (len(names2), REG_HASH), flush=True)


def jet_side(orbnames, tag):
    jp = None
    for i, on in enumerate(orbnames):
        ck = os.path.join(CK, "jet_%s_%02d_%s.pkl" % (tag, i, on))
        if os.path.exists(ck):
            with open(ck, "rb") as fh:
                payload = pickle.load(fh)
            assert payload["reg_hash"] == REG_HASH, \
                "registry drift vs checkpoint %s" % ck
            assert payload["orbit"] == on
            jp = payload["jp"]
            print("   [ckpt] %s loaded (%d terms)" % (ck, len(jp)),
                  flush=True)
            continue
        jp = R1.gm_jet2((on,), orbs, DD, "D43" + tag, seed=jp)
        tmp = ck + ".tmp.%d" % os.getpid()
        with open(tmp, "wb") as fh:
            pickle.dump({"reg_hash": REG_HASH, "orbit": on, "jp": jp},
                        fh, protocol=4)
        os.replace(tmp, ck)
        print("   [ckpt] %s banked (%d terms, %.1fs)"
              % (ck, len(jp), time.time() - t0), flush=True)
    for (n, s), v in jp.items():
        assert not any(k and k[-1] == R1.HIVAR for k in v), \
            "sentinel loss at (%d,%d)" % (n, s)
    return jp


jf = jet_side(R1.FORB, "f")
jg = jet_side(R1.GORB, "g")
print("jets: f %d, g %d terms (%.1fs); assembling rows"
      % (len(jf), len(jg), time.time() - t0), flush=True)
R = D.jrows(jf, jg, DD)
byk = {}
for (n, k), v in R.items():
    if v:
        byk.setdefault(k, {})[n] = v
tmp = OUT + ".tmp.%d" % os.getpid()
with open(tmp, "wb") as fh:
    pickle.dump({"byk": byk, "vars": [v["name"] for v in R1.VARS],
                 "D": DD}, fh, protocol=4)
os.replace(tmp, OUT)
for k in sorted(byk):
    comp = byk[k]
    print("Row_%d: eta components %s" % (k, sorted(comp)), flush=True)
print("DONE %.1fs; banked directionb_tails_D43.pkl" % (time.time() - t0))
