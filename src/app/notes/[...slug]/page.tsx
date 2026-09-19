import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { ArrowLeft } from "lucide-react";

import { notes } from "#site/content";
import { siteConfig } from "@/config/site";
import { sortNotes } from "@/lib/utils";

import { MDXContent } from "@/components/mdx-components";
import { NotesPager } from "@/components/notes/pager";
import { Toc, TocDisclosure } from "@/components/notes/toc";

import "@/styles/mdx.css";

interface NoteDetailPageProps {
  params: Promise<{
    slug: string[];
  }>;
}

function getNoteFromSlug(slug: string[]) {
  return notes.find((note) => note.slugAsParam === slug.join("/"));
}

export async function generateMetadata({
  params,
}: NoteDetailPageProps): Promise<Metadata> {
  const { slug } = await params;
  const note = getNoteFromSlug(slug);

  if (!note) {
    return {};
  }

  const ogSearchParams = new URLSearchParams();
  ogSearchParams.set("title", note.title);

  return {
    title: note.title,
    description: note.description,
    authors: { name: siteConfig.author },
    openGraph: {
      title: note.title,
      description: note.description,
      type: "article",
      url: note.slug,
      images: [
        {
          url: `/api/og?${ogSearchParams.toString()}`,
          width: 1200,
          height: 630,
          alt: note.title,
        },
      ],
    },
    twitter: {
      card: "summary_large_image",
      title: note.title,
      description: note.description,
      images: [`/api/og?${ogSearchParams.toString()}`],
    },
  };
}

export function generateStaticParams(): { slug: string[] }[] {
  return notes.map((note) => ({ slug: note.slugAsParam.split("/") }));
}

export default async function NoteDetailPage({ params }: NoteDetailPageProps) {
  const { slug } = await params;
  const note = getNoteFromSlug(slug);

  if (!note || !note.published) {
    notFound();
  }

  const published = sortNotes(notes.filter((item) => item.published));
  const index = published.findIndex((item) => item.slug === note.slug);
  const previous = published[index - 1];
  const next = published[index + 1];

  return (
    <main className="flex flex-1 flex-col">
      <div className="mx-auto w-full max-w-(--breakpoint-xl) p-4">
        <div className="lg:grid lg:grid-cols-[minmax(0,1fr)_16rem] lg:gap-12">
          <article className="prose dark:prose-invert min-w-0 max-w-none">
            <div className="not-prose mb-8 space-y-4">
              <Link
                href="/notes"
                className="inline-flex items-center gap-1 text-sm text-muted-foreground no-underline hover:text-foreground"
              >
                <ArrowLeft className="h-4 w-4" />
                All notes
              </Link>
              <h1 className="text-3xl font-bold leading-tight tracking-tight md:text-4xl">
                {note.title}
              </h1>
              <p className="text-lg text-muted-foreground">
                {note.description}
              </p>
            </div>

            <TocDisclosure entries={note.toc} />
            <MDXContent code={note.body} />
            <NotesPager previous={previous} next={next} />
          </article>

          <aside className="hidden lg:block">
            <div className="sticky top-8 max-h-[calc(100vh-4rem)] overflow-y-auto pb-8">
              <Toc entries={note.toc} />
            </div>
          </aside>
        </div>
      </div>
    </main>
  );
}
