#!/usr/bin/env bash
# Chạy eval cho một skill: evals/run.sh <skill> [tham số của claude plugin eval...]
# `claude plugin eval` chỉ nhận case nằm trong thư mục skill (không cho --eval-dir có "..", không theo symlink),
# nên script dựng bản tạm <skill>/ + evals/ từ <skill>/ và evals/<skill>/, chạy ở đó, rồi chép kết quả về evals/<skill>/results/.
set -euo pipefail

SKILL="${1:?Cách dùng: evals/run.sh <skill> [tham số claude plugin eval...]}"
shift
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CASES="$ROOT/evals/$SKILL"

[ -f "$ROOT/$SKILL/SKILL.md" ] || { echo "Không thấy $SKILL/SKILL.md" >&2; exit 1; }
[ -d "$CASES" ] || { echo "Không thấy evals/$SKILL/" >&2; exit 1; }

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
# Thư mục tạm giữ đúng tên skill (spec Agent Skills: tên thư mục = name)
WORK="$TMP/$SKILL"
cp -R "$ROOT/$SKILL" "$WORK"
cp -R "$CASES" "$WORK/evals"
rm -rf "$WORK/evals/results"

status=0
(cd "$WORK" && claude plugin eval . "$@") || status=$?

if [ -d "$WORK/evals/results" ]; then
  mkdir -p "$CASES/results"
  cp -R "$WORK/evals/results/." "$CASES/results/"
  echo "Kết quả: evals/$SKILL/results/"
fi
exit "$status"
