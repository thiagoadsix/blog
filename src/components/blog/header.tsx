"use client";

import Image from "next/image";
import Link from "next/link";
import { ArrowLeft, Clock, Calendar, Share2 } from 'lucide-react';
import { useState, useEffect } from 'react';
import { formatDate } from "@/lib/utils";

import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { ClientOnlyDate } from "@/components/client/client-only-date";

interface BlogHeaderProps {
  title: string;
  description: string;
  date: string;
  author?: {
    name: string;
    avatar?: string;
  };
  estimatedReadingTime?: string;
  categories?: string[];
  featuredImage?: string;
}

export function BlogHeader({
  title,
  description,
  date,
  author,
  estimatedReadingTime,
  categories,
  featuredImage,
}: BlogHeaderProps) {
  return (
    <div className="space-y-6">
      <div className="flex items-center gap-2 text-sm text-muted-foreground">
        <Button variant="ghost" size="sm" asChild className="gap-1 px-0 hover:bg-transparent">
          <Link href="/blog" className="inline-flex items-center gap-1 no-underline">
            <ArrowLeft className="h-4 w-4" />
            Back to blog
          </Link>
        </Button>
      </div>

      {featuredImage && (
        <div className="relative aspect-video w-full overflow-hidden rounded-lg">
          <Image
            src={featuredImage || "/placeholder.svg"}
            alt={title}
            fill
            className="object-cover"
            priority
          />
        </div>
      )}

      <div className="space-y-4">
        <h1 className="font-heading text-3xl font-bold leading-tight tracking-tighter md:text-4xl lg:text-5xl">
          {title}
        </h1>
        <p className="text-lg text-muted-foreground md:text-xl">
          {description}
        </p>
      </div>

      <div className="flex flex-col items-start justify-between gap-4 border-b border-border pb-6 pt-2 md:flex-row md:items-center">
        <div className="flex items-center gap-4">
          {author && (
            <div className="flex items-center gap-2">
              <Avatar className="h-10 w-10">
                <AvatarImage src={author.avatar} alt={author.name} />
                <AvatarFallback>{author.name.charAt(0)}</AvatarFallback>
              </Avatar>
              <div className="text-sm">
                <p className="font-medium">{author.name}</p>
              </div>
            </div>
          )}
        </div>

        <div className="flex flex-wrap items-center gap-4 text-sm text-muted-foreground">
          <div className="flex items-center gap-1">
            <Calendar className="h-4 w-4" />
            <ClientOnlyDate date={date} as="time" />
          </div>
          {estimatedReadingTime && (
            <div className="flex items-center gap-1">
              <Clock className="h-4 w-4" />
              <span>{estimatedReadingTime} min read</span>
            </div>
          )}
          <Button variant="outline" size="icon" className="h-8 w-8 rounded-full">
            <Share2 className="h-4 w-4" />
            <span className="sr-only">Share</span>
          </Button>
        </div>
      </div>

      {categories && categories.length > 0 && (
        <div className="flex flex-wrap gap-2">
          {categories.map((category) => (
            <Badge key={category} variant="secondary">
              {category}
            </Badge>
          ))}
        </div>
      )}
    </div>
  );
}
