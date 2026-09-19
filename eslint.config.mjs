import nextCoreWebVitals from "eslint-config-next/core-web-vitals";

const config = [
  {
    ignores: ["examples/**", ".next/**", ".velite/**", "public/static/**"],
  },
  ...nextCoreWebVitals,
];

export default config;
