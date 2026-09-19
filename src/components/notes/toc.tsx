"use client";

import { useEffect, useMemo, useState } from "react";

export interface TocEntry {
  title: string;
  url: string;
  items: TocEntry[];
}

function flattenUrls(entries: TocEntry[]): string[] {
  return entries.flatMap((entry) => [entry.url, ...flattenUrls(entry.items)]);
}

function useActiveHeading(urls: string[]) {
  const [activeUrl, setActiveUrl] = useState<string | null>(urls[0] ?? null);

  useEffect(() => {
    const ids = urls.map((url) => url.replace(/^#/, ""));
    const visible = new Set<string>();

    const observer = new IntersectionObserver(
      (entries) => {
        for (const entry of entries) {
          if (entry.isIntersecting) {
            visible.add(entry.target.id);
          } else {
            visible.delete(entry.target.id);
          }
        }

        const firstVisible = ids.find((id) => visible.has(id));
        if (firstVisible) {
          setActiveUrl(`#${firstVisible}`);
        }
      },
      { rootMargin: "-80px 0px -70% 0px", threshold: 0 }
    );

    for (const id of ids) {
      const element = document.getElementById(id);
      if (element) {
        observer.observe(element);
      }
    }

    return () => observer.disconnect();
  }, [urls]);

  return activeUrl;
}

function TocList({
  entries,
  activeUrl,
  depth,
}: {
  entries: TocEntry[];
  activeUrl: string | null;
  depth: number;
}) {
  if (entries.length === 0) {
    return null;
  }

  return (
    <ul className={depth === 0 ? "space-y-2" : "mt-2 space-y-2 border-l pl-3"}>
      {entries.map((entry) => (
        <li key={entry.url} className="space-y-2">
          <a
            href={entry.url}
            className={`block text-sm leading-snug no-underline transition-colors hover:text-foreground ${
              activeUrl === entry.url
                ? "font-medium text-foreground"
                : "text-muted-foreground"
            }`}
          >
            {entry.title}
          </a>
          <TocList
            entries={entry.items}
            activeUrl={activeUrl}
            depth={depth + 1}
          />
        </li>
      ))}
    </ul>
  );
}

export function Toc({ entries }: { entries: TocEntry[] }) {
  const urls = useMemo(() => flattenUrls(entries), [entries]);
  const activeUrl = useActiveHeading(urls);

  if (entries.length === 0) {
    return null;
  }

  return (
    <nav aria-label="Table of contents" className="not-prose">
      <p className="mb-4 text-xs font-semibold uppercase tracking-wider text-muted-foreground">
        On this page
      </p>
      <TocList entries={entries} activeUrl={activeUrl} depth={0} />
    </nav>
  );
}

export function TocDisclosure({ entries }: { entries: TocEntry[] }) {
  if (entries.length === 0) {
    return null;
  }

  return (
    <details className="not-prose mb-8 rounded-lg border p-4 lg:hidden">
      <summary className="cursor-pointer text-sm font-medium">
        Table of contents
      </summary>
      <div className="mt-4">
        <TocList entries={entries} activeUrl={null} depth={0} />
      </div>
    </details>
  );
}
