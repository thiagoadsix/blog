"use client";

import React, { useState } from "react";
import Image from "next/image";
import { FaLinkedin, FaGithub } from "react-icons/fa";
import { siteConfig } from "@/config/site";

const mockBlogs = [
  {
    id: 1,
    title: "First Blog Post",
    description: "This is the first blog post.",
    url: "https://example.com/first-blog-post",
  },
  {
    id: 2,
    title: "Second Blog Post",
    description: "This is the second blog post.",
    url: "https://example.com/second-blog-post",
  },
  {
    id: 3,
    title: "Third Blog Post",
    description: "This is the third blog post.",
    url: "https://example.com/third-blog-post",
  },
];

const mockProjects = [
  {
    id: 1,
    title: "Project One",
    description: "Description for project one.",
    imageUrl: "/project1.png",
  },
  {
    id: 2,
    title: "Project Two",
    description: "Description for project two.",
    imageUrl: "",
  },
];

const Home = () => {
  const [searchTerm, setSearchTerm] = useState("");

  const handleSearch = (event: any) => {
    setSearchTerm(event.target.value);
  };

  const filteredBlogs = mockBlogs.filter((blog) =>
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
            {mockProjects.map((project) => (
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
            ))}
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
            {filteredBlogs.map((blog) => (
              <li
                key={blog.id}
                className="p-4 border rounded-lg shadow-sm hover:shadow-md"
              >
                <h3 className="text-2xl font-semibold">{blog.title}</h3>
                <p>{blog.description}</p>
              </li>
            ))}
          </ul>
        </section>
      </div>
    </main>
  );
};

export default Home;
