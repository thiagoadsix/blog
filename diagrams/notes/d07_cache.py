from common import DEFS, render_all

LAYERS = """    <svg viewBox="0 0 960 328" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="cache-layers{v}-title cache-layers{v}-desc">
      <title id="cache-layers{v}-title">Where a response is allowed to rest</title>
      <desc id="cache-layers{v}-desc">A request path from client through the browser cache and a shared CDN cache to the origin, showing which Cache-Control directive governs each hop: max-age and private bind the browser, s-maxage and Vary bind the shared cache, and the origin emits the ETag validator that turns a miss into a 304.</desc>
""" + DEFS + """
      <rect width="100%" height="100%" fill="{paper}"/>

      <!-- forward path -->
      <line x1="188" y1="72" x2="276" y2="72" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow{v})"/>
      <line x1="436" y1="72" x2="524" y2="72" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow{v})"/>
      <line x1="684" y1="72" x2="772" y2="72" stroke="{link}" stroke-width="1.2" marker-end="url(#arrow-link{v})"/>

      <!-- return path -->
      <line x1="276" y1="96" x2="188" y2="96" stroke="{muted}" stroke-width="1.2" stroke-dasharray="5,4" marker-end="url(#arrow{v})"/>
      <line x1="524" y1="96" x2="436" y2="96" stroke="{muted}" stroke-width="1.2" stroke-dasharray="5,4" marker-end="url(#arrow{v})"/>
      <line x1="772" y1="96" x2="684" y2="96" stroke="{link}" stroke-width="1.2" stroke-dasharray="5,4" marker-end="url(#arrow-link{v})"/>

      <!-- forward labels -->
      <rect x="196" y="52" width="72" height="12" rx="2" fill="{paper}"/>
      <text x="232" y="61" fill="{soft}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">GET /ORDERS</text>
      <rect x="446" y="52" width="68" height="12" rx="2" fill="{paper}"/>
      <text x="480" y="61" fill="{soft}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">STALE COPY</text>
      <rect x="690" y="52" width="76" height="12" rx="2" fill="{paper}"/>
      <text x="728" y="61" fill="{link}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">IF-NONE-MATCH</text>

      <!-- return labels -->
      <rect x="196" y="104" width="72" height="12" rx="2" fill="{paper}"/>
      <text x="232" y="113" fill="{soft}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">200 ETAG V7</text>
      <rect x="442" y="104" width="76" height="12" rx="2" fill="{paper}"/>
      <text x="480" y="113" fill="{soft}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">200 REFRESHED</text>
      <rect x="692" y="104" width="72" height="12" rx="2" fill="{paper}"/>
      <text x="728" y="113" fill="{link}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">304 NO BODY</text>

      <!-- nodes -->
      <rect x="28" y="48" width="160" height="72" rx="6" fill="{paper}"/>
      <rect x="28" y="48" width="160" height="72" rx="6" fill="{muted010}" stroke="{soft}" stroke-width="1"/>
      <text x="108" y="82" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">Client</text>
      <text x="108" y="100" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">one user</text>

      <rect x="276" y="48" width="160" height="72" rx="6" fill="{paper}"/>
      <rect x="276" y="48" width="160" height="72" rx="6" fill="{ink005}" stroke="{muted}" stroke-width="1"/>
      <text x="356" y="82" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">Browser cache</text>
      <text x="356" y="100" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">private, per user</text>

      <rect x="524" y="48" width="160" height="72" rx="6" fill="{paper}"/>
      <rect x="524" y="48" width="160" height="72" rx="6" fill="{accent_tint}" stroke="{accent}" stroke-width="1"/>
      <text x="604" y="82" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">CDN / shared cache</text>
      <text x="604" y="100" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">one copy, many users</text>

      <rect x="772" y="48" width="160" height="72" rx="6" fill="{paper}"/>
      <rect x="772" y="48" width="160" height="72" rx="6" fill="{paper}" stroke="{ink}" stroke-width="1"/>
      <text x="852" y="82" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">Origin</text>
      <text x="852" y="100" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">emits the validator</text>

      <!-- directive chips -->
      <text x="28" y="152" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace" letter-spacing="0.14em">WHAT THE ORIGIN SENDS, AND WHO OBEYS IT</text>

      <rect x="276" y="164" width="76" height="24" rx="4" fill="{paper}" stroke="{rule_solid}" stroke-width="1"/>
      <text x="314" y="179" fill="{ink}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">max-age</text>
      <rect x="360" y="164" width="76" height="24" rx="4" fill="{paper}" stroke="{rule_solid}" stroke-width="1"/>
      <text x="398" y="179" fill="{ink}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">private</text>

      <rect x="524" y="164" width="76" height="24" rx="4" fill="{paper}" stroke="{rule_solid}" stroke-width="1"/>
      <text x="562" y="179" fill="{ink}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">s-maxage</text>
      <rect x="608" y="164" width="76" height="24" rx="4" fill="{paper}" stroke="{rule_solid}" stroke-width="1"/>
      <text x="646" y="179" fill="{ink}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">Vary</text>

      <rect x="772" y="164" width="76" height="24" rx="4" fill="{paper}" stroke="{rule_solid}" stroke-width="1"/>
      <text x="810" y="179" fill="{ink}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">ETag</text>
      <rect x="856" y="164" width="76" height="24" rx="4" fill="{paper}" stroke="{rule_solid}" stroke-width="1"/>
      <text x="894" y="179" fill="{ink}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">no-store</text>

      <!-- editorial aside -->
      <text x="604" y="224" fill="{accent}" font-size="14" font-style="italic" font-family="'Instrument Serif', serif" text-anchor="middle">the shared cache is the only one</text>
      <text x="604" y="242" fill="{accent}" font-size="14" font-style="italic" font-family="'Instrument Serif', serif" text-anchor="middle">that can hand your data to a stranger</text>

      <!-- legend -->
      <line x1="28" y1="284" x2="932" y2="284" stroke="{rule}" stroke-width="0.8"/>
      <text x="28" y="301" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace" letter-spacing="0.14em">LEGEND</text>
      <line x1="150" y1="297" x2="174" y2="297" stroke="{muted}" stroke-width="1.2"/>
      <text x="182" y="301" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Request</text>
      <line x1="300" y1="297" x2="324" y2="297" stroke="{muted}" stroke-width="1.2" stroke-dasharray="5,4"/>
      <text x="332" y="301" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Response</text>
      <line x1="460" y1="297" x2="484" y2="297" stroke="{link}" stroke-width="1.2"/>
      <text x="492" y="301" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Revalidation</text>
      <rect x="640" y="291" width="24" height="12" rx="2" fill="{ink005}" stroke="{muted}" stroke-width="1"/>
      <text x="672" y="301" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Stores a copy</text>
      <rect x="800" y="291" width="24" height="12" rx="2" fill="{accent_tint}" stroke="{accent}" stroke-width="1"/>
      <text x="832" y="301" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Shared by all</text>
    </svg>
"""

