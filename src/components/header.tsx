import Image from "next/image";
import Link from "next/link";
import { ModeToggle } from "./ui/mode-toggle";
import { siteConfig } from "@/config/site";

export const Header = () => (
  <header className="w-full">
    <div className="max-w-screen-lg mx-auto flex justify-between items-center p-4">
      <div className="flex items-center">
        <h1 className="text-xl font-bold">{siteConfig.author}</h1>
      </div>
      <div className="flex items-center space-x-4">
        <Link href="/">
          <button className="btn">Home</button>
        </Link>
        <Link href="/blog">
          <button className="btn">Blog</button>
        </Link>
        <ModeToggle />
      </div>
    </div>
  </header>
);
