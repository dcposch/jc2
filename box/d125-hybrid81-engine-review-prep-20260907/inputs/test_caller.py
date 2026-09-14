"""Only two caller defects; tiny mocked custody plus real timed subprocesses."""
from contextlib import ExitStack,contextmanager
from datetime import datetime,timezone
import ast,importlib.util,inspect,json,os,signal,subprocess,sys,tempfile,time
from pathlib import Path
from unittest.mock import patch
import unittest
import driver as D
import exact as E
import hybrid as H
from test_exact import result
HERE=Path(__file__).resolve().parent
OLD=HERE.parent/'d125-hybrid81-solver-prep-20260907/driver.py'
SOL=HERE.parent/'d125-hybrid81-solver-gate-sol56-20260907'
spec=importlib.util.spec_from_file_location('old_driver',OLD);O=importlib.util.module_from_spec(spec);spec.loader.exec_module(O)
DATA=(SOL/'tiny-engine-fixture.jsonl').read_bytes()
V=['x','y','k','z'];TS=['0','x/2','0','x/2','1-x','0','k*z-1']
@contextmanager
def scratch():
    old=Path.cwd()
    with tempfile.TemporaryDirectory(prefix='tiny-',dir=HERE) as p:
        os.chdir(p)
        try:yield Path(p)
        finally:os.chdir(old)
