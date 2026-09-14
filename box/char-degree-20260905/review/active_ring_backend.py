#!/usr/bin/env python3
"""First four exact divisions in the occurring-variable ring; then embed.

Every ambient coordinate is restored before characteristic/source rows.
The original backend is left unchanged.  The ordered generator injection,
its images, full source h/D image checks and output identities are emitted.
"""
from pathlib import Path
import hashlib,json,re,sys
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'d108'))
from normalized_backend import normalized_script

IDENT=re.compile(r'\b[A-Za-z_][A-Za-z_0-9]*\b')

def active_normalized_script(h_expr,D_expr,C_expr,residual_strings,names,k,target,face_expr,
                             leader_name=None,leader_inverse=None,localizer_rows=('Zc*c-1',),
                             predefinitions=(),check_full_source_images=True,
                             division_only=False):
    names=list(names);assert len(names)==len(set(names))
    assert all(IDENT.fullmatch(name) for name in names)
    predefinitions=list(predefinitions)
    definitions=dict(predefinitions);assert len(definitions)==len(predefinitions)
    assert not set(definitions).intersection(set(names)|{'zz','tt','RDIV','R'})
    roots=set(IDENT.findall(h_expr+' '+D_expr))|{'target_a','target_b'}
    needed=set();todo=list(roots)
    while todo:
        name=todo.pop()
        if name in needed:continue
        needed.add(name)
        if name in definitions:todo.extend(IDENT.findall(definitions[name]))
    assert needed<=set(names)|set(definitions)|{'zz','tt'},needed-set(names)-set(definitions)-{'zz','tt'}
    active=[name for name in names if name in needed]
    active_definitions=[(name,expr) for name,expr in predefinitions if name in needed]
    defined=set(active)|{'zz','tt'}
    for name,expression in active_definitions:
        assert set(IDENT.findall(expression))<=defined,('forward/unknown definition',name)
        defined.add(name)
    assert set(IDENT.findall(h_expr+' '+D_expr))<=defined
    base=normalized_script(h_expr,D_expr,C_expr,residual_strings,names,k,target,face_expr,
                           leader_name,leader_inverse,localizer_rows)
    lines=base.splitlines()
    assert lines[4].startswith('poly aa=') and lines[5].startswith('poly pp=') and lines[7].startswith('poly VV=')
    first=next(i for i,l in enumerate(lines) if l.startswith('print("BEGIN_DIVIDE_vv2")'))
    last=next(i for i,l in enumerate(lines) if l.startswith('poly derivedV='))
    division_lines=lines[first:last]
    # Drop intermediate containers after extracting each output.  Retaining
    # all list/matrix/ideal copies needlessly extends their lifetimes.
    division_lines=list(division_lines)
    for i,(quo,rem) in enumerate([('UU','RR'),('PP','RR1'),('Qpart','RR2'),('WW','RR3')]):
        old=f'matrix M{i}=L{i}[1];ideal N{i}=L{i}[2];poly {quo}=M{i}[1,1];poly {rem}=N{i}[1];'
        new=f'print("DIVISION{i}_RETURNED");matrix M{i}=L{i}[1];ideal N{i}=L{i}[2];kill L{i};poly {quo}=M{i}[1,1];kill M{i};poly {rem}=N{i}[1];kill N{i};'
        assert sum(old in line for line in division_lines)==1
        division_lines=[line.replace(old,new) for line in division_lines]
    old_generators=['zz','tt']+active
    full_generators=['zz','tt']+names
    script=[f'ring RDIV=0,({",".join(old_generators)}),(lp(1),dp({len(active)+1}));',
            'option(redSB);print("BEGIN_BUILD_ACTIVE_RING");',
            *[f'poly {name}={expression};' for name,expression in active_definitions],
            f'poly h={h_expr};poly D={D_expr};',
            f'poly H=h-(1/6)*target_b*tt^{k};',
            f'poly vv=D+((1/3)*target_a+(1/18)*target_b^2)*tt^{2*k-1};',
            # lp(1) makes this an exact leader rather than a name assumption.
            f'if(lead(H)!=zz^{k}){{ERROR("H is not monic z-degree k");}}',
            *division_lines]
    if division_only:
        script+=['print("ACTIVE_DIVISIONS_COMPLETE");quit;']
    else:
        outputs=['h','D','H','vv','UU','RR','PP','RR1','Qpart','RR2','WW','RR3']
        # Identity of generator images proves this is an injective polynomial
        # extension, with no evaluation of the omitted ambient coordinates.
        script += ['ideal activeGenerators='+','.join(old_generators)+';',
                   lines[0],
                   'option(redSB);print("BEGIN_EMBED_FULL_RING");',
                   'ideal injectedGenerators=imap(RDIV,activeGenerators);']
        script += [f'if(injectedGenerators[{i+1}]-{name}!=0){{ERROR("generator image {i} failed");}}'
                   for i,name in enumerate(old_generators)]
        script += [f'poly {name}=imap(RDIV,{name});setring RDIV;kill {name};setring R;' for name in outputs]
        if check_full_source_images:
            script += [f'poly {name}={expression};' for name,expression in active_definitions]
            script += [f'poly sourceImageH={h_expr};poly sourceImageD={D_expr};',
                       'if(h-sourceImageH!=0){ERROR("full h source image failed");}',
                       'if(D-sourceImageD!=0){ERROR("full D source image failed");}',
                       'kill sourceImageH,sourceImageD;']
        script += [f'if(H-h+(1/6)*target_b*tt^{k}!=0){{ERROR("shifted H image failed");}}',
                   f'if(vv-D-((1/3)*target_a+(1/18)*target_b^2)*tt^{2*k-1}!=0){{ERROR("shifted v image failed");}}',
                   'print("END_EMBED_FULL_RING");kill RDIV;',
                   f'poly C={C_expr};',lines[4],lines[5],lines[7],*lines[last:]]
    text='\n'.join(script)+'\n'
    record={'field':'Q','active_generator_order':old_generators,'full_generator_order':full_generators,
            'generator_map':[{'source_index':i+1,'source':name,'target_index':full_generators.index(name)+1,
                              'target':name} for i,name in enumerate(old_generators)],
            'omitted_during_division_only':[name for name in names if name not in active],
            'all_source_coordinates_restored_before_rows':not division_only,
            'temporary_division_containers_released':True,
            'mapped_polynomials_released_incrementally':not division_only,
            'source_h_D_images_checked':check_full_source_images and not division_only,
            'division_only':division_only,'source_input_hashes':{key:hashlib.sha256(value.encode()).hexdigest()
                for key,value in [('h',h_expr),('D',D_expr),('C',C_expr),('residuals','\n'.join(residual_strings))]},
            'predefinitions':[name for name,_ in active_definitions],
            'original_backend_script_sha256':hashlib.sha256(base.encode()).hexdigest(),
            'script_sha256':hashlib.sha256(text.encode()).hexdigest(),
            'backend_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    return text,record

def from_g9966_input(inputpath):
    import sympy as sp
    from char_degree_driver import exprS
    data=json.loads(Path(inputpath).read_text());maps=data['maps'];branch=data['branch']
    def poly(tab):return '+'.join(f'({exprS(sp.sympify(v))})*tt^{r}*zz^{q}' for r,q,v in tab) or '0'
    sep='rho' if branch=='delta2' else 'c';inverse='Zrho' if branch=='delta2' else 'Zc'
    names=sorted(set(data['full_free_coordinates'])|{sep,inverse})
    kwargs={'h_expr':'baseH^3+innerC2*baseH+innerC3','D_expr':poly(maps['B2']),
            'C_expr':poly(maps['A3']),'residual_strings':[exprS(sp.sympify(v)) for _,v in data['residual_rows']],
            'names':names,'k':33,'target':55,'face_expr':'zz^16*(1+zz)^6',
            'leader_name':'leader55','leader_inverse':'Z55','localizer_rows':(inverse+'*'+sep+'-1',),
            'predefinitions':[(name,poly(maps[key])) for name,key in [('baseH','h3'),('innerC2','C2'),('innerC3','C3')]]}
    return kwargs

if __name__=='__main__':
    import argparse
    ap=argparse.ArgumentParser();ap.add_argument('--g9966-input',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True);ap.add_argument('--division-only',action='store_true')
    args=ap.parse_args();script,record=active_normalized_script(**from_g9966_input(args.g9966_input),division_only=args.division_only)
    args.out.parent.mkdir(parents=True,exist_ok=True);args.out.write_text(script)
    args.out.with_suffix('.map.json').write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:record[k] for k in ('script_sha256','division_only')})+' '+str(len(record['active_generator_order']))+'/'+str(len(record['full_generator_order'])))
