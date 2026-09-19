import { build } from "velite";

const isDev = process.argv.includes("dev");
await build({ watch: isDev, clean: !isDev });

/** @type {import('next').NextConfig} */
const nextConfig = {
  turbopack: {},
};

export default nextConfig;
