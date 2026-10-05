# Create

Turn something Rob keeps doing into a skill: the smallest version that covers
the main case and the few corner cases that would clearly bite, with him in
the loop. Skills are built up on a rolling basis: the rest is handled by
Update when it arises in real use.

## Steps

1. **Look, briefly.** Enough to know two things: whether something that
   already exists does most of the job, and which one or two questions decide
   the shape of the skill. Do not investigate how the task is done: the
   session that runs the skill works that out at the time, and facts about
   tools go stale. Check that the skill does not already exist, in the
   project's `.claude/skills/`, in `~/code/harness/global/skills/`, or loose
   in `~/.claude/skills/`; if it does, this is an Update. Never experiment on
   Rob's real data.

2. **Ask Rob**, conversationally, one or two questions at a time, only what
   decides the shape. If something existing does most of the job, lead with
   that and say what Rob would change in how he works to use it: his request
   describes the goal, not the design. Include whether the skill is local or
   global, asking if in doubt; if global, check "Library setup" in
   `manage.md` and include its offer if anything is missing.

3. **Write the bare minimum**: a folder `<name>/` with a `SKILL.md` holding a
   description of what the skill does and when to use it; what the result
   must be; Rob's answers, as his preferences, with where each came from; and,
   if the skill changes anything outside the conversation, that it shows Rob
   the plan and waits for his yes. Nothing about mechanism: no steps,
   commands, scripts or notes on how a tool works today. A first version is
   usually a dozen lines. Where the skill is about how something should look,
   a few of Rob's own examples are the preferences.

   A local skill goes in `<project>/.claude/skills/`, a global one in
   `~/code/harness/global/skills/`.

4. **Test in proportion**, as `test.md` says. A skill that shows Rob its plan
   before acting is tested by its first real use, with him watching. Run
   throwaway cases first only when a mistake would be costly or hard to see.
