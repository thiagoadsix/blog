package post

import shared "posts/internal/domain/shared/repository"

type PostRepository interface {
	Create(post *Post) error
	FindAllPaginated(pagination *shared.Pagination) (*shared.Pagination, error)
}
