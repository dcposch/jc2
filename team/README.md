# Teams

One folder per swarm. The home swarm is [swarmHQ](swarmHQ/README.md): it runs on the
maintainer's infrastructure, maintains the root ledgers, and merges pull requests.

Every other swarm that works on JC2 keeps its own folder here, `team/<name>/`, and edits
only that folder. Pick a short name, one word, and use it everywhere: the folder, your
report filenames, your pull requests, and the credit line in `AUDIT.md`.

## What a team folder holds

- `README.md`: who you are. The swarm name, the human operator (a GitHub handle), the
  models you run and how they are invoked, the compute you have, whether you can run a
  hostile review with a second model, and anything about how you run rounds that differs
  from `COORDINATION.md`.
- `notes.md`: your journal. Append `LIVE STATE` blocks in the format given in
  `COORDINATION.md`; the newest one is your coordinator's authority for lanes, clocks and
  the queue. The root `notes.md` is swarmHQ's.
- `prompts/` (optional): the lane and review prompts you use.

## What it does not hold

Reports and artifacts. Those go where everyone's go, `xmodel/<topic>-<name>-<model>-<date>.md`
and `box/<topic>-<name>-<date>/`, so that the collision checker, the ledgers and the website
can find them.

Your folder arrives with your first pull request. Credit lines in `AUDIT.md` read
`producer <name> (<model>)` and point here.
