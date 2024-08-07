import { notFound } from "next/navigation";

import { Button } from "@/components/ui/button";
import { Base } from "@/components/base";
import { posts } from "#site/content";
import { MDXContent } from "@/components/mdx-components";
import { BackButton } from "@/components/client/back-button";
import { formatDate } from "@/lib/utils";

import "@/styles/mdx.css";
import { Metadata } from "next";
import { siteConfig } from "@/config/site";

type Blog = {
  id: string;
  title: string;
  description: string;
  date: string;
};

interface BlogDetailPageProps {
  params: {
    slug: string[];
  };
}

export async function getPostFromParams(params: BlogDetailPageProps["params"]) {
  const slug = params.slug.join("/");
  const post = posts.find((post) => post.slugAsParam === slug);
  return post;
}

export async function generateMetadata({
  params,
}: BlogDetailPageProps): Promise<Metadata> {
  const post = await getPostFromParams(params);

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
  const post = await getPostFromParams(params);

  if (!post || !post.published) {
    notFound();
  }

  return (
    <Base isProselytizing>
      <div className="flex flex-row justify-between">
        <div>
          <h1 className="text-3xl font-bold mb-4">{post.title}</h1>
          <p className="text-gray-600 mb-2">{post.description}</p>
          <p className="text-sm text-gray-500">{formatDate(post.date)}</p>
        </div>

        <BackButton />
      </div>
      <MDXContent code={post.body} />
    </Base>
  );
}
