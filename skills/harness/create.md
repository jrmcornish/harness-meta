# Create

Turn something Rob keeps doing into a skill, with him in the loop from the
start. He is the only judge of whether it is right, so the aim is to get
something small in front of him early, not to arrive with a finished design.

## Steps

1. **Look.** Work out what the skill is for and how the task should be done.
   Use whatever gets you there, and usually one or more of: Rob's own
   examples of doing it; what he has said about it, here and in past
   sessions; trying things out; a quick search for an existing tool or
   established practice. Keep this brief: enough to propose a shape, not to
   settle every detail.

   Check first that the skill does not already exist: in the project's
   `.claude/skills/`, in `~/code/harness/global/skills/`, or loose in
   `~/.claude/skills/`. If it does, this is an Update.

   Two things hold whatever you do:
   - Never experiment on Rob's real data. Build throwaway data and try
     things on that.
   - What a search or the documentation tells you is a claim. Say what you
     have tested and what you are taking on trust.

   To read past sessions, `scripts/user_messages.py` in this skill's folder
   prints only what Rob typed. Give it full paths to folders under
   `~/.claude/projects/`, since their names begin with `-`, and search its
   output. Never read a transcript whole.

2. **Come back to Rob before building**, with what you found, the shape you
   propose, and the choices that are his to make. If something
   that already exists does most of the job, lead with that, and say what
   Rob would have to change in how he works to use it. His request describes
   the goal, not the design: a lighter way that costs him a small change of
   habit beats a faithful build of what he described. Include whether
   the skill is local to this project or global; if global, check "Library
   setup" in `manage.md` and include its offer if anything is missing. Add
   anything else you would otherwise have to guess. Wait for his answer.

3. **Build the smallest draft that does what he confirmed.** A folder
   `<name>/` with a `SKILL.md`: a description saying what the skill does and
   when to use it, then the rules. Say briefly where each rule came from, and
   mark a guess as a guess. Be exact about what Rob wants and what the
   result must be, and sparing about how: tools change, so a rule that would
   be wrong after a Claude Code update should state the goal instead. Prefer
   rules a session applies at the time over a script; write a script only
   when the loop shows that rules alone are not enough. A skill that changes
   anything outside the conversation shows Rob what it is about to do and
   waits for his yes. Where the skill is about how something should look,
   include a few of Rob's own examples. All else being equal, shorter is better, so he will be able to read it.
   Write rules as reasons, not orders, so that a reader can apply them to a
   case the rule did not foresee, and only where the obvious thing would be
   wrong. Anything long, such as reference material, goes in its own file
   that `SKILL.md` points to, so it is read only when needed.

   A local skill goes in `<project>/.claude/skills/`, a global one in
   `~/code/harness/global/skills/`.

4. **Go into the loop** in `test.md`: try the draft on cases with Rob
   until he accepts it.
