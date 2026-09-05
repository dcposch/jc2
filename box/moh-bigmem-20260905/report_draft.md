# DRAFT — filled into xmodel/moh-bigmem-grok46-20260905.md after pipelines end

Charged-input verification (receipt awk join of `_sha256`/`_basename` + `sha256sum -c`): 7/7 OK, no content mismatch.

Workers launched (terminate these only):
r7i.24xlarge 768GB: i-0e95f8ff97f6462ce 172.30.0.183; i-0ce9ea50559403c22 172.30.0.202; i-0193dc1295fc5234a 172.30.0.108; i-0baedea1d34e4b978 172.30.0.190
x2idn.16xlarge 1TB: i-0780c67ecdc79cb0a 172.30.0.121; i-018484399fd100293 172.30.0.55; i-043f250f1956bd34b 172.30.0.45; i-02efd7ecd26becc5a 172.30.0.125
Do not touch: 172.30.0.7/.28/.18 c7i.8xlarge; 172.30.0.67 r7i.16xlarge.

msolve 0.10.1 SHA 0436525b06fe83b1a6a00097a96d9bcafdc40d8de6315c724b9ada9a4c04ff5f
Workers' /usr/bin/msolve is 0.6.5 SHA c2722288…; all solves use the official AVX512 0.10.1 binary.

Flags: -g 2 -t 32 -v 2 -l 44; -m left at default 0 (unlimited pairs); no -s 12 (gate used 2^12 hash). ulimit -v 700000000 KiB (~667 GiB), NOT 8–48 GiB. Watchdog 10800s.

FALLACY-v2: msolve -g 2 is first-prime GB; char-0 [1] is UNIT_SIGNAL_MODULAR_ONLY; timeout/header/halt is not a result.

Custody:
m12 union 425-gen rows SHA af3cf058c7e949d7e9958b1c9120b9350436c6eca7a952afbc8ea32f9794ef58 (astra true s'=4 control). meta SHA 2d5ce8b87443b24b02e249bebde9c7ada098968aeba7e5fcc672c1ea0d31187f. 425 rows + z*c-1 = 426 gens, 78 msolve vars (77+z). .ms SHA 2c3ec84260713e3f721a10b7dc37247364a011f5d5c82ca75b52185feb8cc453 29438880 bytes. Ring Q[h,A,B,c] extraction (lp(1),dp(78)) y-first; solver grevlex on renamed v1..v76,c,z. Circuit (new): 148 aux + 150 jac = 298 eqs, 225 vars, rows SHA 27cfa0fb50cbc7e71d0608e8a16ad8b9857a4f2794a17696705a7674db46e6b8, 2/2 differential controls pass.

v38 native rows SHA 2b59ba92… 174 gens. meta SHA 3040c7ce… matches verification.json. .ms SHA 4d3d8eac54467ba5be167c1d75b6c338772d5588e21bc38915dac2dc11c71128 IDENTICAL to gate native input. 175 gens, 112 vars. Graph 335+header=336 lines, 280 solver vars.

m15 native rows SHA ad9c53e3… 177 gens. meta SHA cdeaf280… matches verification.json. .ms SHA c5d52ad31b03bcb756d12d570c2dc0a8b86d5447f252509c37b904992ec1631a IDENTICAL to gate native. 178 gens, 130 vars. Graph 403 lines.

v18 native: extracting from builder SHA 121aac3d… (verification.json). Graph 650 gens, 439 vars, rows SHA 35ad3ecb…

Gate prior: all ALLOC_FAIL rc139 at 8–48 GiB or TIMEOUT 900s. This lane's first minutes: m12 F4 d=7 RSS 28 GiB; v38 F4 d=6 RSS 11 GiB (past gate crash); m15 F4 d=5 RSS 8 GiB.
