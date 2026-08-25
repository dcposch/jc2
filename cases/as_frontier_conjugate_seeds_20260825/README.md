# Tame right-composed Artin--Schreier seeds at the max-12 frontier

Here "right-composed" is literal: the displayed maps are `A∘B`, equivalently
source-coordinate transforms of `A`.  They are not group conjugates
`B^{-1}∘A∘B`.

Run on AWS:

```sh
python3 verify_seeds.py
```

The registered source is `verify_seeds.py`; freeze source and output hashes
only after an AWS run.  See `PREREGISTRATION.md` for the exact claim and
firewall.
