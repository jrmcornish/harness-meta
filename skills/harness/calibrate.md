# Calibrate

Try a draft skill on real cases and correct it with Rob until it does the
task the way he does. This follows Capture in the same conversation.

A draft is only a guess at Rob's style. The best way to judge it is usually not by reading its
rules directly (although sometimes this can be helpful); he can judge what it produces. So each round shows him outputs, and
his reactions become the rules.

## Steps

1. **Pick two or three real cases** from the project: things the skill
   should be able to do. Do not reuse the artefacts the draft was written
   from, or the test only shows copying. Prefer cases Rob has already done by
   hand, so there is something to compare against. Tell him which you picked.

2. **Run the skill as a stranger would.** Give each case to a fresh subagent
   that has the skill folder and the case, and nothing from this
   conversation. You wrote the draft knowing more than it says; a later
   session will know only what is written down.

3. **Show the outputs, not a description of them.** Render anything visual
   and show the picture. Put Rob's own version beside it where one exists.

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
   request that produced it. They are the cases Refine reruns later. Then
   tell Rob the skill is ready and where it is.

Keep each round small: the outputs, what changed in the rules, nothing else.
If there are many outputs to compare, the `skill-creator` skill has a review
page that shows them side by side; offer it, do not default to it.
