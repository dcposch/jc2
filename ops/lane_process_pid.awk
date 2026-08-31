# Given `pgrep -fl '[o]ps/lane[.]sh'` rows and `-v tag=...`, print the PID
# only when TAG is exactly argv[2] after the lane launcher:
#
#   PID /bin/sh /repo/ops/lane.sh ADAPTER TAG PROMPT
#
# Equality at the fixed argv position prevents tag-prefix and prompt-name
# collisions.  The input is already restricted to campaign lane launchers.
{
  pid = $1
  for (field = 2; field + 2 <= NF; field++) {
    if ($field ~ /(^|\/)ops\/lane[.]sh$/ && $(field + 2) == tag) {
      print pid
      exit
    }
  }
}
