"use client";

import React, { useState } from "react";
import Image from "next/image";
import { FaLinkedin, FaGithub } from "react-icons/fa";
import { siteConfig } from "@/config/site";
import { posts } from "#site/content";
import { sorPosts } from "@/lib/utils";
import Link from "next/link";
import { ClientOnlyDate } from "@/components/client/client-only-date";

const projects: any[] = [];

const Home = () => {
  const [searchTerm, setSearchTerm] = useState("");

  const handleSearch = (event: any) => {
    setSearchTerm(event.target.value);
  };

  const sortedPosts = sorPosts(posts.filter((post) => post.published))
    .slice(0, 3)
    .filter((blog) =>
      blog.title.toLowerCase().includes(searchTerm.toLowerCase())
    );

  return (
    <main className="flex min-h-screen flex-col items-center">
      <div className="w-full max-w-screen-lg mx-auto p-4">
        <section className="mb-8">
          <h2 className="text-2xl font-bold mb-2">About Me</h2>
          <p className="text-lg">
            Hi, I&apos;m {siteConfig.author}, a backend engineer with a passion
            for creating efficient and scalable solutions. Welcome to my blog
            where I share my thoughts and experiences on various tech topics.
          </p>
          <div className="flex space-x-4 mt-4">
            <a
              href={siteConfig.links.linkedIn}
              target="_blank"
              rel="noopener noreferrer"
              className="text-blue-600 hover:text-blue-800"
            >
              <FaLinkedin size={30} />
            </a>
            <a
              href={siteConfig.links.github}
              target="_blank"
              rel="noopener noreferrer"
              className="text-gray-900 hover:text-gray-700 dark:text-white"
            >
              <FaGithub size={30} />
            </a>
          </div>
        </section>
        <section className="mb-8">
          <h2 className="text-3xl font-bold mb-4">Latest Projects</h2>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
            {projects.length > 0 ? (
              projects.map((project) => (
                <div
                  key={project.id}
                  className="p-4 border rounded-lg shadow-sm hover:shadow-md"
                >
                  <Image
                    src={project.imageUrl}
                    alt={project.title}
                    width={400}
                    height={200}
                    className="rounded-lg mb-4"
                  />
                  <h3 className="text-2xl font-semibold">{project.title}</h3>
                  <p>{project.description}</p>
                </div>
              ))
            ) : (
              <h1>Very soon ...</h1>
            )}
          </div>
        </section>
        <section className="mb-8">
          <h2 className="text-3xl font-bold mb-4">Latest Blogs</h2>
          <input
            type="text"
            placeholder="Search blogs..."
            value={searchTerm}
            onChange={handleSearch}
            className="w-full p-2 mb-8 border rounded focus:outline-none focus:border-zinc-500"
          />
          <ul className="space-y-4">
            {sortedPosts.map((blog) => (
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
          </ul>
        </section>
      </div>
    </main>
  );
};

export default Home;
