#!/usr/bin/env python3
"""Builds the animated SVGs in assets/. Run from the repo root.
Update scripts/calendar.json first to refresh the contribution city."""
import json, math

FONT = "-apple-system,'Segoe UI',Roboto,Helvetica,Arial,sans-serif"
THEMES = {
    "dark": dict(bg="#0d1022", panel="#161b2e", line="#2b3150", text="#f4f5fb", sub="#b6bad0",
                 a1="#4f8ff7", a2="#3fd0e0", rec="#ff5470", tile="#1c2238",
                 tops=["#2b5fb8", "#3f8ee8", "#3fd0e0", "#8cf2f5"], sides=["#1d3f7c", "#2a609e", "#268e9c", "#55b4ba"], sides2=["#16305e", "#1f4778", "#1c6b76", "#3f8a8f"]),
    "light": dict(bg="#f3f6ff", panel="#ffffff", line="#d5deef", text="#14172b", sub="#4a4f68",
                  a1="#2f6fe0", a2="#0b8ea1", rec="#e0284f", tile="#e1e8f6",
                  tops=["#8fb6f5", "#4f8ff7", "#17a9bd", "#0b7f90"], sides=["#6d97db", "#3572d6", "#10899a", "#086472"], sides2=["#587fc0", "#2a5fb8", "#0c6e7c", "#064f5a"]),
}
REDUCE = "@media (prefers-reduced-motion:reduce){*{animation:none!important}}"

def svg(w, h, label, css, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="{label}">'
            f'<style>text{{font-family:{FONT}}}{css}{REDUCE}</style>{body}</svg>')

def hero(t):
    P = 12
    perf = lambda y: "".join(f'<rect x="{x}" y="{y}" width="26" height="16" rx="4" fill="{t["line"]}"/>' for x in range(-48, 1248, 48))
    css = (f".film{{animation:film 3s linear infinite}}@keyframes film{{to{{transform:translateX(48px)}}}}"
           f".rec{{animation:rec 1.4s steps(2,jump-none) infinite}}@keyframes rec{{from{{opacity:1}}to{{opacity:.2}}}}"
           f".wipe{{transform:translateX(1160px);animation:wipe {P}s cubic-bezier(.6,0,.3,1) infinite both}}"
           f"@keyframes wipe{{0%,4%{{transform:translateX(0)}}24%,100%{{transform:translateX(1160px)}}}}"
           f".cut{{opacity:0;transform:translateX(1160px);animation:cut {P}s cubic-bezier(.6,0,.3,1) infinite both}}"
           f"@keyframes cut{{0%,4%{{transform:translateX(0);opacity:1}}24%{{transform:translateX(1160px);opacity:1}}25%,100%{{transform:translateX(1160px);opacity:0}}}}"
           f".tag{{animation:tag {P}s ease infinite both}}@keyframes tag{{0%,22%{{opacity:0;transform:translateY(14px)}}32%,100%{{opacity:1;transform:none}}}}"
           f".fill{{transform-box:fill-box;transform-origin:left;animation:fill {P}s linear infinite both}}@keyframes fill{{from{{transform:scaleX(0)}}to{{transform:scaleX(1)}}}}"
           f".head{{animation:head {P}s linear infinite both}}@keyframes head{{from{{transform:translateX(0)}}to{{transform:translateX(1060px)}}}}")
    clips = [(70, 340, "CODE"), (416, 340, "CREATE"), (762, 368, "SHIP")]
    rail = "".join(f'<rect x="{x}" y="296" width="{w}" height="44" rx="8" fill="{t["panel"]}" stroke="{t["line"]}"/>'
                   f'<text x="{x+18}" y="327" font-size="25" font-weight="600" letter-spacing="2" fill="{t["sub"]}">{n}</text>' for x, w, n in clips)
    body = (f'<defs><linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="{t["a1"]}"/><stop offset="1" stop-color="{t["a2"]}"/></linearGradient>'
            f'<clipPath id="c"><rect width="1200" height="400" rx="20"/></clipPath></defs><g clip-path="url(#c)">'
            f'<rect width="1200" height="400" fill="{t["bg"]}"/>'
            f'<g class="film">{perf(12)}</g><g class="film">{perf(372)}</g>'
            f'<circle class="rec" cx="1064" cy="70" r="11" fill="{t["rec"]}"/><text x="1084" y="81" font-size="30" font-weight="700" fill="{t["text"]}">REC</text>'
            f'<text x="70" y="172" font-size="108" font-weight="800" fill="{t["text"]}">Haleem Rafat</text>'
            f'<rect class="wipe" x="60" y="70" width="980" height="130" fill="{t["bg"]}"/><rect class="cut" x="58" y="70" width="5" height="130" fill="{t["a2"]}"/>'
            f'<text class="tag" x="70" y="245" font-size="42" fill="{t["sub"]}">Senior Front-end Engineer · Egypt</text>'
            f'{rail}<rect class="fill" x="70" y="346" width="1060" height="6" rx="3" fill="url(#g)"/>'
            f'<g class="head"><rect x="68" y="284" width="4" height="72" fill="{t["a2"]}"/><path d="M60 280h20v10l-10 10-10-10z" fill="{t["a2"]}"/></g></g>')
    return svg(1200, 400, "Haleem Rafat, Senior Front-end Engineer, Egypt", css, body)

