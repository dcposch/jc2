#!/usr/bin/env python3
"""Verify both antecedent source graphs, their merge, and final Jacobian rows.

No graph is inferred by deleting solved coordinates. Every pivot is replayed
in its declared ring, and the actual source-coordinate identity map between
the two antecedents is checked before their relations are combined.
"""
from pathlib import Path
import argparse,hashlib,json,re,subprocess,sys,time
import sympy as sp
HERE=Path(__file__).resolve().parent;sys.path.insert(0,str(HERE))
import minor_final_verify as M


def read(path):return json.loads(Path(path).read_text())


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--merged',type=Path,required=True)
    ap.add_argument('--source-result',type=Path,required=True)
    ap.add_argument('--weak-result',type=Path,required=True)
    ap.add_argument('--code-dir',type=Path,required=True)
    ap.add_argument('--weak-code-dir',type=Path,required=True)
    ap.add_argument('--driver',type=Path,required=True)
    ap.add_argument('--backend',type=Path)
    ap.add_argument('--quotient-seed',type=Path)
    ap.add_argument('--execution-config',type=Path)
    ap.add_argument('--execution-runner',type=Path)
    ap.add_argument('--ancestor-driver',type=Path,action='append',default=[])
    ap.add_argument('--ancestor-backend',type=Path,action='append',default=[])
    ap.add_argument('--safe-exporter',type=Path,required=True)
    ap.add_argument('--certificate-root',type=Path,action='append',default=[])
    ap.add_argument('--verified-prefix',type=Path)
    ap.add_argument('--verified-prefix-input',type=Path)
    ap.add_argument('--trusted-verifier-code',type=Path,action='append',default=[])
    ap.add_argument('--out',type=Path,required=True)
    ap.add_argument('--graphs-only',action='store_true')
    ap.add_argument('--jacobian-method',choices=['direct','factored','flint-direct'],default='direct')
    a=ap.parse_args();start=time.monotonic();M.PATH_ROOTS.extend(path.resolve() for path in a.certificate_root)
    merged=read(a.merged);source=read(a.source_result);weaksource=read(a.weak_result)
    branch=merged['branch'];assert source['branch']==weaksource['branch']==branch
    assert merged['field']=='Q'
    own_hash=M.digest(__file__);core_hash=M.digest(HERE/'minor_final_verify.py')
    cached=None;cache_record=None
    if a.verified_prefix:
        assert a.verified_prefix_input,'verified prefix needs its exact previously verified input'
        cached=read(a.verified_prefix);cached_input=read(a.verified_prefix_input)
        assert cached['status']=='PASS' and cached['branch']==branch
        assert M.digest(a.verified_prefix_input)==cached['merged_result_sha256'],'verified prefix input custody mismatch'
        trusted=[HERE,*a.trusted_verifier_code]
        assert any(M.digest(directory/'minor_merged_verify.py')==cached['verifier_sha256'] and M.digest(directory/'minor_final_verify.py')==cached['verifier_core_sha256_at_start'] for directory in trusted),'prefix verifier code is not an explicit frozen trusted snapshot'
        for key in ['strong_checkpoint_sha256','strong_summary_sha256','weak_checkpoint_sha256','weak_complete_free_ring','code_sha256']:
            assert cached_input[key]==merged[key],('cached prefix comes from another source/antecedent chart',key)
        cache_record={'path':str(a.verified_prefix.resolve()),'sha256':M.digest(a.verified_prefix),
                      'input_path':str(a.verified_prefix_input.resolve()),'input_sha256':M.digest(a.verified_prefix_input),
                      'loaded_verifier_sha256':cached['verifier_sha256'],'loaded_core_sha256':cached['verifier_core_sha256_at_start'],
                      'basis':'previously executed independent verification, exact source identity and every reused phase hash rechecked'}
    execution=None
    if a.execution_config:
        execution=read(a.execution_config)
        assert a.execution_runner and execution['runner_sha256']==M.digest(a.execution_runner)
        assert execution['driver_sha256']==merged['driver_sha256'] and isinstance(execution['threads'],int) and execution['threads']>0
    assert M.digest(a.driver)==merged['driver_sha256'],'merge driver custody mismatch'
    if 'coefficient_backend_sha256' in merged:
        assert a.backend and M.digest(a.backend)==merged['coefficient_backend_sha256'],'coefficient backend custody mismatch'
    if merged.get('coefficient_quotient'):
        assert a.quotient_seed and M.digest(a.quotient_seed)==merged['quotient_seed_sha256'],'quotient seed code custody mismatch'
        assert merged['quotient_transition']['driver_sha256']==merged['quotient_seed_sha256']
    assert M.digest(a.safe_exporter)==merged['safe_exporter_sha256'],'safe exporter custody mismatch'
    for name,value in merged['code_sha256'].items():assert M.digest(a.code_dir/name)==value,('strong code custody',name)
    for obj,directory in [(source,a.code_dir),(weaksource,a.weak_code_dir)]:
        for key,name in [('engine_sha256','engine.py'),('source_derivation_sha256','source_data.py'),('helpers_sha256','deep_rows.py'),('driver_sha256','deep_driver.py')]:
            assert obj[key]==M.digest(directory/name),('antecedent code custody',name)
        assert obj['initial_inner']['gauge_slice']['wrapper_sha256']==M.digest(directory/'deep_gauge_accelerated.py')
    E=M.load_code(a.code_dir,gauge=True);v=M.Verifier(E,branch);v.native_map_verification=True
    sourcecheck=v.check_source(source);weakcheck=v.check_source(weaksource)
    weakimages_path=a.out.with_name(a.out.stem+'-weak-source-images.json')
    image_helper=HERE/'minor_weak_source_image.py'
    subprocess.run([sys.executable,str(image_helper),'--code',str(a.weak_code_dir),'--branch',branch,'--out',str(weakimages_path)],check=True)
    weakimages=read(weakimages_path)
    images={'h3':v.h,'C2':v.c2,'C3':v.c3,**v.outer}
    strong_images={'field':'Q','branch':branch,'ordered_generators':sorted(map(str,v.basefree)),
        'source_images':{name:[[r,q,str(sp.expand(value))] for (r,q),value in sorted(poly.items())] for name,poly in images.items()},
        'initial_residue':[[label,str(sp.expand(value))] for label,value in v.major['additional_rows']],
        'outer_specs':E.jsonable(v.S['outer_specs']) if hasattr(E,'jsonable') else {k:list(value) for k,value in v.S['outer_specs'].items()},
        'gauge':{'jet0':'0'}}
    assert strong_images==weakimages['payload'],'separately imported antecedent source images differ'
    source_image_hash=hashlib.sha256(json.dumps(strong_images,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    assert source_image_hash==weakimages['payload_sha256']
    if merged.get('ring_transport'):
        assert merged['ring_transport']['source_images_sha256']==source_image_hash
    # check_source rebuilds every h3/source image and the outer source box.
    # The coefficient engine and source derivation are also byte-identical;
    # wrappers have different later hooks but identical checked source images.
    assert source['engine_sha256']==weaksource['engine_sha256']
    assert source['source_derivation_sha256']==weaksource['source_derivation_sha256']
    assert merged['weak_complete_free_ring']==sorted(map(str,v.basefree))
    transport={'field':'Q','source_images_rebuilt_and_equal':True,
               'strong_source':sourcecheck,'weak_source':weakcheck,
               'actual_separately_imported_source_images_sha256':source_image_hash,
               'weak_source_image_certificate_sha256':M.digest(weakimages_path),
               'ordered_generator_map':[[str(x),str(x)] for x in sorted(v.basefree,key=str)]}
    transport['ordered_generator_map_sha256']=hashlib.sha256(json.dumps(transport['ordered_generator_map'],separators=(',',':')).encode()).hexdigest()
    summarypath=M.local_certificate_path(merged['strong_summary'],a.merged.resolve())
    assert M.digest(summarypath)==merged['strong_summary_sha256'];summary=read(summarypath)
    graph=[x for x in summary['phases'] if x['name']=='D1_graph'];assert len(graph)==1
    meta=graph[0]['derivation'];declared=meta['protected_during_graph_elimination']
    assert len(declared)==len(set(declared)) and all(re.fullmatch(r'Zface_(H2|A2|A3|B1|B2)_\d+',x) for x in declared)
    v.extra_generators=set(map(sp.Symbol,declared));assert not v.extra_generators&set(v.locals.values())
    v.locals.update({str(x):x for x in v.extra_generators})
    face_locals={**v.locals,'Pi':sp.Symbol('Pi')};v.graph_faces={}
    assert set(meta['graph_faces'])=={'H2','A2','A3','B1','B2'}
    for name,value in meta['graph_faces'].items():
        assert set(re.findall(r'[A-Za-z_][A-Za-z_0-9]*',value))<=set(face_locals)
        expr=sp.sympify(value,locals=face_locals)
        assert not expr.atoms(sp.Float) and all(p.exp.is_Integer and p.exp>=0 for p in expr.atoms(sp.Pow))
        assert expr.free_symbols<=v.extra_generators|{sp.Symbol('Pi')}
        v.graph_faces[name]=expr
    def paths(links,serial=False):
        out=[]
        for i,link in enumerate(links):
            path=M.local_certificate_path(link['path'],a.merged.resolve())
            assert M.digest(path)==link['sha256'],('phase custody mismatch',path)
            if serial:assert re.search(r'_phase%04d\.json$'%i,path.name),'noncontiguous saved source chain'
            out.append(path)
        return out
    quotient_audits=[]
    def activate_quotient(cert):
        assert merged.get('coefficient_quotient'),'transition lacks declared quotient data'
        import minor_quotient_transition_verify as QV
        assert Path(QV.__file__).resolve().parent==HERE
        report=QV.verify(v,cert,merged['quotient_transition'],merged['coefficient_quotient'],a.out.with_name(a.out.stem+'-quotient-transition.sing'))
        quotient_audits.append(report)
        return report
    def replay(chain,label,initial=None,regen_new=False,cache_key=None):
        reports=[];previous=initial
        offset=0
        if cached and cache_key:
            certified=cached[cache_key];offset=len(certified)
            assert offset<=len(chain)
            assert [M.digest(path) for path in chain[:offset]]==[report['sha256'] for report in certified],('cached phase-prefix identity differs',cache_key)
            if offset:
                first=read(chain[0])
                if initial is None:assert first['phase']=='source_residue' and not first['map_before'] and not first['residual_before']
                else:
                    assert v.equal_map(v.mapping(initial['map_after']),v.mapping(first['map_before']))
                    assert v.rows(initial['residual_after'])==v.rows(first['residual_before'])
                reports=list(certified);previous=read(chain[offset-1])
                print(f'{label}: reused {offset} hash-bound independently verified phases',flush=True)
                for _path in chain[:offset]:
                    _cert=read(_path)
                    if _cert['phase']=='certified_quotient_transition':activate_quotient(_cert)
        for i,path in enumerate(chain[offset:],start=offset):
            cert=read(path)
            if previous is None:
                assert cert['phase']=='source_residue' and not cert['map_before'] and not cert['residual_before']
            else:
                assert v.equal_map(v.mapping(previous['map_after']),v.mapping(cert['map_before'])),('antecedent chain map mismatch',label,i)
                assert v.rows(previous['residual_after'])==v.rows(cert['residual_before']),('antecedent chain residual mismatch',label,i)
            transition=activate_quotient(cert) if cert['phase']=='certified_quotient_transition' else None
            report={'path':str(path),'sha256':M.digest(path),**v.replay_phase(cert)}
            if transition:report['independent_quotient_transition']=transition
            if regen_new and cert['phase'] in ('D1_graph','D1_J','corner_J','merge_weak_complete_graph'):
                report['raw_regeneration']=v.regenerate(cert,a.jacobian_method)
            reports.append(report);previous=cert
            if label=='merged/full-J chain' or i%25==0 or i==len(chain)-1:print(f'{label}: verified {i+1}/{len(chain)} {cert["phase"]}',flush=True)
        return previous,reports
    weakpaths=paths(merged['weak_chain'],True)
    assert M.digest(weakpaths[-1])==merged['weak_checkpoint_sha256']
    weak,weakreports=replay(weakpaths,'weak source/J chain',cache_key='weak_source_chain')
    v.weak_map=v.mapping(weak['map_after']);v.weak_residual=v.rows(weak['residual_after'])
    assert v.equal_map(v.weak_map,v.mapping(merged['weak_map_after']))
    assert v.weak_residual==v.rows(merged['weak_residual_after'])
    assert sorted(map(str,v.weak_map))==merged['weak_graph_targets']
    jphases=[]
    for path in weakpaths:
        match=re.fullmatch(r'(?:deep|stage)(\d+)_Jacobian',read(path)['phase'])
        if match:jphases.append(int(match.group(1)))
    assert merged['weak_J_bands_already_proved']==list(range(max(jphases)+1))
    assert set(range(max(jphases)+1))<=set(jphases)
    strongpaths=paths(merged['strong_antecedent_chain'],True)+paths(merged['strong_added_phases'])
    assert M.digest(strongpaths[-1])==merged['strong_checkpoint_sha256']
    strong,strongreports=replay(strongpaths,'strong printed-face chain',regen_new=True,cache_key='strong_printed_face_chain')
    assert sorted(set(strong['map_after'])|set(strong['free_after']))==merged['initial_complete_free_ring']
    ancestry=[]
    def continuation_paths(state):
        previous=[]
        if state.get('resumed_from'):
            link=state['resumed_from']
            statepath=M.local_certificate_path(link['state'],a.merged.resolve())
            assert M.digest(statepath)==link['state_sha256'],'resumed state custody mismatch'
            antecedent=read(statepath)
            assert antecedent['branch']==branch and antecedent['field']=='Q'
            assert antecedent['driver_sha256'] in {M.digest(path) for path in a.ancestor_driver},'ancestor driver custody unavailable'
            if 'coefficient_backend_sha256' in antecedent:
                assert antecedent['coefficient_backend_sha256'] in {M.digest(path) for path in a.ancestor_backend},'ancestor backend custody unavailable'
            for key in ['strong_checkpoint_sha256','strong_summary_sha256','weak_checkpoint_sha256','weak_complete_free_ring','code_sha256','safe_exporter_sha256']:
                assert antecedent[key]==state[key],('resumed antecedent/source mismatch',key)
            assert antecedent['phase_certificates']==link['all_preceding_phase_certificates']
            terminal=M.local_certificate_path(link['terminal_phase'],a.merged.resolve())
            last_link=(antecedent['phase_certificates'][-1] if antecedent['phase_certificates'] else {'sha256':antecedent['resumed_from']['terminal_phase_sha256']})
            assert M.digest(terminal)==link['terminal_phase_sha256']==last_link['sha256']
            last=read(terminal)
            assert last['phase']==f'Jacobian_t{antecedent["last_completed_t"]}' or (last['phase']=='certified_quotient_transition' and antecedent.get('coefficient_quotient'))
            if antecedent.get('coefficient_quotient'):
                assert antecedent['coefficient_quotient']==state['coefficient_quotient'] and antecedent['quotient_transition']==state['quotient_transition'],'resumed coefficient quotient or its proof was changed'
            assert v.equal_map(v.mapping(last['map_after']),v.mapping(antecedent['cumulative_map']))
            assert v.rows(last['residual_after'])==v.rows(antecedent['residual_rows'])
            assert state['inherited_J_bands_already_proved']==list(range(antecedent['last_completed_t']+1))
            previous=continuation_paths(antecedent)
            ancestry.append({'state_path':str(statepath),'sha256':M.digest(statepath),
                             'terminal_phase_sha256':M.digest(terminal),'through_t':antecedent['last_completed_t']})
        return previous+paths(state['phase_certificates'],True)
    newpaths=continuation_paths(merged);assert newpaths
    new_j=[]
    for path in newpaths:
        match=re.fullmatch(r'Jacobian_t(\d+)',read(path)['phase'])
        if match:new_j.append(int(match.group(1)))
    if new_j:
        assert new_j==list(range(max(jphases)+1,max(new_j)+1)),'merged Jacobian band schedule has a gap or duplication'
        assert merged['last_completed_t']<=max(new_j)<=merged['last_completed_t']+1,'endpoint completion metadata differs from saved phase chain'
    final,newreports=replay(newpaths,'merged/full-J chain',initial=strong,regen_new=True,cache_key='merged_J_chain')
    terminal_regeneration=({'status':'NOT_PERFORMED','scope':'complete graph chain and final residual ideal only; terminal raw source band not independently regenerated'} if a.graphs_only else (quotient_audits[-1] if final['phase']=='certified_quotient_transition' else v.regenerate(final,a.jacobian_method)))
    assert v.equal_map(v.mapping(final['map_after']),v.mapping(merged['cumulative_map']))
    assert v.rows(final['residual_after'])==v.rows(merged['residual_rows'])
    assert E.rows_hash(v.rows(final['residual_after']))==merged['residual_hash']
    singular=M.singular_replay(v.rows(final['residual_after']),branch,len(final['free_after']),a.out.with_suffix('.sing'))
    assert singular['full_dimension']==merged['records'][-1]['dimension']
    assert singular['unit_ideal']==merged['records'][-1]['unit_ideal']
    out={'status':('GRAPH_CHAIN_AND_FINAL_IDEAL_VERIFIED' if a.graphs_only else 'PASS'),'not_a_complete_raw_row_verification':bool(a.graphs_only),'type':'INDEPENDENT TWO-ANTECEDENT FULL-SOURCE CHART VERIFICATION','branch':branch,
         'merged_result_sha256':M.digest(a.merged),'source_transport':transport,
         'weak_source_chain':weakreports,'strong_printed_face_chain':strongreports,'merged_J_chain':newreports,
         'resume_ancestry':ancestry,'execution_configuration':execution,
         'verified_prefix_cache':cache_record,'independent_quotient_audits':quotient_audits,
         'last_verified_J_t':max(new_j) if new_j else max(jphases),
         'terminal_raw_regeneration':terminal_regeneration,'Singular':singular,
         'gauge_isomorphism_audit':'minor_gauge-final-audit.md','extra_graph_generators':declared,
         'verifier_sha256':own_hash,'verifier_core_sha256_at_start':core_hash,
         'elapsed_seconds':time.monotonic()-start}
    a.out.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'status':out['status'],'branch':branch,'dimension':singular['full_dimension'],'unit':singular['unit_ideal'],'seconds':out['elapsed_seconds']},indent=2))


if __name__=='__main__':main()
