# Optional direct full-ring minimal-prime regressions

These runners ask Singular to decompose the original eleven-variable,
seven-row ideal directly.  They are independent regressions of the
stratified proof consumed by the report; no direct runner result is consumed
by this freeze.

The preregistered exact discriminator is:

```text
minimal-prime count: 13
global dimension histogram: dim4=8, dim5=3, dim6=1, dim7=1
every reported prime contains the seven source rows
```

Any completed result that disagrees quarantines the 13-component theorem.
A timeout, memory exhaustion, or unfinished output has no mathematical
meaning.  The three variants are:

- `subsystem`: `minAssGTZ(I,"SL","facstd","subsystem")` in degree-reverse
  order;
- `char-dp`: `minAssChar(I)` in degree-reverse order;
- `char-xfirst`: `minAssChar(I,0)` with the three digit variables first in
  lexicographic order.

Each Singular computation is single-threaded.  Local discovery runs stayed
below 1 GB resident memory but did not finish promptly.  Allocate 8 GB per
runner (16 GB conservative; 32 GB hard ceiling) and one CPU core.  Parallel
machines or processes improve wall time; extra cores within one runner do
not.

Portable invocation:

```sh
./run_optional_full_minass.sh subsystem /tmp/d7-full-subsystem.out
./run_optional_full_minass.sh char-dp /tmp/d7-full-char-dp.out
./run_optional_full_minass.sh char-xfirst /tmp/d7-full-char-xfirst.out
```

The wrapper first checks `MANIFEST.sha256`, prints the selected input SHA-256
and Singular version, then writes only to the explicit output path.  On
Linux, collect timing and memory separately, for example:

```sh
/usr/bin/time -v ./run_optional_full_minass.sh subsystem /tmp/d7-full-subsystem.out 2>/tmp/d7-full-subsystem.time
sha256sum /tmp/d7-full-subsystem.out /tmp/d7-full-subsystem.time
```
