CREATE TABLE public.posts (
  id uuid DEFAULT gen_random_uuid() NOT NULL,
  title text,
  type text NOT NULL,
  coupon text,
  price numeric,
  due_date timestamp with time zone,
  status text NOT NULL,
  text text NOT NULL,
  description text,
  link text,
  fixed boolean NOT NULL,
  created_at timestamp with time zone NOT NULL,
  updated_at timestamp with time zone,
  deleted_at timestamp with time zone
);