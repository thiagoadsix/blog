-- name: SearchPosts :many
SELECT p.id,
  p.title,
  p.type,
  p.coupon,
  p.price,
  p.due_date,
  p.status,
  p.link,
  p.fixed,
  p.created_at,
  p.updated_at,
  p.deleted_at
FROM public.posts p
WHERE COALESCE(
    p.search @@ websearch_to_tsquery('simple', sqlc.narg('search')),
    TRUE
  )
  AND (
    p.type = ANY(@types::text [])
    OR NOT @filter_by_type
  )
  AND (
    (
      p.price >= sqlc.narg('min_price')
      AND p.price <= sqlc.narg('max_price')
    )
    OR NOT @filter_by_price
  ) OFFSET sqlc.arg('offset')
LIMIT sqlc.arg('limit');
-- name: CountPosts :one
SELECT COUNT(*)
FROM posts;
-- name: CreatePost :one
INSERT INTO public.posts (
    id,
    title,
    type,
    coupon,
    price,
    due_date,
    status,
    link,
    fixed,
    created_at,
    updated_at,
    deleted_at
  )
VALUES (
    $1,
    $2,
    $3,
    $4,
    $5,
    $6,
    $7,
    $8,
    $9,
    $10,
    $11,
    $12
  )
RETURNING *;