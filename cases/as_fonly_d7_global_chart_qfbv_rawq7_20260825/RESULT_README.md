# Frozen raw-Q7 global-chart result custody

The producer theorem and full proof custody correspond to the complete
13-trit accepted Q9 chart with all 32 Q8 and all 18 raw Q7 trits symbolic.
Unlike the quarantined reduced formula, this payload imposes the 23 Q9,
22 Q8, and 19 Q7 source rows directly and uses no globally constant Q7
matrix premise.

AWS producer:

```text
host     Box02 (34.203.207.55)
job      /home/ubuntu/jobs/as_global_chart_rawq7_qfbv_20260825T0650Z
SMT2     46b755e1e274203f838ad663675075379f4df93068e0a7f0028728178edbb417
CNF      19c1551cb284c6f55a32dff2f703426f15eb1001f229f0853c59330a59db79d6
DRAT     5b36f87705de3ba823b44797fc635ec2073a206b3428fb669bd3f5a884387350
checker  s VERIFIED
```

The repository copy of the full custody archive is
`results_box02_full_custody/full_custody.tar.zst`, SHA-256
`e61d2c3dfb5aa1254d0df5fdb05156d3da51db8164e6874b2b5506360ec9a9ab`.
It is 295 MB compressed and includes the 641 MB CNF and 908 MB textual DRAT
trace, so routine repository verification should hash the archive rather than
extract it.  Full replay is AWS-only.

Strict scope: this is an exclusion of the frozen accepted aligned F-only
`D=7` chart at the encoded terminal-high gate.  Coverage of all original
boundary components remains a separate theorem obligation.

