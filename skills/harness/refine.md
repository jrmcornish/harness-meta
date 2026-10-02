# Refine

Change an existing skill because it got something wrong in real work. Rob
says so, or fixes the output by hand.

The aim is a skill that stays short and right. Appending a rule for every
correction makes a skill long and self-contradictory, so first work out what
kind of correction this is.

## Steps

1. **Find the skill responsible** and where it lives: the project's
   `.claude/skills/` or `~/code/harness/global/skills/`. If no skill produced
   the output, this is not a Refine; say so.

2. **Establish the correction.** Use Rob's words. If he edited the output by
   hand, compare his version with what the skill produced and list what he
   changed.

3. **Decide what kind it is.** Ask if you cannot tell.
   - *A rule is missing or wrong.* Change the rule.
   - *The rule exists but was not followed.* The skill is unclear or the rule
     is buried. Fix the wording or add a check; do not add a second rule
     saying the same thing.
   - *A one-off for this case.* Change nothing, and say so.

4. **Make the smallest change that fixes it.** Give the source as Rob's words
   and the date. Replace a rule the new one supersedes; do not leave both.
   If the correction contradicts an existing rule that has its own source,
   show Rob both and ask which holds.

5. **Rerun the saved cases.** Run the skill's `examples/` again as Calibrate
   does, with a fresh subagent that sees only the skill, and run its check
   script if it has one. If an output Rob had accepted now comes out
   differently, show him.

6. **Keep the corrected output** in `examples/` if it covers something the
   existing examples do not.

7. **Show Rob the change and wait for his yes**, as the rules in `SKILL.md`
   require: which skill, what changed, the diff, a before and after where the
   output can be shown, and the result of step 5.