def save(name,value):Path(name).write_bytes(E.canonical(value))
class CallerTests(unittest.TestCase):
    def test_posthash_old_publishes_new_does_not(self):
        for module,published in [(O,True),(D,False)]:
            with scratch() as p,patch.object(module,'context',return_value=({},'a'*64,10)),patch.object(module,'SOURCE',p/'source.jsonl'),patch.object(module.subprocess,'run',return_value=subprocess.CompletedProcess([],0)):
                (p/'source.jsonl').write_bytes(b'ACTUAL_DIFFERENT_TINY_BYTES\n')
                with self.assertRaisesRegex(ValueError,'post-run frozen source drift'):module.launch('MOCK_ONLY','decision')
                self.assertEqual(Path('decision.result.json').exists(),published)
                if published:self.assertNotEqual(E.strict_json(Path('decision.result.json').read_bytes())['source_pins_after'],{'jsonl':H.CONSTRUCTION_SHA})
    def test_matching_posthash_publishes_exact_phase(self):
        with scratch() as p,patch.object(D,'context',return_value=({},'a'*64,10)),patch.object(D,'SOURCE',p/'source.jsonl'),patch.object(H,'CONSTRUCTION_SHA',E.digest(DATA)),patch.object(D.subprocess,'run',return_value=subprocess.CompletedProcess([],0)):
            (p/'source.jsonl').write_bytes(DATA)
            self.assertEqual(D.launch('MOCK_ONLY','decision'),0)
            r=E.strict_json(Path('decision.result.json').read_bytes());self.assertEqual(r['phase'],'decision');self.assertEqual(r['source_pins_after'],{'jsonl':E.digest(DATA)})
    def verify_case(self,module,mutation):
        with scratch() as p,ExitStack() as stack:
            source=p/'tiny.jsonl';source.write_bytes(DATA)
            stack.enter_context(patch.object(module,'context',return_value=({},'a'*64,10)))
            stack.enter_context(patch.object(module,'arm_deadline',lambda a,d:None,create=True))
            stack.enter_context(patch.object(module,'SOURCE',source));stack.enter_context(patch.object(module,'limits',lambda phase:None))
            stack.enter_context(patch.object(module,'observed_host',lambda:{'boot':'toy'}));stack.enter_context(patch.object(module.os,'getpgrp',os.getpid))
            original_read=Path.read_bytes
            def read(q):
                if str(q)==f'/proc/{os.getppid()}/cmdline':return (module.CWD+'/run_capped.py').encode()+b'\0'
                return original_read(q)
            stack.enter_context(patch.object(Path,'read_bytes',read))
            actual=H.read_hybrid;stack.enter_context(patch.object(H,'read_hybrid',lambda data,production:actual(data,False)))
            stack.enter_context(patch.object(H,'CONSTRUCTION_SHA',E.digest(DATA)))
            identity={'pid':42,'pgid':42,'authority_sha256':'a'*64,'host':{'boot':'toy'},'start_ticks':'7'}
            telemetry={'schema':'CAPRUN/v1','error':None,'status':'NORMAL_EXIT','child_returncode':0,'pid':42,'pgid':42,'cwd':module.CWD,'start_identity':'boot=toy;start_ticks=7'}
            save('decision.identity.json',identity);save('decision.telemetry.json',telemetry)
            Path('decision.stdout').write_bytes(result(TS,['1'],['0','1','0','1','1','0','0'],variables=V,source=E.digest(DATA)));Path('decision.stderr').write_bytes(b'')
            receipt={'phase':'decision','source_pins_after':{'jsonl':E.digest(DATA)},'authority_sha256':'a'*64,'runner_rc':0,'artifacts':{'identity.json':module.file_sha('decision.identity.json')},'outputs':{n:module.file_sha('decision.'+n) for n in ('stdout','stderr','telemetry.json')}}
            receipt.update(mutation);save('decision.result.json',receipt)
            module.payload('MOCK_ONLY','verify')
    def test_receipt_readback_old_accepts_new_rejects(self):
        for mutation in ({'phase':'control'},{'phase':'verify'},{'source_pins_after':{'jsonl':'b'*64}},{'source_pins_after':{}},{'source_pins_after':{'jsonl':E.digest(DATA),'extra':'x'}}):
            self.verify_case(O,mutation)
            with self.assertRaisesRegex(ValueError,'decision custody/return/source status'):self.verify_case(D,mutation)
        self.verify_case(D,{})
    def test_real_delayed_parse_and_exec(self):
        for mode in ('parse','exec'):
            for version in ('old','new'):
                with scratch():
                    flags=['-O'] if not __debug__ else []
                    r=subprocess.run([sys.executable,'-B',*flags,str(HERE/'timed_probe.py'),version,mode],capture_output=True,text=True,start_new_session=True,timeout=5)
                    finished=time.time()
                lines=r.stdout.splitlines();events=[json.loads(x) for x in lines if x.startswith('{')];start=events[0]
                self.assertEqual(start['marker'],'START');self.assertEqual(start['pid'],start['pgid']);self.assertFalse(Path('/proc',str(start['pid'])).exists())
                print(json.dumps({'timed_case':mode,'version':version,'returncode':r.returncode,'events':events,'finished_utc':finished,'deadline_delivery_lag_seconds':finished-start['deadline'],'survived':'SURVIVED' in lines,'stderr':r.stderr}),flush=True)
                if version=='old':self.assertEqual(r.returncode,0);self.assertIn('SURVIVED',lines)
                else:
                    self.assertEqual(r.returncode,-signal.SIGALRM);self.assertNotIn('SURVIVED',lines)
                    self.assertGreaterEqual(finished,start['deadline']);self.assertLess(finished-start['deadline'],.25)
                    if mode=='parse':self.assertFalse(any(e['marker']=='PARSE_DONE' for e in events))
                    else:
                        event=next(e for e in events if e['marker']=='EXEC_ALIVE');self.assertEqual(event['pid'],start['pid']);self.assertTrue(event['default']);self.assertGreater(event['timer'][0],0);self.assertLess(event['utc'],start['deadline'])
    def test_expired_arm_rejects_and_unique_early_call(self):
        with patch.object(D.signal,'signal'),patch.object(D.signal,'pthread_sigmask'),patch.object(D.signal,'setitimer') as arm:
            with self.assertRaisesRegex(ValueError,'deadline expired'):D.arm_deadline({'deadline_utc':'1970-01-01T00:00:01Z'},300)
            arm.assert_not_called()
        source=inspect.getsource(D.payload);self.assertLess(source.index('arm_deadline('),source.index('SOURCE.read_bytes'))
        text=Path(D.__file__).read_text();self.assertEqual(text.count('signal.setitimer('),1)
        self.assertFalse(any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(text))))
    def test_frozen_arithmetic_footer_and_sol_fixture(self):
        self.assertEqual(inspect.getsource(D.footer),inspect.getsource(O.footer))
        self.assertEqual(inspect.getsource(D.limits),inspect.getsource(O.limits))
        self.assertEqual(E.digest(Path(E.__file__).read_bytes()),'7ca2b24ee5d04ff6d60fd2212a05586c8bba24327a51c7718351434c7eda60e9')
        self.assertEqual(E.digest(Path(H.__file__).read_bytes()),'c9755a7172eaa7f1393860931d55c38a0b9d79b5b170eadbf14baff0203c35a3')
        self.assertEqual(E.digest(DATA),'d00df83bafddcd3436dad44034bdb1680d306f6d67f8bfa83d4b32de19961bbf')
        sing=(SOL/'tiny-engine-fixture.sing').read_bytes();self.assertEqual(E.digest(sing),'d1c334443efb9d31eedc6a821970ce990f9ba9a551b6c8c94fa4411ab4904b2e')
        v,rows,labels,prefix=H.read_hybrid(DATA);self.assertEqual((prefix+D.footer(v,E.digest(DATA))).encode(),sing)
        self.assertIn('slimgb(I)',sing.decode());self.assertNotIn('slimgb',(prefix+D.footer(v,E.digest(DATA),control=True)))
if __name__=='__main__':unittest.main()
