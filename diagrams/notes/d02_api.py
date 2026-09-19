from common import DEFS, render_all

SVG_A = """    <svg viewBox="0 0 960 672" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="pagination{v}-title pagination{v}-desc">
      <title id="pagination{v}-title">Why cursor pagination survives page 500</title>
      <desc id="pagination{v}-desc">Two ways to fetch page 501 of the same index. The offset query walks and throws away the first ten thousand rows before it reaches the twenty it returns, so every page costs more than the last. The keyset cursor seeks straight to the last row it saw, reads only those twenty rows, and stays anchored when a new row is inserted between page loads.</desc>
""" + DEFS + """
      <rect width="100%" height="100%" fill="{paper}"/>

      <!-- band dividers -->
      <line x1="32" y1="200" x2="928" y2="200" stroke="{rule}" stroke-width="0.8"/>
      <line x1="32" y1="400" x2="928" y2="400" stroke="{rule}" stroke-width="0.8"/>

      <!-- arrows first -->
      <line x1="320" y1="140" x2="760" y2="140" stroke="{accent}" stroke-width="1.5" marker-end="url(#arrow-accent{v})"/>
      <line x1="800" y1="356" x2="800" y2="306" stroke="{ink}" stroke-width="1.5" marker-end="url(#arrow{v})"/>

      <!-- arrow labels -->
      <rect x="492" y="120" width="96" height="12" rx="2" fill="{paper}"/>
      <text x="540" y="129" fill="{accent}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">WALK + DISCARD</text>

      <rect x="812" y="320" width="40" height="12" rx="2" fill="{paper}"/>
      <text x="832" y="329" fill="{ink}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">SEEK</text>

      <!-- band 01 index strip -->
      <rect x="320" y="72" width="436" height="44" rx="6" fill="{accent_tint}" stroke="{accent_50}" stroke-width="1"/>
      <line x1="340" y1="80" x2="340" y2="108" stroke="{accent_50}" stroke-width="0.8"/>
      <line x1="372" y1="80" x2="372" y2="108" stroke="{accent_50}" stroke-width="0.8"/>
      <line x1="404" y1="80" x2="404" y2="108" stroke="{accent_50}" stroke-width="0.8"/>
      <line x1="436" y1="80" x2="436" y2="108" stroke="{accent_50}" stroke-width="0.8"/>
      <line x1="468" y1="80" x2="468" y2="108" stroke="{accent_50}" stroke-width="0.8"/>
      <line x1="500" y1="80" x2="500" y2="108" stroke="{accent_50}" stroke-width="0.8"/>
      <line x1="532" y1="80" x2="532" y2="108" stroke="{accent_50}" stroke-width="0.8"/>
      <line x1="564" y1="80" x2="564" y2="108" stroke="{accent_50}" stroke-width="0.8"/>
      <line x1="596" y1="80" x2="596" y2="108" stroke="{accent_50}" stroke-width="0.8"/>
      <line x1="628" y1="80" x2="628" y2="108" stroke="{accent_50}" stroke-width="0.8"/>
      <line x1="660" y1="80" x2="660" y2="108" stroke="{accent_50}" stroke-width="0.8"/>
      <line x1="692" y1="80" x2="692" y2="108" stroke="{accent_50}" stroke-width="0.8"/>
      <line x1="724" y1="80" x2="724" y2="108" stroke="{accent_50}" stroke-width="0.8"/>
      <rect x="472" y="88" width="132" height="12" rx="2" fill="{paper}"/>
      <text x="538" y="98" fill="{accent}" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.08em">READ, THEN THROWN AWAY</text>

      <rect x="760" y="72" width="80" height="44" rx="6" fill="{paper}"/>
      <rect x="760" y="72" width="80" height="44" rx="6" fill="{ink005}" stroke="{ink}" stroke-width="1"/>
      <text x="800" y="98" fill="{ink}" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.08em">20 ROWS</text>

      <rect x="844" y="72" width="84" height="44" rx="6" fill="{ink002}" stroke="{rule_solid}" stroke-width="1"/>
      <text x="886" y="98" fill="{soft}" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.08em">REST</text>

      <text x="538" y="64" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.14em">ROWS 1 &#8211; 10,000</text>
      <text x="800" y="64" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.14em">PAGE 501</text>

      <!-- band 02 index strip -->
      <rect x="320" y="260" width="436" height="44" rx="6" fill="{ink002}" stroke="{rule_solid}" stroke-width="1"/>
      <line x1="340" y1="268" x2="340" y2="296" stroke="{rule_solid}" stroke-width="0.8"/>
      <line x1="372" y1="268" x2="372" y2="296" stroke="{rule_solid}" stroke-width="0.8"/>
      <line x1="404" y1="268" x2="404" y2="296" stroke="{rule_solid}" stroke-width="0.8"/>
      <line x1="436" y1="268" x2="436" y2="296" stroke="{rule_solid}" stroke-width="0.8"/>
      <line x1="468" y1="268" x2="468" y2="296" stroke="{rule_solid}" stroke-width="0.8"/>
      <line x1="500" y1="268" x2="500" y2="296" stroke="{rule_solid}" stroke-width="0.8"/>
      <line x1="532" y1="268" x2="532" y2="296" stroke="{rule_solid}" stroke-width="0.8"/>
      <line x1="564" y1="268" x2="564" y2="296" stroke="{rule_solid}" stroke-width="0.8"/>
      <line x1="596" y1="268" x2="596" y2="296" stroke="{rule_solid}" stroke-width="0.8"/>
      <line x1="628" y1="268" x2="628" y2="296" stroke="{rule_solid}" stroke-width="0.8"/>
      <line x1="660" y1="268" x2="660" y2="296" stroke="{rule_solid}" stroke-width="0.8"/>
      <line x1="692" y1="268" x2="692" y2="296" stroke="{rule_solid}" stroke-width="0.8"/>
      <line x1="724" y1="268" x2="724" y2="296" stroke="{rule_solid}" stroke-width="0.8"/>
      <rect x="506" y="276" width="64" height="12" rx="2" fill="{paper}"/>
      <text x="538" y="286" fill="{soft}" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.08em">NEVER READ</text>

      <rect x="760" y="260" width="80" height="44" rx="6" fill="{paper}"/>
      <rect x="760" y="260" width="80" height="44" rx="6" fill="{ink005}" stroke="{ink}" stroke-width="1"/>
      <text x="800" y="286" fill="{ink}" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.08em">20 ROWS</text>

      <rect x="844" y="260" width="84" height="44" rx="6" fill="{ink002}" stroke="{rule_solid}" stroke-width="1"/>
      <text x="886" y="286" fill="{soft}" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.08em">REST</text>

      <text x="538" y="252" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.14em">ROWS 1 &#8211; 10,000</text>
      <text x="800" y="252" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.14em">PAGE 501</text>

      <!-- query cards -->
      <rect x="32" y="56" width="240" height="88" rx="6" fill="{paper}"/>
      <rect x="32" y="56" width="240" height="88" rx="6" fill="{paper}" stroke="{ink}" stroke-width="1"/>
      <rect x="44" y="66" width="36" height="12" rx="2" fill="none" stroke="{ink040}" stroke-width="0.8"/>
      <text x="62" y="75" fill="{muted}" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.08em">SQL</text>
      <text x="152" y="100" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">Offset pagination</text>
      <text x="152" y="118" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">LIMIT 20 OFFSET 10000</text>
      <text x="152" y="134" fill="{soft}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">reads 10,020 rows</text>

      <rect x="32" y="244" width="240" height="88" rx="6" fill="{paper}"/>
      <rect x="32" y="244" width="240" height="88" rx="6" fill="{paper}" stroke="{ink}" stroke-width="1"/>
      <rect x="44" y="254" width="36" height="12" rx="2" fill="none" stroke="{ink040}" stroke-width="0.8"/>
      <text x="62" y="263" fill="{muted}" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.08em">SQL</text>
      <text x="152" y="288" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">Cursor pagination</text>
      <text x="152" y="306" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">WHERE (created_at, id) &lt;</text>
      <text x="152" y="322" fill="{soft}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">reads 20 rows</text>

      <!-- band captions -->
      <text x="320" y="172" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace">cost grows with every page</text>
      <text x="320" y="376" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace">cost is the same at page 1 or page 501</text>
      <text x="800" y="376" fill="{soft}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">(:last_ts, :last_id)</text>

      <!-- band 03 insert panels -->
      <rect x="32" y="452" width="432" height="120" rx="8" fill="{ink002}" stroke="{rule_solid}" stroke-width="1"/>
      <rect x="48" y="464" width="52" height="12" rx="2" fill="none" stroke="{ink040}" stroke-width="0.8"/>
      <text x="74" y="473" fill="{muted}" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.08em">OFFSET</text>
      <text x="48" y="498" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif">Window slides</text>
      <rect x="48" y="508" width="44" height="28" rx="4" fill="{ink002}" stroke="{ink030}" stroke-width="1" stroke-dasharray="4,3"/>
      <text x="70" y="526" fill="{muted}" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.08em">NEW</text>
      <rect x="96" y="508" width="44" height="28" rx="4" fill="{paper}" stroke="{rule_solid}" stroke-width="1"/>
      <rect x="144" y="508" width="44" height="28" rx="4" fill="{ink010}" stroke="{ink}" stroke-width="1.4"/>
      <text x="166" y="526" fill="{ink}" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.08em">DUP</text>
      <rect x="192" y="508" width="44" height="28" rx="4" fill="{paper}" stroke="{rule_solid}" stroke-width="1"/>
      <rect x="240" y="508" width="44" height="28" rx="4" fill="{paper}" stroke="{rule_solid}" stroke-width="1"/>
      <rect x="288" y="508" width="44" height="28" rx="4" fill="{paper}" stroke="{rule_solid}" stroke-width="1"/>
      <rect x="336" y="508" width="44" height="28" rx="4" fill="{paper}" stroke="{rule_solid}" stroke-width="1"/>
      <rect x="384" y="508" width="44" height="28" rx="4" fill="{paper}" stroke="{rule_solid}" stroke-width="1"/>
      <text x="48" y="556" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace">page 2 shows one row twice</text>

      <rect x="496" y="452" width="432" height="120" rx="8" fill="{ink002}" stroke="{rule_solid}" stroke-width="1"/>
      <rect x="512" y="464" width="52" height="12" rx="2" fill="none" stroke="{ink040}" stroke-width="0.8"/>
      <text x="538" y="473" fill="{muted}" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.08em">CURSOR</text>
      <text x="512" y="498" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif">Window holds</text>
      <text x="652" y="496" fill="{ink}" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.08em">ANCHOR</text>
      <line x1="652" y1="502" x2="652" y2="544" stroke="{ink}" stroke-width="1.2" stroke-dasharray="4,3"/>
      <rect x="512" y="508" width="44" height="28" rx="4" fill="{ink002}" stroke="{ink030}" stroke-width="1" stroke-dasharray="4,3"/>
      <text x="534" y="526" fill="{muted}" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.08em">NEW</text>
      <rect x="560" y="508" width="44" height="28" rx="4" fill="{paper}" stroke="{rule_solid}" stroke-width="1"/>
      <rect x="608" y="508" width="44" height="28" rx="4" fill="{paper}" stroke="{rule_solid}" stroke-width="1"/>
      <rect x="656" y="508" width="44" height="28" rx="4" fill="{paper}" stroke="{rule_solid}" stroke-width="1"/>
      <rect x="704" y="508" width="44" height="28" rx="4" fill="{paper}" stroke="{rule_solid}" stroke-width="1"/>
      <rect x="752" y="508" width="44" height="28" rx="4" fill="{paper}" stroke="{rule_solid}" stroke-width="1"/>
      <rect x="800" y="508" width="44" height="28" rx="4" fill="{paper}" stroke="{rule_solid}" stroke-width="1"/>
      <rect x="848" y="508" width="44" height="28" rx="4" fill="{paper}" stroke="{rule_solid}" stroke-width="1"/>
      <text x="512" y="556" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace">no gaps, no repeats</text>

      <!-- band eyebrows -->
      <text x="32" y="44" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace" letter-spacing="0.14em">01 &#183; OFFSET, PAGE 501</text>
      <text x="32" y="232" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace" letter-spacing="0.14em">02 &#183; KEYSET CURSOR, PAGE 501</text>
      <text x="32" y="436" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace" letter-spacing="0.14em">03 &#183; ONE ROW INSERTED BETWEEN PAGE LOADS</text>

      <!-- legend -->
      <line x1="32" y1="636" x2="928" y2="636" stroke="{rule}" stroke-width="0.8"/>
      <text x="32" y="653" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace" letter-spacing="0.14em">LEGEND</text>
      <rect x="118" y="643" width="24" height="12" rx="2" fill="{accent_tint}" stroke="{accent_50}" stroke-width="1"/>
      <text x="150" y="653" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Read, then discarded</text>
      <rect x="292" y="643" width="24" height="12" rx="2" fill="{ink005}" stroke="{ink}" stroke-width="1"/>
      <text x="324" y="653" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Returned page</text>
      <rect x="444" y="643" width="24" height="12" rx="2" fill="{ink002}" stroke="{rule_solid}" stroke-width="1"/>
      <text x="476" y="653" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Never read</text>
      <line x1="596" y1="649" x2="620" y2="649" stroke="{accent}" stroke-width="1.5"/>
      <text x="628" y="653" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Sequential walk</text>
      <line x1="760" y1="649" x2="784" y2="649" stroke="{ink}" stroke-width="1.5"/>
      <text x="792" y="653" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Index seek</text>
    </svg>
"""

