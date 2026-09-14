#!/bin/bash
set -euo pipefail
test "$(id -u)" = 0
test "$(tr -d '\n' < /sys/class/dmi/id/board_asset_tag)" = i-0941baf1a7ff9131b
test "$(systemctl show jc2-f10-r2-fullunit-ready-20260910T1800-typefix.service -p MainPID --value)" = 0
test "$(systemctl show jc2-f10-r2-fullunit-ready-20260910T1800-typefix.service -p ControlPID --value)" = 0
test ! -e /sys/fs/cgroup/system.slice/jc2-f10-r2-fullunit-ready-20260910T1800-typefix.service
test ! -e /proc/17260
test ! -e /proc/17330
test ! -e /proc/17329
test ! -e /proc/17338
test ! -e /proc/17337
test ! -e /proc/17343
test ! -e /proc/17342
test ! -e /proc/17348
test ! -e /proc/17347
date -u '+FULLUNIT_TERMINAL_HARVEST_BEGIN %Y-%m-%d %H:%M:%S.%N UTC'
sha256sum -c <<'JC2_ALL_TERMINAL_PINS' > /home/ubuntu/jc2-r2-fullunit-ready-20260910T1800-typefix/stage/terminal-pin-recheck.log
13ea41aa0f67c93582574a466d830e5a31817e9235cb30d2b3b2034557b0e014  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/dummy.post.json
13ea41aa0f67c93582574a466d830e5a31817e9235cb30d2b3b2034557b0e014  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/dummy.post.json
74c640c9bca587723813428aeb9a487bf322591ecfb41c491f1e0638175aa389  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/dummy.pre.json
74c640c9bca587723813428aeb9a487bf322591ecfb41c491f1e0638175aa389  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/dummy.pre.json
5a4770b10cb03b7648ef56d980b57e7be4036c13b96677d37739df94e9ac0d7e  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/dummy.python-live.json
5a4770b10cb03b7648ef56d980b57e7be4036c13b96677d37739df94e9ac0d7e  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/dummy.python-live.json
ba62e26b1b383e10b603be5b61dad213a68e7db0986894b95e872b0f06a61061  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/dummy.runner-live.json
ba62e26b1b383e10b603be5b61dad213a68e7db0986894b95e872b0f06a61061  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/dummy.runner-live.json
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/dummy.runner.stderr
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/dummy.runner.stderr
e762a1dfa7d7d8b6003dda6e95b257758f8bb0fb1605e7a0414663fac98c0fe1  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/dummy.runner.stdout
e762a1dfa7d7d8b6003dda6e95b257758f8bb0fb1605e7a0414663fac98c0fe1  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/dummy.runner.stdout
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/dummy.stderr
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/dummy.stderr
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/dummy.stdout
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/dummy.stdout
7dec038583f33f0067c7fb2ae056f1b7a4564155fee3ab68f08f2fc8979094ab  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/dummy.telemetry.json
7dec038583f33f0067c7fb2ae056f1b7a4564155fee3ab68f08f2fc8979094ab  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/dummy.telemetry.json
ed4c2a48430ff7692d3b59168ba403dce0eae1a1faf7aed13cad6c49b0a6ec9d  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-binding.json
ed4c2a48430ff7692d3b59168ba403dce0eae1a1faf7aed13cad6c49b0a6ec9d  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-binding.json
31c1b32542bf8c46d66b44c7890080117ea417f6d4f7ccdef716c75c212c23eb  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-negative.post.json
31c1b32542bf8c46d66b44c7890080117ea417f6d4f7ccdef716c75c212c23eb  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-negative.post.json
615e38dfe779abf5a098e0ea6c373b7afc0c2f31b9f1c2e317f243f4e8d8e9d5  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-negative.pre.json
615e38dfe779abf5a098e0ea6c373b7afc0c2f31b9f1c2e317f243f4e8d8e9d5  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-negative.pre.json
ad27d1feeb65e1df7bb792b9b445f5f094f0ce34961d0164aefd536c535a0c8a  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-negative.python-live.json
ad27d1feeb65e1df7bb792b9b445f5f094f0ce34961d0164aefd536c535a0c8a  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-negative.python-live.json
d3da9dddf40c67c2a95b42a60a856990a3e3238b2243380c49d103583191075e  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-negative.runner-live.json
d3da9dddf40c67c2a95b42a60a856990a3e3238b2243380c49d103583191075e  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-negative.runner-live.json
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-negative.runner.stderr
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-negative.runner.stderr
3addea19d82e63956c7dd6b0f4939946af0f26871fb701ac952687990b114382  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-negative.runner.stdout
3addea19d82e63956c7dd6b0f4939946af0f26871fb701ac952687990b114382  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-negative.runner.stdout
399a74d08daf911cd59e38a0eddfdab40288ec19db9d5e403053be58a220c550  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-negative.stderr
399a74d08daf911cd59e38a0eddfdab40288ec19db9d5e403053be58a220c550  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-negative.stderr
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-negative.stdout
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-negative.stdout
4274618cf4c52e41ac57ca889bb756d006a2890c879b47368fdd91f2220dcbd1  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-negative.telemetry.json
4274618cf4c52e41ac57ca889bb756d006a2890c879b47368fdd91f2220dcbd1  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-negative.telemetry.json
aa111416464967e32e38f49c08811c0bcb0881e9a8109aecfff636c2db1c02e5  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-positive.post.json
aa111416464967e32e38f49c08811c0bcb0881e9a8109aecfff636c2db1c02e5  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-positive.post.json
94d11c0c549e9532cbd68c7a8438b8e39bcfa12d7ab32adfac555bb81ef3914a  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-positive.pre.json
94d11c0c549e9532cbd68c7a8438b8e39bcfa12d7ab32adfac555bb81ef3914a  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-positive.pre.json
344637a9bb3897779e157d4b689d4161cdbde3ea82f5600486908aa2ca19a5ec  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-positive.python-live.json
344637a9bb3897779e157d4b689d4161cdbde3ea82f5600486908aa2ca19a5ec  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-positive.python-live.json
a1c5a1f8a42a6d1b38b2401cf92710c77fabfd97d46d4e1446e4a981650296c2  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-positive.runner-live.json
a1c5a1f8a42a6d1b38b2401cf92710c77fabfd97d46d4e1446e4a981650296c2  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-positive.runner-live.json
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-positive.runner.stderr
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-positive.runner.stderr
a03375017b639c9161dbbd28f5ac8de2ceac07498429ffbee4d40b9b23133709  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-positive.runner.stdout
a03375017b639c9161dbbd28f5ac8de2ceac07498429ffbee4d40b9b23133709  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-positive.runner.stdout
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-positive.stderr
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-positive.stderr
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-positive.stdout
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-positive.stdout
1b1c47d23c5944168395e05c736bd0f10359b4ee5c4aade764b35fe07b776c7b  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-positive.telemetry.json
1b1c47d23c5944168395e05c736bd0f10359b4ee5c4aade764b35fe07b776c7b  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-positive.telemetry.json
22f48da46c07c6cef3820ac69d0a51797757438e1553042fc2d09f9f3c553811  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-produce.post.json
22f48da46c07c6cef3820ac69d0a51797757438e1553042fc2d09f9f3c553811  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-produce.post.json
d573b833257eb9607c932438a1ae621177c225aacff51877a4103c37f4ac29e7  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-produce.pre.json
d573b833257eb9607c932438a1ae621177c225aacff51877a4103c37f4ac29e7  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-produce.pre.json
f16499874a834599cf6ad07cd02510f8defe9e78b395a7a2cd53c79112089a6d  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-produce.python-live.json
f16499874a834599cf6ad07cd02510f8defe9e78b395a7a2cd53c79112089a6d  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-produce.python-live.json
df7be5bc454308ad2aee5f03230ba06b27cd20f9517bef0398f0ec278d2caa0f  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-produce.runner-live.json
df7be5bc454308ad2aee5f03230ba06b27cd20f9517bef0398f0ec278d2caa0f  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-produce.runner-live.json
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-produce.runner.stderr
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-produce.runner.stderr
e732719e8a10556eeafe937749cf30e68468594f6c79a6157949f8a7496b9d92  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-produce.runner.stdout
e732719e8a10556eeafe937749cf30e68468594f6c79a6157949f8a7496b9d92  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-produce.runner.stdout
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-produce.stderr
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-produce.stderr
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-produce.stdout
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-produce.stdout
262cd2fc2ee2a5d3a788cdfabd4db045664cc74872880af8aeaa9ecea18f7ff9  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-produce.telemetry.json
262cd2fc2ee2a5d3a788cdfabd4db045664cc74872880af8aeaa9ecea18f7ff9  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit-produce.telemetry.json
beb6b01751ddc1da8fd81732ecabba80430cf97ed65464ad55239bc623869d19  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/mutate.post.json
beb6b01751ddc1da8fd81732ecabba80430cf97ed65464ad55239bc623869d19  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/mutate.post.json
0a4dbb6ac66ba525705eeb9dac6cfe5f5993cff54ad40a430f6b6e15fe83330f  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/mutate.pre.json
0a4dbb6ac66ba525705eeb9dac6cfe5f5993cff54ad40a430f6b6e15fe83330f  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/mutate.pre.json
e9d72b7d9f789d9b7e913b3ce9270cb2c4e43f8639f3ca1b09c37147753c76f2  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/mutate.python-live.json
e9d72b7d9f789d9b7e913b3ce9270cb2c4e43f8639f3ca1b09c37147753c76f2  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/mutate.python-live.json
3076a469c0c95dcb41a00e26dc370c1995397caaf955728a79ed01ab2e6b22e9  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/mutate.runner-live.json
3076a469c0c95dcb41a00e26dc370c1995397caaf955728a79ed01ab2e6b22e9  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/mutate.runner-live.json
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/mutate.runner.stderr
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/mutate.runner.stderr
840e310ed33c3c95bb3e897a95bf495b3a613bd6d0d08800292c8eeaae620675  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/mutate.runner.stdout
840e310ed33c3c95bb3e897a95bf495b3a613bd6d0d08800292c8eeaae620675  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/mutate.runner.stdout
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/mutate.stderr
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/mutate.stderr
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/mutate.stdout
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/mutate.stdout
dbb1ece76588f20494dc2f3bb1d97c61ed081bf10e02fef50fe7197aa1626f60  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/mutate.telemetry.json
dbb1ece76588f20494dc2f3bb1d97c61ed081bf10e02fef50fe7197aa1626f60  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/mutate.telemetry.json
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/outer.stderr
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/outer.stderr
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/outer.stdout
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/outer.stdout
4d8e961a52267741136bd9fd5e4716199bc78d6f0eb332b31dcd39c09525eb66  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-caps.post.json
4d8e961a52267741136bd9fd5e4716199bc78d6f0eb332b31dcd39c09525eb66  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-caps.post.json
1a5dac48ebc2f76a685b4c944f7691177c22577d85197b3f70868bf167eeccd0  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-caps.pre.json
1a5dac48ebc2f76a685b4c944f7691177c22577d85197b3f70868bf167eeccd0  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-caps.pre.json
6d6c460d5199bc7d16cf6bc82b5db193836b184846edcde0aa93161e6fe8febf  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-caps.python-live.json
6d6c460d5199bc7d16cf6bc82b5db193836b184846edcde0aa93161e6fe8febf  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-caps.python-live.json
689b08ded2f1d2231107f457537a82dd85f1a28c6b3d351d4494c49ee53e959b  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-caps.runner-live.json
689b08ded2f1d2231107f457537a82dd85f1a28c6b3d351d4494c49ee53e959b  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-caps.runner-live.json
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-caps.runner.stderr
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-caps.runner.stderr
1bf55e7ea7bab6a71dd5237c27ca5b17de86dc812d5ce890e9784b68c1bf8403  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-caps.runner.stdout
1bf55e7ea7bab6a71dd5237c27ca5b17de86dc812d5ce890e9784b68c1bf8403  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-caps.runner.stdout
dae62a8069debe9ee96da73729fff509ea94e283474e31fcbb052e4096765f92  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-caps.stderr
dae62a8069debe9ee96da73729fff509ea94e283474e31fcbb052e4096765f92  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-caps.stderr
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-caps.stdout
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-caps.stdout
f7958fa582d97bff9f063d3b32f68095664aee22857dd231ad6e1a1e0c51fb1f  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-caps.telemetry.json
f7958fa582d97bff9f063d3b32f68095664aee22857dd231ad6e1a1e0c51fb1f  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-caps.telemetry.json
dabe5634aa7d6e259a730c12e81c28df336d59bd315f3b41a3c81e4db4bd7af9  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-hash.post.json
dabe5634aa7d6e259a730c12e81c28df336d59bd315f3b41a3c81e4db4bd7af9  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-hash.post.json
73e4d7bc597ddb7a2d1ae782ec89166bb19de2e7c06333905fe27ab13b5f854d  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-hash.pre.json
73e4d7bc597ddb7a2d1ae782ec89166bb19de2e7c06333905fe27ab13b5f854d  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-hash.pre.json
b982833a7290eb90314d2babf8f9a3331158ece58ea9d02a0059b90315451d77  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-hash.python-live.json
b982833a7290eb90314d2babf8f9a3331158ece58ea9d02a0059b90315451d77  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-hash.python-live.json
a546812bf6d754afc3f9698a75a8f0f8d8482c3a239fb8c75422cf9413f9f73e  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-hash.runner-live.json
a546812bf6d754afc3f9698a75a8f0f8d8482c3a239fb8c75422cf9413f9f73e  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-hash.runner-live.json
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-hash.runner.stderr
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-hash.runner.stderr
e13e4175a4f3e46108c9c743046bf8a762509d9342d05db74d61232eb18fa739  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-hash.runner.stdout
e13e4175a4f3e46108c9c743046bf8a762509d9342d05db74d61232eb18fa739  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-hash.runner.stdout
041724d54a4dd4e7c35f0fedf2d9eaf6c24449fca02fde474921d571eb66f158  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-hash.stderr
041724d54a4dd4e7c35f0fedf2d9eaf6c24449fca02fde474921d571eb66f158  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-hash.stderr
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-hash.stdout
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-hash.stdout
386a10c28143a7a8780c133fb1340e14a3b6d6b21e72dd81cb9a6353be1f0309  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-hash.telemetry.json
386a10c28143a7a8780c133fb1340e14a3b6d6b21e72dd81cb9a6353be1f0309  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-hash.telemetry.json
12f413fe57fe4e8fd30e6e61d3fbbdb851ef4ead101ab5409b47bd2b571b457a  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-inventory.post.json
12f413fe57fe4e8fd30e6e61d3fbbdb851ef4ead101ab5409b47bd2b571b457a  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-inventory.post.json
6bf60013b3304679c4613140ce9adef79ab48944b780a33bbd34097fee1c9770  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-inventory.pre.json
6bf60013b3304679c4613140ce9adef79ab48944b780a33bbd34097fee1c9770  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-inventory.pre.json
e5334cdf74ef70cb9ac250dc3141aad0788344d77d80ac0ec11b1bdab1d5336f  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-inventory.python-live.json
e5334cdf74ef70cb9ac250dc3141aad0788344d77d80ac0ec11b1bdab1d5336f  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-inventory.python-live.json
cc7cf1127cea034d2ea53f25988f73319a30d202455a370b2e033ade1df2eed1  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-inventory.runner-live.json
cc7cf1127cea034d2ea53f25988f73319a30d202455a370b2e033ade1df2eed1  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-inventory.runner-live.json
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-inventory.runner.stderr
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-inventory.runner.stderr
e3ecca4f0a04e006765ff1038eecbb8123e2a4b0719b55a83f72d804255cc3c2  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-inventory.runner.stdout
e3ecca4f0a04e006765ff1038eecbb8123e2a4b0719b55a83f72d804255cc3c2  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-inventory.runner.stdout
dae62a8069debe9ee96da73729fff509ea94e283474e31fcbb052e4096765f92  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-inventory.stderr
dae62a8069debe9ee96da73729fff509ea94e283474e31fcbb052e4096765f92  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-inventory.stderr
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-inventory.stdout
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-inventory.stdout
3d74ac87737925d0bc88268d51caabca3628201455a0971cafd97aa2a6e34901  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-inventory.telemetry.json
3d74ac87737925d0bc88268d51caabca3628201455a0971cafd97aa2a6e34901  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-inventory.telemetry.json
618410b9abcdf9c5c175d1d7203eef66c1eadc18361d0e7a6435558766ac2861  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-source.post.json
618410b9abcdf9c5c175d1d7203eef66c1eadc18361d0e7a6435558766ac2861  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-source.post.json
841a9f92932ccdf0f1415565e103052ef963ad18cf37e9c7024d2e79b4a351fb  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-source.pre.json
841a9f92932ccdf0f1415565e103052ef963ad18cf37e9c7024d2e79b4a351fb  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-source.pre.json
6ed4227af701b5e89747245ed0e38b17f5225461ac7c740df32f9fc23f569eba  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-source.python-live.json
6ed4227af701b5e89747245ed0e38b17f5225461ac7c740df32f9fc23f569eba  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-source.python-live.json
1c54188173241e31c393d47dd9f6899107100230eb49c6667fe7b5bfe2d86117  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-source.runner-live.json
1c54188173241e31c393d47dd9f6899107100230eb49c6667fe7b5bfe2d86117  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-source.runner-live.json
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-source.runner.stderr
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-source.runner.stderr
61c4821f4b5da03010c651a3de3a22aab5d48d352b18512489c15f26bc51b67a  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-source.runner.stdout
61c4821f4b5da03010c651a3de3a22aab5d48d352b18512489c15f26bc51b67a  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-source.runner.stdout
24d2d0226228a57cf3702687a4e0dc9357d381209ce941a62d617f1e06e08d38  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-source.stderr
24d2d0226228a57cf3702687a4e0dc9357d381209ce941a62d617f1e06e08d38  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-source.stderr
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-source.stdout
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-source.stdout
f99a6ea84d7c823a49f887dae2c3e6be899f7b8e9efbdf027dfbc64e0a39eb3d  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-source.telemetry.json
f99a6ea84d7c823a49f887dae2c3e6be899f7b8e9efbdf027dfbc64e0a39eb3d  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-source.telemetry.json
817e809a60cb725d4bcbf9f2062b7e75c9f823515721dec17d6a9a2ffcd2d755  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-status.post.json
817e809a60cb725d4bcbf9f2062b7e75c9f823515721dec17d6a9a2ffcd2d755  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-status.post.json
eb77a747472b1cfa133798d2bc089060f7b01283bade13f3a1d237cd72bebde7  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-status.pre.json
eb77a747472b1cfa133798d2bc089060f7b01283bade13f3a1d237cd72bebde7  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-status.pre.json
734e3b62dd8384976b166de3cd915b97362349fde782d8f74c5881917e9077f2  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-status.python-live.json
734e3b62dd8384976b166de3cd915b97362349fde782d8f74c5881917e9077f2  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-status.python-live.json
566b44cfa610219307d0dc1a52ba342725036d89703f481c4117cf8b02e296f5  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-status.runner-live.json
566b44cfa610219307d0dc1a52ba342725036d89703f481c4117cf8b02e296f5  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-status.runner-live.json
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-status.runner.stderr
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-status.runner.stderr
5df6b00b38613df234f0b82c80ae542a540fddb20e9551ede41ba7821aee574d  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-status.runner.stdout
5df6b00b38613df234f0b82c80ae542a540fddb20e9551ede41ba7821aee574d  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-status.runner.stdout
42f168d6e45cdd4033b9976ccfc4802801267953afe2582dafa9aedd54335dd9  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-status.stderr
42f168d6e45cdd4033b9976ccfc4802801267953afe2582dafa9aedd54335dd9  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-status.stderr
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-status.stdout
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-status.stdout
9578fbc8e17db52daa558e0648a8afd847e76daf3ab3a383b9dc53fc887db3ee  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-status.telemetry.json
9578fbc8e17db52daa558e0648a8afd847e76daf3ab3a383b9dc53fc887db3ee  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/refuse-status.telemetry.json
2f2c6c42a2652aa09ea828d1b7468e9d0ee3164a4e147d5b32ea1a70161659e3  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/startup-check.post.json
2f2c6c42a2652aa09ea828d1b7468e9d0ee3164a4e147d5b32ea1a70161659e3  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/startup-check.post.json
c11f87fea755835ec4003946a9f3e2c2e1053b7eb0e3c51fd1b6acaa25ddd109  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/startup-check.pre.json
c11f87fea755835ec4003946a9f3e2c2e1053b7eb0e3c51fd1b6acaa25ddd109  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/startup-check.pre.json
60a7aa8209cda5b24c1987f9f78e6774bc895ca40ad07b2edd279faf138d6354  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/startup-check.python-live.json
60a7aa8209cda5b24c1987f9f78e6774bc895ca40ad07b2edd279faf138d6354  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/startup-check.python-live.json
3e3bf46a7ffd30f1da873ed32cc2f1f6c0efc11b1cb499581efba164e81bc818  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/startup-check.runner-live.json
3e3bf46a7ffd30f1da873ed32cc2f1f6c0efc11b1cb499581efba164e81bc818  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/startup-check.runner-live.json
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/startup-check.runner.stderr
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/startup-check.runner.stderr
6291692f3df754d9a20069b66cf23db3b3b5cd7e5ca02386299ac47168d5577a  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/startup-check.runner.stdout
6291692f3df754d9a20069b66cf23db3b3b5cd7e5ca02386299ac47168d5577a  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/startup-check.runner.stdout
fcb37579a72a36707ba32fe6b2a6006054c0b5d2d01c43ee3a4be44cab78c102  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/startup-check.stderr
fcb37579a72a36707ba32fe6b2a6006054c0b5d2d01c43ee3a4be44cab78c102  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/startup-check.stderr
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/startup-check.stdout
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/startup-check.stdout
ca5db63e83f694afdf5c60aea0c96cab9cd9ba5555e50320c364f7d1c0baf783  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/startup-check.telemetry.json
ca5db63e83f694afdf5c60aea0c96cab9cd9ba5555e50320c364f7d1c0baf783  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/startup-check.telemetry.json
c745e9e560ea58651472e92958257684d45213390183d01b07bb41d3b9a7c1c7  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/startup-produce.post.json
c745e9e560ea58651472e92958257684d45213390183d01b07bb41d3b9a7c1c7  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/startup-produce.post.json
4d573dc0914b808607040662b0a7028a36eb07da369f96cd3c59a206de6c20f6  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/startup-produce.pre.json
4d573dc0914b808607040662b0a7028a36eb07da369f96cd3c59a206de6c20f6  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/startup-produce.pre.json
e513131f4eab2177e383fd7a4d0b28969f51bd162479b8c3cbd4cf4f0d4c2148  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/startup-produce.python-live.json
e513131f4eab2177e383fd7a4d0b28969f51bd162479b8c3cbd4cf4f0d4c2148  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/startup-produce.python-live.json
0e0ed7469719fb9067e1c64399acba2985bab8b236a14b09ea55252491285793  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/startup-produce.runner-live.json
0e0ed7469719fb9067e1c64399acba2985bab8b236a14b09ea55252491285793  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/startup-produce.runner-live.json
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/startup-produce.runner.stderr
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/startup-produce.runner.stderr
abb5a6cffe3c04905de558ae0631ab2b6fda9409c00ac9bd89b14152efb6fc4f  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/startup-produce.runner.stdout
abb5a6cffe3c04905de558ae0631ab2b6fda9409c00ac9bd89b14152efb6fc4f  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/startup-produce.runner.stdout
fcb37579a72a36707ba32fe6b2a6006054c0b5d2d01c43ee3a4be44cab78c102  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/startup-produce.stderr
fcb37579a72a36707ba32fe6b2a6006054c0b5d2d01c43ee3a4be44cab78c102  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/startup-produce.stderr
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/startup-produce.stdout
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/startup-produce.stdout
5a903dcd05c017e3ce3c7960166c728f22ff3bccd0590415bcc5bc9b0a4f4c3d  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/startup-produce.telemetry.json
5a903dcd05c017e3ce3c7960166c728f22ff3bccd0590415bcc5bc9b0a4f4c3d  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/startup-produce.telemetry.json
2c2054dbfa434f7b31c0b31f105c47ddd604f8a9a73d33d5c4651e8491557524  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/valid.post.json
2c2054dbfa434f7b31c0b31f105c47ddd604f8a9a73d33d5c4651e8491557524  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/valid.post.json
a1897234e6ead6f86e9c6bd6b3875a10e3da4568af0e7e8f2d3132ded404322b  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/valid.pre.json
a1897234e6ead6f86e9c6bd6b3875a10e3da4568af0e7e8f2d3132ded404322b  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/valid.pre.json
923766cb46207978df70747d5212d3af0d0e8c7e6ff466081dd17ac82efe9b70  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/valid.python-live.json
923766cb46207978df70747d5212d3af0d0e8c7e6ff466081dd17ac82efe9b70  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/valid.python-live.json
85f05166e40bdaf2520a7819adf502369e4be1de7b57eda9d420cdc867dd6a96  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/valid.runner-live.json
85f05166e40bdaf2520a7819adf502369e4be1de7b57eda9d420cdc867dd6a96  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/valid.runner-live.json
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/valid.runner.stderr
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/valid.runner.stderr
52a5d1c85e7d5fa70e2f8b554de71a3e58c8113d76058dd005340d3f4741fcfa  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/valid.runner.stdout
52a5d1c85e7d5fa70e2f8b554de71a3e58c8113d76058dd005340d3f4741fcfa  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/valid.runner.stdout
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/valid.stderr
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/valid.stderr
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/valid.stdout
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/valid.stdout
18b8dcc76265d45508ba002eb3b4a560248e775e5d42336187146b08b05aa09d  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/valid.telemetry.json
18b8dcc76265d45508ba002eb3b4a560248e775e5d42336187146b08b05aa09d  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/valid.telemetry.json
57d3e85c1f016aa5b05eed81ac6dda2e7bbbba8cdf05f3a1084708ad1228d20b  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/writer/dummy.payload
57d3e85c1f016aa5b05eed81ac6dda2e7bbbba8cdf05f3a1084708ad1228d20b  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/writer/dummy.payload
94c1f3ac5a3eff01ac31e6a7e82e1e641f7820472acced61849af2981420dab8  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/writer/valid.payload
94c1f3ac5a3eff01ac31e6a7e82e1e641f7820472acced61849af2981420dab8  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/writer/valid.payload
a8890f17f04e9d4b54dfb68e7ff13e3ab192baa1235abc0004ba7a75b5f72cfe  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/frozen/candidate.json
a8890f17f04e9d4b54dfb68e7ff13e3ab192baa1235abc0004ba7a75b5f72cfe  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/frozen/candidate.json
785a0363aeb23cddbf56a34eb9e876cf115ab85dcbc17029a84b6c3f11549de6  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/frozen/changed.json
785a0363aeb23cddbf56a34eb9e876cf115ab85dcbc17029a84b6c3f11549de6  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/frozen/changed.json
f382b4a46ad0fd0e4d7d97ac2ccc37719ea8af002c8215f1df938d577257e911  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/frozen/fullunit-positive.receipt.json
f382b4a46ad0fd0e4d7d97ac2ccc37719ea8af002c8215f1df938d577257e911  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/frozen/fullunit-positive.receipt.json
d1dac8345b925f5511967396da41e7232eeec40c85cc140bfaf4753f23c5840b  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/frozen/fullunit-produce.receipt.json
d1dac8345b925f5511967396da41e7232eeec40c85cc140bfaf4753f23c5840b  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/frozen/fullunit-produce.receipt.json
00815dc07ef192b6045f786461097536fdd087476d9115e203974778f720dac2  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/frozen/mutate.receipt.json
00815dc07ef192b6045f786461097536fdd087476d9115e203974778f720dac2  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/frozen/mutate.receipt.json
06ee10099961c88fcb1c214121bbf9123e2e2ea73b45fa75ffdd35f8bed82e93  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/authority/dummy.json
06ee10099961c88fcb1c214121bbf9123e2e2ea73b45fa75ffdd35f8bed82e93  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/authority/dummy.json
06ee10099961c88fcb1c214121bbf9123e2e2ea73b45fa75ffdd35f8bed82e93  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/authority/fullunit-negative.json
06ee10099961c88fcb1c214121bbf9123e2e2ea73b45fa75ffdd35f8bed82e93  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/authority/fullunit-negative.json
06ee10099961c88fcb1c214121bbf9123e2e2ea73b45fa75ffdd35f8bed82e93  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/authority/fullunit-positive.json
06ee10099961c88fcb1c214121bbf9123e2e2ea73b45fa75ffdd35f8bed82e93  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/authority/fullunit-positive.json
06ee10099961c88fcb1c214121bbf9123e2e2ea73b45fa75ffdd35f8bed82e93  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/authority/fullunit-produce.json
06ee10099961c88fcb1c214121bbf9123e2e2ea73b45fa75ffdd35f8bed82e93  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/authority/fullunit-produce.json
06ee10099961c88fcb1c214121bbf9123e2e2ea73b45fa75ffdd35f8bed82e93  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/authority/mutate.json
06ee10099961c88fcb1c214121bbf9123e2e2ea73b45fa75ffdd35f8bed82e93  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/authority/mutate.json
84960430860ffe8a1f5c68210165929aa8f58e323abb665eb22d59c1da597bed  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/authority/refuse-caps.json
84960430860ffe8a1f5c68210165929aa8f58e323abb665eb22d59c1da597bed  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/authority/refuse-caps.json
06ee10099961c88fcb1c214121bbf9123e2e2ea73b45fa75ffdd35f8bed82e93  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/authority/refuse-hash.json
06ee10099961c88fcb1c214121bbf9123e2e2ea73b45fa75ffdd35f8bed82e93  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/authority/refuse-hash.json
0f2a944e390aa7e6b58e24c1a7c1d55a4c5e36ee6a662ce258f491553d6e3767  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/authority/refuse-inventory.json
0f2a944e390aa7e6b58e24c1a7c1d55a4c5e36ee6a662ce258f491553d6e3767  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/authority/refuse-inventory.json
d884d28971d30a4aa58b4a30987d42cbc83fe084a51469905ff301486a4be0d3  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/authority/refuse-source.json
d884d28971d30a4aa58b4a30987d42cbc83fe084a51469905ff301486a4be0d3  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/authority/refuse-source.json
969f5e6d10c30218a4033ad4ca13e1bc30958c297b9d9ab92a1885986d84ee48  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/authority/refuse-status.json
969f5e6d10c30218a4033ad4ca13e1bc30958c297b9d9ab92a1885986d84ee48  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/authority/refuse-status.json
06ee10099961c88fcb1c214121bbf9123e2e2ea73b45fa75ffdd35f8bed82e93  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/authority/startup-check.json
06ee10099961c88fcb1c214121bbf9123e2e2ea73b45fa75ffdd35f8bed82e93  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/authority/startup-check.json
06ee10099961c88fcb1c214121bbf9123e2e2ea73b45fa75ffdd35f8bed82e93  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/authority/startup-produce.json
06ee10099961c88fcb1c214121bbf9123e2e2ea73b45fa75ffdd35f8bed82e93  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/authority/startup-produce.json
06ee10099961c88fcb1c214121bbf9123e2e2ea73b45fa75ffdd35f8bed82e93  /run/jc2-r2-fullunit-ready-20260910T1800-typefix/authority/valid.json
06ee10099961c88fcb1c214121bbf9123e2e2ea73b45fa75ffdd35f8bed82e93  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/authority/valid.json
8113a3b52560e1b341b0087758ee8ff421601ed40cd0ebaf7d4ec5dce7ae5681  /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/CUSTODY.json
2a274ac4cf866762bc1f2734b3af8d515ff7be93c0fe0d4500e56dbca2ef093b  /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/science/authority.py
fe9ab1abe9a96fc43b889e1bcb598f8e8c65fd194732c48f3542e13c476e0345  /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/science/arithmetic.py
eeb3fe3bbbe232ffe080a2a0a5db2c1f3ac60b83b61dd7798ff56e2f97977b10  /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/science/produce.py
e5dd4bcb6114df2bdd79c8336583942c18d698d99fffd6f4b171e46a5d503d6e  /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/science/check_arithmetic.py
e6bc7cca0d9c776a898bda3f0648af883e17a675f2b81bba52031459f4c640a0  /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/science/check.py
b6998cae2d38e962777dc1064f39a841cfee3e5bb0fc3905599a5378aa78ff69  /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/wrapper/dispatch.py
1e3bea3ad995ca64780f77b33792ed09c9843fb3925aae5f64c7a2abcaa0ecde  /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/wrapper/probe.py
4548656af387b7e08df5bd5c56504f97c2d11d2b5375cbfbadde5304465c4c97  /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/wrapper/mutate.py
4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2  /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/metadata/run_capped.py
dac655a7ce75287b06010171bce66af1a644aff81de9620a452457a5f65a9587  /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/metadata/artifact.json
6ac39ea21b716938ae0c375e0dc6e7447a1aaba83fb71e96be1bd5bf7f349ffb  /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/metadata/native-manifest.json
d5f147d3c816a2439ee34aec49928d07981fd571e5cc043a05c404ff4ca71c03  /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/metadata/ROOT-EXECUTION-CARD.md
cb0da8dcfe19a033f9daad1de7de4e602a330f15a90c383824550522b8d847eb  /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/metadata/CONTRACT.md
ed4173cff602b016951e178818bdfd3bef1fe7be5f8bfcdafce7ef1e6aa277ea  /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/metadata/ROOT-REGISTRATION.json
c49b7dfabe6dc8cc5b7aaea485171a6b709fc6158f180ae1157afd90b3cf4b1f  /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit/entry.py
60a290aee2ed5def7ed4242743f187dea755659f287707fa79c6c1e05f2d1f10  /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit/produce.py
ccc3d2ddfca98f7faaed9df323fb90ec183b437b3c6b0bfcde0820186e667023  /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/fullunit/check.py
eca8d1e56b4d119c346e56be9730281169097c747468cc195df26c961213e317  /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/metadata/f10-r2-fullunit-runtime-gate-fable5-20260910.md
d6ff5b7ad5248b0ef2a57fb2dbda042a5f4f92237d78c4b12e651288b4de28f5  /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/metadata/native.stdout
13ea6cfb00cc6be26967f50909214b7d14dd93dea8537011365ef6d7204238b1  /opt/jc2-r2-fullunit-ready-20260910T1800-typefix/metadata/native.sha256
JC2_ALL_TERMINAL_PINS
test "$(wc -l < /home/ubuntu/jc2-r2-fullunit-ready-20260910T1800-typefix/stage/terminal-pin-recheck.log)" = 301
sha256sum -c /home/ubuntu/jc2-r2-fullunit-ready-20260910T1800-typefix/stage/native.sha256 > /home/ubuntu/jc2-r2-fullunit-ready-20260910T1800-typefix/stage/native-postcheck.log
bash /home/ubuntu/jc2-r2-fullunit-ready-20260910T1800/stage/native-metadata.sh > /home/ubuntu/jc2-r2-fullunit-ready-20260910T1800-typefix/stage/native-post.stdout 2> /home/ubuntu/jc2-r2-fullunit-ready-20260910T1800-typefix/stage/native-post.stderr
test ! -s /home/ubuntu/jc2-r2-fullunit-ready-20260910T1800-typefix/stage/native-post.stderr
diff -u <(sed '/^NATIVE_START /d; /^NATIVE_END /d' /home/ubuntu/jc2-r2-fullunit-ready-20260910T1800-typefix/stage/native.stdout) <(sed '/^NATIVE_START /d; /^NATIVE_END /d' /home/ubuntu/jc2-r2-fullunit-ready-20260910T1800-typefix/stage/native-post.stdout)
for jc2_frozen in candidate.json changed.json fullunit-produce.receipt.json fullunit-positive.receipt.json mutate.receipt.json; do
 test "$(stat -c '%u %g %a' /run/jc2-r2-fullunit-ready-20260910T1800-typefix/frozen/$jc2_frozen)" = '0 0 444'
