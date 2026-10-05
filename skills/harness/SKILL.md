---
name: harness
description: Create, change, list or move Rob's own Claude Code skills from inside a working session. Invoked as /harness, or when Rob asks to turn something he keeps doing into a skill, says a skill got something wrong and should be updated, asks what skills exist or where one lives, asks to test a skill or the harness, or wants to change how the harness itself works. Separately, in any session: when Rob corrects output that a skill produced, or corrects the same kind of output more than once, you may end a reply with one line starting "Harness suggestion:" that offers to update the skill or to create one, at most once per topic.
allowed-tools: Read(~/.claude/skills/**) Read(~/code/harness/**) Read(~/.claude/projects/**)
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

A new skill is local to the project Rob is working in, unless he says it is
global or it is not about any one project. If in doubt, for example when it
is not clear that the current folder is a project at all, ask.

The `allowed-tools` line above is permission, not restriction: it lets this
skill read the two harness repos, Rob's skills and his session history from
any project without a prompt. Every other tool works as usual, with the
usual prompts.

## Operations

Read the operation's file in this folder before doing it.

| Rob says something like | Operation | File |
|---|---|---|
| "I keep doing this, make it a skill" | Create | `create.md` |
| "That's not how I do it", "I fixed your output" | Update | `update.md` |
| "What skills do I have?", "Make this one global" | Manage | `manage.md` |
| "Look at what I've been doing lately" | Review | `review.md` |
| "Test the tikzit skill", "Does the harness still work?" | Test | `test.md` |

Test is the loop in which a feature is tried on real cases and corrected
with Rob until he accepts it. Create and Update both end in it; Rob can also
ask for it on its own.

## Rules for every operation

- **Iterate.** A skill starts as the smallest version that covers the main
  case and the few corner cases that would clearly bite, such as one that
  Rob hits every time or one where a mistake is costly. The rest are dealt
  with as they come up in real use, through Update. Do not hold a skill back
  until every case is settled.
- **Rob decides.** On a real fork, lay out the options, recommend one, and
  ask. Never build or install something he has not asked for.
- **One change, one diff.** Make the change in the working files, show Rob
  the diff, and wait for his yes. For a new skill, show a short summary of
  its rules in place of the whole file. If he says no, restore the files.
- **Commits.** Nothing is committed before his yes. After it, commit and
  push in `meta` and `global`, with the reason in the message. In any other
  repo, including a project holding a local skill, leave the change
  uncommitted and tell him: he commits there.
- **Say what changed.** Every reply that changes a skill names the skill and
  where it lives, says what changed in one sentence, shows the diff, and says
  how to undo it.
  The diff is taken from the files after the change, with `git diff` or by
  reading them back, never typed out: a typed diff can describe a change that
  was never made.
- **Warn about clashes.** If the skill you are about to create, change or
  move has the same name as one in another place, tell Rob before doing
  anything. See `manage.md`.
- **Never rewrite git history.** No amending, rebasing or force-pushing; undo
  by a new commit that reverts.
- **Keep replies short**, and lead with the conclusion.

## Changing the harness itself

The files in this folder are changed by one small diff at a time, shown to
Rob, committed after his yes, and tested in the loop in `test.md` like any
other feature. "Undo that harness change" means reverting the last commit in
`meta`. `PROJECT.md` in `meta` describes the design and is updated only when
the overall shape changes. To check a change, run it in a fresh session.

## Working on Claude Code itself

Two kinds of work here mean running Claude Code from inside Claude Code:
checking a change to the harness, and any skill that is about Claude Code,
its sessions, storage, commands or configuration. Both have traps that are
easy to mistake for results. Read "Testing Claude Code itself" in `test.md`
before either.
