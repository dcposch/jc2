# TD6 source-dilation contraction audit — negative result

Date: 2026-08-25  
Status: **EXACT SOURCE/WEIGHT AUDIT / SHORTCUT REJECTED**

The hoped-for contraction `t -> b t` does not preserve the normalized TD6
source.  After target rescaling restores `p=t^15` and `q'(0)=1`, the other
fixed q endpoint has coefficient `b^24`; preserving `q_25=1` leaves only the
finite subgroup `mu_24` (at most `mu_8` with determinant-one target scaling).
If q25 is allowed to tend to zero, the degree/pole type drops and the limit
is outside the V76 section.  If q25 rather than q1 is kept monic, q1 has
weight `-24` and diverges.

The landed chart has a further principal-open obstruction: before
normalizing, `x=...+j*t*s^4` with `j!=0`.  Raw contraction sends `j` to zero.
Compensating by determinant-one source scaling fixes j only by assigning
opposite weights to generic centers and higher-q data, so generic orbits
escape to center infinity.  The pole equation `L^8 A^3=9` similarly forces
mixed weights.  V76 covers finite center divisors, not the degree-drop,
`j=0`, center-infinity, or pole-infinity boundary.

Therefore the source is neither a positive-weight affine cone nor proper
under this action.  V76 emptiness cannot be promoted through this Rees
shortcut.  This is only a negative control on the shortcut; it proves no
TD6/SP-2/JC2 result.

Frozen case:
`cases/td6_source_dilation_contraction_negative_20260825/`.