SVG_B = """    <svg viewBox="0 0 960 672" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="webhook{v}-title webhook{v}-desc">
      <title id="webhook{v}-title">The states a webhook delivery moves through</title>
      <desc id="webhook{v}-desc">The lifecycle of one webhook delivery under at-least-once semantics: it is queued, then delivered, and either accepted on a 2xx or counted as a failed attempt on a timeout or 5xx. A failed attempt below five is rescheduled with exponential backoff and delivered again; the fifth failure moves it to the dead letter queue, which needs a human. Because a retry can repeat a call the consumer already processed, the same event id can arrive more than once.</desc>
""" + DEFS + """
      <rect width="100%" height="100%" fill="{paper}"/>

      <!-- transitions first -->
      <line x1="66" y1="148" x2="128" y2="148" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow{v})"/>
      <line x1="288" y1="148" x2="400" y2="148" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow{v})"/>
      <line x1="560" y1="148" x2="736" y2="148" stroke="{ink}" stroke-width="1.5" marker-end="url(#arrow{v})"/>
      <line x1="480" y1="184" x2="480" y2="360" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow{v})"/>
      <line x1="400" y1="396" x2="288" y2="396" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow{v})"/>
      <line x1="560" y1="396" x2="736" y2="396" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow{v})"/>
      <path d="M 208 360 V 280 Q 208 272 216 272 H 424 Q 432 272 432 264 V 184" fill="none" stroke="{muted}" stroke-width="1.2" stroke-dasharray="5,4" marker-end="url(#arrow{v})"/>

      <!-- transition labels -->
      <rect x="73" y="128" width="48" height="12" rx="2" fill="{paper}"/>
      <text x="97" y="137" fill="{soft}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">QUEUED</text>

      <rect x="316" y="128" width="56" height="12" rx="2" fill="{paper}"/>
      <text x="344" y="137" fill="{soft}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">DEQUEUED</text>

      <rect x="628" y="128" width="40" height="12" rx="2" fill="{paper}"/>
      <text x="648" y="137" fill="{ink}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">2XX</text>

      <rect x="492" y="266" width="92" height="12" rx="2" fill="{paper}"/>
      <text x="538" y="275" fill="{soft}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">5XX OR TIMEOUT</text>

      <rect x="282" y="252" width="76" height="12" rx="2" fill="{paper}"/>
      <text x="320" y="261" fill="{soft}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">BACKOFF DONE</text>

      <rect x="306" y="376" width="76" height="12" rx="2" fill="{paper}"/>
      <text x="344" y="385" fill="{soft}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">ATTEMPTS &lt; 5</text>

      <rect x="610" y="376" width="76" height="12" rx="2" fill="{paper}"/>
      <text x="648" y="385" fill="{soft}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">ATTEMPTS = 5</text>

      <!-- start -->
      <circle cx="56" cy="148" r="6" fill="{ink}"/>

      <!-- states -->
      <rect x="128" y="112" width="160" height="72" rx="8" fill="{paper}"/>
      <rect x="128" y="112" width="160" height="72" rx="8" fill="{ink005}" stroke="{muted}" stroke-width="1"/>
      <text x="208" y="146" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">Pending</text>
      <text x="208" y="164" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">queued for delivery</text>

      <rect x="400" y="112" width="160" height="72" rx="8" fill="{paper}"/>
      <rect x="400" y="112" width="160" height="72" rx="8" fill="{paper}" stroke="{ink}" stroke-width="1"/>
      <text x="480" y="146" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">Delivering</text>
      <text x="480" y="164" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">POST /hooks/:id</text>

      <rect x="736" y="112" width="160" height="72" rx="8" fill="{paper}"/>
      <rect x="736" y="112" width="160" height="72" rx="8" fill="{ink005}" stroke="{ink}" stroke-width="1"/>
      <rect x="740" y="116" width="152" height="64" rx="6" fill="none" stroke="{ink030}" stroke-width="0.8"/>
      <text x="816" y="146" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">Delivered</text>
      <text x="816" y="164" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">2xx, receipt stored</text>

      <rect x="128" y="360" width="160" height="72" rx="8" fill="{paper}"/>
      <rect x="128" y="360" width="160" height="72" rx="8" fill="{ink002}" stroke="{ink030}" stroke-width="1" stroke-dasharray="4,3"/>
      <text x="208" y="394" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">Scheduled retry</text>
      <text x="208" y="412" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">1m, 5m, 25m, 2h</text>

      <rect x="400" y="360" width="160" height="72" rx="8" fill="{paper}"/>
      <rect x="400" y="360" width="160" height="72" rx="8" fill="{paper}" stroke="{ink}" stroke-width="1"/>
      <text x="480" y="394" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">Failed attempt</text>
      <text x="480" y="412" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">attempt n recorded</text>

      <rect x="736" y="360" width="160" height="72" rx="8" fill="{paper}"/>
      <rect x="736" y="360" width="160" height="72" rx="8" fill="{accent_tint}" stroke="{accent}" stroke-width="1"/>
      <rect x="740" y="364" width="152" height="64" rx="6" fill="none" stroke="{accent_50}" stroke-width="0.8"/>
      <text x="816" y="394" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">Dead letter</text>
      <text x="816" y="412" fill="{accent}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">needs a human</text>

      <!-- editorial payoff -->
      <text x="480" y="512" fill="{accent}" font-size="14" font-style="italic" font-family="'Instrument Serif', serif" text-anchor="middle">the same event id can arrive more than once,</text>
      <text x="480" y="536" fill="{accent}" font-size="14" font-style="italic" font-family="'Instrument Serif', serif" text-anchor="middle">so the consumer must make the write idempotent</text>

      <!-- legend -->
      <line x1="32" y1="636" x2="928" y2="636" stroke="{rule}" stroke-width="0.8"/>
      <text x="32" y="653" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace" letter-spacing="0.14em">LEGEND</text>
      <rect x="118" y="643" width="24" height="12" rx="3" fill="{paper}" stroke="{ink}" stroke-width="1"/>
      <text x="150" y="653" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Active state</text>
      <rect x="252" y="643" width="24" height="12" rx="3" fill="{ink002}" stroke="{ink030}" stroke-width="1" stroke-dasharray="4,3"/>
      <text x="284" y="653" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Waiting on backoff</text>
      <rect x="416" y="643" width="24" height="12" rx="3" fill="{ink005}" stroke="{ink}" stroke-width="1"/>
      <rect x="419" y="646" width="18" height="6" rx="2" fill="none" stroke="{ink030}" stroke-width="0.8"/>
      <text x="448" y="653" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Terminal state</text>
      <rect x="560" y="643" width="24" height="12" rx="3" fill="{accent_tint}" stroke="{accent}" stroke-width="1"/>
      <rect x="563" y="646" width="18" height="6" rx="2" fill="none" stroke="{accent_50}" stroke-width="0.8"/>
      <text x="592" y="653" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Dead letter</text>
      <line x1="690" y1="649" x2="714" y2="649" stroke="{muted}" stroke-width="1.2" stroke-dasharray="5,4"/>
      <text x="722" y="653" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Retry after wait</text>
    </svg>
"""

DIAGRAMS = [
    ("02-pagination", "Data flow &#183; Diagram Design", "Why cursor pagination survives page 500", SVG_A),
    ("03-webhook-delivery", "State machine &#183; Diagram Design", "The states a webhook delivery moves through", SVG_B),
]

if __name__ == "__main__":
    render_all(DIAGRAMS)
