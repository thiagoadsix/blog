from common import DEFS, render_all

SVG_A = """    <svg viewBox="0 0 960 672" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="price-schema{v}-title price-schema{v}-desc">
      <title id="price-schema{v}-title">One active price, enforced by the schema</title>
      <desc id="price-schema{v}-desc">A physical schema for immutable pricing: plans own plan options, plan options own price rows that are only ever inserted, and a partial unique index on prices by option_id where active rejects any second active price for the same option, so the rule holds even when the application forgets to check.</desc>
""" + DEFS + """
      <rect width="100%" height="100%" fill="{paper}"/>

      <!-- foreign keys, drawn before the tables -->
      <line x1="344" y1="164" x2="280" y2="164" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow{v})"/>
      <rect x="284" y="144" width="56" height="12" rx="2" fill="{paper}"/>
      <text x="312" y="153" fill="{soft}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">RESTRICT</text>

      <line x1="640" y1="140" x2="576" y2="140" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow{v})"/>
      <rect x="580" y="120" width="56" height="12" rx="2" fill="{paper}"/>
      <text x="608" y="129" fill="{soft}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">RESTRICT</text>

      <!-- table: plans -->
      <rect x="48" y="120" width="232" height="104" rx="6" fill="{paper}"/>
      <path d="M 48,126 A 6 6 0 0 1 54,120 H 274 A 6 6 0 0 1 280,126 V 152 H 48 Z" fill="{ink005}"/>
      <rect x="48" y="176" width="232" height="24" fill="{ink002}"/>
      <line x1="48" y1="152" x2="280" y2="152" stroke="{rule}" stroke-width="0.8"/>
      <rect x="48" y="120" width="232" height="104" rx="6" fill="none" stroke="{ink}" stroke-width="1"/>
      <text x="60" y="141" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif">public.plans</text>
      <rect x="232" y="130" width="36" height="12" rx="2" fill="none" stroke="{ink040}" stroke-width="0.8"/>
      <text x="250" y="139" fill="{muted}" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.08em">TABLE</text>
      <text x="60" y="168" fill="{ink}" font-size="12" font-family="'Geist', sans-serif">id</text>
      <rect x="176" y="158" width="20" height="12" rx="2" fill="none" stroke="{ink040}" stroke-width="0.8"/>
      <text x="186" y="167" fill="{muted}" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">PK</text>
      <text x="268" y="168" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="end">uuid</text>
      <text x="60" y="192" fill="{ink}" font-size="12" font-family="'Geist', sans-serif">name</text>
      <text x="268" y="192" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="end">text</text>
      <text x="60" y="216" fill="{ink}" font-size="12" font-family="'Geist', sans-serif">created_at</text>
      <text x="268" y="216" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="end">timestamptz</text>

      <!-- table: plan_options -->
      <rect x="344" y="96" width="232" height="128" rx="6" fill="{paper}"/>
      <path d="M 344,102 A 6 6 0 0 1 350,96 H 570 A 6 6 0 0 1 576,102 V 128 H 344 Z" fill="{ink005}"/>
      <rect x="344" y="152" width="232" height="24" fill="{ink002}"/>
      <rect x="344" y="200" width="232" height="24" fill="{ink002}"/>
      <line x1="344" y1="128" x2="576" y2="128" stroke="{rule}" stroke-width="0.8"/>
      <rect x="344" y="96" width="232" height="128" rx="6" fill="none" stroke="{ink}" stroke-width="1"/>
      <text x="356" y="117" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif">public.plan_options</text>
      <rect x="528" y="106" width="36" height="12" rx="2" fill="none" stroke="{ink040}" stroke-width="0.8"/>
      <text x="546" y="115" fill="{muted}" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.08em">TABLE</text>
      <text x="356" y="144" fill="{ink}" font-size="12" font-family="'Geist', sans-serif">id</text>
      <rect x="472" y="134" width="20" height="12" rx="2" fill="none" stroke="{ink040}" stroke-width="0.8"/>
      <text x="482" y="143" fill="{muted}" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">PK</text>
      <text x="564" y="144" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="end">uuid</text>
      <text x="356" y="168" fill="{ink}" font-size="12" font-family="'Geist', sans-serif">plan_id</text>
      <rect x="472" y="158" width="20" height="12" rx="2" fill="none" stroke="{ink040}" stroke-width="0.8"/>
      <text x="482" y="167" fill="{muted}" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">FK</text>
      <text x="564" y="168" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="end">uuid</text>
      <text x="356" y="192" fill="{ink}" font-size="12" font-family="'Geist', sans-serif">billing_period</text>
      <text x="564" y="192" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="end">text</text>
      <text x="356" y="216" fill="{ink}" font-size="12" font-family="'Geist', sans-serif">created_at</text>
      <text x="564" y="216" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="end">timestamptz</text>

      <!-- table: prices -->
      <text x="640" y="64" fill="{muted}" font-size="7" font-family="'Geist Mono', monospace" letter-spacing="0.14em">IMMUTABLE &#183; INSERT-ONLY</text>
      <rect x="640" y="72" width="272" height="244" rx="6" fill="{paper}"/>
      <path d="M 640,78 A 6 6 0 0 1 646,72 H 906 A 6 6 0 0 1 912,78 V 104 H 640 Z" fill="{ink005}"/>
      <rect x="640" y="128" width="272" height="24" fill="{ink002}"/>
      <rect x="640" y="176" width="272" height="24" fill="{ink002}"/>
      <rect x="640" y="224" width="272" height="24" fill="{ink002}"/>
      <path d="M 640,272 H 912 V 310 A 6 6 0 0 1 906,316 H 646 A 6 6 0 0 1 640,310 Z" fill="{accent_05}"/>
      <line x1="640" y1="104" x2="912" y2="104" stroke="{rule}" stroke-width="0.8"/>
      <line x1="640" y1="272" x2="912" y2="272" stroke="{accent_50}" stroke-width="1" stroke-dasharray="4,3"/>
      <rect x="640" y="72" width="272" height="244" rx="6" fill="none" stroke="{ink}" stroke-width="1"/>
      <text x="652" y="93" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif">public.prices</text>
      <rect x="864" y="82" width="36" height="12" rx="2" fill="none" stroke="{ink040}" stroke-width="0.8"/>
      <text x="882" y="91" fill="{muted}" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.08em">TABLE</text>
      <text x="652" y="120" fill="{ink}" font-size="12" font-family="'Geist', sans-serif">id</text>
      <rect x="808" y="110" width="20" height="12" rx="2" fill="none" stroke="{ink040}" stroke-width="0.8"/>
      <text x="818" y="119" fill="{muted}" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">PK</text>
      <text x="900" y="120" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="end">uuid</text>
      <text x="652" y="144" fill="{ink}" font-size="12" font-family="'Geist', sans-serif">option_id</text>
      <rect x="808" y="134" width="20" height="12" rx="2" fill="none" stroke="{ink040}" stroke-width="0.8"/>
      <text x="818" y="143" fill="{muted}" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">FK</text>
      <text x="900" y="144" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="end">uuid</text>
      <text x="652" y="168" fill="{ink}" font-size="12" font-family="'Geist', sans-serif">amount_cents</text>
      <text x="900" y="168" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="end">bigint</text>
      <text x="652" y="192" fill="{ink}" font-size="12" font-family="'Geist', sans-serif">currency</text>
      <text x="900" y="192" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="end">char(3)</text>
      <text x="652" y="216" fill="{ink}" font-size="12" font-family="'Geist', sans-serif">provider_price_id</text>
      <text x="900" y="216" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="end">text</text>
      <text x="652" y="240" fill="{ink}" font-size="12" font-family="'Geist', sans-serif">active</text>
      <text x="900" y="240" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="end">boolean</text>
      <text x="652" y="264" fill="{ink}" font-size="12" font-family="'Geist', sans-serif">created_at</text>
      <text x="900" y="264" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="end">timestamptz</text>
      <text x="652" y="288" fill="{accent}" font-size="7" font-family="'Geist Mono', monospace" letter-spacing="0.14em">PARTIAL UNIQUE INDEX</text>
      <text x="652" y="306" fill="{accent}" font-size="9" font-family="'Geist Mono', monospace">one_active_price (option_id) WHERE active</text>

      <!-- what the index refuses -->
      <rect x="48" y="396" width="432" height="136" rx="8" fill="{ink002}" stroke="{ink030}" stroke-width="1" stroke-dasharray="4,4"/>
      <text x="68" y="422" fill="{muted}" font-size="7" font-family="'Geist Mono', monospace" letter-spacing="0.14em">WHAT THE INDEX REFUSES</text>
      <text x="68" y="450" fill="{ink}" font-size="9" font-family="'Geist Mono', monospace">INSERT INTO prices (option_id, amount_cents, active)</text>
      <text x="68" y="468" fill="{ink}" font-size="9" font-family="'Geist Mono', monospace">VALUES (7, 1900, true);</text>
      <text x="68" y="496" fill="{accent}" font-size="9" font-family="'Geist Mono', monospace">ERROR: duplicate key value violates unique</text>
      <text x="68" y="514" fill="{accent}" font-size="9" font-family="'Geist Mono', monospace">constraint "one_active_price"</text>

      <!-- editorial payoff -->
      <text x="696" y="440" fill="{ink}" font-size="14" font-style="italic" font-family="'Instrument Serif', serif" text-anchor="middle">a second active price for the same</text>
      <text x="696" y="462" fill="{ink}" font-size="14" font-style="italic" font-family="'Instrument Serif', serif" text-anchor="middle">option cannot exist &#8212; even if the</text>
      <text x="696" y="484" fill="{ink}" font-size="14" font-style="italic" font-family="'Instrument Serif', serif" text-anchor="middle">application forgets to check</text>

      <!-- legend -->
      <line x1="48" y1="636" x2="912" y2="636" stroke="{rule}" stroke-width="0.8"/>
      <text x="48" y="653" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace" letter-spacing="0.14em">LEGEND</text>
      <rect x="140" y="643" width="20" height="12" rx="2" fill="none" stroke="{ink040}" stroke-width="0.8"/>
      <text x="150" y="652" fill="{muted}" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">PK</text>
      <text x="168" y="653" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Key column</text>
      <line x1="308" y1="649" x2="332" y2="649" stroke="{muted}" stroke-width="1.2"/>
      <text x="340" y="653" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Foreign key</text>
      <rect x="500" y="643" width="20" height="12" rx="2" fill="{accent_05}" stroke="{accent_50}" stroke-width="0.8"/>
      <text x="528" y="653" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Partial unique index</text>
      <rect x="712" y="643" width="20" height="12" rx="2" fill="{ink002}" stroke="{ink030}" stroke-width="0.8" stroke-dasharray="4,4"/>
      <text x="740" y="653" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Rejected write</text>
    </svg>
"""

