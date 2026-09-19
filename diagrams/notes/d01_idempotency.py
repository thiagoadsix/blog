from common import DEFS, render_all

SVG = """    <svg viewBox="0 0 960 672" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="idempotency-key{v}-title idempotency-key{v}-desc">
      <title id="idempotency-key{v}-title">What an idempotency key buys you</title>
      <desc id="idempotency-key{v}-desc">A sequence diagram of a payment request carrying an idempotency key. On the first attempt the API inserts the key, charges the provider, saves the response, and the reply is lost in transit. On the retry the same key hits a unique violation, so the API replays the stored response and the provider is never called a second time.</desc>
""" + DEFS + """
      <rect width="100%" height="100%" fill="{paper}"/>

      <!-- retry zone -->
      <rect x="32" y="380" width="896" height="212" rx="8" fill="{ink002}" stroke="{ink030}" stroke-width="1" stroke-dasharray="4,4"/>
      <rect x="48" y="374" width="184" height="12" rx="2" fill="{paper}"/>
      <text x="140" y="383" fill="{muted}" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.14em">RETRY &#183; SAME KEY, SAME BODY</text>

      <!-- lifelines -->
      <line x1="120" y1="84" x2="120" y2="604" stroke="{rule_solid}" stroke-width="1" stroke-dasharray="4,4"/>
      <line x1="380" y1="84" x2="380" y2="604" stroke="{rule_solid}" stroke-width="1" stroke-dasharray="4,4"/>
      <line x1="620" y1="84" x2="620" y2="604" stroke="{rule_solid}" stroke-width="1" stroke-dasharray="4,4"/>
      <line x1="850" y1="84" x2="850" y2="604" stroke="{rule_solid}" stroke-width="1" stroke-dasharray="4,4"/>

      <!-- first attempt -->
      <line x1="120" y1="128" x2="380" y2="128" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow{v})"/>
      <line x1="380" y1="172" x2="620" y2="172" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow{v})"/>
      <line x1="380" y1="216" x2="850" y2="216" stroke="{link}" stroke-width="1.2" marker-end="url(#arrow-link{v})"/>
      <line x1="850" y1="260" x2="380" y2="260" stroke="{link}" stroke-width="1.2" stroke-dasharray="5,4" marker-end="url(#arrow-link{v})"/>
      <line x1="380" y1="304" x2="620" y2="304" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow{v})"/>
      <line x1="380" y1="348" x2="120" y2="348" stroke="{accent}" stroke-width="1.5" marker-end="url(#arrow-accent{v})"/>

      <!-- retry -->
      <line x1="120" y1="416" x2="380" y2="416" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow{v})"/>
      <line x1="380" y1="460" x2="620" y2="460" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow{v})"/>
      <line x1="620" y1="504" x2="380" y2="504" stroke="{muted}" stroke-width="1.2" stroke-dasharray="5,4" marker-end="url(#arrow{v})"/>
      <line x1="380" y1="548" x2="120" y2="548" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow{v})"/>

      <!-- lost response mark -->
      <line x1="244" y1="342" x2="256" y2="354" stroke="{accent}" stroke-width="1.8"/>
      <line x1="256" y1="342" x2="244" y2="354" stroke="{accent}" stroke-width="1.8"/>

      <!-- message labels -->
      <rect x="202" y="108" width="96" height="12" rx="2" fill="{paper}"/>
      <text x="250" y="117" fill="{soft}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">POST /PAYMENTS</text>

      <rect x="456" y="152" width="88" height="12" rx="2" fill="{paper}"/>
      <text x="500" y="161" fill="{soft}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">INSERT KEY K1</text>

      <rect x="558" y="196" width="84" height="12" rx="2" fill="{paper}"/>
      <text x="600" y="205" fill="{link}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">CHARGE 40.00</text>

      <rect x="585" y="240" width="60" height="12" rx="2" fill="{paper}"/>
      <text x="615" y="249" fill="{link}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">CHARGED</text>

      <rect x="454" y="284" width="92" height="12" rx="2" fill="{paper}"/>
      <text x="500" y="293" fill="{soft}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">SAVE RESPONSE</text>

      <rect x="212" y="328" width="76" height="12" rx="2" fill="{paper}"/>
      <text x="250" y="337" fill="{accent}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">201 CREATED</text>
      <rect x="226" y="356" width="48" height="12" rx="2" fill="{paper}"/>
      <text x="250" y="365" fill="{accent}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">LOST</text>

      <rect x="206" y="396" width="88" height="12" rx="2" fill="{paper}"/>
      <text x="250" y="405" fill="{soft}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">RETRY, KEY K1</text>

      <rect x="456" y="440" width="88" height="12" rx="2" fill="{paper}"/>
      <text x="500" y="449" fill="{soft}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">INSERT KEY K1</text>

      <rect x="452" y="484" width="96" height="12" rx="2" fill="{paper}"/>
      <text x="500" y="493" fill="{ink}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">23505 CONFLICT</text>

      <rect x="208" y="528" width="84" height="12" rx="2" fill="{paper}"/>
      <text x="250" y="537" fill="{soft}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">201 REPLAYED</text>

      <!-- editorial payoff -->
      <text x="850" y="470" fill="{accent}" font-size="14" font-style="italic" font-family="'Instrument Serif', serif" text-anchor="middle">the provider is</text>
      <text x="850" y="488" fill="{accent}" font-size="14" font-style="italic" font-family="'Instrument Serif', serif" text-anchor="middle">never called again</text>

      <!-- actors -->
      <rect x="48" y="36" width="144" height="48" rx="6" fill="{paper}"/>
      <rect x="48" y="36" width="144" height="48" rx="6" fill="{muted010}" stroke="{soft}" stroke-width="1"/>
      <text x="120" y="58" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">Client</text>
      <text x="120" y="74" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">retries on timeout</text>

      <rect x="308" y="36" width="144" height="48" rx="6" fill="{paper}"/>
      <rect x="308" y="36" width="144" height="48" rx="6" fill="{paper}" stroke="{ink}" stroke-width="1"/>
      <text x="380" y="58" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">Payments API</text>
      <text x="380" y="74" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">one transaction</text>

      <rect x="548" y="36" width="144" height="48" rx="6" fill="{paper}"/>
      <rect x="548" y="36" width="144" height="48" rx="6" fill="{ink005}" stroke="{muted}" stroke-width="1"/>
      <text x="620" y="58" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">idempotency_keys</text>
      <text x="620" y="74" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">UNIQUE (key)</text>

      <rect x="778" y="36" width="144" height="48" rx="6" fill="{paper}"/>
      <rect x="778" y="36" width="144" height="48" rx="6" fill="{ink003}" stroke="{ink030}" stroke-width="1"/>
      <text x="850" y="58" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">Payment provider</text>
      <text x="850" y="74" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">moves real money</text>

      <!-- legend -->
      <line x1="32" y1="636" x2="928" y2="636" stroke="{rule}" stroke-width="0.8"/>
      <text x="32" y="653" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace" letter-spacing="0.14em">LEGEND</text>
      <line x1="150" y1="649" x2="174" y2="649" stroke="{muted}" stroke-width="1.2"/>
      <text x="182" y="653" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Call</text>
      <line x1="280" y1="649" x2="304" y2="649" stroke="{muted}" stroke-width="1.2" stroke-dasharray="5,4"/>
      <text x="312" y="653" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Return</text>
      <line x1="420" y1="649" x2="444" y2="649" stroke="{link}" stroke-width="1.2"/>
      <text x="452" y="653" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">External call</text>
      <rect x="600" y="643" width="24" height="12" rx="2" fill="{ink002}" stroke="{ink030}" stroke-width="1" stroke-dasharray="4,4"/>
      <text x="632" y="653" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Retry attempt</text>
      <line x1="780" y1="649" x2="804" y2="649" stroke="{accent}" stroke-width="1.5"/>
      <text x="812" y="653" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Lost response</text>
    </svg>
"""

DIAGRAMS = [
    ("01-idempotency-key", "Sequence &#183; Diagram Design", "What an idempotency key buys you", SVG),
]

if __name__ == "__main__":
    render_all(DIAGRAMS)
