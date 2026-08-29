# Custody: root-aware AWS recensus R1

Frozen source gates:

```text
PREREGISTRATION.md       4e2b6cf56746b8a78c6b7ba122c38f515d5508e817a5388347ff50d2183165a9
SOURCE_MANIFEST.sha256   42d54f69241685b06ea8a6100878a67361439106b74f78cdd1f3bc0b0dc503ca
SOURCE.tar               61502686d1ae1646239a5d026f5f36f941e40d8e8f183c4b909505697a8b3968
producer gate            93f98e4df5fd67536f3a5ab9c6f948a6bb06bbdbd10b825980596cc865c811d5
hostile gate             8381659878f039d17cbc4ebb5a3ac364768d690d4a3895d54c29446f7745b060
multipole hostile review ac49c025e3e010d3ecaf3839adf51c40cb88b0088198ae1c5ab1198e07cc8004
```

AWS execution census:

```text
common     i-07eeaf8ba6f0bc419 r6i.8xlarge CPU4 PID/PGID/SID 5386
           2026-08-28T16:45:04Z..16:53:36Z max group RSS 28,852 KiB swap 0
h3hiii     i-07eeaf8ba6f0bc419 r6i.8xlarge CPU5 PID/PGID/SID 5385
           2026-08-28T16:45:04Z..16:49:15Z max group RSS 28,984 KiB swap 0
twopole    i-040b7a1c2ed72d4cc r6i.4xlarge CPU6 PID/PGID/SID 7316
           2026-08-28T16:45:04Z..16:46:35Z max group RSS 28,752 KiB swap 0
invariants i-040b7a1c2ed72d4cc r6i.4xlarge CPU7 PID/PGID/SID 7315
           2026-08-28T16:45:04Z..16:50:26Z max group RSS 27,956 KiB swap 0
```

Harvested terminal archives replay exactly against their remote SHA files:

```text
common     c12e6d90b44f62fef63fbab43c6c43db1970b500d1a9a68d4d9785a4e7bdd2bf
h3hiii     78eacc2f9f5c9bdf655fe23ddc39cd84f5eceae425c4a3f705a29942cb84fb5a
twopole    2a83fd72cf0557360837228628516af0a45fc6204b2e9d61c64bfccacd87128c
invariants d4778f618f663226ef667b423ca08cf067e2a28753cc0fc993a247a1dedece2b
```

All 356 ordinary extracted terminal-manifest entries replayed.  The terminal
manifests also name 64 macOS AppleDouble `._` source metadata entries; local
bsdtar restores those as extended attributes rather than standalone files.
The immutable archive hashes above are therefore the authoritative byte
custody for those metadata records.  No mathematical output is among them.

Key result hashes:

```text
common SUMMARY.json      cdf8d321c3fe048176d65695c842f1454b02b3bfaf267a189ec6591fa3fe5cc5
h3hiii SUMMARY.json      4ffb343f4f98e601d5f32814548ce327c043c1e08adcc924e69fd8a9ed442797
twopole SUMMARY.json     5986fca0ee533e11af0bed2759bab42c5f4b13e0024cd49a5d9c14bd73a11ce5
invariants SUMMARY.json  6c4948ba80e965fc0d7ca5c084107d5b6a95a99588f5b9b10e5d6bb7bf4e95f6
invariant_verdict.json   5456af8fff996c80f51a4eae4ef85f4d22f2cbc02913ab86ac3557c29cc49027
```
