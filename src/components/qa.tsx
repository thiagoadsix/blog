import { Children, isValidElement, ReactNode } from "react";

interface QAProps {
  children: ReactNode;
}

export function QA({ children }: QAProps) {
  const [question, ...answer] = Children.toArray(children);
  const summary = isValidElement<{ children?: ReactNode }>(question)
    ? question.props.children
    : question;

  return (
    <details className="group my-4 border-b pb-4">
      <summary className="flex cursor-pointer items-start gap-2 font-medium text-foreground marker:content-['']">
        <span
          aria-hidden
          className="mt-1 text-xs text-muted-foreground transition-transform group-open:rotate-90"
        >
          ▶
        </span>
        <span>{summary}</span>
      </summary>
      <div className="mt-4 pl-6 [&>:first-child]:mt-0 [&>:last-child]:mb-0">
        {answer}
      </div>
    </details>
  );
}
