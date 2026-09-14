"""Constant matrices and declared tiny supports only; never production metadata."""
import ast,copy,hashlib,json,resource,tempfile,time,unittest
from pathlib import Path
from fractions import Fraction as F
import construct as C
import replay as R
resource.setrlimit(resource.RLIMIT_CPU,(12,12))
resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,512*1024**2))

class Tiny(unittest.TestCase):
    def setUp(self):self.ops=C.Ops(C.CAPS,time.monotonic()+20)
    def rejected(self,fn):
        try:fn()
        except (ValueError,KeyError,TypeError,StopIteration):return
        raise RuntimeError('actual mutation accepted')
    def eq(self,a,b):C.need(a==b,'tiny equality mismatch')
    def trace(self,label,p,index=0):
        r=C.guard_power(label)
        return dict(type='row',label=label,original_index=index,terms=C.wire(p),old_from_new_ell_power=C.factor(label),guard_power=r,guard_cofactor=C.wire(C.guard_cofactor(r)))
    def test_shifted_matrix(self):
        cols=C.columns('B',15);self.eq(cols,[1,2,3]);inv=C.inverse(C.matrix(15,cols))
        self.eq(inv,[[78,12,1],[168,25,2],[91,13,1]])
        g=dict(type='graph',member='B',degree=15,pivots=[[i,15-i] for i in cols],inverse=[[[str(x.numerator),str(x.denominator)] for x in row] for row in inv])
        R.check_graph(g,'B',15);g['pivots'][0]=[0,15];self.rejected(lambda:R.check_graph(g,'B',15))
    def test_inverse_corruption(self):
        g=dict(type='graph',member='A',degree=1,pivots=[[0,1]],inverse=[[['1','1']]])
        self.rejected(lambda:R.check_graph(g,'A',1));g['inverse']=[[['-1','1']]];R.check_graph(g,'A',1)
    def test_affine_toy_hermite(self):
        # Degree3 top p^2(p+g); one descending degree1 pivot, lambda=1.
        coeffs={(0,3):C.const(1),(1,2):C.const(1),(0,1):{},(1,0):C.mono((0,))}
        C.solve_level(coeffs,'A',1,self.ops)
        self.eq(C.liftrow(coeffs,0,-1,self.ops),{})
        coeffs[0,1]=self.ops.add(coeffs[0,1],C.const(1))
        C.need(bool(C.liftrow(coeffs,0,-1,self.ops)),'deleted low row control did not change')
    def test_affine_shapes(self):
        C.shape({(0,):F(3),(C.K,):F(2)},'A');C.shape({(20,):F(1,9),(C.K,C.K):F(5,9)},'B')
        for p,w in [({(0,0):F(1)},'A'),({(C.K,C.K):F(1)},'A'),({():F(1,10)},'B')]:self.rejected(lambda p=p,w=w:C.shape(p,w))
    def test_j_shape(self):
        a=[(),(C.K,)]+[(i,) for i in range(20)];b=[(),(C.K,),(C.K,C.K)]+[(i,) for i in range(20,79)]
        p={tuple(sorted(x+y)):F(1,9) for x in a for y in b};self.eq(len(p),1362);C.jshape(p)
        p[(C.K,)*4]=F(1);self.rejected(lambda:C.jshape(p))
    def test_guard_relations(self):
        for r in (1,2,3):
            self.eq(self.ops.mul(C.guard(1),C.guard_cofactor(r)),C.guard(r));self.eq(R.cover(C.guard(r)),{})
        self.eq(R.cover(C.mono((C.Z,)),power=-6),{((),0):F(1)})
        self.eq(R.cover(C.mono((C.K,)),power=6),{((),0):F(1)})
    def test_fixed_pullback(self):
        for w,D,p,v in [('A',15,[2,1],F(1)),('B',25,[8,5],F(5,3)),('B',25,[1,0],F(5,9))]:
            e=dict(point=p,name='tiny_fixed',fixed=C.B.F(v).wire());q=C.fixed(w,e)
            self.eq(R.old_coefficient(q,D,sum(p)),{((),0):v})
            R.check_coefficient(w,D,e,q,{})
            bad=C.mono((),v)
            self.rejected(lambda:R.check_coefficient(w,D,e,bad,{}))
        zero=dict(point=[2,0],name='tiny_zero',fixed=C.B.F(0).wire())
        R.check_coefficient('A',15,zero,{},{});self.rejected(lambda:R.check_coefficient('A',15,zero,C.const(1),{}))
    def test_cover_cancellation(self):
        self.eq(R.cover({(C.K,C.Z):F(1),():F(-1)}),{})
        self.eq(R.old_coefficient(C.mono((0,)),15,3),{((0,),6):F(1)})
        self.rejected(lambda:R.old_coefficient(C.const(1),15,2))
    def test_j_target_and_factor(self):
        # Declared tiny physical pair; output(2,0) obligation remains present.
        a={(1,0):C.mono((0,))};b={(2,1):C.mono((20,))}
        p=C.jrow(a,b,2,0,self.ops);maps={0:R.old_coefficient(C.mono((0,)),15,1),1:R.old_coefficient(C.mono((20,)),25,3)}
        literal=dict(label='J/2/0',terms=C.wire({(0,1):F(1),():F(5,9)}));trace=self.trace('J/2/0',p)
        R.verify_row(literal,trace,maps,0,self.ops)
        bad=copy.deepcopy(trace);bad['terms']=C.wire({(0,20):F(1)});self.rejected(lambda:R.verify_row(literal,bad,maps,0,self.ops))
        bad=copy.deepcopy(trace);bad['old_from_new_ell_power']=17;self.rejected(lambda:R.verify_row(literal,bad,maps,0,self.ops))
    def test_omission_and_field(self):
        literal=dict(label='FIX/A_toy',terms=[]);trace=self.trace(literal['label'],{})
        R.verify_row(literal,trace,{},0,self.ops)
        bad=copy.deepcopy(trace);bad['original_index']=1;self.rejected(lambda:R.verify_row(literal,bad,{},0,self.ops))
        self.rejected(lambda:R.decode([[[['0','1'],['1','1']],[]]],81))
    def test_guard_corruption(self):
        literal=dict(label='GUARD/c',terms=[]);trace=self.trace('GUARD/c',C.guard(3))
        R.verify_row(literal,trace,{},0,self.ops)
        for field,value in [('terms',[]),('guard_cofactor',[]),('guard_power',0)]:
            bad=copy.deepcopy(trace);bad[field]=value;self.rejected(lambda bad=bad:R.verify_row(literal,bad,{},0,self.ops))
    def test_parity_row(self):
        self.eq(C.factor('J/1/0'),None);self.eq(R.row_factor('LIFT/A/0/-2'),None)
        literal=dict(label='J/1/0',terms=[]);R.verify_row(literal,self.trace('J/1/0',{}),{},0,self.ops)
    def test_lift_independent_expansion(self):
        # Power multiplication in (u,v)-Laurent exponents, not multinomial formula.
        base={(1,4):F(1),(0,1):F(-1),(0,-1):F(-1)}
        powers={(0,0):F(1)}
        for j in range(5):
            coeffs={(1,j):C.const(2)}
            for e in range(-6,0):
                want=powers.get((0,e+1),F(0))*2
                self.eq(C.liftrow(coeffs,0,e,self.ops),C.const(want))
            nxt={}
            for (u,v),a in powers.items():
                for (t,e),b in base.items():nxt[u+t,v+e]=nxt.get((u+t,v+e),F(0))+a*b
            powers={p:c for p,c in nxt.items() if c}
    def test_lift_cover_identity(self):
        # D=15, term p^3: [-v^-1] coefficient is -3 at lambda=1.
        p=C.liftrow({(0,3):C.mono((0,))},0,-1,self.ops)
        maps={0:R.old_coefficient(C.mono((0,)),15,3),268:{((),1):F(1)}}
        literal=dict(label='LIFT/A/0/-1',terms=C.wire({(0,268):F(-3)}))
        # A standalone nonzero row checks the transport factor directly;
        # verify_row deliberately requires every post-Hermite lift to be zero.
        self.eq(R.substitute(R.decode(literal['terms'],269),maps,self.ops),R.cover(p,R.row_factor(literal['label'])))
        self.rejected(lambda:R.verify_row(literal,self.trace(literal['label'],p),maps,0,self.ops))
    def test_whole_shear(self):
        a={(0,15):C.const(1),(2,1):C.mono((C.K,))};b={(0,15):C.const(2),(2,1):C.const(7)}
        sliced={p:self.ops.add(v,self.ops.mul(C.const(2),a[p]),-1) for p,v in b.items()}
        self.eq(sliced[0,15],{})
        self.eq({p:self.ops.add(v,self.ops.mul(C.const(2),a[p])) for p,v in sliced.items()},b)
        C.need(sliced[2,1]!=b[2,1],'lower shear omission')
    def fixture_authority(self):
        pins={n:'a'*64 for n in ('construct.py','replay.py','baseline.py')}
        a=dict(schema='jc2.hybrid-affine-authority/v1',root_green=True,construction_only=True,job='TOY_AUTH_ONLY',mode='normalized-hermite-only-slice',boot_id='toy',code_sha256=pins,registration_sha256='b'*64,root_green_sha256='c'*64,source_path=C.SOURCE_PATH,source_sha256=C.SOURCE,desk_sha256=C.DESK,normalization_gate_sha256=C.NORMALIZATION,hybrid_gate_sha256='d'*64,code_gate_sha256='e'*64,gates_accepted=True,caps=C.CAPS,expires_unix=110)
        o=dict(system='Linux',vendor='Amazon EC2',instance=C.INSTANCE,cwd=str(C.ROOT),boot='toy',now=100)
        return a,o,pins
    def test_authority_mutations(self):
        a,o,p=self.fixture_authority();C.authority_check(a,o,p,'b'*64,'c'*64)
        for field,value in [('root_green',False),('registration_sha256','f'*64),('boot_id','wrong'),('hybrid_gate_sha256',''),('gates_accepted',False),('source_path','/tmp/unregistered')]:
            bad=copy.deepcopy(a);bad[field]=value;self.rejected(lambda bad=bad:C.authority_check(bad,o,p,'b'*64,'c'*64))
        for field,value in [('vendor','other'),('cwd','/home/ubuntu'),('instance','i-wrong')]:
            bad=copy.deepcopy(o);bad[field]=value;self.rejected(lambda bad=bad:C.authority_check(a,bad,p,'b'*64,'c'*64))
    def test_no_local_production(self):
        self.rejected(lambda:C.layout({},self.ops));self.rejected(lambda:C.build({},self.ops));self.rejected(lambda:R.replay_frozen('absent','absent',self.ops))
        self.rejected(lambda:C.authorize('/not-authority'))
    def test_pre_cap_identity(self):
        caps=dict(C.CAPS,polynomial_terms=1);o=C.Ops(caps,time.monotonic()+10);o.stage(member='B',degree=15,pivots=[[1,14]])
        try:o.add(C.const(1),C.mono((20,)))
        except ValueError as e:
            d=json.loads(str(e));self.eq(d['pending_terms'],2);self.eq(d['member'],'B');self.eq(d['degree'],15)
        else:raise RuntimeError('cap mutation accepted')
    def test_stream_real_resync_mutation(self):
        # Toy output/footer hash resynchronization is not mathematical validation.
        literal=dict(label='J/2/0',terms=C.wire(C.const(F(5,9))))
        valid=self.trace('J/2/0',C.mono((C.K,)*3,F(5,9)))
        with tempfile.TemporaryDirectory(prefix='jc2-hybrid-tiny-') as td:
            p=Path(td)/'toy.jsonl';s=C.Stream(p,65536);s.emit(valid);s.emit(dict(type='footer',complete=True,prefix_sha256=s.h.hexdigest()));s.close()
            records=list(R.records(p));R.verify_row(literal,records[0],{},0,self.ops)
            bad=copy.deepcopy(valid);bad['terms']=[];q=Path(td)/'changed.jsonl';s=C.Stream(q,65536);s.emit(bad);s.emit(dict(type='footer',complete=True,prefix_sha256=s.h.hexdigest()));s.close()
            changed=list(R.records(q));self.rejected(lambda:R.verify_row(literal,changed[0],{},0,self.ops))
    def test_ast_no_assert(self):
        for p in Path(__file__).parent.glob('*.py'):C.need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(p.read_bytes()))),'Assert node')

if __name__=='__main__':unittest.main()
