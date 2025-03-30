import { Metadata } from "next";
import { notFound } from "next/navigation";

import { posts } from "#site/content";
import { siteConfig } from "@/config/site";

import { BlogHeader } from "@/components/blog/header";
import { Base } from "@/components/base";
import { MDXContent } from "@/components/mdx-components";

import "@/styles/mdx.css";

interface BlogDetailPageProps {
  params: {
    slug: string[];
  };
}

async function getPostFromParams(params: BlogDetailPageProps["params"]) {
  const resolvedParams = await params;
  const slug = resolvedParams.slug.join("/");
  const post = posts.find((post) => post.slugAsParam === slug);
  return post;
}

export async function generateMetadata(
  { params }: BlogDetailPageProps
): Promise<Metadata> {
  const post = await getPostFromParams(await params);

  if (!post) {
    return {};
  }

  const ogSearchParams = new URLSearchParams();
  ogSearchParams.set("title", post.title);

  return {
    title: post.title,
    description: post.description,
    authors: {
      name: siteConfig.author,
    },
    openGraph: {
      title: post.title,
      description: post.description,
      type: "article",
      url: post.slug,
      images: [
        {
          url: `/api/og?${ogSearchParams.toString()}`,
          width: 1200,
          height: 630,
          alt: post.title,
        },
      ],
    },
    twitter: {
      card: "summary_large_image",
      title: post.title,
      description: post.description,
      images: [`/api/og?${ogSearchParams.toString()}}`],
    },
  };
}

export async function generateStaticParams(): Promise<
  BlogDetailPageProps["params"][]
> {
  return posts.map((post) => ({
    slug: post.slugAsParam.split("/"),
  }));
}

export default async function BlogDetailPage({ params }: BlogDetailPageProps) {

  const post = await getPostFromParams(await params);

  if (!post || !post.published) {
    notFound();
  }

  return (
    <Base isProselytizing>
      <BlogHeader
        title={post.title}
        description={post.description}
        date={post.date}
      />
      <MDXContent code={post.body} />
    </Base>
  );
}
