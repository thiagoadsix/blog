from common import DEFS, render_all

SVG_A = """    <svg viewBox="0 0 960 672" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="explain-plan{v}-title explain-plan{v}-desc">
      <title id="explain-plan{v}-title">How to read an EXPLAIN ANALYZE plan</title>
      <desc id="explain-plan{v}-desc">A plan tree read from the deepest node upward. The sequential scan on orders was estimated to return one row but returned 48,210, so the planner picked a nested loop and then executed the inner index scan 48,210 times, which is where almost all of the 842 milliseconds is spent.</desc>
""" + DEFS + """
      <rect width="100%" height="100%" fill="{paper}"/>

      <!-- query strip -->
      <text x="32" y="44" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace" letter-spacing="0.14em">THE QUERY</text>
      <text x="32" y="66" fill="{ink}" font-size="10" font-family="'Geist Mono', monospace">SELECT o.id, c.name FROM orders o JOIN customers c ON c.id = o.customer_id WHERE o.status = 'pending'</text>
      <line x1="32" y1="84" x2="928" y2="84" stroke="{rule}" stroke-width="0.8"/>

      <!-- connectors: children feed the parent upward -->
      <path d="M 312 304 L 312 264 A 8 8 0 0 1 320 256 L 412 256 A 8 8 0 0 0 420 248 L 420 208" fill="none" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow{v})"/>
      <path d="M 648 304 L 648 264 A 8 8 0 0 0 640 256 L 548 256 A 8 8 0 0 1 540 248 L 540 208" fill="none" stroke="{accent}" stroke-width="1.5" marker-end="url(#arrow-accent{v})"/>
      <line x1="688" y1="160" x2="656" y2="160" stroke="{accent}" stroke-width="1.2" stroke-dasharray="4,3" marker-end="url(#arrow-accent{v})"/>

      <!-- connector labels -->
      <rect x="328" y="236" width="76" height="12" rx="2" fill="{paper}"/>
      <text x="366" y="245" fill="{soft}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">48210 ROWS</text>

      <rect x="552" y="236" width="84" height="12" rx="2" fill="{paper}"/>
      <text x="594" y="245" fill="{accent}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">LOOPS=48210</text>

      <!-- root plan node -->
      <rect x="304" y="112" width="352" height="96" rx="6" fill="{paper}"/>
      <rect x="304" y="112" width="352" height="96" rx="6" fill="{paper}" stroke="{ink}" stroke-width="1"/>
      <rect x="312" y="120" width="36" height="12" rx="2" fill="transparent" stroke="{ink040}" stroke-width="0.8"/>
      <text x="330" y="129" fill="{muted}" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.08em">JOIN</text>
      <text x="480" y="154" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">Nested Loop</text>
      <text x="480" y="176" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">cost=0.43..8112.90 rows=1 width=64</text>
      <text x="480" y="194" fill="{ink}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">actual time=0.05..842.11 rows=48210 loops=1</text>

      <!-- estimate-gap callout (focal) -->
      <rect x="688" y="112" width="224" height="96" rx="6" fill="{paper}"/>
      <rect x="688" y="112" width="224" height="96" rx="6" fill="{accent_tint}" stroke="{accent}" stroke-width="1.2"/>
      <text x="800" y="140" fill="{accent}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.14em">ESTIMATE VS ACTUAL</text>
      <text x="800" y="166" fill="{accent}" font-size="13" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">1 row planned</text>
      <text x="800" y="188" fill="{accent}" font-size="13" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">48,210 returned</text>

      <!-- outer child -->
      <rect x="160" y="304" width="304" height="112" rx="6" fill="{paper}"/>
      <rect x="160" y="304" width="304" height="112" rx="6" fill="{ink003}" stroke="{ink030}" stroke-width="1"/>
      <rect x="168" y="312" width="36" height="12" rx="2" fill="transparent" stroke="{ink040}" stroke-width="0.8"/>
      <text x="186" y="321" fill="{muted}" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.08em">SCAN</text>
      <text x="312" y="346" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">Seq Scan</text>
      <text x="312" y="366" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">on orders</text>
      <text x="312" y="384" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">Filter: (status = 'pending')</text>
      <text x="312" y="402" fill="{ink}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">rows=1 &#183; actual rows=48210</text>

      <!-- inner child -->
      <rect x="496" y="304" width="304" height="112" rx="6" fill="{paper}"/>
      <rect x="496" y="304" width="304" height="112" rx="6" fill="{ink005}" stroke="{muted}" stroke-width="1"/>
      <rect x="504" y="312" width="36" height="12" rx="2" fill="transparent" stroke="{ink040}" stroke-width="0.8"/>
      <text x="522" y="321" fill="{muted}" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.08em">SCAN</text>
      <text x="648" y="346" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">Index Scan</text>
      <text x="648" y="366" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">using customers_pkey</text>
      <text x="648" y="384" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">actual rows=1 loops=48210</text>
      <text x="648" y="402" fill="{ink}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">0.017 ms per loop</text>

      <!-- execution order markers -->
      <circle cx="136" cy="360" r="9" fill="{paper}" stroke="{muted}" stroke-width="1"/>
      <text x="136" y="363" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">1</text>
      <circle cx="824" cy="360" r="9" fill="{paper}" stroke="{muted}" stroke-width="1"/>
      <text x="824" y="363" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">2</text>
      <circle cx="280" cy="160" r="9" fill="{paper}" stroke="{muted}" stroke-width="1"/>
      <text x="280" y="163" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">3</text>

      <!-- where the time goes -->
      <text x="32" y="456" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace" letter-spacing="0.14em">WHERE THE 842 MS GOES</text>
      <text x="304" y="486" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="end">Seq Scan, once</text>
      <rect x="320" y="472" width="12" height="20" rx="2" fill="{ink010}" stroke="{muted}" stroke-width="0.8"/>
      <text x="344" y="486" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace">22 ms</text>
      <text x="304" y="518" fill="{ink}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="end">Index Scan, per row</text>
      <rect x="320" y="504" width="480" height="20" rx="2" fill="{ink005}" stroke="{muted}" stroke-width="0.8"/>
      <text x="332" y="518" fill="{ink}" font-size="9" font-family="'Geist Mono', monospace">820 ms spread across 48,210 loops</text>

      <!-- editorial payoff -->
      <text x="480" y="576" fill="{ink}" font-size="15" font-style="italic" font-family="'Instrument Serif', serif" text-anchor="middle">one wrong estimate, forty-eight thousand trips to the index</text>

      <!-- legend -->
      <line x1="32" y1="636" x2="928" y2="636" stroke="{rule}" stroke-width="0.8"/>
      <text x="32" y="653" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace" letter-spacing="0.14em">LEGEND</text>
      <rect x="116" y="643" width="24" height="12" rx="2" fill="{paper}" stroke="{ink}" stroke-width="1"/>
      <text x="148" y="653" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Plan node</text>
      <line x1="256" y1="649" x2="280" y2="649" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow{v})"/>
      <text x="288" y="653" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Rows to parent</text>
      <line x1="420" y1="649" x2="444" y2="649" stroke="{accent}" stroke-width="1.5" marker-end="url(#arrow-accent{v})"/>
      <text x="452" y="653" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Repeated per row</text>
      <circle cx="600" cy="649" r="7" fill="{paper}" stroke="{muted}" stroke-width="1"/>
      <text x="600" y="652" fill="{muted}" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle">1</text>
      <text x="614" y="653" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Execution order</text>
      <rect x="760" y="643" width="24" height="12" rx="2" fill="{accent_tint}" stroke="{accent}" stroke-width="1"/>
      <text x="792" y="653" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Estimate gap</text>
    </svg>
"""

