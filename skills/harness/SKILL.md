---
name: harness
description: Create, change, list or move Rob's own Claude Code skills from inside a working session. Invoked as /harness, or when Rob asks to turn something he keeps doing into a skill, says a skill got something wrong and should be updated, asks what skills exist or where one lives, asks to note an idea for a skill or for the harness, or wants to change how the harness itself works.
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
| `~/code/harness/global` | The library: Rob's global skills, and `BACKLOG.md` of candidates |
| `<project>/.claude/skills/` | Skills local to one project |

A new skill starts local to the project Rob is working in.

## Operations

Read the operation's file in this folder before doing it.

| Rob says something like | Operation | File |
|---|---|---|
| "I keep doing this, make it a skill" | Capture | not built yet |
| (continuing a capture) | Calibrate | not built yet |
| "That's not how I do it", "I fixed your output" | Refine | not built yet |
| "What skills do I have?", "Make this one global" | Place | not built yet |
| "Look at what I've been doing lately" | Scout | not built yet |
| "Note that ..." | Note | below |

If Rob asks for an operation that is not built yet, say so and stop. Do the
request by hand, under the rules below, only if he then asks you to.

**Note.** Add the idea to `~/code/harness/global/BACKLOG.md` if it is a
candidate skill, or to `~/code/harness/meta/NOTES.md` if it is about the
harness itself. Record where it came up. Asking for a note is the
confirmation: write it, commit and push, say in one line what was added, and
return to the work in hand.

## Rules for every operation

- **Rob decides.** On a real fork, lay out the options, recommend one, and
  ask. Never build or install something he has not asked for.
- **One change, one diff.** Show the diff and wait for his yes. Note is the
  only exception.
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