IF_MATCH = """    <svg viewBox="0 0 960 528" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="if-match{v}-title if-match{v}-desc">
      <title id="if-match{v}-title">If-Match turns a lost update into a 412</title>
      <desc id="if-match{v}-desc">A sequence diagram of two editors loading the same order at version seven. The first write carries If-Match with that version and succeeds, moving the resource to version eight. The second write still carries version seven, so the API answers 412 Precondition Failed instead of silently overwriting the first edit.</desc>
""" + DEFS + """
      <rect width="100%" height="100%" fill="{paper}"/>

      <!-- conflict zone -->
      <rect x="456" y="316" width="472" height="104" rx="8" fill="{ink002}" stroke="{ink030}" stroke-width="1" stroke-dasharray="4,4"/>
      <rect x="472" y="310" width="212" height="12" rx="2" fill="{paper}"/>
      <text x="578" y="319" fill="{muted}" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.14em">SECOND WRITE &#183; STALE BASE VERSION</text>

      <!-- lifelines -->
      <line x1="120" y1="84" x2="120" y2="430" stroke="{rule_solid}" stroke-width="1" stroke-dasharray="4,4"/>
      <line x1="480" y1="84" x2="480" y2="430" stroke="{rule_solid}" stroke-width="1" stroke-dasharray="4,4"/>
      <line x1="840" y1="84" x2="840" y2="430" stroke="{rule_solid}" stroke-width="1" stroke-dasharray="4,4"/>

      <!-- messages -->
      <line x1="120" y1="128" x2="480" y2="128" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow{v})"/>
      <line x1="480" y1="164" x2="120" y2="164" stroke="{muted}" stroke-width="1.2" stroke-dasharray="5,4" marker-end="url(#arrow{v})"/>
      <line x1="840" y1="200" x2="480" y2="200" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow{v})"/>
      <line x1="480" y1="236" x2="840" y2="236" stroke="{muted}" stroke-width="1.2" stroke-dasharray="5,4" marker-end="url(#arrow{v})"/>
      <line x1="120" y1="272" x2="480" y2="272" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow{v})"/>
      <line x1="480" y1="308" x2="120" y2="308" stroke="{muted}" stroke-width="1.2" stroke-dasharray="5,4" marker-end="url(#arrow{v})"/>
      <line x1="840" y1="352" x2="480" y2="352" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow{v})"/>
      <line x1="480" y1="388" x2="840" y2="388" stroke="{accent}" stroke-width="1.5" stroke-dasharray="5,4" marker-end="url(#arrow-accent{v})"/>

      <!-- message labels -->
      <rect x="264" y="108" width="72" height="12" rx="2" fill="{paper}"/>
      <text x="300" y="117" fill="{soft}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">GET /ORDERS</text>
      <rect x="264" y="144" width="72" height="12" rx="2" fill="{paper}"/>
      <text x="300" y="153" fill="{soft}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">200 ETAG V7</text>

      <rect x="624" y="180" width="72" height="12" rx="2" fill="{paper}"/>
      <text x="660" y="189" fill="{soft}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">GET /ORDERS</text>
      <rect x="624" y="216" width="72" height="12" rx="2" fill="{paper}"/>
      <text x="660" y="225" fill="{soft}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">200 ETAG V7</text>

      <rect x="264" y="252" width="72" height="12" rx="2" fill="{paper}"/>
      <text x="300" y="261" fill="{ink}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">PUT IF-MATCH</text>
      <rect x="264" y="288" width="72" height="12" rx="2" fill="{paper}"/>
      <text x="300" y="297" fill="{ink}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">200 ETAG V8</text>

      <rect x="620" y="332" width="80" height="12" rx="2" fill="{paper}"/>
      <text x="660" y="341" fill="{ink}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">STILL SENDS V7</text>
      <rect x="624" y="368" width="72" height="12" rx="2" fill="{paper}"/>
      <text x="660" y="377" fill="{accent}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">412 PRECOND</text>

      <!-- actors -->
      <rect x="32" y="36" width="176" height="48" rx="6" fill="{paper}"/>
      <rect x="32" y="36" width="176" height="48" rx="6" fill="{muted010}" stroke="{soft}" stroke-width="1"/>
      <text x="120" y="58" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">Editor A</text>
      <text x="120" y="74" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">saves first</text>

      <rect x="392" y="36" width="176" height="48" rx="6" fill="{paper}"/>
      <rect x="392" y="36" width="176" height="48" rx="6" fill="{paper}" stroke="{ink}" stroke-width="1"/>
      <text x="480" y="58" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">Orders API</text>
      <text x="480" y="74" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">compares ETag</text>

      <rect x="752" y="36" width="176" height="48" rx="6" fill="{paper}"/>
      <rect x="752" y="36" width="176" height="48" rx="6" fill="{muted010}" stroke="{soft}" stroke-width="1"/>
      <text x="840" y="58" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">Editor B</text>
      <text x="840" y="74" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">loaded the same row</text>

      <!-- editorial payoff -->
      <text x="480" y="454" fill="{accent}" font-size="14" font-style="italic" font-family="'Instrument Serif', serif" text-anchor="middle">B is told the ground moved, instead of quietly erasing A</text>

      <!-- legend -->
      <line x1="32" y1="484" x2="928" y2="484" stroke="{rule}" stroke-width="0.8"/>
      <text x="32" y="501" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace" letter-spacing="0.14em">LEGEND</text>
      <line x1="150" y1="497" x2="174" y2="497" stroke="{muted}" stroke-width="1.2"/>
      <text x="182" y="501" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Request</text>
      <line x1="300" y1="497" x2="324" y2="497" stroke="{muted}" stroke-width="1.2" stroke-dasharray="5,4"/>
      <text x="332" y="501" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Response</text>
      <rect x="470" y="491" width="24" height="12" rx="2" fill="{ink002}" stroke="{ink030}" stroke-width="1" stroke-dasharray="4,4"/>
      <text x="502" y="501" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Conflicting write</text>
      <line x1="680" y1="497" x2="704" y2="497" stroke="{accent}" stroke-width="1.5" stroke-dasharray="5,4"/>
      <text x="712" y="501" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Rejected, nothing lost</text>
    </svg>
"""

