import Image from "next/image";

interface DiagramProps {
  src: string;
  alt: string;
  width: number;
  height: number;
  caption?: string;
}

export function Diagram({ src, alt, width, height, caption }: DiagramProps) {
  return (
    <figure className="my-8">
      <Image
        src={`${src}-light.png`}
        alt={alt}
        width={width}
        height={height}
        className="w-full dark:hidden"
      />
      <Image
        src={`${src}-dark.png`}
        alt={alt}
        width={width}
        height={height}
        className="hidden w-full dark:block"
      />
      {caption ? (
        <figcaption className="mt-3 text-center text-sm text-muted-foreground">
          {caption}
        </figcaption>
      ) : null}
    </figure>
  );
}
