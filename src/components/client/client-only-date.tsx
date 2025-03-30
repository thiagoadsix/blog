"use client";

import { useState, useEffect, ReactNode } from "react";
import { formatDate } from "@/lib/utils";

interface ClientOnlyDateProps {
  date: string;
  className?: string;
  format?: (date: string) => string;
  as?: 'p' | 'time';
}

export function ClientOnlyDate({
  date,
  className = "text-sm text-gray-500",
  format = formatDate,
  as = 'p'
}: ClientOnlyDateProps) {
  const [formattedDate, setFormattedDate] = useState<string>('');

  useEffect(() => {
    setFormattedDate(format(date));
  }, [date, format]);

  if (!formattedDate) {
    return <p className={`${className} opacity-0`}>Loading...</p>;
  }

  if (as === 'time') {
    return <time dateTime={date} className={className}>{formattedDate}</time>;
  }

  return <p className={className}>{formattedDate}</p>;
}