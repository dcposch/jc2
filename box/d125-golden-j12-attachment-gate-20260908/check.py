import sys
sys.dont_write_bytecode=True
import resource,json
from fractions import Fraction as Q
resource.setrlimit(resource.RLIMIT_CPU,(25,25));resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912))
def need(x,m):
    if not x:raise ValueError(m)
mode=sys.argv[1] if len(sys.argv)>1 else 'normal'
need(mode in ('normal','change-alpha-cross','add-even-kernel','change-G1'),'mode')
for r,f,alpha,beta,gamma in ((2,3,5,7,11),(-1,4,0,3,2),(3,-2,1,0,0)):
    delta=gamma-beta*alpha+Q(5,9)*alpha**2
    q=Q(5,3)*r*r+beta-(0 if mode=='change-alpha-cross' else Q(5,9)*alpha)
    derivative=5*r**4+3*beta*r*r+gamma+Q(10,3)*r*f
    need((3*r*r+alpha)*q-derivative==-delta-Q(10,3)*r*f,'actual dR wedge dF including alpha')
kernels=[(25-5*i,i) for i in range(1,5) if (25-5*i)%2==0]
if mode=='add-even-kernel':kernels.append((5,4))
need(sorted(kernels)==[(10,3),(20,1)],'whole odd scalar kernel list rejects actual R^4 addition')
need(12+20>24 and 2*12==24 and 12+24==36,'all retained orders before target')
need(11%5!=0,'no order24 homogeneous scalar centralizer')
mu=Q(4,9) if mode=='change-G1' else Q(5,9)
need(3*mu==Q(5,3),'order24 actual changed coefficient of G1=L*mu')
print(json.dumps({'status':'PASS','mode':mode,'scope':'free coefficient identities and scalar kernel/order controls, not full source or high polynomial powers','kernels':kernels,'mu':'5/9'},sort_keys=True))