SVG_B = """    <svg viewBox="0 0 960 672" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="join-strategies{v}-title join-strategies{v}-desc">
      <title id="join-strategies{v}-title">Three ways to join, and when each one wins</title>
      <desc id="join-strategies{v}-desc">A comparison of nested loop, hash join and merge join for the same two-table join, showing each mechanism, its cost shape and memory need, and the input conditions that make the planner choose it, plus the failure mode where a nested loop is picked on a bad row estimate.</desc>
""" + DEFS + """
      <rect width="100%" height="100%" fill="{paper}"/>

      <text x="32" y="40" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace" letter-spacing="0.14em">SAME JOIN, THREE PLANS</text>
      <text x="32" y="60" fill="{ink}" font-size="10" font-family="'Geist Mono', monospace">orders o JOIN customers c ON c.id = o.customer_id</text>

      <text x="32" y="84" fill="{soft}" font-size="8" font-family="'Geist Mono', monospace" letter-spacing="0.14em">STRATEGY</text>
      <text x="208" y="84" fill="{soft}" font-size="8" font-family="'Geist Mono', monospace" letter-spacing="0.14em">MECHANISM</text>
      <text x="576" y="84" fill="{soft}" font-size="8" font-family="'Geist Mono', monospace" letter-spacing="0.14em">COST SHAPE</text>
      <text x="736" y="84" fill="{soft}" font-size="8" font-family="'Geist Mono', monospace" letter-spacing="0.14em">PLANNER PICKS IT WHEN</text>
      <line x1="32" y1="92" x2="928" y2="92" stroke="{rule}" stroke-width="0.8"/>
      <line x1="32" y1="232" x2="928" y2="232" stroke="{rule}" stroke-width="0.8"/>
      <line x1="32" y1="376" x2="928" y2="376" stroke="{rule}" stroke-width="0.8"/>

      <!-- connectors -->
      <line x1="288" y1="160" x2="424" y2="160" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow{v})"/>
      <line x1="280" y1="304" x2="336" y2="304" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow{v})"/>
      <line x1="488" y1="304" x2="432" y2="304" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow{v})"/>
      <line x1="368" y1="430" x2="440" y2="430" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow{v})"/>
      <line x1="368" y1="466" x2="440" y2="466" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow{v})"/>

      <!-- connector labels -->
      <rect x="310" y="140" width="92" height="12" rx="2" fill="{paper}"/>
      <text x="356" y="149" fill="{soft}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">1 SEEK PER ROW</text>
      <rect x="286" y="284" width="44" height="12" rx="2" fill="{paper}"/>
      <text x="308" y="293" fill="{soft}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">BUILD</text>
      <rect x="438" y="284" width="44" height="12" rx="2" fill="{paper}"/>
      <text x="460" y="293" fill="{soft}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">PROBE</text>
      <rect x="376" y="410" width="56" height="12" rx="2" fill="{paper}"/>
      <text x="404" y="419" fill="{soft}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">IN ORDER</text>

      <!-- row 1: nested loop -->
      <text x="32" y="154" fill="{ink}" font-size="13" font-weight="600" font-family="'Geist', sans-serif">Nested Loop</text>
      <text x="32" y="172" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace">probe per outer row</text>

      <rect x="224" y="128" width="64" height="64" rx="4" fill="{paper}"/>
      <rect x="224" y="128" width="64" height="64" rx="4" fill="{muted010}" stroke="{soft}" stroke-width="1"/>
      <line x1="224" y1="144" x2="288" y2="144" stroke="{soft}" stroke-width="0.6"/>
      <line x1="224" y1="160" x2="288" y2="160" stroke="{soft}" stroke-width="0.6"/>
      <line x1="224" y1="176" x2="288" y2="176" stroke="{soft}" stroke-width="0.6"/>
      <text x="256" y="208" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle">outer rows</text>

      <rect x="432" y="128" width="96" height="64" rx="4" fill="{paper}"/>
      <rect x="432" y="128" width="96" height="64" rx="4" fill="{ink005}" stroke="{muted}" stroke-width="1"/>
      <text x="480" y="156" fill="{ink}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">customers_pkey</text>
      <text x="480" y="172" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle">index seek</text>
      <text x="480" y="208" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle">inner side</text>

      <text x="648" y="154" fill="{ink}" font-size="11" font-family="'Geist Mono', monospace" text-anchor="middle">O(n * m)</text>
      <text x="648" y="172" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">no extra memory</text>

      <text x="736" y="152" fill="{muted}" font-size="10" font-family="'Geist', sans-serif">Small outer side, with an index</text>
      <text x="736" y="168" fill="{muted}" font-size="10" font-family="'Geist', sans-serif">on the inner join key</text>

      <!-- row 2: hash join -->
      <text x="32" y="298" fill="{ink}" font-size="13" font-weight="600" font-family="'Geist', sans-serif">Hash Join</text>
      <text x="32" y="316" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace">build, then probe</text>

      <rect x="224" y="284" width="56" height="40" rx="4" fill="{muted010}" stroke="{soft}" stroke-width="1"/>
      <text x="252" y="308" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle">smaller</text>
      <text x="252" y="348" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle">build side</text>

      <rect x="336" y="272" width="96" height="64" rx="4" fill="{paper}"/>
      <rect x="336" y="272" width="96" height="64" rx="4" fill="{ink005}" stroke="{muted}" stroke-width="1"/>
      <text x="384" y="294" fill="{ink}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">hash table</text>
      <text x="384" y="308" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle">in work_mem</text>
      <line x1="360" y1="316" x2="360" y2="336" stroke="{muted}" stroke-width="0.6"/>
      <line x1="384" y1="316" x2="384" y2="336" stroke="{muted}" stroke-width="0.6"/>
      <line x1="408" y1="316" x2="408" y2="336" stroke="{muted}" stroke-width="0.6"/>

      <rect x="488" y="284" width="56" height="40" rx="4" fill="{muted010}" stroke="{soft}" stroke-width="1"/>
      <text x="516" y="308" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle">larger</text>
      <text x="516" y="348" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle">probe side</text>

      <text x="648" y="298" fill="{ink}" font-size="11" font-family="'Geist Mono', monospace" text-anchor="middle">O(n + m)</text>
      <text x="648" y="316" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">+ build memory</text>

      <text x="736" y="288" fill="{muted}" font-size="10" font-family="'Geist', sans-serif">Large unsorted inputs, and</text>
      <text x="736" y="304" fill="{muted}" font-size="10" font-family="'Geist', sans-serif">enough work_mem to hold the</text>
      <text x="736" y="320" fill="{muted}" font-size="10" font-family="'Geist', sans-serif">smaller side in one hash table</text>

      <!-- row 3: merge join -->
      <text x="32" y="442" fill="{ink}" font-size="13" font-weight="600" font-family="'Geist', sans-serif">Merge Join</text>
      <text x="32" y="460" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace">zip two streams</text>

      <text x="224" y="408" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace">two sorted inputs</text>
      <rect x="224" y="416" width="144" height="28" rx="4" fill="{muted010}" stroke="{soft}" stroke-width="1"/>
      <text x="296" y="434" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">1 &#183; 4 &#183; 7 &#183; 9</text>
      <rect x="224" y="452" width="144" height="28" rx="4" fill="{ink005}" stroke="{muted}" stroke-width="1"/>
      <text x="296" y="470" fill="{ink}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">2 &#183; 4 &#183; 8 &#183; 9</text>
      <text x="224" y="500" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace">a sort is added first if they are not already ordered</text>

      <rect x="440" y="424" width="88" height="48" rx="4" fill="{paper}"/>
      <rect x="440" y="424" width="88" height="48" rx="4" fill="{paper}" stroke="{ink}" stroke-width="1"/>
      <text x="484" y="446" fill="{ink}" font-size="11" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">Merge</text>
      <text x="484" y="462" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle">one pass each</text>

      <text x="648" y="434" fill="{ink}" font-size="10" font-family="'Geist Mono', monospace" text-anchor="middle">O(n log n +</text>
      <text x="648" y="450" fill="{ink}" font-size="10" font-family="'Geist Mono', monospace" text-anchor="middle">m log m)</text>
      <text x="648" y="470" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">only if it sorts</text>

      <text x="736" y="432" fill="{muted}" font-size="10" font-family="'Geist', sans-serif">Inputs already sorted &#8212; by</text>
      <text x="736" y="448" fill="{muted}" font-size="10" font-family="'Geist', sans-serif">index order, or by a merge-</text>
      <text x="736" y="464" fill="{muted}" font-size="10" font-family="'Geist', sans-serif">friendly ORDER BY</text>

      <!-- failure mode (focal) -->
      <rect x="32" y="536" width="896" height="64" rx="8" fill="{accent_05}" stroke="{accent_50}" stroke-width="1" stroke-dasharray="4,4"/>
      <text x="56" y="562" fill="{accent}" font-size="8" font-family="'Geist Mono', monospace" letter-spacing="0.14em">WHEN THE NESTED LOOP GOES WRONG</text>
      <text x="56" y="586" fill="{accent}" font-size="15" font-style="italic" font-family="'Instrument Serif', serif">the planner expects one outer row, gets 48,210 &#8212; and pays for every one of them</text>

      <!-- legend -->
      <line x1="32" y1="636" x2="928" y2="636" stroke="{rule}" stroke-width="0.8"/>
      <text x="32" y="653" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace" letter-spacing="0.14em">LEGEND</text>
      <rect x="120" y="643" width="24" height="12" rx="2" fill="{muted010}" stroke="{soft}" stroke-width="1"/>
      <text x="152" y="653" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Driving side</text>
      <rect x="300" y="643" width="24" height="12" rx="2" fill="{ink005}" stroke="{muted}" stroke-width="1"/>
      <text x="332" y="653" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Probed side</text>
      <line x1="480" y1="649" x2="504" y2="649" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow{v})"/>
      <text x="512" y="653" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Row probe</text>
      <rect x="664" y="643" width="24" height="12" rx="2" fill="{accent_05}" stroke="{accent_50}" stroke-width="1" stroke-dasharray="4,4"/>
      <text x="696" y="653" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Failure mode</text>
    </svg>
"""

