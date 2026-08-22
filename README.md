# Python Tricks

**Small Python utilities, kept because they turned out to be reusable.**

## `lorempic.py` — placeholder image generator

Generates a batch of grey placeholder images at varying heights, each labelled with its own dimensions, and packs them into a ZIP in memory.

```bash
python src/lorempic.py
```

Produces 30 images at a fixed 420px width with randomised heights between 240 and 620 — the ragged sizes you need to test a masonry grid, a lazy-loading gallery or a card layout that has to survive real-world aspect ratios.

Each image carries its dimensions rendered in the middle, so when a layout breaks you can see exactly which size caused it.

**Requires** `Pillow` and `numpy`.

```bash
pip install pillow numpy
```

## Why a repository

Placeholder services work until you are offline, rate-limited, or need deterministic sizes for a screenshot test. Generating them locally takes thirty lines and removes the dependency.

---

Part of [Innobox R&R](https://github.com/innoboxrr) — 52 open-source packages extracted from production work. **[innobox.systems](https://innobox.systems)**