def stats(t):
    P = 12
    H = 72
    items = [("4+", "years of front-end work"), ("2,352", "GitHub contributions in 2026"), ("4.2K", "YouTube subscribers"), ("51", "YouTube videos")]
    adv = {",": 19, ".": 19, "+": 40, "K": 44}
    css = (f".r{{transform:translateY(var(--y));animation:r {P}s cubic-bezier(.2,.8,.2,1) infinite both;animation-delay:var(--d)}}"
           f"@keyframes r{{0%{{transform:translateY(0)}}16%,100%{{transform:translateY(var(--y))}}}}")
    out = []
    for i, (num, label) in enumerate(items):
        x, y = (i % 2) * 408, (i // 2) * 164
        out.append(f'<rect x="{x+1}" y="{y+1}" width="390" height="154" rx="16" fill="{t["panel"]}" stroke="{t["line"]}"/>')
        cx, seq = x + 30, 0
        for ch in num:
            if ch.isdigit():
                d = int(ch)
                col = "".join(f'<text x="0" y="{58 + n*H}" font-size="64" font-weight="800" fill="{t["a1"]}">{n % 10}</text>' for n in range(20))
                out.append(f'<svg x="{cx}" y="{y+20}" width="38" height="{H}"><g class="r" style="--y:-{(10+d)*H}px;--d:{seq*.12:.2f}s">{col}</g></svg>')
                cx += 37; seq += 1
            else:
                out.append(f'<text x="{cx}" y="{y+78}" font-size="64" font-weight="800" fill="{t["a1"]}">{ch}</text>')
                cx += adv[ch]
        out.append(f'<text x="{x+30}" y="{y+126}" font-size="25" fill="{t["sub"]}">{label}</text>')
    return svg(800, 320, ", ".join(f"{n} {l}" for n, l in items), css, "".join(out))

def timeline(t):
    P = 14
    X0, PPY = 24, 150
    px = lambda yr, m: X0 + (yr - 2022 + (m - 1) / 12) * PPY
    now = px(2026, 11.2)
    rows = [("Spiritude", 2022, 4, 2024, 10, 0), ("Axis Pay", 2024, 10, 2026, 11.2, 0),
            ("Trading Dashboard", 2026, 4, 2026, 11.2, 1), ("Framecast", 2026, 8, 2026, 11.2, 1),
            ("AI Video Studio", 2026, 10, 2026, 11.2, 1), ("Zaffa", 2026, 10, 2026, 11.2, 1), ("Kleano", 2026, 10, 2026, 11.2, 1)]
    SWEEP = 62
    frac = lambda x: (x - X0) / (now - X0) * SWEEP
    css = [f".ph{{transform:translateX({now - X0:.0f}px);animation:ph {P}s linear infinite both}}@keyframes ph{{0%{{transform:none}}{SWEEP}%,100%{{transform:translateX({now - X0:.0f}px)}}}}",
           ".c{transform-box:fill-box;transform-origin:left}"]
    grid, body = [], []
    for yr in range(2022, 2027):
        x = px(yr, 1)
        grid.append(f'<line x1="{x}" y1="42" x2="{x}" y2="356" stroke="{t["line"]}"/><text x="{x+6}" y="30" font-size="24" fill="{t["sub"]}">{yr}</text>')
    for i, (name, y1, m1, y2, m2, kind) in enumerate(rows):
        a, b = px(y1, m1), px(y2, m2)
        y = 52 + i * 43
        s, e = frac(a), frac(b)
        css.append(f"@keyframes c{i}{{0%,{s:.1f}%{{transform:scaleX(0)}}{e:.1f}%,100%{{transform:scaleX(1)}}}}@keyframes l{i}{{0%,{s:.1f}%{{opacity:0}}{s+3:.1f}%,100%{{opacity:1}}}}")
        anim = f'style="animation:c{i} {P}s linear infinite both"'
        lanim = f'style="animation:l{i} {P}s linear infinite both"'
        fill = t["a1"] if kind == 0 else t["a2"]
        body.append(f'<rect class="c" x="{a:.1f}" y="{y}" width="{b-a:.1f}" height="34" rx="7" fill="{fill}" {anim}/>')
        if b - a > 200:
            body.append(f'<text x="{a+12:.1f}" y="{y+25}" font-size="23" font-weight="700" fill="#fff" {lanim}>{name}</text>')
        else:
            body.append(f'<text x="{a-10:.1f}" y="{y+25}" font-size="23" font-weight="600" text-anchor="end" fill="{t["text"]}" {lanim}>{name}</text>')
    head = (f'<g class="ph"><rect x="{X0-1.5}" y="42" width="3" height="314" fill="{t["rec"]}"/><path d="M{X0-9} 38h18v9l-9 9-9-9z" fill="{t["rec"]}"/></g>')
    return svg(800, 362, "Career timeline: Spiritude from April 2022 to October 2024, Axis Pay from October 2024 to now, then Trading Dashboard, Framecast, AI Video Studio, Zaffa and Kleano in 2026", "".join(css), "".join(grid + body) + head)

def pipeline(t):
    P = 10
    stages = ["Script", "Narration", "Footage", "Render", "Metadata", "Thumbnail", "Shorts", "Upload"]
    css, out = [], []
    for i, s in enumerate(stages):
        x, y = (i % 4) * 202, (i // 4) * 80
        on = 3 + i * 8
        css.append(f"@keyframes p{i}{{0%,{on}%{{opacity:0}}{on+3}%,92%{{opacity:1}}97%,100%{{opacity:0}}}}")
        out.append(f'<rect x="{x+1}" y="{y+1}" width="190" height="68" rx="12" fill="{t["panel"]}" stroke="{t["line"]}"/>'
                   f'<g style="animation:p{i} {P}s ease infinite both"><rect x="{x+1}" y="{y+1}" width="190" height="68" rx="12" fill="{t["a1"]}" fill-opacity=".16" stroke="{t["a2"]}" stroke-width="2.5"/>'
                   f'<path d="M{x+160} {y+36}l7 7 13-15" fill="none" stroke="{t["a2"]}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/></g>'
                   f'<text x="{x+18}" y="{y+44}" font-size="24" font-weight="600" fill="{t["text"]}">{s}</text>')
    return svg(800, 152, "Framecast stages: " + ", ".join(stages), "".join(css), "".join(out))

def city(t):
    P = 16
    cal = json.load(open("scripts/calendar.json"))["data"]["user"]["contributionsCollection"]["contributionCalendar"]
    weeks = cal["weeks"]
    total = cal["totalContributions"]
    days = [(wi, d["weekday"], d["contributionCount"]) for wi, w in enumerate(weeks) for d in w["contributionDays"]]
    all_c = [c for _, _, c in days]
    peak, active = max(all_c), sum(1 for c in all_c if c)
    best = cur = 0
    for c in all_c:
        cur = cur + 1 if c else 0
        best = max(best, cur)
    TW, TH = 13, 6.5
    OX, OY = 150, 150
    css = [f".b{{animation:b {P}s cubic-bezier(.3,1.3,.5,1) infinite both}}@keyframes b{{0%{{transform:scaleY(0)}}7%,90%{{transform:scaleY(1)}}98%,100%{{transform:scaleY(0)}}}}"]
    css += [f".w{w}{{animation-delay:{w*.07:.2f}s}}" for w in range(len(weeks))]
    out = []
    for w, d, c in sorted(days, key=lambda r: (r[0] + r[1], r[0])):
        x, y = OX + (w - d) * TW, OY + (w + d) * TH
        base = f"M0 0l{TW} {TH}l-{TW} {TH}l-{TW} -{TH}z"
        if not c:
            out.append(f'<path transform="translate({x:g} {y:g})" d="{base}" fill="{t["tile"]}"/>')
            continue
        lvl = min(3, int(math.sqrt(c / peak) * 4))
        h = round(5 + math.sqrt(c / peak) * 118)
        by = y + 2 * TH  # front corner is the scale origin line
        out.append(f'<g transform="translate({x:g} {by:g})"><g class="b w{w}">'
                   f'<path d="M0 0l-{TW} -{TH}v-{h}l{TW} {TH}z" fill="{t["sides"][lvl]}"/>'
                   f'<path d="M0 0l{TW} -{TH}v-{h}l-{TW} {TH}z" fill="{t["sides2"][lvl]}"/>'
                   f'<path d="M0 -{h}l{TW} -{TH}l-{TW} -{TH}l-{TW} {TH}z" fill="{t["tops"][lvl]}"/></g></g>')
    text = (f'<text x="780" y="62" text-anchor="end" font-size="60" font-weight="800" fill="{t["a1"]}">{total:,}</text>'
            f'<text x="780" y="98" text-anchor="end" font-size="26" fill="{t["sub"]}">contributions in 2026</text>'
            f'<text x="24" y="412" font-size="26" fill="{t["sub"]}"><tspan font-weight="700" fill="{t["text"]}">{peak}</tspan> on the biggest day</text>'
            f'<text x="24" y="448" font-size="26" fill="{t["sub"]}"><tspan font-weight="700" fill="{t["text"]}">{active}</tspan> active days</text>'
            f'<text x="24" y="484" font-size="26" fill="{t["sub"]}"><tspan font-weight="700" fill="{t["text"]}">{best}</tspan>-day best streak</text>')
    return svg(800, 500, f"3D city of {total} GitHub contributions in 2026, with one building per active day", "".join(css), "".join(out) + text)

for name, fn in [("hero", hero), ("stats", stats), ("timeline", timeline), ("pipeline", pipeline), ("city", city)]:
    for th, t in THEMES.items():
        open(f"assets/{name}-{th}.svg", "w", encoding="utf8").write(fn(t))
