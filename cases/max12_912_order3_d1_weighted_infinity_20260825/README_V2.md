# V2 AWS launch

V1 is a preserved syntax-failure negative.  Use only the V2 runner, from a
closure-complete staged repository and under a fresh EC2 tag:

```sh
export JC2_AWS_TAG=max12_912_order3_d1_infty_exceptional_v2_<UTC>_<HOST>
export D1_INFINITY_RUN_DIR=/home/ubuntu/jobs/$JC2_AWS_TAG
export D1_INFINITY_CHARACTERISTIC=0
export D1_INFINITY_CHART=global
bash cases/max12_912_order3_d1_weighted_infinity_20260825/run_exceptional_v2_aws.sh
```

Do not launch all eight affine charts unless the global saturated result is
inconclusive or a targeted coverage control is requested.

