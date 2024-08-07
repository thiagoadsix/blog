"use client";

import React from "react";
import { Button } from "@/components/ui/button";

export const BackButton = () => {
  return <Button onClick={() => history.back()}>Back to Blog list</Button>;
};
