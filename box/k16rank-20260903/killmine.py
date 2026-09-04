import os, signal
me = os.getpid(); parent = os.getppid(); killed = []
for pid in os.listdir('/proc'):
    if not pid.isdigit(): continue
    p = int(pid)
    if p in (me, parent): continue
    try:
        cmd = open(f'/proc/{pid}/cmdline','rb').read().replace(b'\0', b' ').decode(errors='replace')
    except Exception: continue
    if not (cmd.startswith('Singular') or cmd.startswith('python3') or cmd.startswith('/usr/bin/time')): continue
    if 'k16rank-20260903/rank_' in cmd or 'rank_driver.py' in cmd:
        try: os.kill(p, signal.SIGKILL); killed.append((p, cmd[:90]))
        except Exception as e: print('fail', p, e)
print('killed', len(killed)); [print(' ', k) for k in killed]
