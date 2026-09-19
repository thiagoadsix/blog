from common import DEFS, render_all

MODES = [
    ("AS", "ACCESS SHARE", ["SELECT"]),
    ("RS", "ROW SHARE", ["SELECT ... FOR UPDATE"]),
    ("RE", "ROW EXCLUSIVE", ["INSERT, UPDATE, DELETE"]),
    ("SUE", "SHARE UPDATE EXCLUSIVE", ["VACUUM, ANALYZE,", "CREATE INDEX CONCURRENTLY"]),
    ("SH", "SHARE", ["CREATE INDEX"]),
    ("AE", "ACCESS EXCLUSIVE", ["ALTER TABLE, DROP, TRUNCATE"]),
]

BLOCKS = [
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 0, 1, 1, 1],
    [0, 0, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1],
]

COL_X = [296, 400, 504, 608, 712, 816]
COL_W = 100
ROW_Y = [84, 160, 236, 312, 388, 464]
ROW_H = 76
LABEL_X = 32
LABEL_W = 256


def build():
    out = []
    add = out.append

    add('      <rect width="100%" height="100%" fill="{paper}"/>\n')

    add('      <text x="%d" y="28" fill="{muted}" font-size="7" '
        'font-family="\'Geist Mono\', monospace" letter-spacing="0.14em">'
        'LOCK ALREADY HELD</text>\n' % LABEL_X)
    add('      <text x="%d" y="28" fill="{muted}" font-size="7" '
        'font-family="\'Geist Mono\', monospace" text-anchor="middle" letter-spacing="0.14em">'
        'LOCK THE NEXT STATEMENT ASKS FOR</text>\n' % ((COL_X[0] + COL_X[5] + COL_W) // 2))

    for index, (code, _, _) in enumerate(MODES):
        center = COL_X[index] + COL_W // 2
        fill = "{accent}" if code == "AE" else "{ink}"
        add('      <text x="%d" y="58" fill="%s" font-size="10" font-weight="600" '
            'font-family="\'Geist Mono\', monospace" text-anchor="middle" '
            'letter-spacing="0.08em">%s</text>\n' % (center, fill, code))

    add('      <line x1="%d" y1="72" x2="%d" y2="72" stroke="{rule_solid}" stroke-width="1"/>\n'
        % (LABEL_X, COL_X[5] + COL_W))

    for row, (code, name, statements) in enumerate(MODES):
        y = ROW_Y[row]
        focal = code == "AE"

        if focal:
            add('      <rect x="%d" y="%d" width="%d" height="%d" rx="6" fill="{accent_05}" '
                'stroke="{accent_50}" stroke-width="1" stroke-dasharray="4,4"/>\n'
                % (LABEL_X, y, COL_X[5] + COL_W - LABEL_X, ROW_H))
        elif row % 2 == 1:
            add('      <rect x="%d" y="%d" width="%d" height="%d" fill="{ink002}"/>\n'
                % (LABEL_X, y, COL_X[5] + COL_W - LABEL_X, ROW_H))

        name_fill = "{accent}" if focal else "{ink}"
        add('      <text x="%d" y="%d" fill="%s" font-size="12" font-weight="600" '
            'font-family="\'Geist\', sans-serif">%s</text>\n'
            % (LABEL_X + 12, y + 28, name_fill, name))
        add('      <text x="%d" y="%d" fill="%s" font-size="8" '
            'font-family="\'Geist Mono\', monospace" text-anchor="end" '
            'letter-spacing="0.08em">%s</text>\n'
            % (LABEL_X + LABEL_W - 4, y + 28, name_fill, code))

        for line, statement in enumerate(statements):
            add('      <text x="%d" y="%d" fill="{muted}" font-size="9" '
                'font-family="\'Geist Mono\', monospace">%s</text>\n'
                % (LABEL_X + 12, y + 48 + line * 14, statement))

        for col in range(6):
            cx = COL_X[col] + COL_W // 2
            cy = y + ROW_H // 2
            blocked = BLOCKS[row][col]

            if blocked:
                glyph_fill = "{accent}" if focal else "{ink}"
                add('      <rect x="%d" y="%d" width="10" height="10" rx="2" fill="%s"/>\n'
                    % (cx - 5, cy - 16, glyph_fill))
                add('      <text x="%d" y="%d" fill="%s" font-size="8" '
                    'font-family="\'Geist Mono\', monospace" text-anchor="middle" '
                    'letter-spacing="0.08em">WAITS</text>\n' % (cx, cy + 12, glyph_fill))
            else:
                add('      <rect x="%d" y="%d" width="10" height="10" rx="2" fill="none" '
                    'stroke="{ink030}" stroke-width="1"/>\n' % (cx - 5, cy - 16))
                add('      <text x="%d" y="%d" fill="{soft}" font-size="8" '
                    'font-family="\'Geist Mono\', monospace" text-anchor="middle" '
                    'letter-spacing="0.08em">RUNS</text>\n' % (cx, cy + 12))

    add('      <text x="480" y="580" fill="{accent}" font-size="14" font-style="italic" '
        'font-family="\'Instrument Serif\', serif" text-anchor="middle">'
        'one row blocks everything, and it is the row every ALTER TABLE lives in</text>\n')
    add('      <text x="480" y="604" fill="{muted}" font-size="9" '
        'font-family="\'Geist Mono\', monospace" text-anchor="middle">'
        'columns are the same six modes, in the same order</text>\n')

    add('      <line x1="32" y1="636" x2="928" y2="636" stroke="{rule}" stroke-width="0.8"/>\n')
    add('      <text x="32" y="653" fill="{muted}" font-size="8" '
        'font-family="\'Geist Mono\', monospace" letter-spacing="0.14em">LEGEND</text>\n')
    add('      <rect x="150" y="644" width="10" height="10" rx="2" fill="{ink}"/>\n')
    add('      <text x="170" y="653" fill="{muted}" font-size="9" '
        'font-family="\'Geist\', sans-serif">Conflict, the second statement waits</text>\n')
    add('      <rect x="430" y="644" width="10" height="10" rx="2" fill="none" '
        'stroke="{ink030}" stroke-width="1"/>\n')
    add('      <text x="450" y="653" fill="{muted}" font-size="9" '
        'font-family="\'Geist\', sans-serif">Compatible, both run</text>\n')
    add('      <rect x="640" y="643" width="24" height="12" rx="2" fill="{accent_05}" '
        'stroke="{accent_50}" stroke-width="1" stroke-dasharray="4,4"/>\n')
    add('      <text x="672" y="653" fill="{muted}" font-size="9" '
        'font-family="\'Geist\', sans-serif">Conflicts with every mode</text>\n')

    return "".join(out)


SVG = (
    '    <svg viewBox="0 0 960 672" xmlns="http://www.w3.org/2000/svg" role="img" '
    'aria-labelledby="lock-conflicts{v}-title lock-conflicts{v}-desc">\n'
    '      <title id="lock-conflicts{v}-title">Which PostgreSQL table locks block each other</title>\n'
    '      <desc id="lock-conflicts{v}-desc">A conflict matrix of the six PostgreSQL table lock '
    'modes an application meets, naming the statement that takes each one and showing which '
    'pairs can run together. Ordinary reads and writes are compatible with each other, while '
    'ACCESS EXCLUSIVE, taken by ALTER TABLE, DROP and TRUNCATE, conflicts with every mode '
    'including the ACCESS SHARE that a plain SELECT takes.</desc>\n'
    + DEFS
    + build()
    + "    </svg>\n"
)

DIAGRAMS = [
    ("13-lock-conflicts", "Matrix &#183; Diagram Design",
     "Which table locks block each other", SVG),
]

if __name__ == "__main__":
    render_all(DIAGRAMS)
