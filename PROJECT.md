# Harness

One version-controlled home for Claude Code extensions that grow out of Rob's
working sessions, keeping him in the loop. Math research first; industrial
autoformalization later, from the same core.

## Goals

1. **Math research (now).** Speed up theory-building work whose deliverable is a
   crisp, minimal, readable paper (later: human-friendly code). For Rob's own
   use, so it need not be polished.
2. **Autoformalization (later).** Turn policy documents into formal models (Z3
   now, perhaps Lean) that an auditor can quickly confirm say what was meant.
   Eventually a deployable product.

Both are the same problem: an agent proposes an artefact, and a human must
confirm it is faithful to an intent held in their head or in a document. The
shared core is that audit loop, not the mathematics.

## Principles

- **Rob decides.** On a real fork the agent lays out the options, recommends
  one, and asks. Nothing is built or installed without his say.
- **Small steps.** Every output, and every change to the harness, is small
  enough to read in one sitting.
- **Show the concrete thing.** A rendered diagram, a worked example, a solver
  scenario; not a paraphrase.
- **Verify before asserting.** Claims about a file or a paper are checked at the
  source and quoted with a location.
- **Adopt before building.** Check whether a tool or practice already solves
  the problem.

## Architecture

The project folder is `~/code/harness/`, holding two separate git repos:
`meta/` (this one) and `global/` (the skills library).

Claude Code is the interface. This repo is a plugin holding only the meta
layer: one skill that creates and manages other skills from inside an ordinary
working session. Rob talks to it in plain language ("Harness: ..."); it works
out which operation applies. Each operation is one instruction file.

| Rob says | Operation | Does |
|---|---|---|
| "I keep doing this, make it a skill" | Capture | Checks for prior art, then drafts a skill from Rob's existing artefacts and past sessions |
| (same conversation) | Calibrate | Runs the draft on real cases; Rob's corrections become rules; accepted outputs become exemplars and tests |
| "That's not how I do it" | Refine | Turns a later correction into a diff to the skill responsible |
| "What skills do I have?" | Place | Lists what exists where; keeps new skills local; promotes one to the library when a second project wants it |
| "Look at what I've been doing" | Scout | Reviews recent sessions for repeated or corrected work and proposes candidates, each with a prior-art check |

The **prior-art check** is a shared step, run by default: a quick search for an
existing tool or established practice, reported in a few lines as adopt, adapt
or build.

Claude may also suggest a candidate mid-session: one line, clearly marked as a
harness suggestion, at the end of a reply and never inside the work itself.

Skills are what the meta layer produces, such as the TikZiT string-diagram
style. Each is a folder of instructions, exemplars and a check script, and
lives in one of two places:

| Where | Holds | History |
|---|---|---|
| `global/`, the library (own repo, beside this one) | Global skills and the backlog of candidates | The library's git |
| A project's `.claude/skills/` | Skills local to that project | That project's git |

A skill change is recorded only in the repo that holds the skill; it never
touches this one. There is no central registry: Place reads the folders
directly.

## How it grows

- **Evidence first.** A candidate comes from real work, and is recorded in the
  library's backlog with where it was seen. Corrections and reverts count for
  more than repetition.
- **One change, one skill, one diff**, in the repo that holds it. Claude shows
  the diff; when Rob accepts, Claude commits it. This applies to this repo and
  the library only; commits in project repos stay Rob's.
- **Every change comes with a report** in the same reply: which skill and
  where, what changed in one sentence, the diff, a before-and-after example
  where the output can be shown, whether saved exemplars still pass, and how
  to undo it. Nothing is changed silently.
- **The meta layer changes the same way**, by conversation from any session:
  "Harness: ..." to change an operation, undo a change, or see the history. An
  idea can also be noted for later.
- **One line per change** in that repo's changelog. This file stays one page and
  always describes the current whole.

## Next steps

1. **Build the meta harness**: the entry point, Capture, Calibrate, the
   prior-art check and the change report. It wraps Claude Code's built-in
   skill creator where that already does the job.
2. **Decide what follows** once it has been used for real.

Candidate skills are listed in the library's `BACKLOG.md`.
