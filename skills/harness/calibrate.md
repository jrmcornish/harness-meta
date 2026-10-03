# Calibrate: the loop

How a skill gets corrected with Rob. Create uses it on a new draft; Refine
uses it after changing an existing skill.

A skill is only a guess at how Rob wants something done. The best way to
judge it is usually not by reading its rules directly (although sometimes
this can be helpful); he can judge what it produces. So each round shows him
outputs, and his reactions become the rules.

## Steps

1. **Pick the cases.** Two or three real things the skill should be able to
   do, plus any cases already saved in the skill's `examples/`. Do not reuse
   what a new draft was written from, or the test only shows copying. Prefer
   cases Rob has already done by hand, so there is something to compare
   against. Tell him which you picked.

   If the skill changes things, such as moving files, editing configuration
   or sending anything, build throwaway cases for it and run it only on
   those. Never test such a skill on Rob's real data.

2. **Run the skill as a stranger would.** Give each case to a fresh subagent
   that has the skill folder and the case, and nothing from this
   conversation. You know more than the skill says; a later session will
   know only what is written down.

3. **Show the outputs, not a description of them.** Render anything visual
   and show the picture. Put Rob's own version beside it where one exists.
   Where there is a tool he would normally use to edit that kind of output,
   open the output in it so that he can correct it there and then, and read
   the result back as his edit. The skill says which tool; the loop only
   asks for one.

4. **Turn each correction into a rule.** Rob will comment, or edit an output
   by hand; if he edits, compare his version with yours to see what he
   changed. Find the general rule behind the correction, not a patch for
   that one case. If you cannot tell whether it is general, ask. Change the
   skill's rules, giving the source as his words and the date, and show him
   the rule diff.

5. **Run every case again**, including ones he already accepted, so a new
   rule does not break an old case. Repeat from step 3.

6. **Stop when Rob accepts every output unchanged**, or says it is good
   enough. If two rounds bring no improvement, say so and ask how he wants
   to proceed.

7. **Save the accepted outputs** in the skill's `examples/`, each with the
   request that produced it, so they can be rerun later. Then tell Rob the
   skill is ready and where it is.

Keep each round small: the outputs, what changed in the rules, nothing else.
If there are many outputs to compare, `anthropic-skills:skill-creator` has a
review page that shows them side by side; offer it, do not default to it.
