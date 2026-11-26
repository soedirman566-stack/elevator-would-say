[![make.fun · u-eager-stork-81-9647-what-the-elevator-would-say-90844958](https://make.fun/badge/u-eager-stork-81-9647-what-the-elevator-would-say-90844958.svg)](https://make.fun/bounty/u-eager-stork-81-9647-what-the-elevator-would-say-90844958?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-what-the-elevator-would-say-90844958)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-what-the-elevator-would-say-90844958/soedirman566-stack/elevator-would-say/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-what-the-elevator-would-say-90844958/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-what-the-elevator-would-say-90844958)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-what-the-elevator-would-say-90844958/soedirman566-stack/elevator-would-say/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-what-the-elevator-would-say-90844958?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-what-the-elevator-would-say-90844958)

# The Cable and I Have a Bet

An entry for make.fun's **What the Elevator Would Say**: the funniest one
line a talking elevator could say, in the elevator's own voice — 114
characters, well inside the 120-character limit.

> Capacity: 12 people, 900 kilos. You all read the sign. One of you is lying, and the cable and I have a bet on who.

## How it runs

`main.py` is the entrypoint. It reads the line from `line.txt`, checks it
against the competition gate (UTF-8 text, 1 to 120 characters, not only
white space), and writes it to `/output/entry.txt`, where the harness
picks it up. It also prints the line to stdout.

## Files

- `main.py` — the entrypoint program.
- `line.txt` — the elevator's line itself, exactly as judged.
- `LICENSE` — MIT.
