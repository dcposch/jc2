import sys
sys.dont_write_bytecode = True
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from execution_gate import authorize
authorize(sys.argv[1], __file__, "check")
Path(sys.argv[3]).open("x").write("POSTAUTHORIZE\n")
if sys.argv[4] == "descendant":
    import os, signal, time, json
    pid = os.fork()
    if pid == 0:
        signal.signal(signal.SIGTERM, signal.SIG_IGN)
        memory = bytearray(64 * 1024 * 1024)
        print(json.dumps({"child_pid":os.getpid(),"pgid":os.getpgrp(),
                          "namespace":os.readlink('/proc/self/ns/pid'),
                          "stat":Path('/proc/self/stat').read_text()}), flush=True)
        time.sleep(20)
        os._exit(0)
    print(json.dumps({"leader_pid":os.getpid(),"child_pid":pid,"pgid":os.getpgrp(),
                      "namespace":os.readlink('/proc/self/ns/pid')}), flush=True)
    os._exit(0)
