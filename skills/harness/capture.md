# Capture

Turn something Rob keeps doing into a draft skill. The hard part is getting
how *he* does the task into the skill, so most of the work is finding and
reading evidence of that, not writing.

## Steps

1. **Pin down the task.** State in a sentence or two what the skill does and
   when it should be used. Ask Rob only if that is unclear. Pick a short
   kebab-case name.

2. **Check it is not already there.** Look in the project's
   `.claude/skills/` and in `~/code/harness/global/skills/`. If the skill
   exists, this is a Refine, not a Capture.

3. **Check prior art, in the background.** Start a quick search for an
   existing tool, plugin or established practice while you do step 4. Report
   it in a few lines ending in one verdict: adopt, adapt or build. Link the
   sources and say which you have not read yourself. If Rob says "look hard",
   make it a proper review.

4. **Gather how Rob does it**, in this order of value:
   - *His existing artefacts.* Find the files in the project where he has
     already done this task by hand. Read a good sample. Look for what is
     consistent across them; that is the style. Note the exceptions too.
   - *What he has said.* Corrections in the current conversation, and in past
     sessions: transcripts are in `~/.claude/projects/<project path with / as ->/*.jsonl`.
     They are large, so search them for his messages on the topic; never read
     one whole.
   - *The prior-art result*, for technique, not for style.

5. **Write the draft.** A folder `<name>/` containing:
   - `SKILL.md`: a description saying what it does and when to use it, then
     the rules. Give each rule its reason and its source, e.g.
     "(from `figures/fib-morphisms.tikz`)" or "(Rob, 12 Sep: 'put it back')".
     A rule with no source is a guess: mark it as one.
   - `examples/`: a few of Rob's own artefacts, copied in as exemplars.
   - a check script, where a rule can be checked mechanically.

   Keep it short. For how to write good skill instructions, follow the
   guidance in the `skill-creator` skill.

   Put it in `<project>/.claude/skills/`. Put it in
   `~/code/harness/global/skills/` instead only if Rob says it is global or
   the task does not belong to any project.

6. **Show Rob the draft**: the name, where it is, and the rules as a short
   list with their sources, guesses marked. Not the whole file.

7. **Go on to Calibrate** in the same conversation, so the draft is tried on
   real cases before Rob relies on it.
