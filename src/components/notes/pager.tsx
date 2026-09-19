import Link from "next/link";
import { ArrowLeft, ArrowRight } from "lucide-react";

interface PagerLink {
  slug: string;
  title: string;
}

interface NotesPagerProps {
  previous?: PagerLink;
  next?: PagerLink;
}

export function NotesPager({ previous, next }: NotesPagerProps) {
  if (!previous && !next) {
    return null;
  }

  return (
    <nav
      aria-label="Note navigation"
      className="not-prose mt-16 grid gap-4 border-t pt-8 sm:grid-cols-2"
    >
      {previous ? (
        <Link
          href={`/${previous.slug}`}
          className="group flex flex-col gap-1 rounded-lg border p-4 no-underline transition-colors hover:bg-muted/50"
        >
          <span className="flex items-center gap-1 text-xs text-muted-foreground">
            <ArrowLeft className="h-3 w-3" />
            Previous
          </span>
          <span className="font-medium">{previous.title}</span>
        </Link>
      ) : (
        <span />
      )}
      {next ? (
        <Link
          href={`/${next.slug}`}
          className="group flex flex-col gap-1 rounded-lg border p-4 text-right no-underline transition-colors hover:bg-muted/50 sm:col-start-2"
        >
          <span className="flex items-center justify-end gap-1 text-xs text-muted-foreground">
            Next
            <ArrowRight className="h-3 w-3" />
          </span>
          <span className="font-medium">{next.title}</span>
        </Link>
      ) : null}
    </nav>
  );
}