STAMPEDE = """    <svg viewBox="0 0 960 480" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="stampede{v}-title stampede{v}-desc">
      <title id="stampede{v}-title">What happens the instant a hot key expires</title>
      <desc id="stampede{v}-desc">Two lanes comparing cache behaviour at the moment a hot key expires. Without coordination, six concurrent requests all miss and each one queries the origin. With stale-while-revalidate and single flight, one request refreshes the entry in the background while the other five are served the stale copy, so the origin sees a single query.</desc>
""" + DEFS + """
      <rect width="100%" height="100%" fill="{paper}"/>

      <!-- lanes -->
      <rect x="28" y="64" width="904" height="156" rx="8" fill="{ink002}" stroke="{ink030}" stroke-width="1" stroke-dasharray="4,4"/>
      <rect x="44" y="58" width="216" height="12" rx="2" fill="{paper}"/>
      <text x="152" y="67" fill="{muted}" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.14em">TTL EXPIRES &#183; NO COORDINATION</text>

      <rect x="28" y="252" width="904" height="156" rx="8" fill="{ink002}" stroke="{ink030}" stroke-width="1" stroke-dasharray="4,4"/>
      <rect x="44" y="246" width="240" height="12" rx="2" fill="{paper}"/>
      <text x="164" y="255" fill="{muted}" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.14em">STALE-WHILE-REVALIDATE &#183; SINGLE FLIGHT</text>

      <!-- lane A: every miss reaches the origin -->
      <text x="64" y="88" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace" letter-spacing="0.06em">6 CONCURRENT REQUESTS</text>
      <line x1="64" y1="104" x2="900" y2="104" stroke="{rule_solid}" stroke-width="1"/>
      <line x1="140" y1="108" x2="140" y2="176" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow{v})"/>
      <line x1="236" y1="108" x2="236" y2="176" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow{v})"/>
      <line x1="332" y1="108" x2="332" y2="176" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow{v})"/>
      <line x1="404" y1="108" x2="404" y2="176" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow{v})"/>
      <line x1="516" y1="108" x2="516" y2="176" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow{v})"/>
      <line x1="620" y1="108" x2="620" y2="176" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow{v})"/>
      <rect x="64" y="180" width="700" height="28" rx="4" fill="{ink005}" stroke="{muted}" stroke-width="1"/>
      <text x="414" y="198" fill="{ink}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">ORIGIN &#183; ONE DB QUERY PER MISS</text>
      <circle cx="140" cy="104" r="4" fill="{muted}"/>
      <circle cx="236" cy="104" r="4" fill="{muted}"/>
      <circle cx="332" cy="104" r="4" fill="{muted}"/>
      <circle cx="404" cy="104" r="4" fill="{muted}"/>
      <circle cx="516" cy="104" r="4" fill="{muted}"/>
      <circle cx="620" cy="104" r="4" fill="{muted}"/>
      <rect x="788" y="168" width="112" height="44" rx="6" fill="{accent_tint}" stroke="{accent}" stroke-width="1"/>
      <text x="844" y="195" fill="{accent}" font-size="12" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">6 queries</text>

      <!-- lane B: one refresh, five stale hits -->
      <text x="64" y="276" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace" letter-spacing="0.06em">6 CONCURRENT REQUESTS</text>
      <line x1="64" y1="292" x2="900" y2="292" stroke="{rule_solid}" stroke-width="1"/>
      <line x1="140" y1="296" x2="140" y2="364" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow{v})"/>
      <rect x="152" y="318" width="72" height="12" rx="2" fill="{paper}"/>
      <text x="188" y="327" fill="{soft}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">REVALIDATE</text>
      <text x="560" y="327" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">5 SERVED STALE, NOTHING LEAVES THE EDGE</text>
      <rect x="64" y="368" width="700" height="28" rx="4" fill="{ink005}" stroke="{muted}" stroke-width="1"/>
      <text x="414" y="386" fill="{ink}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">ORIGIN &#183; ONE BACKGROUND REFRESH</text>
      <circle cx="140" cy="292" r="4" fill="{muted}"/>
      <circle cx="236" cy="292" r="4" fill="{muted}"/>
      <circle cx="332" cy="292" r="4" fill="{muted}"/>
      <circle cx="404" cy="292" r="4" fill="{muted}"/>
      <circle cx="516" cy="292" r="4" fill="{muted}"/>
      <circle cx="620" cy="292" r="4" fill="{muted}"/>
      <rect x="788" y="356" width="112" height="44" rx="6" fill="{accent_tint}" stroke="{accent}" stroke-width="1"/>
      <text x="844" y="383" fill="{accent}" font-size="12" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">1 query</text>

      <!-- legend -->
      <line x1="28" y1="436" x2="932" y2="436" stroke="{rule}" stroke-width="0.8"/>
      <text x="28" y="453" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace" letter-spacing="0.14em">LEGEND</text>
      <circle cx="162" cy="449" r="4" fill="{muted}"/>
      <text x="178" y="453" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Incoming request</text>
      <line x1="340" y1="443" x2="340" y2="455" stroke="{muted}" stroke-width="1.2"/>
      <text x="352" y="453" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Reaches the origin</text>
      <rect x="520" y="443" width="24" height="12" rx="2" fill="{ink005}" stroke="{muted}" stroke-width="1"/>
      <text x="552" y="453" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Origin work</text>
      <rect x="700" y="443" width="24" height="12" rx="2" fill="{accent_tint}" stroke="{accent}" stroke-width="1"/>
      <text x="732" y="453" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Cost of the expiry</text>
    </svg>
"""

DIAGRAMS = [
    ("14-cache-layers", "Data flow &#183; Diagram Design", "Where a response is allowed to rest", LAYERS),
    ("15-if-match", "Sequence &#183; Diagram Design", "If-Match turns a lost update into a 412", IF_MATCH),
    ("16-stampede", "Timeline &#183; Diagram Design", "What happens the instant a hot key expires", STAMPEDE),
]

if __name__ == "__main__":
    render_all(DIAGRAMS)
