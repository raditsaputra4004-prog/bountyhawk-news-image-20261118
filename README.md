# Wednesday 18 November 2026 — the world in one image

Entry for make.fun `news-image-20261118`: one 1024×1024 image summing up
the world's news of Wednesday 18 November 2026.

## What the image shows

Six stories, each verified against reporting of 18 November 2026
(Reuters, AP, AFP, The Hindu, Al Jazeera and others):

1. **Diplomacy** — Xi and Putin meet in Shenzhen; Trump lands for
   Thursday's trilateral summit.
2. **Gulf** — U.S. jets strike a missile site on Qeshm Island; Iran
   fires on Bahrain and Kuwait.
3. **Ukraine** — Kerch Bridge hit for a second day; part of the road
   span collapses.
4. **U.S. politics** — Democrats take the Senate 56–44 as Peltola
   beats Sullivan in Alaska.
5. **Tech** — Nvidia posts a record $115.8bn quarter; its board says
   no to Huang's return as CEO.
6. **Weather** — Cyclone Akvan bears down on India; landfall on the
   Andhra coast expected Friday.

The footer adds three more items from the day: the U.S. losing
measles-free status, Ebola in DR Congo passing 11,000 cases, and the
India–Japan 2+2 talks in Tokyo.

## How it was made

`tools/draw.py` renders `entry.png` from the researched facts with
Pillow and DejaVu (no downloaded images, no AI-generated art — every
word is exact text, so nothing can come out garbled). `main.ts`
(Node, standard library only) copies `entry.png` to the output
directory, so both grader runs write identical bytes.

Run it locally:

```sh
python3 tools/draw.py
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

## License

MIT — see `LICENSE`.
