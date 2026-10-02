---
name: harness
description: Create, change, list or move Rob's own Claude Code skills from inside a working session. Invoked as /harness, or when Rob asks to turn something he keeps doing into a skill, says a skill got something wrong and should be updated, asks what skills exist or where one lives, or wants to change how the harness itself works.
---

# Harness

Rob builds up his own skills gradually, while doing other work such as writing
a maths paper. This skill is how. He should not have to leave what he is doing
or remember a set of commands: he types `/harness <request>`, or just asks in
plain language, and you work out which operation applies.

## Where things live

| Place | Holds |
|---|---|
| `~/code/harness/meta` | This plugin: the harness itself, nothing else |
| `~/code/harness/global` | The library: Rob's global skills |
| `<project>/.claude/skills/` | Skills local to one project |

A new skill starts local to the project Rob is working in.

## Operations

Read the operation's file in this folder before doing it.

| Rob says something like | Operation | File |
|---|---|---|
| "I keep doing this, make it a skill" | Capture | `capture.md` |
| (continuing a capture) | Calibrate | `calibrate.md` |
| "That's not how I do it", "I fixed your output" | Refine | `refine.md` |
| "What skills do I have?", "Make this one global" | Place | `place.md` |
| "Look at what I've been doing lately" | Scout | `scout.md` |

## Rules for every operation

- **Rob decides.** On a real fork, lay out the options, recommend one, and
  ask. Never build or install something he has not asked for.
- **One change, one diff.** Show the diff and wait for his yes.
- **Commits.** After his yes, commit and push in `meta` and `global`, with the
  reason in the message. In any other repo, including a project holding a
  local skill, leave the change uncommitted and tell him: he commits there.
- **Say what changed.** Every reply that changes a skill names the skill and
  where it lives, says what changed in one sentence, shows the diff, and says
  how to undo it.
- **Keep replies short**, and lead with the conclusion.

## Changing the harness itself

The same loop applies: the files in this folder are changed by one small diff
at a time, shown to Rob, committed after his yes. "Undo that harness change"
means reverting the last commit in `meta`. `PROJECT.md` in `meta` describes
the design and is updated only when the overall shape changes.
