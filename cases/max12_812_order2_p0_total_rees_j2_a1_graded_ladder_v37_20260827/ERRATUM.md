# V37 validation and custody erratum

Date: 2026-08-27

The frozen V37 computation is valid **mathematical discovery evidence**, but
its validator and harvested custody contract are not promotion-grade.  The
frozen preregistration, programs, manifests, and AWS outputs remain immutable.

An independent audit found:

1. `validate_graded_ladder_v37.py` replays every fixed-weight census and exact
   membership/nonmembership certificate, so the four mathematical outcomes
   are sound.  It is nevertheless fail-open over emitted metadata: among
   other fields it does not independently enforce each recorded rank,
   per-record selector prime, completeness flag, implication, registered lane,
   preregistration hash, or canonical scope.  It also omits the compiler's
   one-coordinate W17/W18 control and permissively coerces some fraction data.
2. `run_aws.sh` wrote absolute EC2 paths to `EVIDENCE.sha256`.  Consequently a
   relocated manifest cannot be checked by a literal local `sha256sum -c`.
   Removing the remote prefix and checking the relative suffix verifies all
   11/11 files in each harvested lane.

Independent exact replay confirms both selector lanes and their agreement:

```text
weight:             17        18        19        20
outcome:      nonmember nonmember nonmember nonmember
rank:                 0         0        50       156
dual terms:           1         1         5        14
```

The canonical mathematical records from the two lanes are identical after
removing selector/lane metadata.  W17--W19 are complete at their weights;
W20 nonmembership is only relative to rows through grade 19.  No saturated
Rees, honest-chart, Gate-T, or JC2 inference follows.

A successor must harden exact schema/provenance validation, require canonical
integer fraction encodings, repeat all special controls, emit relocatable
evidence paths, and independently replay any claimed completeness/scope text.
