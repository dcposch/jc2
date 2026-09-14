# Independent final computation review

PASS. I independently read the harvested raw GB, F4 transcript, shell status, time report, remote hashes, audit JSON, and both formal export-map logs. No discrepancy was found. No CAS computation was rerun and no worker access was used.

The actual non-comment body of `worker/h2b.gb` is exactly `[1]:`. Its own headers declare characteristic 32027, ordered variables `q2,q3,q4,q5,q6,q7`, ordinary grevlex, and one basis element. The F4 transcript independently declares six variables, 28 equations, zero invalid equations, characteristic 32027, and 32 threads. It ends with a one-element/one-term basis and `No solution`. The deepest F4 degree is 19, with 490,019 rows reduced and 244,165 pairs reduced.

Both `worker/h2b.status` and GNU time report exit 0. The worker wrapper and timing command specify `timeout --signal=TERM --kill-after=30s 10200s ... -g 2 -t 32 -v 2`, i.e. the 170-minute watchdog. The run started 19:07:55Z and finished 21:17:08Z on 2026-09-05. Core F4 elapsed time was 7,751.47 seconds, while msolve's outer timing reports 7,751.99 seconds and GNU time rounds to 2:09:12. These are distinct timing scopes, with no material inconsistency. Peak RSS was 37,268,736 KiB.

I mechanically rehashed all six artifacts listed by `h2b-audit.json` and all four listed by `worker/h2b.outputs.sha256`; every digest matched. The harvested and local `run_h2b.sh` files are byte-identical. The remote input digest matches a fresh local rehash of `affinew_p32027.ms` and the input digest already independently sampled in `controls/t8_images.json`. The remote binary digest matches a fresh rehash of the static msolve binary used for the four fresh t = 6 controls:

```text
8be78590cbd8ab8edba4097372f3978986c18e9aa8c0b17da8066ed8f796a8d4  affinew_p32027.ms
0436525b06fe83b1a6a00097a96d9bcafdc40d8de6315c724b9ada9a4c04ff5f  msolve (worker and local control binary)
92cdd9d1ae0a566ceaac4f830990b8b84e23d020de8b8754091db4296bd74ff8  worker/h2b.gb
```

Both formal identity logs finish with their correctly labelled `FORMAL_EXPORT_MAP p32003 generators=28 ALL_EQUAL=1` / `FORMAL_EXPORT_MAP p32027 generators=28 ALL_EQUAL=1`. Both also carry `PREFIX_S_OK`, `PREFIX_P_OK ngens(I2)=21`, the correct t = 8 variable/weight declaration and H8, and no failure/error/division-by-zero line. The two exact export-map results therefore pass at the transcript level in addition to the earlier independent arithmetic sample checks.

This review confirms the harvested second-prime affine H2b computation and its artifact/input/engine consistency. It does not claim a second solving engine, a characteristic-zero lifting theorem, or completion of worker termination; the root lane handles those separate conclusions and the termination receipt.
