import Image from "next/image";
import type { ComponentType } from "react";
import * as runtime from "react/jsx-runtime";
import { Callout } from "./callout";
import { Details } from "./details";
import { Diagram } from "./diagram";
import { QA } from "./qa";

type MDXComponent = ComponentType<{ components: Record<string, unknown> }>;

const compiled = new Map<string, MDXComponent>();

function getMDXComponent(code: string): MDXComponent {
  const cached = compiled.get(code);
  if (cached) {
    return cached;
  }

  const component = new Function(code)({ ...runtime }).default as MDXComponent;
  compiled.set(code, component);
  return component;
}

const components = {
  Image,
  Callout,
  Details,
  Diagram,
  QA,
};

interface MdxProps {
  code: string;
}

export function MDXContent({ code }: MdxProps) {
  const Component = getMDXComponent(code);
  // eslint-disable-next-line react-hooks/static-components
  return <Component components={components} />;
}
