import os, pathlib

OUT = pathlib.Path(__file__).resolve().parent
OUT.mkdir(parents=True, exist_ok=True)

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
        <marker id="arrow" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"><polygon points="0 0, 8 3, 0 6" fill="{muted}"/></marker>
        <marker id="arrow-accent" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"><polygon points="0 0, 8 3, 0 6" fill="{accent}"/></marker>
        <marker id="arrow-link" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"><polygon points="0 0, 8 3, 0 6" fill="{link}"/></marker>
      </defs>
"""

def label(x_mid, y_line, text, w, t, side="above", gap=8, color="{soft}"):
    """Arrow label with mask. side=above -> mask sits above the horizontal line."""
    if side == "above":
        mask_y = y_line - gap - 12
        return (f'      <rect x="{x_mid - w//2}" y="{mask_y}" width="{w}" height="12" rx="2" fill="{{paper}}"/>\n'
                f'      <text x="{x_mid}" y="{mask_y + 9}" fill="{color}" font-size="8" '
                f'font-family="\'Geist Mono\', monospace" text-anchor="middle" letter-spacing="0.06em">{text}</text>\n')
    raise ValueError

# ---------------------------------------------------------------- diagram 1
D1_SVG = """    <svg viewBox="0 0 960 660" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="gsi-feedback-loop{v}-title gsi-feedback-loop{v}-desc">
      <title id="gsi-feedback-loop{v}-title">Where a wrong GSI name gets caught</title>
      <desc id="gsi-feedback-loop{v}-desc">A flowchart comparing two ways to run a new DynamoDB index query: against a local emulator, where a wrong index name surfaces in seconds before anything is deployed, and directly in AWS, where the same error costs a full pipeline run and forces a rework loop back through the pull request.</desc>
""" + DEFS + """
      <rect width="100%" height="100%" fill="{paper}"/>

      <!-- arrows -->
      <line x1="480" y1="80" x2="480" y2="124" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow)"/>
      <path d="M 384,164 H 228 Q 220,164 220,172 V 256" fill="none" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow)"/>
      <path d="M 576,164 H 732 Q 740,164 740,172 V 256" fill="none" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow)"/>
      <line x1="220" y1="316" x2="220" y2="380" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow)"/>
      <line x1="220" y1="440" x2="220" y2="504" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow)"/>
      <line x1="740" y1="316" x2="740" y2="380" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow)"/>
      <line x1="740" y1="440" x2="740" y2="504" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow)"/>
      <path d="M 630,534 H 598 Q 590,534 590,526 V 294 Q 590,286 598,286 H 630" fill="none" stroke="{accent}" stroke-width="1.5" marker-end="url(#arrow-accent)"/>

      <!-- arrow labels -->
      <rect x="286" y="144" width="40" height="12" rx="2" fill="{paper}"/>
      <text x="306" y="153" fill="{soft}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">LOCAL</text>
      <rect x="632" y="144" width="44" height="12" rx="2" fill="{paper}"/>
      <text x="654" y="153" fill="{soft}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">CLOUD</text>
      <rect x="538" y="404" width="44" height="12" rx="2" fill="{paper}"/>
      <text x="560" y="413" fill="{accent}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">REWORK</text>

      <!-- start -->
      <rect x="360" y="40" width="240" height="40" rx="20" fill="{paper}"/>
      <rect x="360" y="40" width="240" height="40" rx="20" fill="{paper}" stroke="{ink}" stroke-width="1"/>
      <text x="480" y="65" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">A query needs a new GSI</text>

      <!-- decision -->
      <polygon points="480,124 576,164 480,204 384,164" fill="{paper}"/>
      <polygon points="480,124 576,164 480,204 384,164" fill="{paper}" stroke="{ink}" stroke-width="1"/>
      <text x="480" y="160" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">Where does it</text>
      <text x="480" y="176" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">run first?</text>

      <!-- local lane -->
      <rect x="110" y="256" width="220" height="60" rx="6" fill="{paper}"/>
      <rect x="110" y="256" width="220" height="60" rx="6" fill="{paper}" stroke="{ink}" stroke-width="1"/>
      <text x="220" y="282" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">Emulator container</text>
      <text x="220" y="300" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">localhost:4566</text>

      <rect x="110" y="380" width="220" height="60" rx="6" fill="{paper}"/>
      <rect x="110" y="380" width="220" height="60" rx="6" fill="{paper}" stroke="{ink}" stroke-width="1"/>
      <text x="220" y="406" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">ValidationException</text>
      <text x="220" y="424" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">~2s &#183; nothing deployed</text>

      <rect x="100" y="504" width="240" height="56" rx="28" fill="{paper}"/>
      <rect x="100" y="504" width="240" height="56" rx="28" fill="{paper}" stroke="{ink}" stroke-width="1"/>
      <text x="220" y="536" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">Fixed before the PR</text>

      <!-- cloud lane -->
      <rect x="630" y="256" width="220" height="60" rx="6" fill="{paper}"/>
      <rect x="630" y="256" width="220" height="60" rx="6" fill="{paper}" stroke="{ink}" stroke-width="1"/>
      <text x="740" y="282" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">PR + terraform apply</text>
      <text x="740" y="300" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">ci pipeline</text>

      <rect x="630" y="380" width="220" height="60" rx="6" fill="{paper}"/>
      <rect x="630" y="380" width="220" height="60" rx="6" fill="{paper}" stroke="{ink}" stroke-width="1"/>
      <text x="740" y="406" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">Deploy app, run query</text>
      <text x="740" y="424" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">cd pipeline</text>

      <rect x="630" y="504" width="220" height="60" rx="6" fill="{paper}"/>
      <rect x="630" y="504" width="220" height="60" rx="6" fill="{accent_tint}" stroke="{accent}" stroke-width="1"/>
      <text x="740" y="530" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">ValidationException</text>
      <text x="740" y="548" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">~14min &#183; 2 deploys</text>

      <!-- legend -->
      <line x1="30" y1="604" x2="930" y2="604" stroke="{rule}" stroke-width="0.8"/>
      <text x="30" y="621" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace" letter-spacing="0.14em">LEGEND</text>
      <rect x="150" y="612" width="24" height="10" rx="5" fill="none" stroke="{ink}" stroke-width="1"/>
      <text x="182" y="621" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Start / end</text>
      <rect x="310" y="612" width="24" height="10" rx="2" fill="none" stroke="{ink}" stroke-width="1"/>
      <text x="342" y="621" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Step</text>
      <polygon points="482,611 493,620 482,629 471,620" fill="none" stroke="{ink}" stroke-width="1"/>
      <text x="502" y="621" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Decision</text>
      <line x1="630" y1="620" x2="654" y2="620" stroke="{accent}" stroke-width="1.5"/>
      <text x="662" y="621" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Rework loop</text>
    </svg>
