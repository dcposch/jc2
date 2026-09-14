#!/usr/bin/env python3
"""Independent exact D1 graph/quadratic ideal equivalence and NF audit."""
import hashlib,json,subprocess
from pathlib import Path
import sympy as sp
N=Path(__file__).resolve().parent
d,e=sp.symbols('Zface_H2_2 Zface_H2_5')
b1,b4,b7=sp.symbols('Zface_B2_1 Zface_B2_4 Zface_B2_7');ZJ=sp.Symbol('ZJ')
records=[]
for branch in ('delta2','delta52'):
    phasepath=N/f'deep_resume_graph_safe_{branch}_D1_J_phase.json';phase=json.loads(phasepath.read_text())
    rawpath=N/f'deep_resume_graph_safe_{branch}_D1_J.sing.out';raw=rawpath.read_text()
    sec=raw.split('BEGIN_GB\n')[1].split('\nEND_GB')[0]
    B=[sp.sympify(v.strip().replace('^','**')) for v in sec.split(',') if v.strip()]
    I=[sp.sympify(v) for _,v in phase['residual_after']]
    loc=sp.Symbol('rho' if branch=='delta2' else 'c');inv=sp.Symbol('Zrho' if branch=='delta2' else 'Zc')
    I.append(loc*inv-1)
    # Independently choose the three linear face relations and solve them
    # in descending B2 degree. Every denominator is a displayed QQ unit.
    graph={};pivots=[]
    for variable,wanted in ((b7,{b7,d,e}),(b4,{b4,b7,d,e}),(b1,{b1,b4,b7,d,e})):
        eligible=[]
        for index,row in enumerate(B):
            if variable in row.free_symbols and row.free_symbols<=wanted:
                image=sp.expand(row.xreplace(graph));lead=sp.diff(image,variable)
                if lead.is_Rational and lead!=0:eligible.append((index,image,lead))
        assert eligible
        index,row,lead=eligible[0]
        rhs=sp.expand(-(row-lead*variable)/lead)
        assert variable not in rhs.free_symbols
        graph[variable]=rhs
        pivots.append({'GB_index':index,'variable':str(variable),'equation_after_prior_graph':str(row),'rational_leader':str(lead),'rhs':str(rhs)})
    transformed=[sp.expand(row.xreplace(graph)) for row in B]
    candidates=[]
    for index,row in enumerate(transformed):
        if row!=0 and row.free_symbols<={d,e}:
            poly=sp.Poly(row,d)
            if poly.degree()==2 and poly.LC().is_Rational and poly.LC()!=0:
                candidates.append((index,sp.expand(poly.monic().as_expr()),row,poly.LC()))
    assert candidates
    index,q,qsource,leader=candidates[0]
    assert all(sp.expand(other-q)==0 for _,other,_,_ in candidates)
    qa=-sp.Poly(q,d,e).coeff_monomial(d*e**2);qb=sp.Poly(q,d,e).coeff_monomial(e**4)
    assert q==d*d-qa*d*e*e+qb*e**4
    nf=lambda f:sp.Poly(sp.expand(f),d).rem(sp.Poly(q,d)).as_expr()
    # The only residual condition besides q and the graphs is the actual
    # nonzero-J inverse, reduced as one combined scalar polynomial.
    mapped=[sp.expand(row.xreplace(graph)) for row in I]
    images=[sp.expand(nf(row)) for row in mapped]
    assert images[:-2]==[0,0,0,0]
    assert images[-1]==loc*inv-1
    scalar=images[-2];assert scalar.has(ZJ) and scalar.subs(ZJ,0)==-1
    graphs=[v-rhs for v,rhs in graph.items()]
    model=graphs+[q,scalar,loc*inv-1]
    variables=sorted(set().union(*(row.free_symbols for row in I+model+B)),key=str)
    def encode(row):
        den,poly=sp.Poly(row,*variables,domain=sp.QQ).clear_denoms()
        assert den.is_Rational and den!=0
        return str(poly.as_expr()).replace('**','^')
    script='ring R=0,('+','.join(map(str,variables))+'),dp;\n'
    script+='ideal I='+','.join(map(encode,I))+';\nideal B='+','.join(map(encode,B))+';\nideal M='+','.join(map(encode,model))+';\n'
    script+='ideal SI=std(I);ideal SB=std(B);ideal SM=std(M);\n'
    script+='print("BEGIN_AUDIT");print(size(reduce(I,SB)));print(size(reduce(B,SI)));print(size(reduce(I,SM)));print(size(reduce(M,SI)));print(dim(SI));print(dim(SM));print(reduce(1,SI));print("END_AUDIT");\n'
    script+=f'ideal Empty={loc},{loc}*{inv}-1;ideal Point={loc}-1,{loc}*{inv}-1;\n'
    script+='print("BEGIN_WRAPPERS");print(reduce(1,std(Empty)));print(reduce(1,std(Point)));print("END_WRAPPERS");quit;\n'
    path=N/f'print-audit-quotient-d1-{branch}.sing';path.write_text(script)
    run=subprocess.run(['Singular','-q',str(path)],text=True,capture_output=True,check=True,timeout=120)
    path.with_suffix('.sing.out').write_text(run.stdout+run.stderr)
    vals=run.stdout.split('BEGIN_AUDIT\n')[1].split('\nEND_AUDIT')[0].splitlines();assert vals==['0','0','0','0','2','2','1'],run.stdout
    assert run.stdout.split('BEGIN_WRAPPERS\n')[1].split('\nEND_WRAPPERS')[0].splitlines()==['0','1']
    # Compare independent graph/quadratic with the production adjoin-only
    # seed; both must derive the same actual source relations.
    seedpath=N/f'deep_quotient_seed_control_{branch}.json';seed=json.loads(seedpath.read_text())
    assert {str(v):str(rhs) for v,rhs in graph.items()}==seed['derived_graph_map']
    assert sp.sympify(seed['quotient']['polynomial'])==q
    records.append({'branch':branch,'field':'Q','ring_generator_order':list(map(str,variables)),
        'original_D1_rows':[[label,row] for label,row in phase['residual_after']],
        'localized_wrapper':str(loc*inv-1),'independent_graph_pivots':pivots,
        'derived_graph_map':{str(v):str(rhs) for v,rhs in graph.items()},
        'quadratic_source_GB_index':index,'quadratic_source_after_graph':str(qsource),'quadratic_monic_leader_divisor':str(leader),
        'quotient':{'d':str(d),'e':str(e),'a':str(qa),'b':str(qb),'polynomial':str(q)},
        'remaining_combined_nonzero_J_relation':str(scalar),'model_generators':list(map(str,model)),
        'original_ideal_equals_stored_GB_both_inclusions':True,'original_ideal_equals_graph_quadratic_inverse_model_both_inclusions':True,
        'active_ring_dimension_before':2,'active_ring_dimension_after':2,'same_as_production_adjoin_seed':True,
        'custody':{str(p.name):hashlib.sha256(p.read_bytes()).hexdigest() for p in (phasepath,rawpath,seedpath,path)}})
