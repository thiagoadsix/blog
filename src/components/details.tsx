import { ReactNode } from "react";

interface DetailsProps {
  summary: string;
  children: ReactNode;
}

export function Details({ summary, children }: DetailsProps) {
  return (
    <details className="my-8 rounded-lg border px-4 py-3">
      <summary className="cursor-pointer text-sm font-medium text-muted-foreground transition-colors hover:text-foreground">
        {summary}
      </summary>
      <div className="mt-4 [&>:first-child]:mt-0 [&>:last-child]:mb-0">
        {children}
      </div>
    </details>
  );
}