"""

# ---------------------------------------------------------------- diagram 2
D2_SVG = """    <svg viewBox="0 0 960 660" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="emulated-slice{v}-title emulated-slice{v}-desc">
      <title id="emulated-slice{v}-title">The event-driven slice, emulated locally</title>
      <desc id="emulated-slice{v}-desc">An architecture diagram showing a queue, a Lambda consumer and a DynamoDB table with a global secondary index running inside a single LocalStack container on port 4566, provisioned by Terraform through tflocal and exercised end to end by an integration test that publishes through the application and then asserts against the index.</desc>
""" + DEFS + """
      <rect width="100%" height="100%" fill="{paper}"/>

      <!-- boundary zone -->
      <rect x="300" y="192" width="620" height="136" rx="8" fill="{accent_05}" stroke="{accent_50}" stroke-width="1" stroke-dasharray="4,4"/>
      <rect x="316" y="196" width="168" height="12" rx="2" fill="{paper}"/>
      <text x="400" y="205" fill="{accent}" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.14em">LOCALSTACK &#183; localhost:4566</text>

      <!-- arrows -->
      <line x1="220" y1="264" x2="320" y2="264" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow)"/>
      <line x1="470" y1="264" x2="535" y2="264" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow)"/>
      <line x1="685" y1="264" x2="750" y2="264" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow)"/>
      <line x1="825" y1="136" x2="825" y2="224" stroke="{muted}" stroke-width="1" stroke-dasharray="4,3" marker-end="url(#arrow)"/>
      <line x1="140" y1="440" x2="140" y2="304" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow)"/>
      <path d="M 220,480 H 817 Q 825,480 825,472 V 304" fill="none" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow)"/>

      <!-- arrow labels -->
      <rect x="244" y="244" width="52" height="12" rx="2" fill="{paper}"/>
      <text x="270" y="253" fill="{soft}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">PUBLISH</text>
      <rect x="484" y="244" width="38" height="12" rx="2" fill="{paper}"/>
      <text x="503" y="253" fill="{soft}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">EVENT</text>
      <rect x="699" y="244" width="38" height="12" rx="2" fill="{paper}"/>
      <text x="718" y="253" fill="{soft}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">WRITE</text>
      <rect x="833" y="168" width="38" height="12" rx="2" fill="{paper}"/>
      <text x="852" y="177" fill="{soft}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">APPLY</text>
      <rect x="148" y="366" width="66" height="12" rx="2" fill="{paper}"/>
      <text x="181" y="375" fill="{soft}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">POST /ORDERS</text>
      <rect x="486" y="460" width="64" height="12" rx="2" fill="{paper}"/>
      <text x="518" y="469" fill="{soft}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">QUERY GSI</text>

      <!-- nodes -->
      <rect x="60" y="224" width="160" height="80" rx="6" fill="{paper}"/>
      <rect x="60" y="224" width="160" height="80" rx="6" fill="{paper}" stroke="{ink}" stroke-width="1"/>
      <rect x="68" y="230" width="28" height="12" rx="2" fill="none" stroke="{ink040}" stroke-width="0.8"/>
      <text x="82" y="239" fill="{muted}" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.08em">APP</text>
      <text x="140" y="272" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">Order API</text>
      <text x="140" y="290" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">endpoint :4566</text>

      <rect x="320" y="224" width="150" height="80" rx="6" fill="{paper}"/>
      <rect x="320" y="224" width="150" height="80" rx="6" fill="{paper}" stroke="{ink}" stroke-width="1"/>
      <rect x="328" y="230" width="28" height="12" rx="2" fill="none" stroke="{ink040}" stroke-width="0.8"/>
      <text x="342" y="239" fill="{muted}" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.08em">SQS</text>
      <text x="395" y="272" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">orders-events</text>
      <text x="395" y="290" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">queue</text>

      <rect x="535" y="224" width="150" height="80" rx="6" fill="{paper}"/>
      <rect x="535" y="224" width="150" height="80" rx="6" fill="{paper}" stroke="{ink}" stroke-width="1"/>
      <rect x="543" y="230" width="42" height="12" rx="2" fill="none" stroke="{ink040}" stroke-width="0.8"/>
      <text x="564" y="239" fill="{muted}" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.08em">LAMBDA</text>
      <text x="610" y="272" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">orders-projector</text>
      <text x="610" y="290" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">consumer</text>

      <rect x="750" y="224" width="150" height="80" rx="6" fill="{paper}"/>
      <rect x="750" y="224" width="150" height="80" rx="6" fill="{ink005}" stroke="{muted}" stroke-width="1"/>
      <rect x="758" y="230" width="28" height="12" rx="2" fill="none" stroke="{ink040}" stroke-width="0.8"/>
      <text x="772" y="239" fill="{muted}" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.08em">DDB</text>
      <text x="825" y="272" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">orders</text>
      <text x="825" y="290" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">gsi_status_created_at</text>

      <rect x="750" y="64" width="150" height="72" rx="6" fill="{paper}"/>
      <rect x="750" y="64" width="150" height="72" rx="6" fill="{ink003}" stroke="{ink030}" stroke-width="1"/>
      <rect x="758" y="70" width="28" height="12" rx="2" fill="none" stroke="{ink040}" stroke-width="0.8"/>
      <text x="772" y="79" fill="{muted}" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.08em">IAC</text>
      <text x="825" y="108" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">Terraform</text>
      <text x="825" y="126" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">tflocal apply</text>

      <rect x="60" y="440" width="160" height="80" rx="6" fill="{paper}"/>
      <rect x="60" y="440" width="160" height="80" rx="6" fill="{muted010}" stroke="{soft}" stroke-width="1"/>
      <rect x="68" y="446" width="32" height="12" rx="2" fill="none" stroke="{ink040}" stroke-width="0.8"/>
      <text x="84" y="455" fill="{muted}" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.08em">TEST</text>
      <text x="140" y="488" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">Integration test</text>
      <text x="140" y="506" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">vitest run</text>

      <!-- legend -->
      <line x1="30" y1="604" x2="930" y2="604" stroke="{rule}" stroke-width="0.8"/>
      <text x="30" y="621" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace" letter-spacing="0.14em">LEGEND</text>
      <rect x="150" y="612" width="24" height="10" rx="2" fill="{accent_05}" stroke="{accent_50}" stroke-width="1" stroke-dasharray="4,4"/>
      <text x="182" y="621" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Emulated locally</text>
      <line x1="370" y1="617" x2="392" y2="617" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow)"/>
      <text x="402" y="621" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Runtime call</text>
      <line x1="580" y1="617" x2="602" y2="617" stroke="{muted}" stroke-width="1" stroke-dasharray="4,3" marker-end="url(#arrow)"/>
      <text x="612" y="621" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Provisioning</text>
    </svg>
