#!/usr/bin/env python3
"""Exact rational point controls at every pole power and Jacobian degree.

The point is substituted in coefficient blocks before multiplying F/G.  Local
composition is independent of engine.local_rows: substitute the actual minor
series in the normalized (t,z) polynomial using Fraction arithmetic.  This is
a point control, NEVER a claim that a restricted point is the full locus.

Targets at the last pole power are used only if the engine provides them via
minor_pole_targets(branch).  Otherwise that obligation is explicitly pending.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time

import sympy as sp

sys.path.insert(0,str(Path(__file__).resolve().parent))
from source_data import SOURCE


def load_engine(path):
    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location("g9966_deep_point_engine", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def add(*polys):
    out = defaultdict(Q)
    for poly in polys:
        for key, value in poly.items():
            out[key] += value
    return {key: value for key, value in out.items() if value}


def mul(left, right, cutoff):
    out = defaultdict(Q)
    for (n, k), value in left.items():
        for (m, j), other in right.items():
            if n + m <= cutoff:
                out[n + m, k + j] += value * other
    return {key: value for key, value in out.items() if value}


def scale(poly, scalar):
    return {key: scalar * value for key, value in poly.items() if scalar * value}


def specialize(poly, assignment):
    out = {}
    for key, expression in poly.items():
        value = sp.expand(sp.sympify(expression).xreplace(assignment))
        if value.free_symbols or not value.is_Rational:
            raise AssertionError(f"nonrational image at {key}: {value}")
        if value:
            out[key] = Q(int(value.p), int(value.q))
    return out


def local_series(branch, assignment):
    def val(name):
        value = assignment.get(sp.Symbol(name), sp.Integer(0))
        return Q(int(value.p), int(value.q))
    data=SOURCE['minor'][branch]
    cover=data['cover']
    generic=int(cover*data['radius_z'])
    result={(generic,1):Q(1)}
    names=('jet0','u','v')
    for integer,name in enumerate(names,1):
        if cover*integer<generic:
            result[cover*integer,0]=val(name)
    if data['partition']==(2,1):
        result[generic,0]=val('minor_a2')
    return cover,add(result)


def compose_local(poly, cover, wseries, cutoff):
    """Compose z=w-1; keys in output are (cover order,generic power)."""
    zseries = add(wseries, {(0, 0): Q(-1)})
    powers = [{(0, 0): Q(1)}]
    for _ in range(max((q for _r, q in poly), default=0)):
        powers.append(mul(powers[-1], zseries, cutoff))
    out = defaultdict(Q)
    for (r, q), value in poly.items():
        for (n, k), coefficient in powers[q].items():
            if cover*r + n <= cutoff:
                out[cover*r+n, k] += value*coefficient
    return {key: value for key, value in out.items() if value}


def polynomial_record(poly):
    return {f"{n},{k}": str(value) for (n, k), value in sorted(poly.items())}


def monic_z_division(numerator, divisor):
    """Q[t][z] division; returns exact quotient/remainder, with no parameter division."""
    degree = max(q for _r,q in divisor)
    leader = {r:v for (r,q),v in divisor.items() if q==degree}
    assert leader == {0:Q(1)}, leader
    remainder = dict(numerator)
    quotient = {}
    while remainder and max(q for _r,q in remainder)>=degree:
        qdegree = max(q for _r,q in remainder)
        band = {r:v for (r,q),v in remainder.items() if q==qdegree}
        for r,value in band.items():
            quotient[r,qdegree-degree] = quotient.get((r,qdegree-degree),Q(0))+value
            for (s,q),coefficient in divisor.items():
                key = (r+s,q+qdegree-degree)
                remainder[key] = remainder.get(key,Q(0))-value*coefficient
                if not remainder[key]:
                    remainder.pop(key,None)
    return quotient,remainder


def row_hash(rows):
    return hashlib.sha256("".join(f"{label}\t{value}\n" for label,value in rows).encode()).hexdigest()


def run(engine_path, branch, output):
    started = time.monotonic()
    engine_hash=hashlib.sha256(engine_path.read_bytes()).hexdigest()
    driver_hash=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    e = load_engine(engine_path)
    k2degree=SOURCE["k2_degree"]
    native_inner=hasattr(e,'inner_state')
    if native_inner:
        native_h3,native_c2,native_c3,inner,major=e.inner_state(branch)
    else:
        k2, inner, major = e.build_major_h2(branch, k2degree)
    outer, outer_free, outer_meta = e.outer_state(7)
    all_free = inner | outer_free
    assignment = dict.fromkeys(all_free, sp.Integer(0))
    localizer = "rho" if branch == "delta2" else "c"
    assignment[sp.Symbol("jet0")] = assignment[sp.Symbol(localizer)] = sp.Integer(1)
    if native_inner:
        nh3=specialize(native_h3,assignment)
        nc2=specialize(native_c2,assignment)
        nc3=specialize(native_c3,assignment)
        power={(0,0):Q(1)}
        for _ in range(SOURCE['inner_power']):
            power=mul(power,nh3,k2degree)
        numeric_k2=add(power,mul(nc2,nh3,k2degree),nc3)
    else:
        numeric_k2 = specialize(k2, assignment)
    numeric_outer = {name: specialize(block, assignment) for name, block in outer.items()}
    cover, wseries = local_series(branch, assignment)
    supports = {name: e.raw_minor_support(branch, name) for name in ("F", "G")}
    maxima = {name: max(table) for name, table in supports.items()}
    cutoff = max(maxima.values())
    if hasattr(e,"h3_branch_map"):
        h3,hvars = e.h3_template()
        hmap,hfree,hmeta = e.h3_branch_map(branch)
        h3resolved = {key:e.substitute_map(sp.sympify(value),hmap) for key,value in h3.items()}
        point_coordinate_type="gate diagnostic K2 output coordinates"
    else:
        h3resolved,_c2,_c3,_free,_meta=e.inner_state(branch)
        point_coordinate_type="new origin candidate in explicit source C2/C3 coordinates; not the old gate assignment"
    numeric_h3 = specialize(h3resolved,assignment)
    lh3 = compose_local(numeric_h3,cover,wseries,cutoff)
    h3leader = min(n for n,_k in lh3)
    h3face = {key:value for key,value in lh3.items() if key[0]==h3leader}
    h3power={(0,0):Q(1)}
    for _ in range(SOURCE['inner_power']):
        h3power=mul(h3power,numeric_h3,k2degree)
    c2,c3 = monic_z_division(add(numeric_k2,scale(h3power,Q(-1))),numeric_h3)
    assert max((q for _r,q in c2),default=-1)<SOURCE['h3_degree']
    assert max((q for _r,q in c3),default=-1)<SOURCE['h3_degree']
    assert add(h3power,mul(c2,numeric_h3,k2degree),c3,scale(numeric_k2,Q(-1)))=={}
    if native_inner:
        assert add(c2,scale(nc2,Q(-1)))=={}
        assert add(c3,scale(nc3,Q(-1)))=={}
    # This inverse map is exact Euclidean division.  It tests the Def 5.1 /
    # Thm 1.1-1.2 source-floor obligations on a point of the diagnostic output ring.
    source_floor_failures={}
    weight_t,weight_z=SOURCE["D2_weight"]
    for name,poly,floor in (("C2",c2,SOURCE["C2_floor"]),("C3",c3,SOURCE["C3_floor"])):
        bad={(r,q):value for (r,q),value in poly.items() if weight_t*r+weight_z*q<floor}
        source_floor_failures[name]={"normalized_weight_floor":floor,
            "nonzero_below_floor_count":len(bad),"first_failures":list(polynomial_record(bad).items())[:12],
            "minimum_nonzero_weight":min((weight_t*r+weight_z*q for r,q in poly),default=None)}
    minor_remainder_failures={}
    for name,poly,power in (('C2',c2,2),('C3',c3,SOURCE['inner_power'])):
        floor=power*SOURCE['minor'][branch]['h3_local_floor']
        local=compose_local(poly,cover,wseries,floor-1)
        minor_remainder_failures[name]={'strict_local_floor':floor,
            'nonzero_below_floor_count':len(local),
            'first_failures':list(polynomial_record(local).items())[:12]}
    lk2 = compose_local(numeric_k2, cover, wseries, cutoff)
    lout = {}
    for name, poly in numeric_outer.items():
        lout[name] = compose_local({(r+1,q):v for (r,q),v in poly.items()},
                                  cover, wseries, cutoff)
    lk2sq = mul(lk2, lk2, cutoff)
    local_fg = {
        "F": add(mul(lk2sq, lk2, cutoff), mul(lout["A2"], lk2, cutoff), lout["A3"]),
        "G": add(lk2sq, mul(lout["B1"], lk2, cutoff), lout["B2"]),
    }
    target_source = "Exact specialized K3 leading face, powered by degree ratios 99/11 and 66/11 (Thm 1.1-1.2)"
    powers=[{(0,0):Q(1)}]
    Fpower=SOURCE["n"]//SOURCE["h3_degree"]
    Gpower=SOURCE["m"]//SOURCE["h3_degree"]
    for i in range(1,Fpower+1):
        powers.append(mul(powers[-1],h3face,cutoff))
    targets = {"F":powers[Fpower],"G":powers[Gpower]}
    if hasattr(e, "minor_pole_targets"):
        raw_targets = e.minor_pole_targets(branch)
        for name in targets:
            value=raw_targets[name]
            if isinstance(value,tuple):
                power,band=value
                value={(power,k):coefficient for k,coefficient in band.items()}
            targets[name]=specialize(value,assignment)
        target_source = "engine.minor_pole_targets(branch), checked after coefficient specialization"
    pole_records, all_pole_rows = [], []
    for n in range(1, cutoff+1):
        rows = []
        for name in ("F", "G"):
            for k in supports[name].get(n, ()):
                value = local_fg[name].get((n,k), Q(0)) - targets[name].get((n,k), Q(0))
                rows.append((f"{name}_local{n}_coord{k}", value))
        all_pole_rows.extend(rows)
        if rows:
            bad = [(label,str(value)) for label,value in rows if value]
            pole_records.append({"local_power":n,"raw_rows":len(rows),
                                 "nonzero_rows":len(bad),"first_failures":bad[:5],
                                 "row_images_sha256":row_hash(rows)})
    zero_outer = all(not poly for poly in numeric_outer.values())
    if zero_outer:
        jacobian = {"all_positive_degree_rows_vanish":True,
                    "all_constant_rows_vanish":True,
                    "proof":"outer=0 => F=h2^3,G=h2^2 => [F,G]=0 identically by product rule",
                    "positive_degree_row_count":sum(range(2,SOURCE["n"]+SOURCE["m"])),
                    "nonzero_constant_localizer_control":{"Jc":1,"ZJ":1,
                        "constant_equation_image":-1,"wrapper_equation_image":0}}
    else:
        jacobian = {"status":"NOT_EVALUATED: nonzero outer point requires explicit full products"}
    stage_records = []
    terminal_stage = max(SOURCE["n"]+SOURCE["m"]-2, cutoff-e.stage_spec(branch,0)["pole_local_power"])
    for stage in range(terminal_stage+1):
        spec = e.stage_spec(branch,stage)
        n = spec["pole_local_power"]
        current = [r for r in pole_records if r["local_power"]<=n]
        first = next((r for r in current if r["nonzero_rows"]),None)
        stage_records.append({"stage":stage,"pole_local_power":n,
                              "point_survives_pole_prefix":first is None,
                              "first_failed_local_power":first["local_power"] if first else None,
                              "point_survives_positive_degree_J":zero_outer})
    # Independent comparison with the engine's local emitter at old gate depth.
    depth = 8 if branch=="delta2" else 16
    sk2 = {k:sp.Rational(v.numerator,v.denominator) for k,v in numeric_k2.items()}
    sout = {name:{k:sp.Rational(v.numerator,v.denominator) for k,v in poly.items()}
            for name,poly in numeric_outer.items()}
    f,g = e.build_FG(sk2,sout,8)
    comparison = []
    for name,poly in (("F",f),("G",g)):
        emitted = e.local_rows(poly,branch,depth)
        for n in range(1,depth+1):
            for k in supports[name].get(n,()):
                actual = sp.expand(sp.sympify(emitted.get((n,k),0)).xreplace(assignment))
                expected = local_fg[name].get((n,k),Q(0))
                assert actual == sp.Rational(expected.numerator,expected.denominator), (name,n,k)
                comparison.append((f"{name}_local{n}_coord{k}",expected))
    point_payload = "".join(f"{v}={assignment[v]}\n" for v in sorted(assignment,key=str))
    first_failure = next((r for r in pole_records if r["nonzero_rows"]),None)
    record = {"type":"EXACT-Q FULL POWER RATIONAL POINT CONTROL; NOT LOCUS RESTRICTION",
              "engine":str(engine_path),"engine_sha256":engine_hash,"driver_sha256":driver_hash,
              "branch":branch,"free_unknown_count":len(all_free),
              "point_coordinate_type":point_coordinate_type,
              "nonzero_assignment":{"jet0":"1",localizer:"1"},
              "every_other_free_coordinate":"0",
              "point_sha256":hashlib.sha256(point_payload.encode()).hexdigest(),
              "minor_series_w":polynomial_record(wseries),"cover":cover,
              "local_maxima":maxima,"target_source":target_source,
              "h3_minor_leading_order":h3leader,"h3_minor_leading_face":polynomial_record(h3face),
              "inverse_K2_output_to_C2_C3":source_floor_failures,
              "inverse_coordinate_map_control":{"monic_Q_t_z_division":True,
                  "quotient_and_remainder_y_degree_bounds_checked":True,
                  "full_K2_reconstruction_identity_checked":True,
                  "native_C2_C3_images_match_division":True if native_inner else "not_applicable"},
              "minor_C2_C3_strict_floor_control":minor_remainder_failures,
              "all_outer_blocks_identically_zero":zero_outer,
              "K2_local_first_nonzero":polynomial_record({k:v for k,v in lk2.items()
                  if k[0]==min((n for n,_ in lk2),default=-1)}),
              "first_pole_failure":first_failure,"pole_powers":pole_records,
              "all_pole_rows":len(all_pole_rows),"all_pole_images_sha256":row_hash(all_pole_rows),
              "stages":stage_records,"Jacobian":jacobian,
              "independent_local_emitter_control":{"depth":depth,"compared_rows":len(comparison),
                  "all_match":True,"images_sha256":row_hash(comparison)},
              "elapsed_seconds":round(time.monotonic()-started,3)}
    output.write_text(json.dumps(record,indent=2,default=str)+"\n")
    print(json.dumps({"branch":branch,"first_pole_failure":first_failure,"zero_outer":zero_outer,
                      "output":str(output),"elapsed_seconds":record["elapsed_seconds"]}),flush=True)


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--engine",type=Path,required=True)
    parser.add_argument("--branch",choices=["delta2","delta52"],required=True)
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    run(args.engine.resolve(),args.branch,args.output.resolve())
