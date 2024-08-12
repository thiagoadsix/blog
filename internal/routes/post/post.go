package routes

import (
	"net/http"

	"github.com/go-chi/render"

	"posts/internal/domain/post"
)

func (h *PostHandler) PostPost(w http.ResponseWriter, r *http.Request) (interface{}, int, error) {
	var request CreatePostRequest
	if err := render.DecodeJSON(r.Body, &request); err != nil {
		return nil, http.StatusBadRequest, err
	}

	newPost := post.Post{
		Title:   request.Title,
		Type:    request.Type,
		Coupon:  request.Coupon,
		Price:   request.Price,
		DueDate: request.DueDate.Time,
		Status:  request.Status,
		Link:    request.Link,
		Fixed:   request.Fixed,
	}

	err := h.PostService.Create(newPost)
	if err != nil {
		return nil, http.StatusInternalServerError, err
	}

	return nil, http.StatusCreated, nil
}
