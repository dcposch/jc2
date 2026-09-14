# A further front-band consequence of the full characteristic block

This supplements `front-band-lemma.md`. It is an algebraic-set consequence
of the full characteristic upper rows and the same actual source floors;
it introduces no gauge, leader specialization, or deleted target term.

Use the normalized remainder backend notation H,v,U,R, with H monic of
z-degree k, v of degree below k, and R of degree below k. The high-remainder
rows give the polynomial identity

    v^2-UH=R.

The full normalized characteristic equations, at ambient degree 6k-2,
state that all t-bands below the leader depth vanish in

    Qn = 3 R H^2/4 - t v U H/8 + t v R - 9 t^2 U^2/64
         + p t^(4k-2)H^2 + p t^(4k-1)v + q t^(6k-2).

Let r be the first nonzero t-band of the source D. Assume

    3r+1 < min(leader depth,4k-2),  r<2k-1.

The latter condition puts the scalar correction to v strictly after its
first band. Write d=[t^r]v=[t^r]D and H0=[t^0]H.

Monic division, or the high-remainder identity, gives ord_t U>=2r and
ord_t R>=2r. The only Qn term at orders from 2r through 3r is 3RH^2/4,
after previously zero R bands have been removed. Multiplication by the
nonzero H0^2 is injective over a field. Thus every R band below 3r+1 is
zero. At t^(2r), the remainder identity therefore gives

    H0 [t^(2r)]U=d^2.

At t^(3r+1), only 3RH^2/4 and -t vUH/8 contribute to Qn: the term tvR
starts at 4r+2 after the preceding zero bands, U^2 also starts at 4r+2,
and the scalar p,q terms have not yet appeared. Hence

    H0^2 [t^(3r+1)]R = d^3/6.                    (1)

In particular, H0^2 divides d^3. This proof includes every cross term;
corrections to H and to v,U have no earlier R band with which to pair.

## Consequences for the two clients

For 99, the earlier theorem gives r>=28. If r=28, the source floor
3r+4j>=189 gives z-order(d)>=27 and deg_z d<=32. But
H0=z^24(1+z)^9, so (1) forces (1+z)^6 to divide d. The coprime factors
z^27 and (1+z)^6 then force degree at least33, a contradiction. Thus

    D_r=0 for r<=28;  C_r=0 for r<=58.

The second assertion follows from the normalized quotient identity:
D starts at29, the quotient contribution to C at2*29+1=59, the bD
correction at29+33=62, and the scalar correction at98.

For 108, the earlier theorem gives r>=31. If r=31 or32, the source
floor4r+5j>=276 gives z-order(d)>=31 or30, respectively. Here
H0=z^28(1+z)^8. Equation (1) forces (1+z)^6 to divide d, whereas its
z-degree cap is35. Both cases are impossible. Consequently

    D_r=0 for r<=32;  C_r=0 for r<=66.

D starts at33; the three possible C contributions start at67,69,107.
All required r satisfy the displayed depth hypotheses: the largest
3r+1 used is97, below target151 and first p-depth142. For99 the only
new test is85, below141 and130. Therefore the result is independent
of the finite stage, once the full characteristic block is adjoined.

These deductions are pointwise over every characteristic-zero field
extension. Adding the resulting zero-coordinate equations is justified
as radical preprocessing; the original source and characteristic rows
must still be transported and retained. No claim of ideal membership
of each individual zero coordinate is made here.

The next possible leading shapes are not killed by this argument:
99 at r=29 can have d=tau*z^26*(1+z)^6, and108 at r=33 can have
d=tau*z^29*(1+z)^6. They satisfy both leading square and cube
divisibilities. No fourth-power divisibility has been assumed; higher
bands may contain corrections from H and D and require a new proof.
