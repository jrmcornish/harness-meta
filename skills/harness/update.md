# Update

Change an existing skill because it got something wrong in real work. Rob
says so, or fixes the output by hand.

The aim is a skill that stays short and right. Appending a rule for every
correction makes a skill long and self-contradictory, so first work out what
kind of correction this is.

## Steps

1. **Find the skill responsible** and where it lives: the project's
   `.claude/skills/`, `~/code/harness/global/skills/`, or loose in
   `~/.claude/skills/`. If no skill produced
   the output, this is not an Update; say so.

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

5. **Go into the loop** in `test.md` at its step 5: rerun the case that
   went wrong and every saved case, show Rob the outputs, and carry on from
   there until he accepts. An output he had accepted that now comes out
   differently is the thing to show him first.
