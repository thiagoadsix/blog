interface BaseProps {
  children: React.ReactNode;
  isProselytizing?: boolean;
}

export const Base = ({ children, isProselytizing = false }: BaseProps) => (
  <main className="flex min-h-screen flex-col">
    <div
      className={`${
        isProselytizing
          ? "prose dark:prose-invert w-full max-w-screen-lg mx-auto p-4"
          : "w-full max-w-screen-lg mx-auto p-4"
      }`}
    >
      {children}
    </div>
  </main>
);
