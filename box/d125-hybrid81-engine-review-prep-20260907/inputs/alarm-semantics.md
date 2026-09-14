# Narrow primary-documentation check, 2026-09-07

Linux man-pages [setitimer(2)](https://man7.org/linux/man-pages/man2/setitimer.2.html)
documents ITIMER_REAL as a wall-clock countdown delivering SIGALRM, and explicitly
preserves interval timers across execve (unlike fork inheritance). It also warns
that expiry/delivery may be slightly late under scheduling/load. This is not a
real-time scheduling guarantee or a promise about hostile executable behavior.

[signal(7)](https://man7.org/linux/man-pages/man7/signal.7.html) lists the default
SIGALRM action as termination. The driver installs SIG_DFL and unblocks SIGALRM
before arming. [execve(2)](https://man7.org/linux/man-pages/man2/execve.2.html)
distinguishes program replacement from creating a new process and explains signal
disposition behavior; the timer fact used here is from setitimer, not POSIX timers.

[Python signal documentation](https://docs.python.org/3/library/signal.html#signal.setitimer)
documents floating-point seconds, interval0 as the default one-shot call, and
zero seconds as disabling the timer. The driver rejects nonpositive remaining
time rather than accidentally disabling its deadline. It makes exactly one
setitimer call and never resets it after parsing or before exec.

Fresh remaining time is computed from deadline_utc AFTER context/host/code-hash
checks, immediately when arming, bounded additionally by the checked phase
duration. Source reads and all parsing/serialization/verification/exec follow.
Terminal parent-side hash/custody harvest is not included in the450-second
payload arithmetic budget. CAPRUN continues to enforce phase CPU/wall/group RSS
and cleanup; its accepted code is unchanged.

Actual Linux tests use a Python executable, not Singular. They start with SIGALRM
ignored+blocked, then show default/unblocked behavior, declining inherited timer
in the SAME PID after real execve, and termination at the registered short
deadline. A future pinned-Singular engineering test must establish its actual
startup/alarm interaction; this generic exec test does not claim that result.
Two current upstream Singular files (ipshell.cc,fevoices.cc) were searched for
SIGALRM without a match; that limited unpinned search is not relied upon as a
whole-program guarantee. No CAS was executed or installed.
