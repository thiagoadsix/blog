package routes

import (
	"posts/internal/domain/post"
)

type PostHandler struct {
	PostService post.Service
}
