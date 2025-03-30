"use client";

import { useState, useMemo } from "react";
import { ArrowLeftIcon, ArrowRightIcon } from "@radix-ui/react-icons";
import Link from "next/link";

import { Button } from "@/components/ui/button";
import { ClientOnlyDate } from "@/components/client/client-only-date";

interface Blog {
  slug: string;
  title: string;
  description: string;
  date: string;
  published: boolean;
  body: string;
}

interface BlogsListProps {
  posts: Blog[];
}

function paginate<T>(items: T[], currentPage: number, itemsPerPage: number) {
  const startIndex = (currentPage - 1) * itemsPerPage;
  return items.slice(startIndex, startIndex + itemsPerPage);
}

export default function BlogList({ posts }: BlogsListProps) {
  const [currentPage, setCurrentPage] = useState(1);
  const itemsPerPage = 5;

  const totalPages = useMemo(
    () => Math.ceil(posts.length / itemsPerPage),
    [posts.length, itemsPerPage]
  );

  const paginatedBlogs = useMemo(
    () => paginate(posts, currentPage, itemsPerPage),
    [posts, currentPage, itemsPerPage]
  );

  const goToNextPage = () =>
    setCurrentPage((page) => Math.min(page + 1, totalPages));
  const goToPrevPage = () => setCurrentPage((page) => Math.max(page - 1, 1));

  return (
    <main>
      <div className="space-y-6 mb-8">
        {paginatedBlogs.map((blog) => (
          <div key={blog.slug} className="border rounded p-4">
            <Link href={`/blog/${blog.slug}`}>
              <h2 className="text-xl font-semibold mb-2 cursor-pointer">
                {blog.title}
              </h2>
            </Link>
            <p className="text-gray-800 dark:text-gray-200 mb-2">{blog.description}</p>
            <ClientOnlyDate date={blog.date} />
          </div>
        ))}
      </div>

      <div className="flex flex-col sm:flex-row justify-between items-center space-y-4 sm:space-y-0 sm:space-x-4 mt-8">
        <p>
          Showing {currentPage * itemsPerPage - itemsPerPage + 1}-
          {Math.min(currentPage * itemsPerPage, posts.length)} of {posts.length}{" "}
          blogs
        </p>
        <div className="flex justify-center items-center space-x-2">
          <Button
            variant="outline"
            size="sm"
            onClick={goToPrevPage}
            disabled={currentPage === 1}
          >
            <ArrowLeftIcon />
          </Button>
          {Array.from({ length: totalPages }, (_, i) => i + 1).map((page) => (
            <Button
              key={page}
              variant="outline"
              size="sm"
              onClick={() => setCurrentPage(page)}
              disabled={currentPage === page}
            >
              {page}
            </Button>
          ))}
          <Button
            variant="outline"
            size="sm"
            onClick={goToNextPage}
            disabled={currentPage === totalPages}
          >
            <ArrowRightIcon />
          </Button>
        </div>
      </div>
    </main>
  );
}