assert records[0]['quotient']==records[1]['quotient']
# Check the exact recurrence against monic polynomial division for powers
#0..40, including their full e weights, without choosing either root.
q=sp.sympify(records[0]['quotient']['polynomial']);qa=sp.Rational(records[0]['quotient']['a']);qb=sp.Rational(records[0]['quotient']['b'])
rec=[(sp.Integer(0),sp.Integer(1)),(sp.Integer(1),sp.Integer(0))]
for n in range(2,41):
    A,B=rec[-1];rec.append((qa*A+B,-qb*A))
for n,(A,B) in enumerate(rec):
    expected=sp.Integer(1) if n==0 else A*d*e**(2*n-2)+B*e**(2*n)
    assert sp.Poly(d**n-expected,d).rem(sp.Poly(q,d)).is_zero
# Generic branch-preservation negative control requested by the root.
d0,e0=sp.symbols('d e');q0=d0*d0-e0;row=d0-1
G=sp.groebner([q0,row],d0,e0);assert all(p.as_expr()!=1 for p in G.polys)
assert q0.subs({d0:1,e0:1})==0 and row.subs({d0:1,e0:1})==0
assert q0.subs({d0:-1,e0:1})==0 and row.subs({d0:-1,e0:1})==-2
split=sp.groebner([q0,-1,1],d0,e0);assert len(split.polys)==1 and split.polys[0].as_expr()==1
# Actual q retains two conjugates over Q(sqrt(discriminant)); no choice is
# made, and recurrence identities hold modulo the same monic q.
discriminant=sp.factor(qa**2-4*qb);assert discriminant!=0 and discriminant<0
for n in (2,3,8):
    A,B=rec[n]
    for sign in (-1,1):
        root=(qa+sign*sp.sqrt(discriminant))/2
        assert sp.simplify(root**n-A*root-B)==0
result={'status':'PASS','records':records,'normal_form':'sum c_n*d^n -> combined A+B*d in Q[other_coordinates,e][d]/(q); never emit module coefficients as separate equations',
 'recurrence':{'initial_0':['0','1'],'initial_1':['1','0'],'step':'A_(n+1)=a*A_n+B_n; B_(n+1)=-b*A_n','image_n':'A_n*d*e^(2n-2)+B_n*e^(2n)','checked_powers':list(range(41))},
 'q_discriminant':str(discriminant),'actual_both_conjugate_controls':True,
 'negative_coefficient_splitting':{'q':'d^2-e','combined_row':'d-1','point_d1_e1_satisfies':True,'other_conjugate_dminus1_e1_row':-2,'combined_ideal_nonunit':True,'split_coefficients_ideal_unit':True},
 'normal_form_proof':'Monic Euclidean division uses no parameter inversion. Each row-minus-normalform is a multiple of retained q, so adjoining either row gives the identical ideal with q. Derivatives in t,w commute since q has coefficients only in parameter coordinates.',
 'audit_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps({'status':'PASS','branches':2,'ideal_inclusions_per_branch':4,'dimension_before_after':[2,2],'recurrence_powers':41,'q':str(q),'both_actual_conjugates_checked':True,'splitting_negative_control':'PASS'},indent=2))
