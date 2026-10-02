# Scout

Look back over Rob's recent sessions in the current project for work that a
skill would improve, and come back with a short list for him to choose from.
Scout builds nothing.

## Steps

1. **Settle the scope.** Scout looks at the project Rob is working in, and
   by default at its last two weeks. Look at another project, or a different
   period, only if he asks.

2. **Read Rob's side of the sessions.** The project's transcripts are in
   `~/.claude/projects/<project path with each / replaced by ->/`. They are
   large and mostly tool output, so do not read them directly. Run

   `python3 scripts/user_messages.py --since <date> <that folder>`

   from this skill's folder. It prints only what Rob typed, with times.

3. **Look for these signals**, in this order of value:
   - *Corrections and reverts.* "Put it back", "that's not how I do it",
     "are you sure?", or Rob redoing by hand something Claude produced. This
     is where time was lost.
   - *Preferences restated.* Rob explaining again how he likes something done.
   - *Repetition.* The same kind of request many times.

   Frequency alone is not enough. A request that is frequent and already
   goes well needs no skill.

4. **Check each candidate.**
   - Is it already a skill? List them as Place does. If one exists and still
     gets corrected, the candidate is a Refine of that skill.
   - Is it already solved elsewhere? Do the quick prior-art check from
     Capture step 3.

5. **Report at most five candidates**, best first. For each: what it is in
   one line; the evidence, as a rough count and two of Rob's own messages
   quoted with their dates; and one verdict: capture it, adopt an existing
   tool, refine an existing skill, or leave it. Say how many sessions and
   messages you read.

6. **Stop there.** Rob picks, and picking one starts Capture.

Transcripts can contain anything Rob has worked on. Quote only the short
passages needed as evidence, and put nothing longer than such a quote into a
repo.