"""

# ---------------------------------------------------------------- diagram 3
D3_SVG = """    <svg viewBox="0 0 960 470" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="confidence-ladder{v}-title confidence-ladder{v}-desc">
      <title id="confidence-ladder{v}-title">What each test layer can and cannot see</title>
      <desc id="confidence-ladder{v}-desc">A four-layer stack ordered from fast and free at the bottom to slow and public at the top: unit tests prove business rules but check no AWS contract, the local emulator proves wiring, index names and key schema but is blind to IAM, quotas and index backfill, an ephemeral AWS stack proves the parts the emulator cannot at the cost of minutes and money, and production exposes whatever is left in front of users.</desc>
""" + DEFS + """
      <rect width="100%" height="100%" fill="{paper}"/>

      <!-- direction indicator -->
      <line x1="72" y1="372" x2="72" y2="108" stroke="{soft}" stroke-width="1" marker-end="url(#arrow)"/>
      <text x="72" y="90" fill="{soft}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.1em">SLOWER, COSTLIER</text>
      <text x="72" y="394" fill="{soft}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.1em">FASTER, FREE</text>

      <!-- stack -->
      <rect x="120" y="100" width="780" height="272" rx="6" fill="{paper}"/>
      <rect x="120" y="100" width="780" height="272" rx="6" fill="{paper}" stroke="{ink}" stroke-width="1"/>
      <line x1="120" y1="168" x2="900" y2="168" stroke="{rule}" stroke-width="1"/>
      <line x1="120" y1="236" x2="900" y2="236" stroke="{rule}" stroke-width="1"/>
      <line x1="120" y1="304" x2="900" y2="304" stroke="{rule}" stroke-width="1"/>
      <rect x="120" y="236" width="780" height="68" fill="{accent_tint}" stroke="{accent}" stroke-width="1"/>

      <text x="140" y="138" fill="{soft}" font-size="9" font-family="'Geist Mono', monospace" letter-spacing="0.14em">04</text>
      <text x="190" y="129" fill="{ink}" font-size="14" font-weight="600" font-family="'Geist', sans-serif">Production</text>
      <text x="190" y="147" fill="{muted}" font-size="10" font-family="'Geist', sans-serif">the only environment that proves everything</text>
      <text x="884" y="138" fill="{soft}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="end">failures are public</text>

      <text x="140" y="206" fill="{soft}" font-size="9" font-family="'Geist Mono', monospace" letter-spacing="0.14em">03</text>
      <text x="190" y="197" fill="{ink}" font-size="14" font-weight="600" font-family="'Geist', sans-serif">Ephemeral AWS stack</text>
      <text x="190" y="215" fill="{muted}" font-size="10" font-family="'Geist', sans-serif">real IAM, real quotas, real index backfill</text>
      <text x="884" y="206" fill="{soft}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="end">minutes per run, real money</text>

      <text x="140" y="274" fill="{accent}" font-size="9" font-family="'Geist Mono', monospace" letter-spacing="0.14em">02</text>
      <text x="190" y="265" fill="{ink}" font-size="14" font-weight="600" font-family="'Geist', sans-serif">Local emulator</text>
      <text x="190" y="283" fill="{muted}" font-size="10" font-family="'Geist', sans-serif">wiring, index names, key schema, payload shape</text>
      <text x="884" y="274" fill="{ink}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="end">blind to: IAM, quotas, backfill</text>

      <text x="140" y="342" fill="{soft}" font-size="9" font-family="'Geist Mono', monospace" letter-spacing="0.14em">01</text>
      <text x="190" y="333" fill="{ink}" font-size="14" font-weight="600" font-family="'Geist', sans-serif">Unit tests</text>
      <text x="190" y="351" fill="{muted}" font-size="10" font-family="'Geist', sans-serif">business rules against a fake, no network</text>
      <text x="884" y="342" fill="{soft}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="end">blind to: every AWS contract</text>
    </svg>
"""

DIAGRAMS = [
    ("01-feedback-loop", "Flowchart &#183; Diagram Design", "Where a wrong GSI name gets caught", D1_SVG),
    ("02-emulated-slice", "Architecture &#183; Diagram Design", "The event-driven slice, emulated locally", D2_SVG),
    ("03-confidence-ladder", "Layer stack &#183; Diagram Design", "What each test layer can and cannot see", D3_SVG),
]

for slug, eyebrow, title, svg_tpl in DIAGRAMS:
    for variant, tokens in (("light", LIGHT), ("dark", DARK)):
        v = "" if variant == "light" else "-dark"
        svg = svg_tpl.replace("{v}", v).format(**tokens)
        html = SHELL.format(page_title=title, eyebrow=eyebrow, svg=svg, **tokens)
        (OUT / f"{slug}-{variant}.html").write_text(html)
        print("wrote", slug, variant)