done
install -o 1000 -g 1000 -m 0444 /var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix/CUSTODY.json /home/ubuntu/jc2-r2-fullunit-ready-20260910T1800-typefix/CUSTODY.json
systemctl stop jc2-r2-fullunit-ready-outer-term-20260910T1800-typefix.timer jc2-r2-fullunit-ready-outer-kill-20260910T1800-typefix.timer
date -u '+ORIGINAL_CORRECTED_SYSTEM_TIMERS_CLOSED %Y-%m-%d %H:%M:%S.%N UTC'
test ! -e /home/ubuntu/jc2-r2-fullunit-ready-20260910T1800-typefix/evidence.tar.gz
tar -czf /home/ubuntu/jc2-r2-fullunit-ready-20260910T1800-typefix/evidence.tar.gz -C / opt/jc2-r2-fullunit-ready-20260910T1800-typefix run/jc2-r2-fullunit-ready-20260910T1800-typefix var/lib/jc2-r2-fullunit-ready-20260910T1800-typefix home/ubuntu/jc2-r2-fullunit-ready-20260910T1800-typefix/stage home/ubuntu/jc2-r2-fullunit-ready-20260910T1800/refusal-evidence.tar.gz
tar -df /home/ubuntu/jc2-r2-fullunit-ready-20260910T1800-typefix/evidence.tar.gz -C /
sync /home/ubuntu/jc2-r2-fullunit-ready-20260910T1800-typefix/evidence.tar.gz /home/ubuntu/jc2-r2-fullunit-ready-20260910T1800-typefix/CUSTODY.json
sha256sum /home/ubuntu/jc2-r2-fullunit-ready-20260910T1800-typefix/evidence.tar.gz /home/ubuntu/jc2-r2-fullunit-ready-20260910T1800-typefix/CUSTODY.json
stat -c '%s' /home/ubuntu/jc2-r2-fullunit-ready-20260910T1800-typefix/evidence.tar.gz
date -u '+FULLUNIT_ARCHIVE_COMPARE_SYNC_DONE %Y-%m-%d %H:%M:%S.%N UTC'
