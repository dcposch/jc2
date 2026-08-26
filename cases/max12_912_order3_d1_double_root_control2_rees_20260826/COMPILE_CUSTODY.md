# Dual AWS compile custody

Both AWS compilers returned rc zero, empty stderr, exactly one compiler PASS
marker, and identical generator-initial reports.  The displayed residue kills
the minimum-weight form of all eight charged rows and the toric relation.

## Box02 / encoding A job

```text
tag  max12_912_order3_d1_double_root_control2_rees_20260826T004241Z_box02_A
payload  bae00d766c8ccb6a1ab0c5eae2de4982248e8f7664e8d9cc8d19a07bc859111a
912a6e27768a68753a63ff9d4dbed3c05af3051a4308892b11a4a3b140a5a944  compiled/control2_rees_A_factored_sat_dp.sing
012facdaf129ab8cf8d4c0445f08b65e5a8f6559e87332c24a4204bbbec8b1cd  compiled/control2_rees_B_expanded_inverse_lpdp.sing
```

## r6d / encoding B job

```text
tag  max12_912_order3_d1_double_root_control2_rees_20260826T004241Z_r6d_B
payload  fe56c12b6718c8df75dceb4b4391b43751a991b50043990d056e21a7186f0db2
99a0ed11a276a736e2ea183f7d9dfbd306bfeb62cec200b794a51662eaec54d1  compiled/control2_rees_A_factored_sat_dp.sing
13e141777a6c9a5c48a7030c29b6df10c1d7b93ee7b2adf8b6a4d5a415c39e69  compiled/control2_rees_B_expanded_inverse_lpdp.sing
```

Only the embedded AWS tag differs.  After replacing that tag by `TAG`, the
cross-host hashes agree exactly:

```text
faee98eb729eb0ed2099e89871d7894636b82d227efa2213725beb1fd99ee451  control2_rees_A_factored_sat_dp.sing.normalized
f55f7e51408328f46322ba077f074e6ecf928acc2dc8b16f6e910542c1c5afdf  control2_rees_B_expanded_inverse_lpdp.sing.normalized
```

This compile endpoint is a source check only.  It is not the initial-ideal
residue verdict.

