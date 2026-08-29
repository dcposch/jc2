#!/usr/bin/env python3
"""Cap-free special-nu theorem for the first td=7 case-III consumer.

Chain 1 is frozen at (mu,w)=(1,2).  Chain 2 is the neutral ray
``(mu0,w,nu_H)=(2,3/2,h)`` with h odd and h>=3.  For the P3 ZCH merge shape

    dp = g+2,  dq = (l+1)g+1,  g=nu_G>=2, l>=1,

the two handshakes give kbar=3h-2 and X=3h-4.  The ratio equation is
equivalent to

    g*((3h-4)l-2) = 3h.

The unique legal integer solution is (h,l,g)=(3,1,3), yielding
(dp,dq,M_G)=(5,7,1), hence the known interior MP2 kill.  Every odd h>=5
is uniformly empty for this consumer.
"""

from __future__ import annotations

import hashlib
import json


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def derive() -> dict[str, object]:
    # If l>=2, D=(3h-4)l-2 >= 6h-10.  For h>=3 this is greater
    # than 3h/2, while g>=2 in g*D=3h requires D<=3h/2.
    # Thus l=1.  Then g*(h-2)=h, so (h-2)|(h-(h-2))=2.
    # Odd h makes h-2 odd; h>=3 makes it positive, hence h-2=1.
    h, l, g = 3, 1, 3
    D = (3 * h - 4) * l - 2
    require(g * D == 3 * h, "candidate does not satisfy ratio equation")
    dp = g + 2
    dq = (l + 1) * g + 1
    import math
    M = math.gcd(dp, dq)
    require((dp, dq, M) == (5, 7, 1), "candidate cell mismatch")
    payload: dict[str, object] = {
        "schema": "td7-caseiii-special-nu-r1",
        "charged_ray": {
            "chain1": {"mu": 1, "w": "2"},
            "chain2": {"mu0": 2, "w": "3/2",
                       "nu_H": "odd h >= 3"},
        },
        "equation": "nu_G*((3*nu_H-4)*l-2)=3*nu_H",
        "proof": [
            "l>=2 implies D>=6h-10>3h/2, contradicting nu_G>=2",
            "l=1 implies nu_G*(h-2)=h and therefore h-2 divides 2",
            "h odd and h>=3 implies h-2=1",
        ],
        "special_values": [{"nu_H": h, "l": l, "nu_G": g,
                            "dp": dp, "dq": dq, "M_G": M,
                            "verdict": "MP2_DEAD_INTERIOR_M1"}],
        "generic_classes": [{"nu_H": "odd >= 5",
                             "verdict": "CASE_III_ZCH_EMPTY"}],
        "cap_free": True,
        "scope_firewall": {
            "other_partner_states": False,
            "other_case_III_shapes": False,
            "full_td7_book": False,
            "landing": False,
            "jc2": False,
        },
    }
    body = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["certificate_sha256"] = hashlib.sha256(body).hexdigest()
    return payload


def main() -> int:
    print(json.dumps(derive(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
