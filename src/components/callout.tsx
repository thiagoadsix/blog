import { ReactNode } from "react";

interface CalloutProps {
  type: "default" | "warning" | "danger";
  children: ReactNode;
}

export function Callout({
  type = "default",
  children,
  ...props
}: CalloutProps) {
  return (
    <div
      className={`border-l-4 p-4 ${
        type === "default"
          ? "border-gray-300"
          : type === "warning"
          ? "border-yellow-300"
          : type === "danger"
          ? "border-red-300"
          : "border-blue-300"
      }`}
      {...props}
    >
      {children}
    </div>
  );
}
