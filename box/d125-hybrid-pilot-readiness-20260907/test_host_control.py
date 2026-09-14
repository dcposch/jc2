"""Tiny local mocked-host controls. No AWS, source, full metadata or subprocess."""
import ast,copy,hashlib,json,resource,sys,tempfile,time,unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
import host_control as H
HERE=Path(__file__).resolve().parent
FROZEN=HERE.parent/'d125-hybrid-affine-code-prep-20260907'
sys.path.insert(0,str(FROZEN))
import construct as C
resource.setrlimit(resource.RLIMIT_CPU,(12,12));resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,512*1024**2))

def need(ok,msg):
    if not ok:raise RuntimeError(msg)
def rejected(fn):
    try:fn()
    except (ValueError,RuntimeError,KeyError):return
    raise RuntimeError('actual negative control accepted')

class Tiny(unittest.TestCase):
    def fixture(self):
        h=dict(system='Linux',vendor='Amazon EC2',instance=H.INSTANCE,boot='DECLARED-MOCK-BOOT',cwd=str(H.WORK),hostname='DECLARED-MOCK',now=time.time())
        reg='b'*64;green='c'*64;engineering={'host_control.py':H.sha(HERE/'host_control.py'),'run_capped.py':H.RUNNER}
        a=dict(schema='jc2.hybrid-affine-authority/v1',engineering_control_only=True,engineering_control='authorize',root_green=True,construction_only=True,boot_id=h['boot'],registration_sha256=reg,root_green_sha256=green,code_sha256=dict(H.PINS),engineering_code_sha256=engineering,hybrid_gate_sha256=H.MATH,code_gate_sha256='d'*64,gates_accepted=True,caps=dict(H.CAPS),expires_unix=h['now']+9,job='DECLARED-MOCK-NO-AUTHORITY',mode='normalized-hermite-only-slice',source_path=C.SOURCE_PATH,source_sha256=C.SOURCE,desk_sha256=C.DESK,normalization_gate_sha256=C.NORMALIZATION)
        return a,h,reg,green,dict(H.PINS),engineering
    def test_positive_comparisons(self):H.validate(*self.fixture(),'authorize')
    def test_authority_negative(self):
        for field,value in [('engineering_control_only',False),('engineering_control','rss'),('root_green',False),('boot_id','wrong'),('registration_sha256','0'*64),('root_green_sha256','0'*64),('hybrid_gate_sha256','0'*64),('code_gate_sha256',''),('gates_accepted',False)]:
            args=list(self.fixture());args[0][field]=value;rejected(lambda args=args:H.validate(*args,'authorize'))
    def test_missing_host_caps_pins(self):
        args=list(self.fixture());args[0]={};rejected(lambda:H.validate(*args,'authorize'))
        for field in ('vendor','instance','cwd','boot'):
            args=list(self.fixture());args[1][field]='';rejected(lambda args=args:H.validate(*args,'authorize'))
        args=list(self.fixture());args[0]['caps']['wall_seconds']=11;rejected(lambda:H.validate(*args,'authorize'))
        args=list(self.fixture());args[4]['construct.py']='0'*64;rejected(lambda:H.validate(*args,'authorize'))
    def test_both_output_paths_and_dangling_link(self):
        with tempfile.TemporaryDirectory(prefix='jc2-hybrid-paths-') as td:
            H.outputs_absent(td)
            for name in ('construction.jsonl','replay-result.json'):
                p=Path(td)/name;p.touch();rejected(lambda:H.outputs_absent(td));p.unlink()
            p=Path(td)/'replay-result.json';p.symlink_to(Path(td)/'absent-target')
            rejected(lambda:H.outputs_absent(td));p.unlink();H.outputs_absent(td)
    def test_actual_frozen_authorizer_and_toy(self):
        a,h,reg,green,code,engineering=self.fixture();H.validate(a,h,reg,green,code,engineering,'authorize')
        def read_bytes(p):
            need(p==H.WORK/'authority.json','unapproved mock read');return json.dumps(a).encode()
        def read_text(p,*args,**kw):
            return {'/sys/class/dmi/id/sys_vendor':'Amazon EC2','/sys/class/dmi/id/board_asset_tag':H.INSTANCE,'/proc/sys/kernel/random/boot_id':h['boot']}[str(p)]
        original_bytes=Path.read_bytes
        def code_sha(p):
            if p.name in code:return hashlib.sha256(original_bytes(FROZEN/p.name)).hexdigest()
            return {'REGISTRATION.md':reg,'ROOT-GREEN.md':green}[p.name]
        with patch.object(C.Path,'cwd',return_value=H.WORK),patch.object(C.Path,'read_bytes',read_bytes),patch.object(C.Path,'read_text',read_text),patch.object(C.platform,'system',return_value='Linux'),patch.object(C,'sha',code_sha),patch.object(C.resource,'setrlimit') as limits,patch.object(C.signal,'setitimer') as timer,patch.object(C,'build',side_effect=RuntimeError('FORBIDDEN')) as build,patch.object(C,'reconstruct',side_effect=RuntimeError('FORBIDDEN')) as reconstruct,patch.object(C.B,'make_contract',side_effect=RuntimeError('FORBIDDEN')) as metadata:
            H.tiny(C,H.WORK/'authority.json');need(limits.call_count==4 and timer.call_count==1,'real gate setters not reached')
            need(not build.called and not reconstruct.called and not metadata.called,'production function called')
            for field,value in [('boot_id','wrong'),('root_green',False),('registration_sha256','0'*64),('hybrid_gate_sha256','')]:
                old=a[field];a[field]=value;rejected(lambda:H.tiny(C,H.WORK/'authority.json'));a[field]=old
    def test_actual_tripwires_and_audit(self):
        fake=SimpleNamespace(B=SimpleNamespace(),SOURCE_PATH=C.SOURCE_PATH)
        with patch.object(H.sys,'addaudithook') as hook:H.install_tripwires(fake)
        for name in ('main','build','reconstruct','layout','rows'):rejected(getattr(fake,name))
        rejected(fake.B.make_contract);rejected(fake.B.validate_contract)
        audit=hook.call_args.args[0]
        rejected(lambda:audit('open',(C.SOURCE_PATH,'r',0)))
        rejected(lambda:audit('open',(str(H.WORK/'construction.jsonl'),'w',0)))
        audit('open',(str(H.ENG/'fixture.identity.json'),'w',0))
    def test_explicit_dispatch_limitation(self):
        # This is intentional evidence of GAP-AUTH, not a passing security gate:
        # the frozen authorizer's pure checks accept the engineering-only flag.
        a,h,reg,green,code,engineering=self.fixture()
        C.authority_check(a,h,code,reg,green)
        need(a['engineering_control_only'] is True,'gap fixture lost')
    def test_templates_are_disabled(self):
        for name in ('ENGINEERING-AUTHORITY.template.json','PRODUCTION-AUTHORITY.template.json'):
            a=json.loads((HERE/name).read_bytes());need(a['root_green'] is False and a['gates_accepted'] is False and a['expires_unix']==0,'template acquired authority')
            _,h,reg,green,code,engineering=self.fixture()
            rejected(lambda:C.authority_check(a,h,code,reg,green))
    def test_frozen_payload_unchanged(self):
        for name,pin in H.PINS.items():need(H.sha(FROZEN/name)==pin,'frozen producer drift')
    def test_ast_and_no_generation(self):
        for name in ('host_control.py','test_host_control.py'):
            tree=ast.parse((HERE/name).read_bytes());need(not any(isinstance(n,ast.Assert) for n in ast.walk(tree)),'Assert node')
        tree=ast.parse((HERE/'host_control.py').read_bytes())
        forbidden={'build','reconstruct','layout','rows','make_contract','replay_frozen','main'}
        need(not any(isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute) and n.func.attr in forbidden for n in ast.walk(tree)),'production method call in control')

if __name__=='__main__':unittest.main()
