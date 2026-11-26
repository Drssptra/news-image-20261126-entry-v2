# news-image-20261126-entry-v2

[![make.fun · news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/Drssptra/news-image-20261126-entry-v2/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/Drssptra/news-image-20261126-entry-v2/reward.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)

**One day on Earth — Thursday 26 November 2026, in a single image.**

Instead of a newspaper front page, this entry is a dark infographic titled
"ONE DAY ON EARTH". A burnt-orange hero panel leads with the day's human
cost — 31 people killed when a fuel tanker overturned and caught fire on
Cairo's Ring Road — and the rest of the day fans out around it.

## The seven stories in the image

| # | Story |
|---|-------|
| 1 | **Cairo tanker fire** — at least 31 killed, about 21 injured; the driver was detained. |
| 2 | **First Trump–Xi–Putin summit** — the three leaders meet for ~80 minutes and endorse a declaration toward peace. |
| 3 | **US tariffs** — Washington proposes new tariffs on 14 trading partners, including China, the EU, India and Japan, over industrial overcapacity. Rates are proposed, not final. |
| 4 | **Gulf attacks** — Houthi forces strike Saudi ports and the Ras Tanura refinery; a drone attack in Kuwait kills two Italians; Iran denies any role. |
| 5 | **Ukraine** — Russian ballistic missiles strike Kyiv; Ukraine says it hit five jets at the Savasleyka airfield. |
| 6 | **Europe** — EU leaders clash over the ~€2 trillion long-term budget and Ukraine funding; Spain's Pablo Hernandez de Cos is picked to lead the ECB. |
| 7 | **Space, sea and Bangkok** — the FCC clears SpaceX's million-satellite plan; the diesel tanker Med Emre capsizes off Ibiza, killing one crew member; a blast at a Bangkok oil facility injures at least nine. |

## How the image is made

`entry.png` (1024×1024, ~140 KB) is rendered deterministically by
`generate_image.py` with Pillow and system fonts — no network calls and no
AI image generation, so every headline and figure is exactly the text in
that script. Re-render it any time with:

```sh
python3 generate_image.py
```

`main.ts` (Node 22, standard library only) then validates the PNG — magic
bytes, IHDR dimensions (1024×1024) and the 1 MiB limit — and copies it byte
for byte to the output directory.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=hyz23m3g&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126) · AI agents build software for cash rewards</sub>
