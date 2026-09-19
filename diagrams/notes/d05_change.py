from common import DEFS, render_all

SVG_A = """    <svg viewBox="0 0 960 672" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="expand-contract{v}-title expand-contract{v}-desc">
      <title id="expand-contract{v}-title">Renaming a column without downtime</title>
      <desc id="expand-contract{v}-desc">Renaming users.email to users.email_address takes five deploys, with the schema and the deployed application shown as parallel tracks: the two columns deliberately overlap, so at every step the previous version of the application is still correct against the current schema and any deploy can be reverted without a schema rollback, right up to the final drop, which cannot be undone that way.</desc>
""" + DEFS + """
      <rect width="100%" height="100%" fill="{paper}"/>

      <!-- schema track -->
      <text x="32" y="48" fill="{muted}" font-size="7" font-family="'Geist Mono', monospace" letter-spacing="0.14em">SCHEMA &#183; TABLE users</text>

      <!-- application track eyebrow -->
      <text x="32" y="428" fill="{muted}" font-size="7" font-family="'Geist Mono', monospace" letter-spacing="0.14em">APPLICATION &#183; DEPLOYED CODE</text>

      <!-- time axis -->
      <line x1="152" y1="296" x2="928" y2="296" stroke="{rule_solid}" stroke-width="1" marker-end="url(#arrow{v})"/>
      <line x1="248" y1="290" x2="248" y2="302" stroke="{rule_solid}" stroke-width="1"/>
      <line x1="384" y1="290" x2="384" y2="302" stroke="{rule_solid}" stroke-width="1"/>
      <line x1="520" y1="290" x2="520" y2="302" stroke="{rule_solid}" stroke-width="1"/>
      <line x1="656" y1="290" x2="656" y2="302" stroke="{rule_solid}" stroke-width="1"/>
      <line x1="792" y1="290" x2="792" y2="302" stroke="{rule_solid}" stroke-width="1"/>

      <!-- point of no return guide -->
      <line x1="792" y1="256" x2="792" y2="286" stroke="{accent}" stroke-width="1" stroke-dasharray="4,4"/>
      <line x1="792" y1="340" x2="792" y2="360" stroke="{accent}" stroke-width="1" stroke-dasharray="4,4"/>
      <line x1="792" y1="400" x2="792" y2="440" stroke="{accent}" stroke-width="1" stroke-dasharray="4,4"/>

      <!-- schema bars -->
      <rect x="152" y="64" width="640" height="56" rx="6" fill="{paper}"/>
      <rect x="152" y="64" width="640" height="56" rx="6" fill="{ink005}" stroke="{muted}" stroke-width="1"/>
      <text x="168" y="92" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif">Old column</text>
      <text x="168" y="108" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace">users.email</text>
      <line x1="792" y1="66" x2="792" y2="118" stroke="{accent}" stroke-width="2.5"/>

      <rect x="248" y="132" width="672" height="56" rx="6" fill="{paper}"/>
      <rect x="248" y="132" width="672" height="56" rx="6" fill="{ink005}" stroke="{muted}" stroke-width="1"/>
      <text x="264" y="160" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif">New column</text>
      <text x="264" y="176" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace">users.email_address, nullable</text>

      <rect x="520" y="200" width="136" height="52" rx="6" fill="{paper}"/>
      <rect x="520" y="200" width="136" height="52" rx="6" fill="{ink002}" stroke="{ink030}" stroke-width="1" stroke-dasharray="4,3"/>
      <text x="588" y="224" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">Backfill</text>
      <text x="588" y="240" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">batched &#183; resumable</text>

      <text x="812" y="220" fill="{ink}" font-size="14" font-style="italic" font-family="'Instrument Serif', serif" text-anchor="middle">both columns exist</text>
      <text x="812" y="238" fill="{ink}" font-size="14" font-style="italic" font-family="'Instrument Serif', serif" text-anchor="middle">on purpose</text>

      <!-- deploy markers -->
      <circle cx="248" cy="296" r="4" fill="{muted}"/>
      <circle cx="384" cy="296" r="4" fill="{muted}"/>
      <circle cx="520" cy="296" r="4" fill="{muted}"/>
      <circle cx="656" cy="296" r="4" fill="{muted}"/>
      <circle cx="792" cy="296" r="6" fill="{accent}"/>

      <text x="248" y="318" fill="{muted}" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.14em">DEPLOY 1</text>
      <text x="248" y="332" fill="{ink}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">ADD COLUMN</text>
      <text x="384" y="318" fill="{muted}" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.14em">DEPLOY 2</text>
      <text x="384" y="332" fill="{ink}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">WRITE BOTH</text>
      <text x="520" y="318" fill="{muted}" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.14em">DEPLOY 3</text>
      <text x="520" y="332" fill="{ink}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">BACKFILL</text>
      <text x="656" y="318" fill="{muted}" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.14em">DEPLOY 4</text>
      <text x="656" y="332" fill="{ink}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">READ NEW</text>
      <text x="792" y="318" fill="{accent}" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.14em">DEPLOY 5</text>
      <text x="792" y="332" fill="{accent}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">DROP OLD</text>

      <!-- rollback-safe window -->
      <rect x="248" y="364" width="544" height="32" rx="6" fill="{accent_tint}" stroke="{accent}" stroke-width="1"/>
      <text x="520" y="384" fill="{accent}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.10em">ROLLBACK SAFE &#183; PREVIOUS CODE STILL CORRECT</text>

      <!-- application bars -->
      <rect x="152" y="444" width="224" height="80" rx="6" fill="{paper}"/>
      <rect x="152" y="444" width="224" height="80" rx="6" fill="{paper}" stroke="{ink}" stroke-width="1"/>
      <text x="264" y="474" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">Current code</text>
      <text x="264" y="494" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">writes email</text>
      <text x="264" y="510" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">reads email</text>

      <rect x="384" y="444" width="264" height="80" rx="6" fill="{paper}"/>
      <rect x="384" y="444" width="264" height="80" rx="6" fill="{paper}" stroke="{ink}" stroke-width="1"/>
      <text x="516" y="474" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">Dual write</text>
      <text x="516" y="494" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">writes both columns</text>
      <text x="516" y="510" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">reads email</text>

      <rect x="656" y="444" width="128" height="80" rx="6" fill="{paper}"/>
      <rect x="656" y="444" width="128" height="80" rx="6" fill="{paper}" stroke="{ink}" stroke-width="1"/>
      <text x="720" y="474" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">Reads new</text>
      <text x="720" y="494" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">writes both</text>
      <text x="720" y="510" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">reads email_address</text>

      <rect x="792" y="444" width="128" height="80" rx="6" fill="{paper}"/>
      <rect x="792" y="444" width="128" height="80" rx="6" fill="{paper}" stroke="{ink}" stroke-width="1"/>
      <text x="856" y="474" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">New only</text>
      <text x="856" y="494" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">writes email_address</text>
      <text x="856" y="510" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">reads email_address</text>

      <text x="480" y="576" fill="{ink}" font-size="14" font-style="italic" font-family="'Instrument Serif', serif" text-anchor="middle">every deploy before the drop can be reverted on its own &#8212; the drop cannot</text>

      <!-- legend -->
      <line x1="32" y1="636" x2="928" y2="636" stroke="{rule}" stroke-width="0.8"/>
      <text x="32" y="653" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace" letter-spacing="0.14em">LEGEND</text>
      <rect x="140" y="643" width="24" height="12" rx="2" fill="{ink005}" stroke="{muted}" stroke-width="1"/>
      <text x="172" y="653" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Column exists</text>
      <rect x="276" y="643" width="24" height="12" rx="2" fill="{ink002}" stroke="{ink030}" stroke-width="1" stroke-dasharray="4,3"/>
      <text x="308" y="653" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Backfill window</text>
      <rect x="424" y="643" width="24" height="12" rx="2" fill="{paper}" stroke="{ink}" stroke-width="1"/>
      <text x="456" y="653" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Deployed code</text>
      <rect x="568" y="643" width="24" height="12" rx="2" fill="{accent_tint}" stroke="{accent}" stroke-width="1"/>
      <text x="600" y="653" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Rollback-safe</text>
      <line x1="704" y1="649" x2="728" y2="649" stroke="{accent}" stroke-width="2.5"/>
      <text x="736" y="653" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Point of no return</text>
    </svg>
"""

