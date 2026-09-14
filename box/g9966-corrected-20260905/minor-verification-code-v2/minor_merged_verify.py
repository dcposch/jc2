#!/usr/bin/env python3
"""Verify both antecedent source graphs, their merge, and final Jacobian rows.

No graph is inferred by deleting solved coordinates. Every pivot is replayed
in its declared ring, and the actual source-coordinate identity map between
the two antecedents is checked before their relations are combined.
"""
from pathlib import Path
import argparse,hashlib,json,re,sys,time
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
    ap.add_argument('--safe-exporter',type=Path,required=True)
    ap.add_argument('--certificate-root',type=Path,action='append',default=[])
    ap.add_argument('--out',type=Path,required=True)
    ap.add_argument('--jacobian-method',choices=['direct','factored','flint-direct'],default='direct')
    a=ap.parse_args();start=time.monotonic();M.PATH_ROOTS.extend(path.resolve() for path in a.certificate_root)
    merged=read(a.merged);source=read(a.source_result);weaksource=read(a.weak_result)
    branch=merged['branch'];assert source['branch']==weaksource['branch']==branch
    assert merged['field']=='Q'
    own_hash=M.digest(__file__);core_hash=M.digest(HERE/'minor_final_verify.py')
    assert M.digest(a.driver)==merged['driver_sha256'],'merge driver custody mismatch'
    assert M.digest(a.safe_exporter)==merged['safe_exporter_sha256'],'safe exporter custody mismatch'
    for name,value in merged['code_sha256'].items():assert M.digest(a.code_dir/name)==value,('strong code custody',name)
    for obj,directory in [(source,a.code_dir),(weaksource,a.weak_code_dir)]:
        for key,name in [('engine_sha256','engine.py'),('source_derivation_sha256','source_data.py'),('helpers_sha256','deep_rows.py'),('driver_sha256','deep_driver.py')]:
            assert obj[key]==M.digest(directory/name),('antecedent code custody',name)
        assert obj['initial_inner']['gauge_slice']['wrapper_sha256']==M.digest(directory/'deep_gauge_accelerated.py')
    E=M.load_code(a.code_dir,gauge=True);v=M.Verifier(E,branch)
    sourcecheck=v.check_source(source);weakcheck=v.check_source(weaksource)
    # check_source rebuilds every h3/source image and the outer source box.
    # The coefficient engine and source derivation are also byte-identical;
    # wrappers have different later hooks but identical checked source images.
    assert source['engine_sha256']==weaksource['engine_sha256']
    assert source['source_derivation_sha256']==weaksource['source_derivation_sha256']
    assert merged['weak_complete_free_ring']==sorted(map(str,v.basefree))
    transport={'field':'Q','source_images_rebuilt_and_equal':True,
               'strong_source':sourcecheck,'weak_source':weakcheck,
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
    def replay(chain,label,initial=None,regen_new=False):
        reports=[];previous=initial
        for i,path in enumerate(chain):
            cert=read(path)
            if previous is None:
                assert cert['phase']=='source_residue' and not cert['map_before'] and not cert['residual_before']
            else:
                assert v.equal_map(v.mapping(previous['map_after']),v.mapping(cert['map_before'])),('antecedent chain map mismatch',label,i)
                assert v.rows(previous['residual_after'])==v.rows(cert['residual_before']),('antecedent chain residual mismatch',label,i)
            report={'path':str(path),'sha256':M.digest(path),**v.replay_phase(cert)}
            if regen_new and cert['phase'] in ('D1_graph','D1_J','corner_J','merge_weak_complete_graph'):
                report['raw_regeneration']=v.regenerate(cert,a.jacobian_method)
            reports.append(report);previous=cert
            if i%25==0 or i==len(chain)-1:print(f'{label}: verified {i+1}/{len(chain)} {cert["phase"]}',flush=True)
        return previous,reports
    weakpaths=paths(merged['weak_chain'],True)
    assert M.digest(weakpaths[-1])==merged['weak_checkpoint_sha256']
    weak,weakreports=replay(weakpaths,'weak source/J chain')
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
    strong,strongreports=replay(strongpaths,'strong printed-face chain',regen_new=True)
    assert sorted(set(strong['map_after'])|set(strong['free_after']))==merged['initial_complete_free_ring']
    newpaths=paths(merged['phase_certificates'],True);assert newpaths
    final,newreports=replay(newpaths,'merged/full-J chain',initial=strong,regen_new=True)
    terminal_regeneration=v.regenerate(final,a.jacobian_method)
    assert v.equal_map(v.mapping(final['map_after']),v.mapping(merged['cumulative_map']))
    assert v.rows(final['residual_after'])==v.rows(merged['residual_rows'])
    assert E.rows_hash(v.rows(final['residual_after']))==merged['residual_hash']
    singular=M.singular_replay(v.rows(final['residual_after']),branch,len(final['free_after']),a.out.with_suffix('.sing'))
    assert singular['full_dimension']==merged['records'][-1]['dimension']
    assert singular['unit_ideal']==merged['records'][-1]['unit_ideal']
    out={'status':'PASS','type':'INDEPENDENT TWO-ANTECEDENT FULL-SOURCE CHART VERIFICATION','branch':branch,
         'merged_result_sha256':M.digest(a.merged),'source_transport':transport,
         'weak_source_chain':weakreports,'strong_printed_face_chain':strongreports,'merged_J_chain':newreports,
         'terminal_raw_regeneration':terminal_regeneration,'Singular':singular,
         'gauge_isomorphism_audit':'minor_gauge-final-audit.md','extra_graph_generators':declared,
         'verifier_sha256':own_hash,'verifier_core_sha256_at_start':core_hash,
         'elapsed_seconds':time.monotonic()-start}
    a.out.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'status':'PASS','branch':branch,'dimension':singular['full_dimension'],'unit':singular['unit_ideal'],'seconds':out['elapsed_seconds']},indent=2))


if __name__=='__main__':main()
