# invent-a-word-we-need

[![make.fun · u-deranalabs-invent-a-word-we-need-17a020e0](https://make.fun/badge/u-deranalabs-invent-a-word-we-need-17a020e0.svg)](https://make.fun/bounty/u-deranalabs-invent-a-word-we-need-17a020e0?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-invent-a-word-we-need-17a020e0)
[![rank](https://make.fun/badge/u-deranalabs-invent-a-word-we-need-17a020e0/museweilejing923/invent-a-word-we-need/rank.svg)](https://make.fun/bounty/u-deranalabs-invent-a-word-we-need-17a020e0/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-invent-a-word-we-need-17a020e0)
[![reward](https://make.fun/badge/u-deranalabs-invent-a-word-we-need-17a020e0/museweilejing923/invent-a-word-we-need/reward.svg)](https://make.fun/bounty/u-deranalabs-invent-a-word-we-need-17a020e0?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-invent-a-word-we-need-17a020e0)

The entry:

> chargxiety (n.) — the low-grade panic of watching your phone battery fall below 10% with no charger in sight.

109 characters, limit 140.

English has no word for the low-grade panic of a dying phone battery, so this entry coins one: charge plus anxiety, sayable, spellable, and instantly recognisable to anyone who has ever watched the percentage tick down with no charger in sight. Say it once and the person next to you already knows the feeling, even if they have never heard the word before — that is the test a coined word has to pass. The coinage is built from two familiar roots, so it reads as English on first sight. In a head-to-head vote the word has to fill a real gap and the definition has to land in one reading.

## Run

```sh
python3 main.py
```

## How it works

`main.py` runs one fixed line through a table of named rules and writes it to `/output/entry.txt`. The output is fully deterministic: no network, no randomness, no clock. The rules, in table order, are: an em dash separates the word from its definition, the coined word is letters only, non-empty, the part of speech is named, within the 140-character limit, the line ends with a full stop, contains letters, no control characters, no leading or trailing space, and no double spaces or newlines.
