# TODO — toxicwind/roundup: finish the guidellm→roundup rename + README redo

**Read this first.** Work is IN FLIGHT and UNCOMMITTED. Do not start from a clean checkout — you will lose the rename. Repo: `/home/toxic/workspace/untracked/roundup` (remote `origin` = https://github.com/toxicwind/roundup.git, `upstream` = https://github.com/vllm-project/guidellm.git).

## Goal (user's words)

- "https://github.com/toxicwind/roundup fix it" (m00002)
- "the readme is completely outdated for the fork" (m00010)
- "make sure you figure out and fix upstream" (m00020)
- "uh no i want to keep only roundup" (m00054) → no dual identity, one name
- "complete rename and readme redo" (m00058)

End state: repo is `roundup` everywhere (code, packaging, CLI, env vars, docs, CI, containers), README is rewritten to describe the fork accurately, fork stays merged current with upstream `vllm-project/guidellm`, tests green, CLI verified, pushed to `origin/main`.

Standing rules that apply (`/home/toxic/AGENTS.md`): maximal not minimal, push everything, no review gates, forward-only, verify with real runs, never leave half-done work.

## Exact current state

- Branch: `upstream-merge/20261002`. HEAD = `77e4409f` "merge upstream/main: 5 commits (generation_delay metric, confidence intervals, constraint param doc fix, cleanup)" — **committed, NOT pushed**.
- Working tree: **703 dirty paths** (mostly the mechanical rename, plus `git mv` renames).
- Upstream merge is done: fork was 5 behind / 18 ahead; merged `upstream/main` (bfcae5a3) with `--no-ff`. One conflict, additive, resolved at `src/roundup/benchmark/schemas/base.py` by keeping BOTH sides (fork `scorers`/`scorer_config` + `@model_serializer(mode="wrap") _omit_empty_scoring_fields`; upstream `confidence: float | None = Field(default=0.95, gt=0.0, lt=1.0, …)`).
- `git grep -i guidellm` outside `build/` and `uv.lock` → **0 hits**.
- Tests have **NOT** been run since the rename. The venv is stale (see step 2).

## DONE (do not redo)

1. **Upstream sync** — merged, conflict resolved (details above).
2. **Mechanical text rename** — script `/home/toxic/rename-roundup/rename.py` rewrote 392 files. Rules, in order: `github.com/vllm-project/guidellm`→`github.com/toxicwind/roundup`, `vllm-project.github.io/guidellm`→`toxicwind.github.io/roundup`, `pypi.org/project/guidellm`→`pypi.org/project/roundup`, then `GUIDELLM`→`ROUNDUP`, `GuideLLM`→`Roundup`, `Guidellm`→`Roundup`, `guidellm`→`roundup`.
3. **Wrong-owner leftovers fixed** — 14 files where the text had no `github.com/` prefix had become `vllm-project/roundup`; rewritten to `toxicwind/roundup`. Remaining `vllm-project/*` hits in the repo are legitimate (`vllm-project/vllm` links).
4. **Path renames** — `git mv src/guidellm src/roundup`; `git mv .agents/skills/guidellm-weekly-summary .agents/skills/roundup-weekly-summary`; `git mv docs/assets/guidellm-*.png docs/assets/roundup-*.png` (7 files). `CLAUDE.md` is a symlink → `AGENTS.md`; `.claude/skills` → `../.agents/skills` (fine).
5. **Build artifacts untracked** — `build/` (244 tracked files) and `src/guidellm.egg-info/` removed from git and from disk; `.gitignore` now ends with `build/` and `*.egg-info/`.
6. **Config files** — already renamed and correct: `pyproject.toml` (`name = "roundup"`, entry point `roundup = "roundup.__main__:cli"`, package-data keys, `[tool.mypy] files`, import-linter `root_package = "roundup"`), `setup.py` (`src/roundup`, `ROUNDUP_BUILD_TYPE`, `ROUNDUP_BUILD_ITERATION`), `src/roundup/settings.py` (`env_prefix="ROUNDUP__"`, `log_file = Path("roundup.log")`), `Containerfile` + `Containerfile.vllm` (`ROUNDUP_BUILD_*`, `/home/roundup`, `ROUNDUP__DEFAULT_RESULTS_DIR`, ENTRYPOINT roundup), `.github/workflows/release.yml` + `build-multiarch-container.yml`, `mkdocs.yml` (site_url/repo_url/edit_uri/logo/favicon/`modules: ['src/roundup']`/`/roundup/` + `/roundup/zh/`).
7. **pyproject metadata** — `description = "Benchmark and profile LLM deployments against real inference workloads. Fork of vllm-project/guidellm."`; `[project.urls]` homepage/source/issues → toxicwind/roundup, `docs = "https://toxicwind.github.io/roundup"`, `upstream = "https://github.com/vllm-project/guidellm"`.
8. **Container OCI label** — `org.opencontainers.image.documentation` was wrongly `https://blog.vllm.ai/roundup/stable` (upstream's blog); now `https://toxicwind.github.io/roundup` in both Containerfiles.

## REMAINING WORK — in this order

### 1. Fix the one test the upstream merge broke

`tests/unit/benchmark/test_scoring.py::test_no_scorer_config_additive_scoring_keys_only` fails with `AssertionError: unexpected config deltas vs pre-scoring (74ec8623^): ['confidence']`. The test keeps manual allowlists. At line 629 add the new upstream key, mirroring the comment style at lines 618-628 (which cites upstream commits 148c3bab / 337fc750 for `_ADDITIVE_REQUEST`):

```python
# Upstream-additive (not scoring) BenchmarkConfig field:
#   confidence <- 58ea2f3e confidence intervals for request-level metrics
_ADDITIVE_CONFIG: set = {"confidence"}
```

### 2. Rebuild the venv (mandatory before running anything)

The editable install is stale and still named guidellm: `.venv/lib/python3.12/site-packages/__editable__.guidellm-0.9.0.dev20.pth` + `guidellm-0.9.0.dev20.dist-info`. Run:

```bash
cd /home/toxic/workspace/untracked/roundup
uv lock                       # uv.lock still says name = "guidellm" (line 1209, and 1310/1355 extras)
uv sync --all-extras          # regenerates the .pth as roundup-*.pth
roundup --version             # CLI entry point must resolve
```

Note: install regenerates tracked files `src/roundup/version.py` and `src/roundup/version.txt` (setup.py `write_version_files()`), and recreates `src/roundup.egg-info/` (now gitignored) — that is expected, commit the version files, do not commit egg-info.

### 3. Re-run the suite and triage

Baseline before the rename (on the merged tree) was: `3 failed, 3653 passed, 31 skipped, 188 xfailed in 315.57s` (log `/tmp/roundup-baseline-tests.txt`).

- The 2 `tests/unit/benchmark/test_progress.py` failures (`test_logs_are_periodic_with_or_without_rich[True]`, `test_queued_logs_share_rich_terminal`) are **pre-existing upstream bugs**, reproduced on a clean worktree of `upstream/main` (`/home/toxic/workspace/untracked/roundup-upstream-check`: 2 failed, 6 passed). Cause: the Rich console renders nothing (`assert 'Benchmarks' in '\n'`) when stdout is not a TTY. This repo now owns that code — fix it properly (render to a non-console sink, or make the progress renderer TTY-aware) rather than blanket-xfailing. Do not leave it red.
- The 3rd failure was the scoring one from step 1.

```bash
uv run pytest -q -p no:randomly 2>&1 | tee /tmp/roundup-post-rename-tests.txt   # ~5 min
```

### 4. Docs that need hand-fixing (the mechanical pass mangled upstream credit)

- `UPSTREAM-MERGE.md` — header now reads `**Upstream:** vllm-project/roundup` and `**Renamed:** 2026-09-30 (roundup → roundup, ranch western theme)`, line 19 says `git remote add upstream https://github.com/toxicwind/roundup.git`, and the body says "merge upstream roundup changes". All of these must say **vllm-project/guidellm** (the real upstream) and the rename note must describe the actual rename. Also re-check the "18 commits ahead / 0 behind" numbers — they are now stale after the merge.
- `DEVELOPING.md:112` — weekly-summary skill line still references `vllm-project/roundup` → should be `toxicwind/roundup`.
- `.agents/skills/roundup-weekly-summary/scripts/fetch_activity.sh:6` — `REPO="vllm-project/roundup"` → `REPO="toxicwind/roundup"` (same for the `--repo` help text on line 22), and `SKILL.md:3,4,9,112`.
- `README.md` — full rewrite, see step 5.
- `AGENTS.md` / `MERGE-DECISIONS.md` — update repo identity, paths (`src/guidellm`→`src/roundup`), and the merge record. `AGENTS.md` carries upstream's "NOTE TO AI: SHALL NOT be edited by agents"; the user's explicit order (m00058) to complete the rename overrides it.
- Verify no stale brand text survives: `git grep -inE 'guidellm|guide llm'` (expect only the intentional "Fork of vllm-project/guidellm" / upstream-credit lines), and that `mkdocs build --strict` succeeds (assets were renamed to `roundup-*.png`).

### 5. README rewrite (the user's second explicit ask)

Requirements:

- Written for the **fork**, no dual identity. Header: Roundup, one-line purpose, install, usage.
- Must be accurate to the **merged** code: includes upstream's new `generation_delay` metric (4d733288) and confidence intervals for request-level metrics (58ea2f3e, `confidence` default 0.95), plus the corrected benchmark constraint parameter names (3dd649c5). Verify each claim against the source before writing it.
- Document the fork-specific feature set (scoring: `src/roundup/benchmark/scoring/` — adapters, instruction, protocol, registry; report field `roundup_version` in `src/roundup/benchmark/schemas/report.py`, consumed by `outputs/html.py` and `html_report/report.js`).
- **No PyPI badge and no `pip install roundup`** — an unrelated project owns `pypi.org/project/roundup`. Use install-from-repo (`pip install git+https://github.com/toxicwind/roundup.git` or `uv sync`) and the GitHub container (`ghcr.io/toxicwind/roundup`), and say the PyPI name is not published by this fork.
- Upstream credit: one clear "Fork of vllm-project/guidellm — Apache-2.0, see LICENSE" line, plus a "Merged upstream through `upstream/main` bfcae5a3" note. Do not claim upstream features we dropped.
- Remove any `vllm-project/...` self-links (already rewritten) and re-verify every URL you keep.

### 6. Verify, commit, push

- Lint/type/import contracts: `uv run ruff format --check src tests`, `uv run ruff check src tests`, `uv run mypy`, `uv run lint-imports`.
- **CLI smoke (required, not optional)** — run the real thing, e.g. `roundup run simple --target mock:// --output-dir /tmp/roundup-smoke` against the bundled mock server, confirm the JSON/CSV/HTML report is produced and that `roundup --version`, `roundup run --help`, `roundup mock-server --help` work. Keep the smoke artifacts out of the repo.
- Commit (branch or straight to `main` per forward-only rules — user's standing rule is bruteforce repairs go straight to main, no PR ceremony), then `git push origin main`.
- Cleanup: remove the comparison worktree `git worktree remove /home/toxic/workspace/untracked/roundup-upstream-check` (only when no live worker is reading it) and delete the throwaway `/home/toxic/rename-roundup/`.
- Confirm on GitHub: `gh api repos/toxicwind/roundup` description/homepage still sane; README renders.

## Notes / traps

- `uv run pytest` config has `addopts = '-s -vvv'`; output is huge — redirect to a file and grep it.
- Do not run `uv run pytest` before step 2; the stale `.pth` will import the wrong dist name and every import fails confusingly.
- `docs/en/index.md` and `docs/zh/index.md` point the logo at `raw.githubusercontent.com/toxicwind/roundup/main/docs/assets/roundup-logo-{light,dark}.png` — those asset paths only resolve after step 6 pushes the renamed files.
- `src/roundup/benchmark/outputs/html_report/template.html:245,261` and `tests/unit/benchmark/test_html_output.py:451` (`assert "toxicwind.github.io" not in content`) were rewritten as a pair — keep them consistent if either changes again.