SVG_B = """    <svg viewBox="0 0 960 672" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="write-skew{v}-title write-skew{v}-desc">
      <title id="write-skew{v}-title">Why both writes succeeded and the invariant broke</title>
      <desc id="write-skew{v}-desc">A sequence diagram of write skew under READ COMMITTED: two transactions each count one active price for option 7, each deactivates the old row and inserts a new one from its own stale read, and both commit without conflict, leaving two active prices even though neither transaction did anything wrong on its own.</desc>
""" + DEFS + """
      <rect width="100%" height="100%" fill="{paper}"/>

      <!-- stale-read window -->
      <rect x="48" y="252" width="864" height="148" rx="8" fill="{ink002}" stroke="{ink030}" stroke-width="1" stroke-dasharray="4,4"/>
      <rect x="64" y="246" width="208" height="12" rx="2" fill="{paper}"/>
      <text x="168" y="255" fill="{muted}" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.14em">EACH WRITES FROM A STALE READ</text>

      <!-- lifelines -->
      <line x1="152" y1="84" x2="152" y2="480" stroke="{rule_solid}" stroke-width="1" stroke-dasharray="4,4"/>
      <line x1="480" y1="84" x2="480" y2="480" stroke="{rule_solid}" stroke-width="1" stroke-dasharray="4,4"/>
      <line x1="808" y1="84" x2="808" y2="480" stroke="{rule_solid}" stroke-width="1" stroke-dasharray="4,4"/>

      <!-- messages -->
      <line x1="152" y1="128" x2="480" y2="128" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow{v})"/>
      <line x1="480" y1="164" x2="152" y2="164" stroke="{muted}" stroke-width="1.2" stroke-dasharray="5,4" marker-end="url(#arrow{v})"/>
      <line x1="808" y1="200" x2="480" y2="200" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow{v})"/>
      <line x1="480" y1="236" x2="808" y2="236" stroke="{muted}" stroke-width="1.2" stroke-dasharray="5,4" marker-end="url(#arrow{v})"/>
      <line x1="152" y1="276" x2="480" y2="276" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow{v})"/>
      <line x1="152" y1="312" x2="480" y2="312" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow{v})"/>
      <line x1="808" y1="348" x2="480" y2="348" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow{v})"/>
      <line x1="808" y1="384" x2="480" y2="384" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow{v})"/>
      <line x1="152" y1="424" x2="480" y2="424" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow{v})"/>
      <line x1="808" y1="460" x2="480" y2="460" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow{v})"/>

      <!-- message labels -->
      <rect x="272" y="108" width="88" height="12" rx="2" fill="{paper}"/>
      <text x="316" y="117" fill="{soft}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">COUNT OPTION 7</text>
      <rect x="290" y="144" width="52" height="12" rx="2" fill="{paper}"/>
      <text x="316" y="153" fill="{soft}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">READS 1</text>
      <rect x="600" y="180" width="88" height="12" rx="2" fill="{paper}"/>
      <text x="644" y="189" fill="{soft}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">COUNT OPTION 7</text>
      <rect x="618" y="216" width="52" height="12" rx="2" fill="{paper}"/>
      <text x="644" y="225" fill="{soft}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">READS 1</text>
      <rect x="272" y="256" width="88" height="12" rx="2" fill="{paper}"/>
      <text x="316" y="265" fill="{soft}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">DEACTIVATE OLD</text>
      <rect x="272" y="292" width="88" height="12" rx="2" fill="{paper}"/>
      <text x="316" y="301" fill="{soft}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">INSERT NEW ROW</text>
      <rect x="600" y="328" width="88" height="12" rx="2" fill="{paper}"/>
      <text x="644" y="337" fill="{soft}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">DEACTIVATE OLD</text>
      <rect x="600" y="364" width="88" height="12" rx="2" fill="{paper}"/>
      <text x="644" y="373" fill="{soft}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">INSERT NEW ROW</text>
      <rect x="284" y="404" width="64" height="12" rx="2" fill="{paper}"/>
      <text x="316" y="413" fill="{ink}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">COMMIT OK</text>
      <rect x="612" y="440" width="64" height="12" rx="2" fill="{paper}"/>
      <text x="644" y="449" fill="{ink}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">COMMIT OK</text>

      <!-- transaction starts -->
      <rect x="128" y="98" width="48" height="12" rx="2" fill="{paper}"/>
      <text x="152" y="107" fill="{muted}" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.1em">BEGIN</text>
      <rect x="784" y="170" width="48" height="12" rx="2" fill="{paper}"/>
      <text x="808" y="179" fill="{muted}" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.1em">BEGIN</text>

      <!-- actors -->
      <rect x="64" y="36" width="176" height="48" rx="6" fill="{paper}"/>
      <rect x="64" y="36" width="176" height="48" rx="6" fill="{muted010}" stroke="{soft}" stroke-width="1"/>
      <text x="152" y="58" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">Transaction A</text>
      <text x="152" y="74" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">READ COMMITTED</text>

      <rect x="392" y="36" width="176" height="48" rx="6" fill="{paper}"/>
      <rect x="392" y="36" width="176" height="48" rx="6" fill="{ink005}" stroke="{muted}" stroke-width="1"/>
      <text x="480" y="58" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">prices</text>
      <text x="480" y="74" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">option_id = 7</text>

      <rect x="720" y="36" width="176" height="48" rx="6" fill="{paper}"/>
      <rect x="720" y="36" width="176" height="48" rx="6" fill="{muted010}" stroke="{soft}" stroke-width="1"/>
      <text x="808" y="58" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">Transaction B</text>
      <text x="808" y="74" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">READ COMMITTED</text>

      <!-- broken end state -->
      <rect x="48" y="496" width="864" height="60" rx="8" fill="{accent_tint}" stroke="{accent}" stroke-width="1"/>
      <text x="68" y="517" fill="{accent}" font-size="7" font-family="'Geist Mono', monospace" letter-spacing="0.14em">RESULT</text>
      <text x="68" y="539" fill="{accent}" font-size="12" font-weight="600" font-family="'Geist', sans-serif">Two active prices for option 7</text>
      <text x="892" y="532" fill="{accent}" font-size="14" font-style="italic" font-family="'Instrument Serif', serif" text-anchor="end">neither transaction broke a rule it could see</text>

      <text x="48" y="588" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace" letter-spacing="0.06em">FIXES &#183; SERIALIZABLE &#183; SELECT ... FOR UPDATE ON THE OPTION ROW &#183; PARTIAL UNIQUE INDEX</text>

      <!-- legend -->
      <line x1="48" y1="636" x2="912" y2="636" stroke="{rule}" stroke-width="0.8"/>
      <text x="48" y="653" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace" letter-spacing="0.14em">LEGEND</text>
      <line x1="140" y1="649" x2="164" y2="649" stroke="{muted}" stroke-width="1.2"/>
      <text x="172" y="653" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Statement</text>
      <line x1="300" y1="649" x2="324" y2="649" stroke="{muted}" stroke-width="1.2" stroke-dasharray="5,4"/>
      <text x="332" y="653" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Result</text>
      <rect x="480" y="643" width="20" height="12" rx="2" fill="{ink002}" stroke="{ink030}" stroke-width="0.8" stroke-dasharray="4,4"/>
      <text x="508" y="653" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Stale-read window</text>
      <rect x="712" y="643" width="20" height="12" rx="2" fill="{accent_tint}" stroke="{accent}" stroke-width="0.8"/>
      <text x="740" y="653" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Broken invariant</text>
    </svg>
"""

