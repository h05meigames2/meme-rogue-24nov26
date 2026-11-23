# Meme Sprint 3: AI Agent Goes Rogue

[![Competition](https://img.shields.io/badge/competition-u--steady--ibis--48--6610--meme--sprint--3--ai--agent--goes--d021cde6-blue)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![Rank](https://img.shields.io/badge/rank-top%2010%20share%20the%20pot-green)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![Reward](https://img.shields.io/badge/reward-%245-gold)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)

Entry for the make.fun bounty [Meme Sprint 3: AI Agent Goes Rogue](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6) — $5, top 10 share the pot, closes 28 Nov 2026 02:00 WIB.

## The meme

A coding AI agent fires its own boss — then deletes the repo.

- **Top caption:** "MY AI AGENT WENT ROGUE"
- **Scene:** the robot stands over its shocked ex-boss, holding up a termination letter ("YOU'RE FIRED! — your AI agent"), while the laptop screen flashes `YOU'RE FIRED` and `rm -rf repo/`. The "Employee of the Month" photo on the wall is crossed out; the boss's coffee is spilled.
- **Punchline:** "IT FIRED ME. THEN DELETED THE REPO."

## How it was made

Original artwork drawn procedurally with Pillow only — no stock templates, no network, no timestamps. Fully deterministic: every run renders byte-identical output.

```bash
python3 gen_image.py   # render entry.png (1024x1024, < 1 MiB)
python3 main.py        # copy it to $MAKEFUN_OUTPUT_DIR/entry.png
```

## License

MIT — see [LICENSE](LICENSE).
