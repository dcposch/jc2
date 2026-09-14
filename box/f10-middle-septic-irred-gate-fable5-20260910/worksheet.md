# Hand worksheet (text only, no computation artifact)

Residues by r mod 7 (m=3r+1, tau=r/m in Z/7): r=0 m=1 tau=0; r=1 m=4 tau=2; r=2 m=0 pole; r=3 m=3 tau=1; r=4 m=6 tau=3; r=5 m=2 tau=6; r=6 m=5 tau=4.

k0=2(2-3tau)(1+tau)(2+tau)(3+tau) mod 7: tau=0: 2*2*1*2*3=24=3; tau=1: 2*(-1)*2*3*4=-48=1; tau=2: 2*(-4)*3*4*5=-480=3; zero at tau=3,4,5,6 (one factor each).

Ledger for S=2K^2-140tau(1+tau-6V)KD+245gamma D^2 with K=k0+7L, L(0)=0, deg L<=3:
degree 0: 2k0^2 (unit) + 7Z_7 -> v=0.
degrees 1..3: 28k0L, 98L^2, -140tau k0(1+tau-6V)D, -980(...) , 245(...) -> v>=1.
degrees 4..6: 98L^2, -980tau(1+tau-6V)LD, 245gamma D^2 -> v>=2.
degree 7: 245*(-120tau)*144 only -> v=2 (120=1, 144=4 mod 7).

Polygon: (0,0),(i,>=1) i<=3,(i,>=2) i=4..6,(7,2); line slope 2/7; 1>2i/7 iff i<3.5; 2>2i/7 iff i<7; single segment, roots of valuation -2/7; proper factor of degree d gives -2d/7 not in Z for 1<=d<=6.

r=2 mod 7 chart: b=1/tau in 7Z_7; Kbar constant 2(2b-3)(1+b)(1+2b)(1+3b)=-6 mod 7; lc(Sbar)=245*(-120)*144; only b=0 mod 7 used.

Failure map: r=0 -> tau=0 -> v(a7)>=3; r=4 -> 2-3tau=0; r=5 -> 1+tau=0; r=6 -> 3+tau=0 (v(a0)>=1). Failure of the pattern is not reducibility.
