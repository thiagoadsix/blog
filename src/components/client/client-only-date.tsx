"use client";

import { useSyncExternalStore } from "react";
import { formatDate } from "@/lib/utils";

interface ClientOnlyDateProps {
  date: string;
  className?: string;
  format?: (date: string) => string;
  as?: 'p' | 'time';
}

const subscribe = () => () => {};

export function ClientOnlyDate({
  date,
  className = "text-sm text-gray-500",
  format = formatDate,
  as = 'p'
}: ClientOnlyDateProps) {
  const isHydrated = useSyncExternalStore(subscribe, () => true, () => false);

  if (!isHydrated) {
    return <p className={`${className} opacity-0`}>Loading...</p>;
  }

  const formattedDate = format(date);

  if (as === 'time') {
    return <time dateTime={date} className={className}>{formattedDate}</time>;
  }

  return <p className={className}>{formattedDate}</p>;
}
