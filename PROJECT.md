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

Claude Code is the interface. This repo is a plugin holding only the meta
layer: the operations that create and manage skills from inside an ordinary
working session. It contains no skills of its own kind.

| Operation | Does |
|---|---|
| Capture | Turns "I keep doing this" into a draft skill, using Rob's existing artefacts and past sessions as context |
| Calibrate | Runs the draft on real cases; Rob's edits become rules; accepted outputs become the skill's exemplars and tests |
| Refine | When Rob corrects an output later, proposes a diff to the skill responsible |
| Place | Keeps a new skill local to its project, promotes it here when a second project wants it, and lists what exists where |
| Scout | On request, reviews recent sessions for repeated or corrected work, checks whether a solution already exists, and proposes candidates |

Claude may also suggest a candidate mid-session: one line, clearly marked as a
harness suggestion, at the end of a reply and never inside the work itself.

Skills are what the meta layer produces, such as the TikZiT string-diagram
style. Each is a folder of instructions, exemplars and a check script, and
lives in one of two places:

| Where | Holds | History |
|---|---|---|
| Skills library (own repo, name to be chosen) | Global skills and the backlog of candidates | The library's git |
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
- **The meta layer changes the same way**, by conversation from any session:
  "Harness: ..." to change an operation, undo a change, or see the history. An
  idea can also be noted for later.
- **One line per change** in that repo's changelog. This file stays one page and
  always describes the current whole.

## Next steps (proposed)

0. **Create the library and move in what exists**: the TikZiT skill and the
   working rules now sitting in one project's memory folder. No new behaviour.
1. **Capture and Calibrate**, tested by producing a tikz-cd style skill.
2. **Refine and Place**.
3. **Scout**, on request only.

Candidates for the backlog, not a plan: a diagram edit loop through TikZiT and
quiver; a project notebook; a review command; a blind cold reader and a writer
in Rob's voice; verbatim-quote literature checks; scenario-based review for
autoformalization.
