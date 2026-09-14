# ROOT primary-source context: loader-cache hypothesis only

2026-09-10 14:33 UTC. This is reference context, NOT the recovered cause of the semantic batch STOP and NOT an expansion of any native allowlist.

The Linux dynamic-loader manual lists /etc/ld.so.cache as a loader input. In the glibc-2.39 source tag, _dl_load_cache_lookup requests its contents through _dl_sysdep_read_whole_file with read-only protection; _dl_unload_cache releases the mapping. The helper opens the file and maps its contents. These sources establish that file-backed loader-cache mappings are a real implementation mechanism, not just shared-object mappings. Sources: [loader manual](https://man7.org/linux/man-pages/man8/ld.so.8.html), [glibc-2.39 cache implementation](https://raw.githubusercontent.com/bminor/glibc/glibc-2.39/elf/dl-cache.c), [glibc-2.39 mapping helper](https://raw.githubusercontent.com/bminor/glibc/glibc-2.39/elf/dl-misc.c).

ROOT read the returned complete501-line dl-cache.c and the relevant helper lines27–58 in dl-misc.c; the loader manual was read by relevant search/open excerpts, not claimed WHOLE. No source code was executed or modified. The source tag is reference code, NOT a byte-verified match to the retired worker's Ubuntu-patched loader.

Inference ONLY: an instantaneous map check based on an executable/library ldd inventory can encounter a legitimate non-library startup mapping absent from that inventory. The observed runner failure did NOT preserve its rejected pathname. Neither /etc/ld.so.cache nor any other particular mapping is established as that cause. There is no authority here to add a guessed path, ignore data maps, alter the validated record, or retry until a sample passes. First preserve the bounded rejected observation with the strict guard intact, then evaluate actual evidence under a new ROOT registration if justified.

This source-context microcheck is not a broad mathematical web sweep, cadence reset, model review, or new JC2 claim.