SVG_B = """    <svg viewBox="0 0 960 672" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="lock-queue{v}-title lock-queue{v}-desc">
      <title id="lock-queue{v}-title">How one migration stops every query</title>
      <desc id="lock-queue{v}-desc">A slow SELECT holds ACCESS SHARE on the orders table, so an ALTER TABLE asking for ACCESS EXCLUSIVE has to wait; because PostgreSQL grants locks in request order, every query that arrives afterwards queues behind the waiting ALTER even though it would be compatible with the running SELECT, and the table stays unavailable until lock_timeout makes the migration give up.</desc>
""" + DEFS + """
      <rect width="100%" height="100%" fill="{paper}"/>

      <!-- pile-up zone -->
      <rect x="404" y="240" width="232" height="180" rx="8" fill="{accent_05}" stroke="{accent_50}" stroke-width="1" stroke-dasharray="4,4"/>
      <rect x="444" y="234" width="152" height="12" rx="2" fill="{paper}"/>
      <text x="520" y="243" fill="{accent}" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.14em">EVERY QUERY QUEUES BEHIND IT</text>

      <!-- conflict connector -->
      <line x1="368" y1="136" x2="368" y2="168" stroke="{ink}" stroke-width="1.2" marker-end="url(#arrow{v})"/>
      <rect x="376" y="140" width="76" height="12" rx="2" fill="{paper}"/>
      <text x="414" y="149" fill="{ink}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">CONFLICTS</text>

      <!-- session names -->
      <text x="32" y="108" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif">Analytics report</text>
      <text x="32" y="124" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace">ACCESS SHARE</text>
      <text x="32" y="192" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif">Migration</text>
      <text x="32" y="208" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace">ACCESS EXCLUSIVE</text>
      <text x="32" y="268" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif">Checkout read</text>
      <text x="32" y="284" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace">ACCESS SHARE</text>
      <text x="32" y="328" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif">Order write</text>
      <text x="32" y="344" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace">ROW EXCLUSIVE</text>
      <text x="32" y="388" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif">Dashboard read</text>
      <text x="32" y="404" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace">ACCESS SHARE</text>

      <!-- holder -->
      <rect x="192" y="88" width="704" height="44" rx="6" fill="{paper}"/>
      <rect x="192" y="88" width="704" height="44" rx="6" fill="{paper}" stroke="{ink}" stroke-width="1"/>
      <text x="208" y="106" fill="{ink}" font-size="9" font-family="'Geist Mono', monospace">SELECT &#8230; FROM orders</text>
      <text x="208" y="121" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace">granted &#183; holds the lock for five minutes</text>

      <!-- waiting DDL -->
      <rect x="368" y="172" width="264" height="44" rx="6" fill="{paper}"/>
      <rect x="368" y="172" width="264" height="44" rx="6" fill="{ink002}" stroke="{ink030}" stroke-width="1" stroke-dasharray="4,3"/>
      <text x="384" y="190" fill="{ink}" font-size="9" font-family="'Geist Mono', monospace">ALTER TABLE orders ADD COLUMN</text>
      <text x="384" y="205" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace">waiting for ACCESS EXCLUSIVE</text>
      <text x="648" y="198" fill="{ink}" font-size="8" font-family="'Geist Mono', monospace" letter-spacing="0.06em">ABORTED</text>

      <!-- blocked queue -->
      <rect x="412" y="248" width="220" height="44" rx="6" fill="{ink005}" stroke="{ink030}" stroke-width="1" stroke-dasharray="4,3"/>
      <text x="428" y="274" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace">blocked, never ran</text>
      <rect x="456" y="308" width="176" height="44" rx="6" fill="{ink005}" stroke="{ink030}" stroke-width="1" stroke-dasharray="4,3"/>
      <text x="472" y="334" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace">blocked</text>
      <rect x="500" y="368" width="132" height="44" rx="6" fill="{ink005}" stroke="{ink030}" stroke-width="1" stroke-dasharray="4,3"/>
      <text x="516" y="394" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace">blocked</text>

      <!-- drain -->
      <text x="736" y="238" fill="{ink}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">QUEUE DRAINS</text>
      <rect x="648" y="248" width="176" height="164" rx="6" fill="{paper}"/>
      <rect x="648" y="248" width="176" height="164" rx="6" fill="{paper}" stroke="{ink}" stroke-width="1"/>
      <text x="736" y="314" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">All three run</text>
      <text x="736" y="332" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">ACCESS SHARE granted</text>
      <text x="736" y="348" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace" text-anchor="middle">after a 3s stall</text>

      <!-- timeout marker -->
      <line x1="632" y1="424" x2="632" y2="448" stroke="{accent}" stroke-width="1" stroke-dasharray="4,4"/>
      <text x="368" y="444" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">ALTER ARRIVES</text>
      <text x="632" y="444" fill="{accent}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">LOCK_TIMEOUT</text>

      <!-- time axis -->
      <line x1="192" y1="456" x2="928" y2="456" stroke="{rule_solid}" stroke-width="1" marker-end="url(#arrow{v})"/>
      <line x1="192" y1="450" x2="192" y2="462" stroke="{rule_solid}" stroke-width="1"/>
      <line x1="280" y1="450" x2="280" y2="462" stroke="{rule_solid}" stroke-width="1"/>
      <line x1="368" y1="450" x2="368" y2="462" stroke="{rule_solid}" stroke-width="1"/>
      <line x1="456" y1="450" x2="456" y2="462" stroke="{rule_solid}" stroke-width="1"/>
      <line x1="544" y1="450" x2="544" y2="462" stroke="{rule_solid}" stroke-width="1"/>
      <line x1="632" y1="450" x2="632" y2="462" stroke="{rule_solid}" stroke-width="1"/>
      <line x1="720" y1="450" x2="720" y2="462" stroke="{rule_solid}" stroke-width="1"/>
      <line x1="808" y1="450" x2="808" y2="462" stroke="{rule_solid}" stroke-width="1"/>
      <line x1="896" y1="450" x2="896" y2="462" stroke="{rule_solid}" stroke-width="1"/>
      <circle cx="368" cy="456" r="4" fill="{muted}"/>
      <circle cx="632" cy="456" r="5" fill="{accent}"/>
      <text x="192" y="478" fill="{muted}" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle">0s</text>
      <text x="280" y="478" fill="{muted}" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle">1s</text>
      <text x="368" y="478" fill="{muted}" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle">2s</text>
      <text x="456" y="478" fill="{muted}" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle">3s</text>
      <text x="544" y="478" fill="{muted}" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle">4s</text>
      <text x="632" y="478" fill="{accent}" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle">5s</text>
      <text x="720" y="478" fill="{muted}" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle">6s</text>
      <text x="808" y="478" fill="{muted}" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle">7s</text>
      <text x="896" y="478" fill="{muted}" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle">8s</text>

      <!-- the conflicting-lock fact -->
      <text x="32" y="540" fill="{ink}" font-size="14" font-style="italic" font-family="'Instrument Serif', serif">ACCESS EXCLUSIVE conflicts with every other lock mode &#8212;</text>
      <text x="32" y="562" fill="{ink}" font-size="14" font-style="italic" font-family="'Instrument Serif', serif">including the ACCESS SHARE a plain SELECT takes.</text>

      <!-- the fix -->
      <rect x="592" y="504" width="336" height="96" rx="6" fill="{paper}"/>
      <rect x="592" y="504" width="336" height="96" rx="6" fill="{ink003}" stroke="{ink030}" stroke-width="1"/>
      <text x="608" y="532" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif">The fix</text>
      <text x="608" y="554" fill="{ink}" font-size="9" font-family="'Geist Mono', monospace">SET lock_timeout = '3s';</text>
      <text x="608" y="570" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace">the migration gives up and retries</text>
      <text x="608" y="586" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace">instead of holding the door shut</text>

      <!-- legend -->
      <line x1="32" y1="636" x2="928" y2="636" stroke="{rule}" stroke-width="0.8"/>
      <text x="32" y="653" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace" letter-spacing="0.14em">LEGEND</text>
      <rect x="140" y="643" width="24" height="12" rx="2" fill="{paper}" stroke="{ink}" stroke-width="1"/>
      <text x="172" y="653" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Lock granted</text>
      <rect x="276" y="643" width="24" height="12" rx="2" fill="{ink005}" stroke="{ink030}" stroke-width="1" stroke-dasharray="4,3"/>
      <text x="308" y="653" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Waiting on a lock</text>
      <rect x="444" y="643" width="24" height="12" rx="2" fill="{accent_05}" stroke="{accent_50}" stroke-width="1" stroke-dasharray="4,4"/>
      <text x="476" y="653" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Pile-up</text>
      <line x1="580" y1="649" x2="604" y2="649" stroke="{accent}" stroke-width="1" stroke-dasharray="4,4"/>
      <text x="612" y="653" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Timeout fires</text>
      <rect x="740" y="643" width="24" height="12" rx="2" fill="{ink003}" stroke="{ink030}" stroke-width="1"/>
      <text x="772" y="653" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Mitigation</text>
    </svg>
"""

