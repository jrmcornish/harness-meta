# Place

Say what skills Rob has and where, and move a skill between places.

There is no list to keep up to date. The folders and their git history are
the record, so look every time.

## The three places

| Place | Path | Version control |
|---|---|---|
| Local | `<project>/.claude/skills/<name>/` | The project's git; Rob commits |
| Library | `~/code/harness/global/skills/<name>/` | The library's git; you commit after his yes |
| Loose | `~/.claude/skills/<name>/` | None |

Ignore `~/.claude/skills/synced/`: those are Anthropic's, not Rob's.

## List

Find every skill in the three places. For local skills, search Rob's home
folder for `.claude/skills` directories, a few levels deep, leaving out
`~/.claude` itself.

Show one table: name, place, one line on what it does, when it last changed
(from git where there is git, the file date otherwise). Point out anything
that looks wrong: a loose skill, the same name in two places, a skill
untouched for a long time.

## Move

- **Local to library** ("make this one global"), when a second project wants
  the skill. Read it first for anything tied to the project, such as paths,
  file names or the project's own vocabulary, and show Rob what would need
  generalising. Copy the folder into the library and remove it from the
  project, so the name exists in one place only.
- **Loose to library.** The same, for a skill sitting in `~/.claude/skills/`.
- **Library to local.** The reverse, for a skill that turned out to belong to
  one project.

A move never rewrites git history. It adds a commit in the library and
leaves an uncommitted change in the project. The skill's earlier history
stays in the repo it came from, so say in the library's commit message where
that is: the project's path and its latest commit for the skill.

If the library has no `.claude-plugin/plugin.json` yet, create one with the
name `global`, so that Claude Code loads the library as a plugin.

## Clashes

Local wins over the library. Claude Code loads both: the local skill under
its bare name, the library's as `global:<name>`. `/<name>` runs the local
one, but a plain-language request could pick either, so a clash should be
deliberate and explicit:

- By default a name exists in one place only; Move keeps it so.
- When a project needs its own variant of a library skill, write the local
  one as a short override, not a second full copy: "follow `global:<name>`,
  with these differences", and say in its description that it replaces the
  library skill in this project. Two full copies drift apart.
- List flags every name that exists in two places and says which one wins.
- Never create a clash silently. If a move, or a new skill, would put a name
  in two places, stop and warn Rob first: which two, and which would win.
  Go ahead only if he says the clash is intended.

## Remove

Delete a skill's folder only when Rob asks for that skill by name.

Every move or removal is shown to Rob first and waits for his yes, as the
rules in `SKILL.md` require. Say what moved, from where, to where. In the
library, commit and push; in a project, leave the change for him to commit.
