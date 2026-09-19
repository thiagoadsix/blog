import type { Metadata } from "next";
import Link from "next/link";

import { notes } from "#site/content";
import { Base } from "@/components/base";
import { sortNotes } from "@/lib/utils";

export const metadata: Metadata = {
  title: "Notes",
  description:
    "Long-form study notes on API design, relational data modelling, query performance and safe schema migrations.",
};

export default function NotesPage() {
  const published = sortNotes(notes.filter((note) => note.published));

  return (
    <Base>
      <div className="mb-10 space-y-3">
        <h1 className="text-3xl font-bold">Notes</h1>
        <p className="max-w-2xl text-muted-foreground">
          Study notes I keep for myself. Each one is a full pass over a topic:
          the concept, the code, the trap, and a recall checklist at the end.
        </p>
      </div>

      {published.length > 0 ? (
        <ol className="space-y-4">
          {published.map((note) => (
            <li key={note.slug}>
              <Link
                href={`/${note.slug}`}
                className="block rounded-lg border p-5 no-underline transition-colors hover:bg-muted/50"
              >
                <div className="flex items-baseline gap-3">
                  <span className="font-mono text-sm text-muted-foreground">
                    {String(note.order).padStart(2, "0")}
                  </span>
                  <h2 className="text-xl font-semibold">{note.title}</h2>
                </div>
                <p className="mt-2 text-muted-foreground">{note.description}</p>
                <p className="mt-3 text-sm text-muted-foreground">
                  {note.toc.length} sections
                </p>
              </Link>
            </li>
          ))}
        </ol>
      ) : (
        <p className="text-muted-foreground">No notes yet.</p>
      )}
    </Base>
  );
}
