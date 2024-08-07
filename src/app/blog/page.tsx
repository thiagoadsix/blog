import { posts } from "#site/content";
import { Base } from "@/components/base";
import BlogList from "@/components/blog/list";
import { sorPosts } from "@/lib/utils";

export default async function BlogPage() {
  const sortedPosts = sorPosts(posts.filter((post) => post.published));

  return (
    <Base>
      <h1 className="text-3xl font-bold mb-6">Blog</h1>
      <input
        type="text"
        placeholder="Search blogs..."
        className="w-full p-2 mb-4 border rounded focus:outline-none focus:border-zinc-500"
      />
      {posts?.length > 0 ? (
        <BlogList posts={sortedPosts} />
      ) : (
        <p className="text-gray-600">No blogs found</p>
      )}
    </Base>
  );
}