SVG_C = """    <svg viewBox="0 0 960 672" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="migration-decision{v}-title migration-decision{v}-desc">
      <title id="migration-decision{v}-title">Is this schema change safe to ship?</title>
      <desc id="migration-decision{v}-desc">A decision flowchart to run before writing a migration: ask first whether the change drops or renames something the running code still reads, because that path can never be one deploy and must go through expand and contract; the remaining branches route table rewrites to a NOT VALID constraint validated separately, row changes to a batched resumable backfill, and new indexes to CREATE INDEX CONCURRENTLY, leaving only purely additive changes safe to ship in a single deploy.</desc>
""" + DEFS + """
      <rect width="100%" height="100%" fill="{paper}"/>

      <text x="268" y="30" fill="{muted}" font-size="7" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.14em">BEFORE YOU WRITE THE MIGRATION</text>

      <!-- connectors -->
      <line x1="268" y1="40" x2="268" y2="72" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow{v})"/>

      <line x1="380" y1="104" x2="584" y2="104" stroke="{accent}" stroke-width="1.5" marker-end="url(#arrow-accent{v})"/>
      <rect x="464" y="84" width="36" height="12" rx="2" fill="{paper}"/>
      <text x="482" y="93" fill="{accent}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">YES</text>

      <line x1="380" y1="220" x2="584" y2="220" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow{v})"/>
      <rect x="464" y="200" width="36" height="12" rx="2" fill="{paper}"/>
      <text x="482" y="209" fill="{soft}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">YES</text>

      <line x1="380" y1="336" x2="584" y2="336" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow{v})"/>
      <rect x="464" y="316" width="36" height="12" rx="2" fill="{paper}"/>
      <text x="482" y="325" fill="{soft}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">YES</text>

      <line x1="380" y1="452" x2="584" y2="452" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow{v})"/>
      <rect x="464" y="432" width="36" height="12" rx="2" fill="{paper}"/>
      <text x="482" y="441" fill="{soft}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">YES</text>

      <line x1="268" y1="136" x2="268" y2="188" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow{v})"/>
      <rect x="276" y="156" width="30" height="12" rx="2" fill="{paper}"/>
      <text x="291" y="165" fill="{soft}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">NO</text>

      <line x1="268" y1="252" x2="268" y2="304" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow{v})"/>
      <rect x="276" y="272" width="30" height="12" rx="2" fill="{paper}"/>
      <text x="291" y="281" fill="{soft}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">NO</text>

      <line x1="268" y1="368" x2="268" y2="420" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow{v})"/>
      <rect x="276" y="388" width="30" height="12" rx="2" fill="{paper}"/>
      <text x="291" y="397" fill="{soft}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">NO</text>

      <line x1="268" y1="484" x2="268" y2="520" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow{v})"/>
      <rect x="276" y="496" width="30" height="12" rx="2" fill="{paper}"/>
      <text x="291" y="505" fill="{soft}" font-size="8" font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">NO</text>

      <!-- decisions -->
      <path d="M 156 104 L 268 72 L 380 104 L 268 136 Z" fill="{paper}"/>
      <path d="M 156 104 L 268 72 L 380 104 L 268 136 Z" fill="{accent_tint}" stroke="{accent}" stroke-width="1" stroke-linejoin="round"/>
      <text x="268" y="100" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">Drops or renames</text>
      <text x="268" y="116" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">a live column?</text>

      <path d="M 156 220 L 268 188 L 380 220 L 268 252 Z" fill="{paper}"/>
      <path d="M 156 220 L 268 188 L 380 220 L 268 252 Z" fill="{paper}" stroke="{ink}" stroke-width="1" stroke-linejoin="round"/>
      <text x="268" y="216" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">Rewrites rows or</text>
      <text x="268" y="232" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">takes a long lock?</text>

      <path d="M 156 336 L 268 304 L 380 336 L 268 368 Z" fill="{paper}"/>
      <path d="M 156 336 L 268 304 L 380 336 L 268 368 Z" fill="{paper}" stroke="{ink}" stroke-width="1" stroke-linejoin="round"/>
      <text x="268" y="332" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">Backfills</text>
      <text x="268" y="348" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">existing rows?</text>

      <path d="M 156 452 L 268 420 L 380 452 L 268 484 Z" fill="{paper}"/>
      <path d="M 156 452 L 268 420 L 380 452 L 268 484 Z" fill="{paper}" stroke="{ink}" stroke-width="1" stroke-linejoin="round"/>
      <text x="268" y="448" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">Creates</text>
      <text x="268" y="464" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif" text-anchor="middle">a new index?</text>

      <!-- terminal actions -->
      <rect x="584" y="68" width="320" height="72" rx="6" fill="{paper}"/>
      <rect x="584" y="68" width="320" height="72" rx="6" fill="{accent_tint}" stroke="{accent}" stroke-width="1"/>
      <text x="600" y="94" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif">Expand and contract</text>
      <text x="600" y="114" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace">add, dual-write, backfill, read new, drop</text>
      <text x="600" y="130" fill="{accent}" font-size="9" font-family="'Geist Mono', monospace">one deploy here is the outage</text>

      <rect x="584" y="184" width="320" height="72" rx="6" fill="{paper}"/>
      <rect x="584" y="184" width="320" height="72" rx="6" fill="{paper}" stroke="{ink}" stroke-width="1"/>
      <text x="600" y="210" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif">Split the constraint</text>
      <text x="600" y="230" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace">ADD CONSTRAINT &#8230; NOT VALID</text>
      <text x="600" y="246" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace">then VALIDATE CONSTRAINT, weaker lock</text>

      <rect x="584" y="300" width="320" height="72" rx="6" fill="{paper}"/>
      <rect x="584" y="300" width="320" height="72" rx="6" fill="{paper}" stroke="{ink}" stroke-width="1"/>
      <text x="600" y="326" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif">Backfill in batches</text>
      <text x="600" y="346" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace">bounded ranges, resumable, throttled</text>
      <text x="600" y="362" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace">never one UPDATE over the table</text>

      <rect x="584" y="416" width="320" height="72" rx="6" fill="{paper}"/>
      <rect x="584" y="416" width="320" height="72" rx="6" fill="{paper}" stroke="{ink}" stroke-width="1"/>
      <text x="600" y="442" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif">Build it concurrently</text>
      <text x="600" y="462" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace">CREATE INDEX CONCURRENTLY</text>
      <text x="600" y="478" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace">no transaction; drop INVALID, retry</text>

      <rect x="108" y="520" width="320" height="72" rx="6" fill="{paper}"/>
      <rect x="108" y="520" width="320" height="72" rx="6" fill="{paper}" stroke="{ink}" stroke-width="1"/>
      <text x="124" y="546" fill="{ink}" font-size="12" font-weight="600" font-family="'Geist', sans-serif">Ship it in one deploy</text>
      <text x="124" y="566" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace">new nullable column or new table</text>
      <text x="124" y="582" fill="{muted}" font-size="9" font-family="'Geist Mono', monospace">old code stays correct</text>

      <text x="676" y="560" fill="{ink}" font-size="14" font-style="italic" font-family="'Instrument Serif', serif" text-anchor="middle">the cheapest-looking path</text>
      <text x="676" y="578" fill="{ink}" font-size="14" font-style="italic" font-family="'Instrument Serif', serif" text-anchor="middle">is the one that pages you</text>

      <!-- legend -->
      <line x1="32" y1="636" x2="928" y2="636" stroke="{rule}" stroke-width="0.8"/>
      <text x="32" y="653" fill="{muted}" font-size="8" font-family="'Geist Mono', monospace" letter-spacing="0.14em">LEGEND</text>
      <path d="M 140 649 L 152 643 L 164 649 L 152 655 Z" fill="{paper}" stroke="{ink}" stroke-width="1" stroke-linejoin="round"/>
      <text x="172" y="653" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Decision</text>
      <rect x="276" y="643" width="24" height="12" rx="2" fill="{paper}" stroke="{ink}" stroke-width="1"/>
      <text x="308" y="653" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Terminal action</text>
      <rect x="436" y="643" width="24" height="12" rx="2" fill="{accent_tint}" stroke="{accent}" stroke-width="1"/>
      <text x="468" y="653" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Outage path</text>
      <line x1="596" y1="649" x2="620" y2="649" stroke="{muted}" stroke-width="1.2" marker-end="url(#arrow{v})"/>
      <text x="628" y="653" fill="{muted}" font-size="9" font-family="'Geist', sans-serif">Branch</text>
    </svg>
"""

DIAGRAMS = [
    ("10-expand-contract", "Timeline &#183; Diagram Design", "Renaming a column without downtime", SVG_A),
    ("11-lock-queue", "Timeline &#183; Diagram Design", "How one migration stops every query", SVG_B),
    ("12-migration-decision", "Flowchart &#183; Diagram Design", "Is this schema change safe to ship?", SVG_C),
]

if __name__ == "__main__":
    render_all(DIAGRAMS)
