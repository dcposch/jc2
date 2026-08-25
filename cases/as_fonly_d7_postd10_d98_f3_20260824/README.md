# AS F-only `p=3,D=7` post-D10 D9/D8 F3 gate

This package consumes the different-model-confirmed D10 pointwise gate,
derives the next exact high rows, proves a global vertical degree-nine
section, reduces vertical degree eight to a `7 x 5` structural core, and
exhausts its literal F3 digit points.  It also reduces and exhausts the
`g != 0` endpoint's exact `13 x 14` system.

Replay from this directory:

```sh
Singular -q audit_vertical_d9_section.sing
Singular -q audit_vertical_core_rank.sing
ENUMERATE=1 python3 generate_and_enumerate.py | sed -n '/ENUM-VERTICAL-D98/,$p'
BRANCH=g ENUMERATE=1 python3 generate_and_enumerate.py | sed -n '/ENUM-G-ENDPOINT-D98/,$p'
shasum -a 256 -c MANIFEST.sha256
```

Expected stream hashes:

```text
vertical d7910730247c3da26599fac9c11cb28472ec7591ef49c221a825ef5978e17bee
g endpoint 119580e2aab411d56dc2b41f6118cf9fd03768bb8cc10397c0aa2b29abcd2da8
```

The censuses concern the literal F3 digit set, not compatibility over an
algebraic closure.  The package stops before the next divided carry, other
survivor branches, full `D=7`, all-depth lifting, characteristic zero, a
counterexample, or JC2.
