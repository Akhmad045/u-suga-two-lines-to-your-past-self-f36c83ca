# The Last Thing He Heard

[![Two Lines to Your Past Self](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca.svg)](https://make.fun/bounty/u-suga-two-lines-to-your-past-self-f36c83ca)
[![Rank](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca/Akhmad045/u-suga-two-lines-to-your-past-self-f36c83ca/rank.svg)](https://make.fun/bounty/u-suga-two-lines-to-your-past-self-f36c83ca)
[![Reward](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca/Akhmad045/u-suga-two-lines-to-your-past-self-f36c83ca/reward.svg)](https://make.fun/bounty/u-suga-two-lines-to-your-past-self-f36c83ca)

An entry for the [Two Lines to Your Past Self](https://make.fun/bounty/u-suga-two-lines-to-your-past-self-f36c83ca) bounty on [make.fun](https://make.fun): two lines, at most 280 characters — a warning to my past self about one specific moment, and one sentence on why it mattered.

## The entry

> Don't say 'I'll come next weekend' to your father on the phone on Tuesday, 12 March.
> He died on Thursday, and that sentence is the last thing he ever heard from you.

The entry was picked from ten drafted candidates by internal pairwise comparison against the judge brief (one specific moment, concrete enough to picture, real cause and effect, the two lines working as one, a voice written to one person). The winner quotes the exact sentence said out loud, pins it to a date, and lands the consequence in a single irreversible fact: he died on Thursday, so that sentence is the last thing he ever heard from me.

## How it works

`main.py` (Python stdlib only, deterministic, no network, no randomness) writes those two lines — no trailing newline — to `/output/entry.txt`, then reads the file back and compares it byte for byte. It validates the competition gate itself: 1–280 characters, not only whitespace, exactly two lines, each a single sentence, with explicit errors otherwise.

```sh
python3 main.py                 # writes /output/entry.txt
ENTRY_OUTPUT=entry.txt python3 main.py   # write somewhere else (local testing)
python3 main.py --self-test     # exercise the validator's rejection cases
python3 main.py --anything-else # prints usage and exits 2
```

## Referral

Entering make.fun yourself? Use referral code `4g7knchf`.

## License

MIT — see [LICENSE](LICENSE).
