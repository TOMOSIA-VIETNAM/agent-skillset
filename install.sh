#!/bin/bash
set -e

# Cài skill generate-short-bio vào ~/.claude/skills/generate-short-bio/
#   bash install.sh               cài / cập nhật
#   bash install.sh --uninstall   gỡ
#
# Chạy trong repo (local mode) → symlink, sửa skill có hiệu lực ngay.
# Chạy qua curl | bash (download mode) → tải các file trong FILES từ GitHub.
# Skill nằm ở thư mục con $NAME/ của repo; FILES tính từ thư mục đó.

NAME="generate-short-bio"
REPO="${AGENT_SKILLSET_REPO:-TOMOSIA-VIETNAM/agent-skillset}"   # fork thì đặt AGENT_SKILLSET_REPO=<owner>/<repo>
BRANCH="${AGENT_SKILLSET_BRANCH:-main}"
RAW_BASE="https://raw.githubusercontent.com/$REPO/$BRANCH/$NAME"
SKILLS_HOME="$HOME/.claude/skills"
SKILL_DIR="$SKILLS_HOME/$NAME"

# File được cài — thêm / đổi tên file trong references/ thì sửa ở đây (download mode chỉ tải file có trong danh sách).
# evals/ không liệt kê → không lọt vào thư mục skill đã cài.
FILES=(
  SKILL.md
  references/collect-info.md
  references/checklist.md
  references/jd-match.md
  references/companions.md
  references/write-bio.md
  references/output.md
)

# Dependency: humanizer skill (https://github.com/blader/humanizer)
# Pin theo commit (v3.1.0) — generate-short-bio dựa vào "embedded mode" của humanizer; nâng version thì kiểm tra lại mode này
HUMANIZER_DIR="$SKILLS_HOME/humanizer"
HUMANIZER_REF="8c307f367c91bd974002f10f2be2965d642c13df"
HUMANIZER_URL="https://raw.githubusercontent.com/blader/humanizer/$HUMANIZER_REF/SKILL.md"

SCRIPT_DIR=""
if [ -n "${BASH_SOURCE[0]}" ] && [ -f "${BASH_SOURCE[0]}" ]; then
  SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
fi

# Tải $1 về file $2 qua file tạm — mạng đứt giữa chừng không làm hỏng file đang có
download() {
  local tmp
  tmp="$(mktemp)"
  if curl -fsSL "$1" -o "$tmp" && [ -s "$tmp" ]; then
    chmod 644 "$tmp"
    mv "$tmp" "$2"
  else
    rm -f "$tmp"
    return 1
  fi
}

install_humanizer() {
  if [ -e "$HUMANIZER_DIR" ]; then
    echo "  humanizer already installed: $HUMANIZER_DIR (kept as is)"
    return 0
  fi
  # Symlink hỏng: -e trả false nhưng mkdir -p sẽ lỗi → xóa link rồi cài mới
  if [ -L "$HUMANIZER_DIR" ]; then
    rm "$HUMANIZER_DIR"
  fi
  echo "  Installing dependency: humanizer..."
  mkdir -p "$HUMANIZER_DIR"
  if download "$HUMANIZER_URL" "$HUMANIZER_DIR/SKILL.md"; then
    echo "  Installed: $HUMANIZER_DIR/SKILL.md"
  else
    rm -rf "$HUMANIZER_DIR"
    echo "  Warning: failed to install humanizer. Skills using it fall back to their built-in rules."
  fi
}

remove_install() {
  if [ -L "$SKILL_DIR" ]; then
    rm "$SKILL_DIR"
  elif [ -e "$SKILL_DIR" ]; then
    rm -rf "$SKILL_DIR"
  fi
}

install_local() {
  local top
  echo "Installing $NAME (local, symlink -> $SCRIPT_DIR/$NAME)"
  remove_install
  mkdir -p "$SKILL_DIR"
  # Chỉ link các mục cấp đầu có trong FILES (SKILL.md, references/)
  for top in $(printf '%s\n' "${FILES[@]}" | cut -d/ -f1 | sort -u); do
    ln -sfn "$SCRIPT_DIR/$NAME/$top" "$SKILL_DIR/$top"
  done
}

install_download() {
  local stage f
  if [ -L "$SKILL_DIR" ] || [ -L "$SKILL_DIR/SKILL.md" ]; then
    echo "Skipped: $SKILL_DIR is a symlink to a local repo (pull that repo instead)."
    return 0
  fi
  echo "Installing $NAME (download from $REPO@$BRANCH)"
  stage="$(mktemp -d)"
  # Tải hết vào thư mục tạm trước — thiếu 1 file thì giữ nguyên bản đang cài
  for f in "${FILES[@]}"; do
    mkdir -p "$stage/$(dirname "$f")"
    if ! download "$RAW_BASE/$f" "$stage/$f"; then
      rm -rf "$stage"
      echo "Error: failed to download $f — kept current install. Check repo URL (AGENT_SKILLSET_REPO)."
      return 1
    fi
  done
  remove_install
  mkdir -p "$SKILL_DIR"
  cp -R "$stage/." "$SKILL_DIR/"
  find "$SKILL_DIR" -type d -exec chmod 755 {} +
  rm -rf "$stage"
  echo "  Installed to: $SKILL_DIR"
}

# Tham số tên skill (cú pháp cũ: install.sh [--uninstall] generate-short-bio) vẫn được chấp nhận
MODE="install"
for arg in "$@"; do
  case "$arg" in
    --uninstall) MODE="uninstall" ;;
    "$NAME") ;;
    *) echo "Error: unknown argument '$arg'. Usage: install.sh [--uninstall]"; exit 1 ;;
  esac
done

if [ "$MODE" = "uninstall" ]; then
  remove_install
  echo "Uninstalled: $SKILL_DIR"
  echo "Note: humanizer was kept since other skills may use it."
  exit 0
fi

if [ -n "$SCRIPT_DIR" ] && [ -f "$SCRIPT_DIR/$NAME/SKILL.md" ]; then
  install_local
else
  if ! command -v curl &>/dev/null; then
    echo "Error: curl is required."
    exit 1
  fi
  install_download
fi
install_humanizer

echo ""
echo "Done! Restart Claude Code to load: $NAME"
