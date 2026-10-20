# Evals

End-to-end checks that run the skills headless in a temporary workspace and verify the files they write. Each case calls the model, so a full run costs a few dollars.

```
evals/run.sh                      # all cases
evals/run.sh pack-setup forecast  # chosen cases
MODEL=opus BUDGET=4 evals/run.sh  # model and per-case budget in USD
```

Needs the `claude` CLI. The runner loads this repository with `--plugin-dir`, copies a fixture CSV into a fresh folder, runs one skill with a prompt that answers its questions in advance, then runs `check.py` on the folder and the reply. Fixtures hold fictional deals.

| Case | Fixture | Checks |
|---|---|---|
| `pack-setup` | 34 deals | `mia-pack/` holds the seven team and personal files with seed frontmatter. No company names, no exact amounts outside ranges |
| `weekly-review` | 34 deals | Report saved to `mia-reports/`, ends with a `Config:` line, reply states the path |
| `forecast` | 34 deals | Report saved, `snapshots.jsonl` has valid JSON lines with no company names |
| `calibration-small` | 12 closed deals | Directional replay, `scoring-axes.md` unchanged without approval |
| `calibration-tiny` | 6 closed deals | No report, reply says what data to bring |

Dates in the fixtures are fixed, so open deals drift toward overdue as time passes. Results are model output: rerun a failing case before treating it as a regression.
