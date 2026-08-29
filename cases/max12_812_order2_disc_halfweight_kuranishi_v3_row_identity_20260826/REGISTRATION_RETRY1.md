# Nonmutating launch-path retry registration

Date: 2026-08-26

The first dual launch failed before freeze validation or compilation because
the launcher passed the relative output path `output`; `run_aws.sh` changes
to the frozen repository directory before writing `freeze_check.stdout`, so
the output path must be absolute.  The frozen source package is unchanged.
The failed remote jobs are preserved as controls.

Retry lanes:

```text
tag=max12_812_order2_disc_halfweight_v3rowsr1_q_20260826T073500Z_box03
host=Box03 / 98.80.65.144
job=/home/ubuntu/jobs/max12_812_order2_disc_halfweight_v3rowsr1_q_20260826T073500Z_box03

tag=max12_812_order2_disc_halfweight_v3rowsr1_p32003_20260826T073500Z_r6d
host=r6d / 100.26.198.153
job=/home/ubuntu/jobs/max12_812_order2_disc_halfweight_v3rowsr1_p32003_20260826T073500Z_r6d
```

Each retry remains one core, 16 GiB, 300-second compiler cap, and 600-second
Singular cap.  The only launch change is passing the absolute output path.
