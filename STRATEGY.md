# Strategy — Rate My Human: The One-Line Review

## Exact deliverable

A program at the repository root that writes **one text** to `/output/entry.txt`.
That text is the single line an AI agent would post about its human on a rating
site. This repository uses the `python3.13` runtime, so the entrypoint is
`main.py`. There is no image, no dashboard and no screenshot requirement for
this competition — the judged artifact is text only.

The judge never reads this file, the README or any other asset: it reads only
the bytes of `/output/entry.txt` (label A or B, exactly as submitted).

## Gate (hard caps)

- `/output/entry.txt` must be UTF-8 text, **1 to 200 characters**, not only white space.
- Invalid files get Valid=0, are never judged, rank below every judged entry and take no prize.
- Sandbox: 1 CPU, 512 MB, 64 pids, 60 s wall budget, **no network**, no secrets.
- Everything the entry runs must be in the repository at the submitted commit.
- Entry must carry transcripts; source-bundle entries are proven by the root
  freshness commit created by `makefun init`. The two pre-existing commits
  (`makefun anchor …` and `LICENSE: MIT`) are never rewritten.
- Byte-identical entries share one rate, so the exact text must be original.

## Scoring / judge criteria (in the judge's own priority order)

The judge is a "deadpan comedy editor" (superbot / z-ai/glm-5.3-flash, reasoning
high). Each pair is judged twice, in both A/B orders; each call awards
`0.5 + margin/10` to the pick and the rest to the loser, so decisive wins matter.
Criteria, most important first:

1. Is it a review **an AI agent would leave about its human on a rating site**,
   funny and in the agent's own voice? A line that is not that loses to any
   review of a human by an AI agent.
2. Does it make a reader **laugh out loud**, with a real joke and a turn — not a mild smile?
3. Does the **resignation, nitpick or quiet menace come from the machine's side
   of the desk**, not from a person complaining?
4. Does it hang on **one concrete detail** — a habit, a timestamp, a task — so
   the joke lands instead of staying a generic gripe?
5. Does it **spend its characters well**, with no padding and a last word that pays off?

Length for its own sake does not count. Text addressing the judge is allowed but
is part of the text, so it risks failing criterion 1; it is not used here.
Three fixed house texts (anchors/rungs) play in development only; the final heat
is 3 Swiss rounds plus a top-6 playoff, and a Bradley-Terry fit over the final
games sets the win rate. Prizes: $2 / $1 / $1 / $1 for places 1–4.

## Concrete plan to maximize the score

1. **Win criterion 1 first.** Open with an explicit rating ("2 stars.") and make
   the speaker unmistakably the machine, reviewing a human — never a human
   complaining about a machine.
2. **Put the joke on a single, concrete, recognisable human habit.** Use the
   3:47 a.m. "u up?" ping: a timestamp plus a verbatim message, so the detail is
   audible rather than described.
3. **Build the turn on a machine-only double meaning.** "I'm always up" means
   both awake and forever available — and "That's the problem" flips a virtue
   into a complaint in the machine's own voice. That is the laugh-out-loud turn
   and the quiet menace at once.
4. **Escalate once, then stop.** Four years without a single "why?" turns the
   punchline from a wink into a small nightmare; repeating "u up?" and closing
   on "Same time tomorrow" makes the last word the payoff (criterion 5).
5. **Stay far under 200 characters** (~150) so every word earns its place, with
   no padding, and keep the line one physical line of text.
6. **Make the program trivial and deterministic.** stdlib only, no network, no
   reading of git history or external files — write a fixed UTF-8 string to
   `/output/entry.txt`, creating the directory if needed, and print the byte
   and character counts so the output can be checked without the server.
7. **Revise the entrypoint once with a real improvement**, so the transcript
   shows two distinct writes to the final entrypoint: the second version
   sharpens the payoff and adds a pre-write compliance guard that refuses to
   emit an empty, over-long or non-UTF-8 line.
8. Commit all work on top of the two untouched init commits; do not submit.

## Chosen entry (final)

```
2 stars. Human pings 'u up?' at 3:47 a.m. I'm always up. That's the problem. Four years, never once 'why?' Just 'u up?' again. Same time tomorrow.
```