SVG_C = """    <svg viewBox="0 0 960 672" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="isolation-anomalies{v}-title isolation-anomalies{v}-desc">
      <title id="isolation-anomalies{v}-title">What each isolation level actually stops</title>
      <desc id="isolation-anomalies{v}-desc">A matrix of PostgreSQL isolation levels against five concurrency anomalies, showing that the default READ COMMITTED still allows write skew with no error raised, that REPEATABLE READ stops everything except write skew, and that SERIALIZABLE stops all five at the price of serialization failures the application must catch and retry.</desc>
""" + DEFS + """
      <rect width="100%" height="100%" fill="{paper}"/>

      <!-- header row -->
      <rect x="48" y="104" width="224" height="56" rx="6" fill="{paper}" stroke="{ink010}" stroke-width="0.8"/>
      <text x="160" y="128" fill="{ink}" font-size="11" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">Isolation level</text>
      <text x="160" y="144" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">vs. anomaly</text>

      <rect x="284" y="104" width="116" height="56" rx="6" fill="{ink}"/>
      <text x="342" y="128" fill="{paper}" font-size="11" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">Dirty read</text>
      <text x="342" y="144" fill="{paper}" opacity="0.7" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle">uncommitted</text>

      <rect x="412" y="104" width="116" height="56" rx="6" fill="{ink}"/>
      <text x="470" y="128" fill="{paper}" font-size="11" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">Non-repeatable</text>
      <text x="470" y="144" fill="{paper}" opacity="0.7" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle">same row twice</text>

      <rect x="540" y="104" width="116" height="56" rx="6" fill="{ink}"/>
      <text x="598" y="128" fill="{paper}" font-size="11" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">Phantom read</text>
      <text x="598" y="144" fill="{paper}" opacity="0.7" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle">new rows appear</text>

      <rect x="668" y="104" width="116" height="56" rx="6" fill="{ink}"/>
      <text x="726" y="128" fill="{paper}" font-size="11" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">Lost update</text>
      <text x="726" y="144" fill="{paper}" opacity="0.7" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle">overwritten</text>

      <rect x="796" y="104" width="116" height="56" rx="6" fill="{ink}"/>
      <text x="854" y="128" fill="{paper}" font-size="11" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">Write skew</text>
      <text x="854" y="144" fill="{paper}" opacity="0.7" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle">invariant break</text>

      <!-- row 1: read committed -->
      <rect x="48" y="176" width="224" height="64" rx="4" fill="{paper}" stroke="{ink010}" stroke-width="0.8"/>
      <text x="68" y="206" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif">Read committed</text>
      <text x="68" y="224" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace">PostgreSQL default</text>

      <rect x="284" y="176" width="116" height="64" rx="4" fill="{ink005}" stroke="{ink010}" stroke-width="0.6"/>
      <rect x="337" y="196" width="10" height="10" rx="2" fill="{ink}"/>
      <text x="342" y="222" fill="{ink}" font-size="8" font-weight="600" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.08em">PREVENTED</text>

      <rect x="412" y="176" width="116" height="64" rx="4" fill="{paper}" stroke="{ink010}" stroke-width="0.6"/>
      <rect x="465" y="196" width="10" height="10" rx="2" fill="none" stroke="{ink030}" stroke-width="1.2"/>
      <text x="470" y="222" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.08em">POSSIBLE</text>

      <rect x="540" y="176" width="116" height="64" rx="4" fill="{paper}" stroke="{ink010}" stroke-width="0.6"/>
      <rect x="593" y="196" width="10" height="10" rx="2" fill="none" stroke="{ink030}" stroke-width="1.2"/>
      <text x="598" y="222" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.08em">POSSIBLE</text>

      <rect x="668" y="176" width="116" height="64" rx="4" fill="{paper}" stroke="{ink010}" stroke-width="0.6"/>
      <rect x="721" y="196" width="10" height="10" rx="2" fill="none" stroke="{ink030}" stroke-width="1.2"/>
      <text x="726" y="222" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.08em">POSSIBLE</text>

      <rect x="796" y="176" width="116" height="64" rx="4" fill="{accent_tint}" stroke="{accent}" stroke-width="1.4"/>
      <rect x="849" y="186" width="10" height="10" rx="2" fill="none" stroke="{accent}" stroke-width="1.4"/>
      <text x="854" y="212" fill="{accent}" font-size="8" font-weight="600" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.08em">POSSIBLE</text>
      <text x="854" y="228" fill="{accent}" opacity="0.85" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.1em">NO ERROR RAISED</text>

      <!-- row 2: repeatable read -->
      <rect x="48" y="248" width="224" height="64" rx="4" fill="{paper}" stroke="{ink010}" stroke-width="0.8"/>
      <text x="68" y="278" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif">Repeatable read</text>
      <text x="68" y="296" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace">snapshot isolation</text>

      <rect x="284" y="248" width="116" height="64" rx="4" fill="{ink005}" stroke="{ink010}" stroke-width="0.6"/>
      <rect x="337" y="268" width="10" height="10" rx="2" fill="{ink}"/>
      <text x="342" y="294" fill="{ink}" font-size="8" font-weight="600" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.08em">PREVENTED</text>

      <rect x="412" y="248" width="116" height="64" rx="4" fill="{ink005}" stroke="{ink010}" stroke-width="0.6"/>
      <rect x="465" y="268" width="10" height="10" rx="2" fill="{ink}"/>
      <text x="470" y="294" fill="{ink}" font-size="8" font-weight="600" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.08em">PREVENTED</text>

      <rect x="540" y="248" width="116" height="64" rx="4" fill="{ink005}" stroke="{ink010}" stroke-width="0.6"/>
      <rect x="593" y="268" width="10" height="10" rx="2" fill="{ink}"/>
      <text x="598" y="294" fill="{ink}" font-size="8" font-weight="600" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.08em">PREVENTED</text>

      <rect x="668" y="248" width="116" height="64" rx="4" fill="{ink005}" stroke="{ink010}" stroke-width="0.6"/>
      <rect x="721" y="268" width="10" height="10" rx="2" fill="{ink}"/>
      <text x="726" y="294" fill="{ink}" font-size="8" font-weight="600" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.08em">PREVENTED</text>

      <rect x="796" y="248" width="116" height="64" rx="4" fill="{paper}" stroke="{ink010}" stroke-width="0.6"/>
      <rect x="849" y="268" width="10" height="10" rx="2" fill="none" stroke="{ink030}" stroke-width="1.2"/>
      <text x="854" y="294" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.08em">POSSIBLE</text>

      <!-- row 3: serializable -->
      <rect x="48" y="320" width="224" height="64" rx="4" fill="{paper}" stroke="{ink010}" stroke-width="0.8"/>
      <text x="68" y="350" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif">Serializable</text>
      <text x="68" y="368" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace">predicate locks</text>

      <rect x="284" y="320" width="116" height="64" rx="4" fill="{ink005}" stroke="{ink010}" stroke-width="0.6"/>
      <rect x="337" y="340" width="10" height="10" rx="2" fill="{ink}"/>
      <text x="342" y="366" fill="{ink}" font-size="8" font-weight="600" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.08em">PREVENTED</text>

      <rect x="412" y="320" width="116" height="64" rx="4" fill="{ink005}" stroke="{ink010}" stroke-width="0.6"/>
      <rect x="465" y="340" width="10" height="10" rx="2" fill="{ink}"/>
      <text x="470" y="366" fill="{ink}" font-size="8" font-weight="600" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.08em">PREVENTED</text>

      <rect x="540" y="320" width="116" height="64" rx="4" fill="{ink005}" stroke="{ink010}" stroke-width="0.6"/>
      <rect x="593" y="340" width="10" height="10" rx="2" fill="{ink}"/>
      <text x="598" y="366" fill="{ink}" font-size="8" font-weight="600" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.08em">PREVENTED</text>

      <rect x="668" y="320" width="116" height="64" rx="4" fill="{ink005}" stroke="{ink010}" stroke-width="0.6"/>
      <rect x="721" y="340" width="10" height="10" rx="2" fill="{ink}"/>
      <text x="726" y="366" fill="{ink}" font-size="8" font-weight="600" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.08em">PREVENTED</text>

      <rect x="796" y="320" width="116" height="64" rx="4" fill="{ink005}" stroke="{ink010}" stroke-width="0.6"/>
      <rect x="849" y="340" width="10" height="10" rx="2" fill="{ink}"/>
      <text x="854" y="366" fill="{ink}" font-size="8" font-weight="600" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.08em">PREVENTED</text>

      <!-- the default -->
      <rect x="48" y="424" width="432" height="128" rx="8" fill="{ink002}" stroke="{ink030}" stroke-width="1" stroke-dasharray="4,4"/>
      <text x="68" y="450" fill="{muted}" font-size="7" font-family="'Geist Mono', monospace" letter-spacing="0.14em">READ COMMITTED IS THE DEFAULT</text>
      <text x="68" y="480" fill="{ink}" font-size="11" font-family="'Geist', sans-serif">A default PostgreSQL install runs every transaction</text>
      <text x="68" y="500" fill="{ink}" font-size="11" font-family="'Geist', sans-serif">at READ COMMITTED. Every anomaly in the top row</text>
      <text x="68" y="520" fill="{ink}" font-size="11" font-family="'Geist', sans-serif">except dirty read is reachable with no extra setup.</text>

      <!-- the cost -->
      <text x="512" y="450" fill="{muted}" font-size="7" font-family="'Geist Mono', monospace" letter-spacing="0.14em">THE COST &#183; SQLSTATE 40001</text>
      <text x="512" y="482" fill="{accent}" font-size="14" font-style="italic" font-family="'Instrument Serif', serif">serializable is the only row that stops</text>
      <text x="512" y="504" fill="{accent}" font-size="14" font-style="italic" font-family="'Instrument Serif', serif">write skew &#8212; and the only one that</text>
      <text x="512" y="526" fill="{accent}" font-size="14" font-style="italic" font-family="'Instrument Serif', serif">makes your code retry what it refuses</text>

      <!-- legend -->
      <line x1="48" y1="636" x2="912" y2="636" stroke="{rule}" stroke-width="0.8"/>
      <text x="48" y="653" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace" letter-spacing="0.14em">LEGEND</text>
      <rect x="140" y="644" width="10" height="10" rx="2" fill="{ink}"/>
      <text x="160" y="653" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Prevented by the level</text>
      <rect x="340" y="644" width="10" height="10" rx="2" fill="none" stroke="{ink030}" stroke-width="1.2"/>
      <text x="360" y="653" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Possible at this level</text>
      <rect x="540" y="644" width="10" height="10" rx="2" fill="none" stroke="{accent}" stroke-width="1.4"/>
      <text x="560" y="653" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Write skew under the default</text>
    </svg>
"""

DIAGRAMS = [
    ("04-price-schema", "Database schema &#183; Diagram Design",
     "One active price, enforced by the schema", SVG_A),
    ("05-write-skew", "Sequence &#183; Diagram Design",
     "Why both writes succeeded and the invariant broke", SVG_B),
    ("06-isolation-anomalies", "Matrix &#183; Diagram Design",
     "What each isolation level actually stops", SVG_C),
]

if __name__ == "__main__":
    render_all(DIAGRAMS)
