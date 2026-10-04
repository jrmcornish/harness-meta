# harness-meta

A Claude Code plugin with one skill, `/harness`, that creates and manages
your own skills from inside a working session. The design is in
[PROJECT.md](PROJECT.md).

## Set up

```bash
mkdir -p ~/code/harness && cd ~/code/harness
git clone git@github.com:jrmcornish/harness-meta.git meta
git clone git@github.com:jrmcornish/harness-global.git global
ln -s ~/code/harness/meta ~/.claude/skills/harness
```

The link makes Claude Code load the plugin in every session. To check, run
`claude plugin list`: it should show `harness@skills-dir` as loaded.

The two paths are fixed. The skill's files refer to `~/code/harness/meta` and
`~/code/harness/global` by name.

## Use

In any session, type `/harness` followed by what you want:

| Type | To |
|---|---|
| `/harness I keep doing X, make it a skill` | Draft a skill and correct it on real cases |
| `/harness that's not how I do it` | Fix a skill that got something wrong |
| `/harness what skills do I have?` | List skills and where they live |
| `/harness make <name> global` | Move a skill into the library |
| `/harness look at what I've been doing` | Get suggestions from this project's recent sessions |
| `/harness undo the last harness change` | Revert a change to the harness itself |

A plain-language request also works when it is clearly about skills.

Nothing is changed without showing you the diff and waiting for your yes.

## Layout

| Path | Holds |
|---|---|
| `skills/harness/SKILL.md` | The entry point and the rules every operation follows |
| `skills/harness/{create,update,manage,review,test}.md` | One file per operation; Test is the try-and-correct loop that Create and Update end in |
| `skills/harness/scripts/` | Helper scripts |
| `.claude-plugin/plugin.json` | The plugin's name and version |
