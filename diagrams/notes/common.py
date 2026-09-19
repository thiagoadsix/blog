import pathlib

OUT = pathlib.Path(__file__).resolve().parent

LIGHT = dict(
    paper="#ffffff", paper2="#f6f6f7", ink="#18181b", muted="#7b7b85", soft="#9a9aa3",
    rule="rgba(24,24,27,0.12)", rule_solid="#e3e3e8",
    accent="#ee2b2b", accent_tint="rgba(238,43,43,0.08)", accent_50="rgba(238,43,43,0.50)",
    accent_05="rgba(238,43,43,0.05)", link="#2f6fd0",
    ink002="rgba(24,24,27,0.02)", ink003="rgba(24,24,27,0.03)", ink005="rgba(24,24,27,0.05)",
    ink010="rgba(24,24,27,0.10)", ink030="rgba(24,24,27,0.30)", ink040="rgba(24,24,27,0.40)",
    muted010="rgba(123,123,133,0.10)",
)

DARK = dict(
    paper="#0a0a0b", paper2="#141416", ink="#fafafa", muted="#a1a1ab", soft="#8b8b95",
    rule="rgba(250,250,250,0.12)", rule_solid="rgba(227,227,232,0.22)",
    accent="#ff5a5a", accent_tint="rgba(255,90,90,0.12)", accent_50="rgba(255,90,90,0.50)",
    accent_05="rgba(255,90,90,0.07)", link="#7aa7ec",
    ink002="rgba(250,250,250,0.02)", ink003="rgba(250,250,250,0.03)", ink005="rgba(250,250,250,0.05)",
    ink010="rgba(250,250,250,0.10)", ink030="rgba(250,250,250,0.30)", ink040="rgba(250,250,250,0.40)",
    muted010="rgba(161,161,171,0.12)",
)

SHELL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{page_title}</title>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>
  *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
  :root {{
    --color-paper: {paper};
    --color-ink: {ink};
    --color-muted: {muted};
    --color-accent: {accent};
    --font-sans: 'Geist', system-ui, sans-serif;
    --font-serif: 'Instrument Serif', serif;
    --font-mono: 'Geist Mono', ui-monospace, monospace;
  }}
  body {{
    font-family: var(--font-sans);
    background: var(--color-paper);
    color: var(--color-ink);
    min-height: 100vh;
    display: flex; align-items: center; justify-content: center;
    padding: 3rem 2rem;
  }}
  .frame {{ max-width: 1200px; width: 100%; }}
  .eyebrow {{
    font-family: var(--font-mono); font-size: 0.66rem; font-weight: 500;
    letter-spacing: 0.18em; text-transform: uppercase; color: var(--color-muted);
    margin-bottom: 0.5rem;
  }}
  h1 {{
    font-family: var(--font-serif);
    font-size: clamp(1.5rem, 2.4vw + 0.75rem, 2rem);
    font-weight: 400; letter-spacing: -0.02em; line-height: 1.15;
    color: var(--color-ink); margin-bottom: 1.5rem;
  }}
  svg {{ width: 100%; min-width: 900px; display: block; }}
</style>
</head>
<body>
  <div class="frame">
    <p class="eyebrow">{eyebrow}</p>
    <h1>{page_title}</h1>
{svg}
  </div>
</body>
</html>
"""

DEFS = """      <defs>
        <marker id="arrow{v}" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"><polygon points="0 0, 8 3, 0 6" fill="{muted}"/></marker>
        <marker id="arrow-accent{v}" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"><polygon points="0 0, 8 3, 0 6" fill="{accent}"/></marker>
        <marker id="arrow-link{v}" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"><polygon points="0 0, 8 3, 0 6" fill="{link}"/></marker>
      </defs>
"""


def render_all(diagrams):
    """diagrams: iterable of (slug, eyebrow, page_title, svg_template).

    The template may use {v} for the per-variant id suffix and any token name
    from LIGHT / DARK as a format field.
    """
    for slug, eyebrow, title, svg_tpl in diagrams:
        for variant, tokens in (("light", LIGHT), ("dark", DARK)):
            v = "" if variant == "light" else "-dark"
            svg = svg_tpl.replace("{v}", v).format(**tokens)
            html = SHELL.format(page_title=title, eyebrow=eyebrow, svg=svg, **tokens)
            (OUT / f"{slug}-{variant}.html").write_text(html)
            print("wrote", slug, variant)
