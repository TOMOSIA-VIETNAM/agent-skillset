"""Dựng ảnh SVG dạng cửa sổ terminal cho README (tự đổi màu theo nền sáng / tối).

Mỗi dòng là (kiểu, [(chữ, class), ...]). Kiểu: line, prompt, note, gap, small,
hoặc ("box", tên_box) để gom các dòng vào một khung (file, khối nhắc...).
"""
import textwrap
from html import escape as E

W, X, LH, WRAP = 800, 28, 21, 84

CSS = """
  text { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace; font-size: 13px; }
  .win { fill: #ffffff; stroke: #d0d7de; } .bar { fill: #f6f8fa; } .sep { stroke: #d0d7de; }
  .title { fill: #59636e; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 12px; }
  .ink { fill: #1f2328; } .muted { fill: #59636e; } .head { fill: #0550ae; font-weight: 600; } .sub { fill: #0550ae; }
  .label { fill: #1f2328; font-weight: 700; } .hl { fill: #8250df; font-weight: 700; } .anno { fill: #8250df; font-style: italic; }
  .ph { fill: #9a6700; font-style: italic; } .drop { fill: #8c959f; text-decoration: line-through; } .you { fill: #1a7f37; font-weight: 700; }
  .ok { fill: #1a7f37; font-weight: 700; } .warnh { fill: #9a6700; font-weight: 700; } .fileh { fill: #59636e; font-weight: 600; }
  .box-warn { fill: #fff8c5; stroke: #d4a72c; } .box-file { fill: #f6f8fa; stroke: #d0d7de; } .box-form { fill: #ddf4ff; stroke: #54aeff; }
  @media (prefers-color-scheme: dark) {
    .win { fill: #0d1117; stroke: #3d444d; } .bar { fill: #151b23; } .sep { stroke: #3d444d; } .title { fill: #9198a1; }
    .ink { fill: #e6edf3; } .muted { fill: #9198a1; } .head { fill: #4493f8; } .sub { fill: #4493f8; } .label { fill: #e6edf3; }
    .hl { fill: #ab7df8; } .anno { fill: #ab7df8; } .ph { fill: #d29922; } .drop { fill: #656c76; } .you { fill: #3fb950; }
    .ok { fill: #3fb950; } .warnh { fill: #d29922; } .fileh { fill: #9198a1; }
    .box-warn { fill: #272115; stroke: #9e6a03; } .box-file { fill: #151b23; stroke: #3d444d; } .box-form { fill: #0c2d4a; stroke: #1f6feb; }
  }
"""


def wrap(text, cls="ink", kind="line", width=WRAP):
    """Một đoạn dài → nhiều dòng; dòng bắt đầu bằng '- ' hoặc số thì thụt dòng sau."""
    indent = "  " if text[:2] in ("- ", "1.", "2.", "3.", "4.") else ""
    return [(kind, [(ln, cls)]) for ln in textwrap.wrap(text, width, subsequent_indent=indent)]


def render(path, title, rows, aria):
    y, out, boxes = 46, [], {}
    for kind, parts in rows:
        if kind == "gap":
            y += 10; continue
        if kind == "small":
            y += 6; continue
        y += LH
        x = X
        if isinstance(kind, tuple):
            name = kind[1]
            b = boxes.setdefault(name, [y - LH + 4, y, kind[2] if len(kind) > 2 else "box-file"])
            b[1] = y
            x = X + 14
        spans = "".join(f'<tspan class="{c}">{E(t)}</tspan>' for t, c in parts)
        out.append(f'<text x="{x}" y="{y}" xml:space="preserve">{spans}</text>')
    h = y + 30
    rects = "".join(
        f'<rect class="{cls}" x="{X - 4}" y="{a - 2}" width="{W - 2 * X + 8}" height="{b - a + 12}" rx="6"/>\n'
        for a, b, cls in boxes.values())
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" width="{W}" height="{h}" role="img" aria-label="{E(aria)}">
<style>{CSS}</style>
<rect class="win" x="0.5" y="0.5" width="{W - 1}" height="{h - 1}" rx="10"/>
<path class="bar" d="M1 11a10 10 0 0 1 10-10h{W - 22}a10 10 0 0 1 10 10v23H1z"/>
<line class="sep" x1="1" y1="34" x2="{W - 1}" y2="34"/>
<circle cx="20" cy="17.5" r="6" fill="#ff5f57"/><circle cx="40" cy="17.5" r="6" fill="#febc2e"/><circle cx="60" cy="17.5" r="6" fill="#28c840"/>
<text class="title" x="{W // 2}" y="22" text-anchor="middle">{E(title)}</text>
{rects}{chr(10).join(out)}
</svg>
'''
    open(path, "w").write(svg)
    return h
