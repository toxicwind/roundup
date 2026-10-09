# Upstream Merge Workflow — roundup

**Fork:** `toxicwind/roundup` **Upstream:** `toxicwind/roundup` **Renamed:** 2026-09-30 (roundup → roundup, ranch western theme)

This document describes how to merge upstream roundup changes without losing our patches.

## Our Patches (what to protect)

1. **Rename:** `roundup` → `roundup` throughout (package names, imports, docs)
2. **Ranch integration:** moved into `ranch/roundup/` via git mv (history preserved)
3. **Upstream sync:** 20 commits merged from upstream 2026-09-30 (metrics, tracing, OTel, backend per-request passthrough) — see commit `f7c3cdbb`

## Merge Procedure

```sh
# 1. Add upstream remote (once)
git remote add upstream https://github.com/toxicwind/roundup.git

# 2. Fetch and check divergence
git fetch upstream
git rev-list --count HEAD..upstream/main    # behind: upstream commits we don't have
git rev-list --count upstream/main..HEAD   # ahead: our commits

# 3. Merge on a fresh branch (NEVER main directly)
git checkout -b upstream-merge/$(date +%Y%m%d-%H%M%S)
git merge --no-ff upstream/main -m "merge upstream/main: N commits"

# 4. Resolve conflicts (if any)
# Our files: keep ours. Upstream files we didn't touch: take theirs.
# Modified files: re-apply our changes on top of their new version.

# 5. Run tests
python3 -m pytest -x -q

# 6. If clean + green: open a PR for human review
# NEVER push to main directly — human approves the merge
```

## Automated (trailboss)

trailboss owns this workflow agentically:

```sh
TRAILBOSS_FORKS_DIR=/home/toxic/forks trailboss upstream merge roundup --dry-run
TRAILBOSS_FORKS_DIR=/home/toxic/forks trailboss upstream watch
```

See `toxicwind/trailboss` README for the full agentic upstream feature.

## Last Verified

- 2026-09-30: 0 behind, 17 ahead. Up to date.
- Merge-base with upstream: `a938aaa620045e3b90202f3b3a87f34f86958144`