SVG_C = """    <svg viewBox="0 0 960 672" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="index-prefix{v}-title index-prefix{v}-desc">
      <title id="index-prefix{v}-title">Which queries can use a composite index</title>
      <desc id="index-prefix{v}-desc">Six WHERE clauses matched against a three-column composite index on orders, showing how far into the index each one can seek: equality predicates consume the prefix columns left to right, the first range predicate ends the seek, and a missing leading column or a cast over the column defeats the index entirely.</desc>
""" + DEFS + """
      <rect width="100%" height="100%" fill="{paper}"/>

      <text x="32" y="48" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace" letter-spacing="0.14em">THE INDEX</text>
      <text x="32" y="72" fill="{ink}" font-size="11" font-family="'Geist Mono', monospace">CREATE INDEX ON orders (tenant_id, status, created_at)</text>

      <!-- header row -->
      <rect x="32" y="104" width="352" height="48" rx="6" fill="{paper}" stroke="{ink010}" stroke-width="0.8"/>
      <text x="48" y="126" fill="{ink}" font-size="11" font-weight="600" font-family="'Geist', sans-serif">Predicate</text>
      <text x="48" y="142" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace">what the query filters on</text>

      <rect x="400" y="104" width="88" height="48" rx="6" fill="{ink}"/>
      <text x="444" y="124" fill="{paper}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">tenant_id</text>
      <text x="444" y="140" fill="{paper}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" opacity="0.75">column 1</text>

      <rect x="500" y="104" width="88" height="48" rx="6" fill="{ink}"/>
      <text x="544" y="124" fill="{paper}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">status</text>
      <text x="544" y="140" fill="{paper}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" opacity="0.75">column 2</text>

      <rect x="600" y="104" width="88" height="48" rx="6" fill="{ink}"/>
      <text x="644" y="124" fill="{paper}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">created_at</text>
      <text x="644" y="140" fill="{paper}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" opacity="0.75">column 3</text>

      <rect x="704" y="104" width="224" height="48" rx="6" fill="{paper}" stroke="{ink010}" stroke-width="0.8"/>
      <text x="720" y="126" fill="{ink}" font-size="11" font-weight="600" font-family="'Geist', sans-serif">Seek reach</text>
      <text x="720" y="142" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace">how much of the index is used</text>

      <!-- row 0 -->
      <rect x="32" y="168" width="352" height="44" rx="4" fill="{paper}" stroke="{ink010}" stroke-width="0.8"/>
      <text x="48" y="195" fill="{ink}" font-size="10" font-family="'Geist Mono', monospace">tenant_id = ?</text>
      <rect x="400" y="168" width="88" height="44" rx="4" fill="{ink}"/>
      <text x="444" y="187" fill="{paper}" font-size="11" font-family="'Geist Mono', monospace" text-anchor="middle">=</text>
      <text x="444" y="201" fill="{paper}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" opacity="0.75">seek</text>
      <rect x="500" y="168" width="88" height="44" rx="4" fill="{paper}" stroke="{ink010}" stroke-width="0.8"/>
      <text x="544" y="194" fill="{soft}" font-size="11" font-family="'Geist Mono', monospace" text-anchor="middle">&#8212;</text>
      <rect x="600" y="168" width="88" height="44" rx="4" fill="{paper}" stroke="{ink010}" stroke-width="0.8"/>
      <text x="644" y="194" fill="{soft}" font-size="11" font-family="'Geist Mono', monospace" text-anchor="middle">&#8212;</text>
      <rect x="704" y="168" width="224" height="44" rx="4" fill="{paper}" stroke="{ink010}" stroke-width="0.8"/>
      <text x="720" y="188" fill="{ink}" font-size="11" font-weight="600" font-family="'Geist', sans-serif">Seeks column 1</text>
      <text x="720" y="202" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace">prefix of length 1</text>

      <!-- row 1 -->
      <rect x="32" y="224" width="352" height="44" rx="4" fill="{paper}" stroke="{ink010}" stroke-width="0.8"/>
      <text x="48" y="251" fill="{ink}" font-size="10" font-family="'Geist Mono', monospace">tenant_id = ? AND status = ?</text>
      <rect x="400" y="224" width="88" height="44" rx="4" fill="{ink}"/>
      <text x="444" y="243" fill="{paper}" font-size="11" font-family="'Geist Mono', monospace" text-anchor="middle">=</text>
      <text x="444" y="257" fill="{paper}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" opacity="0.75">seek</text>
      <rect x="500" y="224" width="88" height="44" rx="4" fill="{ink}"/>
      <text x="544" y="243" fill="{paper}" font-size="11" font-family="'Geist Mono', monospace" text-anchor="middle">=</text>
      <text x="544" y="257" fill="{paper}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" opacity="0.75">seek</text>
      <rect x="600" y="224" width="88" height="44" rx="4" fill="{paper}" stroke="{ink010}" stroke-width="0.8"/>
      <text x="644" y="250" fill="{soft}" font-size="11" font-family="'Geist Mono', monospace" text-anchor="middle">&#8212;</text>
      <rect x="704" y="224" width="224" height="44" rx="4" fill="{paper}" stroke="{ink010}" stroke-width="0.8"/>
      <text x="720" y="244" fill="{ink}" font-size="11" font-weight="600" font-family="'Geist', sans-serif">Seeks columns 1 and 2</text>
      <text x="720" y="258" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace">prefix of length 2</text>

      <!-- row 2 -->
      <rect x="32" y="280" width="352" height="44" rx="4" fill="{paper}" stroke="{ink010}" stroke-width="0.8"/>
      <text x="48" y="307" fill="{ink}" font-size="10" font-family="'Geist Mono', monospace">tenant_id = ? AND status = ? AND created_at &gt; ?</text>
      <rect x="400" y="280" width="88" height="44" rx="4" fill="{ink}"/>
      <text x="444" y="299" fill="{paper}" font-size="11" font-family="'Geist Mono', monospace" text-anchor="middle">=</text>
      <text x="444" y="313" fill="{paper}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" opacity="0.75">seek</text>
      <rect x="500" y="280" width="88" height="44" rx="4" fill="{ink}"/>
      <text x="544" y="299" fill="{paper}" font-size="11" font-family="'Geist Mono', monospace" text-anchor="middle">=</text>
      <text x="544" y="313" fill="{paper}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" opacity="0.75">seek</text>
      <rect x="600" y="280" width="88" height="44" rx="4" fill="{ink010}" stroke="{ink030}" stroke-width="1"/>
      <text x="644" y="299" fill="{ink}" font-size="11" font-family="'Geist Mono', monospace" text-anchor="middle">&gt;</text>
      <text x="644" y="313" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle">range</text>
      <rect x="704" y="280" width="224" height="44" rx="4" fill="{paper}" stroke="{ink010}" stroke-width="0.8"/>
      <text x="720" y="300" fill="{ink}" font-size="11" font-weight="600" font-family="'Geist', sans-serif">Seeks all three</text>
      <text x="720" y="314" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace">the range ends the seek</text>

      <!-- row 3 -->
      <rect x="32" y="336" width="352" height="44" rx="4" fill="{paper}" stroke="{ink010}" stroke-width="0.8"/>
      <text x="48" y="363" fill="{ink}" font-size="10" font-family="'Geist Mono', monospace">status = ?</text>
      <rect x="400" y="336" width="88" height="44" rx="4" fill="{accent_tint}" stroke="{accent}" stroke-width="1.4"/>
      <text x="444" y="355" fill="{accent}" font-size="9" font-weight="600" font-family="'Geist Mono', monospace" text-anchor="middle">no prefix</text>
      <text x="444" y="369" fill="{accent}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" opacity="0.85">cannot seek</text>
      <rect x="500" y="336" width="88" height="44" rx="4" fill="{muted010}" stroke="{soft}" stroke-width="1"/>
      <text x="544" y="362" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">filter</text>
      <rect x="600" y="336" width="88" height="44" rx="4" fill="{paper}" stroke="{ink010}" stroke-width="0.8"/>
      <text x="644" y="362" fill="{soft}" font-size="11" font-family="'Geist Mono', monospace" text-anchor="middle">&#8212;</text>
      <rect x="704" y="336" width="224" height="44" rx="4" fill="{paper}" stroke="{ink010}" stroke-width="0.8"/>
      <text x="720" y="356" fill="{ink}" font-size="11" font-weight="600" font-family="'Geist', sans-serif">No seek</text>
      <text x="720" y="370" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace">leading column is missing</text>

      <!-- row 4 -->
      <rect x="32" y="392" width="352" height="44" rx="4" fill="{paper}" stroke="{ink010}" stroke-width="0.8"/>
      <text x="48" y="419" fill="{ink}" font-size="10" font-family="'Geist Mono', monospace">tenant_id = ? AND created_at &gt; ?</text>
      <rect x="400" y="392" width="88" height="44" rx="4" fill="{ink}"/>
      <text x="444" y="411" fill="{paper}" font-size="11" font-family="'Geist Mono', monospace" text-anchor="middle">=</text>
      <text x="444" y="425" fill="{paper}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" opacity="0.75">seek</text>
      <rect x="500" y="392" width="88" height="44" rx="4" fill="{paper}" stroke="{ink010}" stroke-width="0.8"/>
      <text x="544" y="418" fill="{soft}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">skipped</text>
      <rect x="600" y="392" width="88" height="44" rx="4" fill="{muted010}" stroke="{soft}" stroke-width="1"/>
      <text x="644" y="418" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">filter</text>
      <rect x="704" y="392" width="224" height="44" rx="4" fill="{paper}" stroke="{ink010}" stroke-width="0.8"/>
      <text x="720" y="412" fill="{ink}" font-size="11" font-weight="600" font-family="'Geist', sans-serif">Seeks column 1 only</text>
      <text x="720" y="426" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace">created_at is filtered, not sought</text>

      <!-- row 5 -->
      <rect x="32" y="448" width="352" height="44" rx="4" fill="{paper}" stroke="{ink010}" stroke-width="0.8"/>
      <text x="48" y="475" fill="{ink}" font-size="10" font-family="'Geist Mono', monospace">tenant_id::text = ?</text>
      <rect x="400" y="448" width="88" height="44" rx="4" fill="{accent_tint}" stroke="{accent}" stroke-width="1.4"/>
      <text x="444" y="467" fill="{accent}" font-size="9" font-weight="600" font-family="'Geist Mono', monospace" text-anchor="middle">cast</text>
      <text x="444" y="481" fill="{accent}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" opacity="0.85">not sargable</text>
      <rect x="500" y="448" width="88" height="44" rx="4" fill="{paper}" stroke="{ink010}" stroke-width="0.8"/>
      <text x="544" y="474" fill="{soft}" font-size="11" font-family="'Geist Mono', monospace" text-anchor="middle">&#8212;</text>
      <rect x="600" y="448" width="88" height="44" rx="4" fill="{paper}" stroke="{ink010}" stroke-width="0.8"/>
      <text x="644" y="474" fill="{soft}" font-size="11" font-family="'Geist Mono', monospace" text-anchor="middle">&#8212;</text>
      <rect x="704" y="448" width="224" height="44" rx="4" fill="{paper}" stroke="{ink010}" stroke-width="0.8"/>
      <text x="720" y="468" fill="{ink}" font-size="11" font-weight="600" font-family="'Geist', sans-serif">Not sargable</text>
      <text x="720" y="482" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace">the cast hides the column</text>

      <!-- the rule -->
      <rect x="32" y="528" width="896" height="56" rx="8" fill="{ink002}" stroke="{ink010}" stroke-width="1"/>
      <text x="56" y="552" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace" letter-spacing="0.14em">THE RULE</text>
      <text x="56" y="574" fill="{ink}" font-size="15" font-style="italic" font-family="'Instrument Serif', serif">equality predicates consume prefix columns left to right, and the first range predicate ends the seek</text>

      <!-- legend -->
      <line x1="32" y1="636" x2="928" y2="636" stroke="{rule}" stroke-width="0.8"/>
      <text x="32" y="653" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace" letter-spacing="0.14em">LEGEND</text>
      <rect x="112" y="643" width="24" height="12" rx="2" fill="{ink}"/>
      <text x="144" y="653" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Seek</text>
      <rect x="232" y="643" width="24" height="12" rx="2" fill="{ink010}" stroke="{ink030}" stroke-width="1"/>
      <text x="264" y="653" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Range ends seek</text>
      <rect x="416" y="643" width="24" height="12" rx="2" fill="{muted010}" stroke="{soft}" stroke-width="1"/>
      <text x="448" y="653" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Filter only</text>
      <rect x="568" y="643" width="24" height="12" rx="2" fill="{paper}" stroke="{ink010}" stroke-width="1"/>
      <text x="600" y="653" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Unused</text>
      <rect x="696" y="643" width="24" height="12" rx="2" fill="{accent_tint}" stroke="{accent}" stroke-width="1"/>
      <text x="728" y="653" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Index defeated</text>
    </svg>
"""

DIAGRAMS = [
    ("07-explain-plan", "Tree &#183; Diagram Design", "How to read an EXPLAIN ANALYZE plan", SVG_A),
    ("08-join-strategies", "Comparison &#183; Diagram Design", "Three ways to join, and when each one wins", SVG_B),
    ("09-index-prefix", "Matrix &#183; Diagram Design", "Which queries can use a composite index", SVG_C),
]

if __name__ == "__main__":
    render_all(DIAGRAMS)
