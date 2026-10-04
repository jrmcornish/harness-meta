# Test: the loop

How a feature is tried and corrected with Rob. A feature is anything a
session will follow: a new skill (Create), a change to a skill (Update), or a
change to the harness itself. Rob can also ask for a test directly, for
example after editing a skill by hand or after a Claude Code update; then
start at step 1 with the feature he names.

A feature is only a guess at how Rob wants something done. The best way to
judge it is usually not by reading its rules directly (although sometimes
this can be helpful); he can judge what it produces. So each round shows him
outputs, and his reactions become the rules.

## Steps

1. **Pick the cases.** Two or three real things the feature should be able
   to do, plus any cases already saved in a skill's `examples/`. Do not reuse
   what a new draft was written from, or the test only shows copying. Prefer
   cases Rob has already done by hand, so there is something to compare
   against. Tell him which you picked.

   If the feature changes things, such as moving files, editing configuration
   or sending anything, build throwaway cases for it and run it only on
   those. Never test such a feature on Rob's real data.

2. **Run the feature as a stranger would.** Give each case to a fresh
   subagent that has the feature's files and the case, and nothing from this
   conversation. You know more than the files say; a later session will know
   only what is written down.

   For the harness itself, a case is a request Rob might type, and the
   stranger is a subagent given only the harness files and that request.
   Its output is what it did and its account of where the instructions were
   unclear, missing something, or wrong.

   When a case is something Rob types into Claude Code himself, such as a
   slash command, no subagent can run it. Then the test is Rob doing the
   steps while you check the result.

3. **Show the outputs, not a description of them.** Render anything visual
   and show the picture. Put Rob's own version beside it where one exists.
   Where there is a tool he would normally use to edit that kind of output,
   open the output in it so that he can correct it there and then, and read
   the result back as his edit. The feature says which tool; the loop only
   asks for one.

4. **Turn each correction into a rule.** Rob will comment, or edit an output
   by hand; if he edits, compare his version with yours to see what he
   changed. Find the general rule behind the correction, not a patch for
   that one case. If you cannot tell whether it is general, ask. Change the
   feature's rules, giving the source as his words and the date, and show him
   the rule diff.

5. **Run every case again**, including ones he already accepted, so a new
   rule does not break an old case. Repeat from step 3.

6. **Stop when Rob accepts every output unchanged**, or says it is good
   enough. If two rounds bring no improvement, say so and ask how he wants
   to proceed.

7. **Save the accepted outputs** in the skill's `examples/`, each with the
   request that produced it, so they can be rerun later. Then tell Rob the
   feature is ready and where it is.

Keep each round small: the outputs, what changed in the rules, nothing else.
If there are many outputs to compare, `anthropic-skills:skill-creator` has a
review page that shows them side by side; offer it, do not default to it.

## Testing Claude Code itself

When a skill is about Claude Code, its sessions, storage, commands or
configuration, the way to learn how it behaves is to try things; and a change
to the harness is checked by loading it in a fresh session (`claude plugin
validate` first, then `claude -p` in a throwaway folder). Both mean running
Claude Code from inside Claude Code, which has pitfalls that are easy to
mistake for results:

- **Use a throwaway folder** under the session's scratchpad. A conversation
  made there with `claude -p "..." --output-format json` returns its session
  ID, and its store appears under `~/.claude/projects/` with the folder's
  path encoded (every character that is not a letter or digit becomes `-`).
  Delete both the folder and its store afterwards. Never touch the store of
  the session you are in.
- **A nested `claude` may not save its conversation.** If no store appears,
  run it with the `CLAUDE*` environment variables cleared:
  `env $(env | grep -oE '^CLAUDE[A-Z_]*' | sed 's/^/-u /') claude ...`
- **Non-interactive runs cannot do everything.** With `claude -p` there is
  no screen: slash commands such as `/cd` report themselves unavailable,
  permission prompts become refusals, and the folder-trust dialog cannot be
  answered. Anything interactive needs a real terminal, which no subagent
  can drive either: ask Rob to do that step, or drive a terminal yourself
  with `tmux`, remembering that Rob's sessions use vim key bindings.
