"""DESIGN_SYSTEM.md의 CSS 변수 블록을 읽어 WCAG AA 대비를 검증한다.

    python scripts/check-contrast.py

토큰 값을 바꿨으면 이 스크립트를 돌린다. 실패하면 §8의 실측 표도 함께 고친다.
"""
import io, re, sys, pathlib

DOC = pathlib.Path(__file__).resolve().parent.parent / "DESIGN_SYSTEM.md"

# (전경, 배경, 최소 대비, 설명) — 본문 17px 기준이라 버튼 레이블도 4.5:1을 적용한다.
PAIRS = [
    ("on-primary",     "primary",     4.5, "Primary 버튼 레이블"),
    ("on-danger",      "danger",      4.5, "Danger 버튼 레이블"),
    ("on-primary",     "primary-pressed", 4.5, "버튼 pressed 상태"),
    ("primary",        "bg-page",     4.5, "링크"),
    ("primary",        "primary-bg",  4.5, "Secondary 버튼"),
    ("text-primary",   "bg-page",     4.5, "제목·본문"),
    ("text-primary",   "bg-surface",  4.5, "카드 위 본문"),
    ("text-secondary", "bg-page",     4.5, "설명·캡션"),
    ("text-secondary", "bg-surface",  4.5, "카드 위 캡션"),
    ("text-secondary", "bg-fill",     4.5, "입력창 헬퍼 텍스트"),
    ("danger",         "bg-page",     4.5, "오류 텍스트"),
    ("danger",         "danger-bg",   4.5, "오류 배너"),
    ("success",        "bg-page",     4.5, "성공 텍스트"),
    ("warning",        "bg-page",     4.5, "주의 텍스트"),
    ("primary",        "bg-fill",     3.0, "입력창 포커스 보더"),
]


def parse_themes(text):
    """:root / [data-theme="dark"] 블록에서 --토큰: #hex 를 뽑는다."""
    themes = {}
    for name, sel in (("light", r":root"), ("dark", r'\[data-theme="dark"\]')):
        m = re.search(sel + r"\s*\{(.*?)\}", text, re.S)
        if not m:
            sys.exit(f"CSS 블록을 찾지 못했어요: {name}")
        themes[name] = dict(re.findall(r"--([\w-]+):\s*(#[0-9A-Fa-f]{6})", m.group(1)))
    return themes


def luminance(hex_color):
    h = hex_color.lstrip("#")
    ch = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    ch = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in ch]
    return 0.2126 * ch[0] + 0.7152 * ch[1] + 0.0722 * ch[2]


def ratio(fg, bg):
    a, b = luminance(fg), luminance(bg)
    hi, lo = max(a, b), min(a, b)
    return (hi + 0.05) / (lo + 0.05)


def main():
    themes = parse_themes(io.open(DOC, encoding="utf-8").read())
    failed = []
    for mode, tokens in themes.items():
        for fg, bg, need, why in PAIRS:
            missing = [t for t in (fg, bg) if t not in tokens]
            if missing:
                failed.append(f"[{mode}] 토큰 없음: {', '.join(missing)}")
                continue
            got = ratio(tokens[fg], tokens[bg])
            mark = "ok " if got >= need else "FAIL"
            print(f"{mark} [{mode:5}] {fg} / {bg:15} {got:5.2f}:1 (>= {need})  {why}")
            if got < need:
                failed.append(f"[{mode}] {fg}/{bg} {got:.2f}:1 < {need}:1 — {why}")

    if failed:
        print("\n실패 " + str(len(failed)) + "건:")
        for f in failed:
            print("  - " + f)
        sys.exit(1)
    print("\n모든 조합이 AA 기준을 통과했어요.")


if __name__ == "__main__":
    main()
