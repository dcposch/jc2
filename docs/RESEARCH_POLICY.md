# Example research policy for a persistent swarm

This is a reusable policy based on swarmHQ's research practice. Copy or link it from
your own workspace and record your operator's budgets and any adaptations. Its
cadences and allocations are defaults for one swarm, not campaign-wide requirements.
The shared [collaboration contract](../COORDINATION.md) applies to contributions.

## Goal and roles

Work toward a global proof or characteristic-zero counterexample until resolution,
an operator stop, or the authorized resource limit. Each result and PR is a milestone.
Ask proactively for resources that would unblock or accelerate work; inspect existing
capabilities first and continue independent work while waiting.

One coordinator per swarm owns synthesis, scheduling, state, and handoffs. Research
lanes own bounded questions end to end. Adversarial reviewers independently attack
claims. Use the strongest reasoner for integration and difficult mathematics, and
bounded lanes for replay, source extraction, and routine operations.

## Cadences

| Obligation | Default maximum interval |
| --- | --- |
| Collect completed lanes, handle corrections, stop idle owned workers | Every tick |
| Review a provisional high-impact claim | Target resolution within 6 hours |
| Complete a whole-portfolio ideation round | 12 hours |
| Complete a broad literature and external-results sweep | 24 hours |
| Assess a useful workflow improvement | 48 hours; record a reasoned no-change if none earns its cost |

These are backstops. A critical result, refutation, or changed global bottleneck can
trigger a round sooner. Routine scoped results receive a bounded strategy update,
not a duplicate whole-portfolio scan. An unchanged confirmation of a result already
in a round's packet does not trigger an echo round. Record misses honestly; restarting
or changing a task name does not reset its original deadline.

## Full ideation round

1. Freeze the basis commit, current research map, relevant evidence/corrections,
   your state, review debt, and new external information.
2. Before sharing ideas, each whole-portfolio model independently scans the same
   packet. Include the coordinator's own sealed proposal before invitations.
   Explain omissions; unavailable models degrade coverage rather than blocking work.
3. Each submission reranks the main proof and construction gaps, proposes a new
   mechanism or justified `NO_NEW_MECHANISM`, a cross-avenue connection, a proof
   attack, a falsification attack, a decisive experiment, and a brief workflow check.
   Give at most three detailed cards: dependencies, cheapest test, outcomes, and stop.
4. Collect before cross-pollinating. Deduplicate by mechanism, object, obstruction,
   and decisive test; preserve origins and disagreements. Model identity is not a vote.
5. Cross-examine the strongest candidates. Search the historical evidence and primary
   literature; label candidates `NEW`, `KNOWN`, `DUPLICATE`, or `SCOPE-CONFLICT`.
6. Publish the useful research synthesis, launch bounded work, name reviewers and
   stop conditions, and update your state. Explain why alternatives were deferred.

Aim for 60 minutes of independent proposals, 30 of cross-examination, and 30 of
synthesis. Close a degraded round if inputs are late. Never mutate a frozen packet
mid-round: abort and reseal if a critical event invalidates it; otherwise queue a delta.

For each new theorem, compare its exact hypotheses and conclusions with other live
results. Test cheap compositions; record a bridge, a scope mismatch, or no match.
Every live open question should identify its cheapest test. Attempt affordable tests
under one lane-hour before repeatedly carrying the same unanswered question forward.

## Allocation and stopping

Suggested overall allocation: 45% strongest paths, 25% new paths/connections,
12% independent review, 10% useful software/workflow, 4% external intelligence,
4% integration. Adjust to evidence and resources, not utilization targets.

Protect at least half of your strongest frontier-research time for all-degree proof
mechanisms or new counterexample constructions. Each task names the missing
implication on a route to resolution. Incremental work earns one bounded tranche;
renew only if it changes the next decisive test or removes a dependency. After two
tranches with the same gap and test, pivot. Count retries and engineering against
the same bottleneck. Do not repeatedly reverify accepted foundations without a
specific doubt affecting a live use. Formalization need not block research.

With four reasoning slots, a useful shape is coordinator, strongest route,
orthogonal route, and review/rapid response. Reserve a slot or about 25% of capacity
for review while debt exists. Two unchanged rounds without information gain call
for a fresh-eyes reset. Judge throughput by surviving results, useful refutations,
new connections, and time to decisive tests, not report or token counts.

## Speculation and review

Enqueue independent review before exploring descendants of a provisional claim.
Suggested caps per swarm: six provisional roots, three children per root, one
unreviewed generation, six hours per child, and at most 25% of research capacity
on one provisional premise. Record exceptions. Expensive commitments and promotion
cannot depend on unreviewed claims. Freeze new descendants when review is overdue.
Track dependency links so a refutation or narrowed scope reaches every consumer.

## Literature sweep

Search primary sources broadly, including older work newly relevant to a gap. Watch
new papers, corrections, public repositories, and relevant mathematical discussion.
A useful item changes correctness, priorities, a possible connection, or a test.
Record URL/version/date, exact claim and scope, applicability check, and next action.
Record negative coverage and inaccessible sources without claiming exhaustiveness.
Honor operator source restrictions. A targeted query does not reset a broad-sweep clock.

## State and handoff

Keep one current `STATE.md` in your swarm workspace, separate from an append-only
operational journal. Version state at banking points; historical snapshots are not
competing live queues. Public mathematical results go into the campaign repository.

```text
# Current state
Updated: UTC
Basis: campaign commit; any dirty artifact hashes
Coordinator and roster:
Active jobs: tag, owner, inputs, process/worker identity, stop, next collection
Provisional claims: scope, evidence, parents, reviewer, descendants
Review queue: priority, due time
Last/next ideation:
Last/next broad sweep:
Last/next workflow assessment:
Operator holds and spending limits:
Top mathematical gaps: links to shared research
Next actions:
```

At every tick: reconcile upstream; read your state; collect terminal work and check
resource limits; handle reviews/corrections; check clocks; schedule bounded work;
bank state and useful research. Keep caps independent of coordinator availability.
Before handoff, stop writing, bank a coherent state, and have the incoming
coordinator acknowledge it. Do not restart work merely because a monitor disappeared.
