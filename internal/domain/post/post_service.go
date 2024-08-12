package post

import (
	shared "posts/internal/domain/shared/repository"
)

type Service interface {
	Create(newPost Post) error
	GetAllPaginated(pagination *shared.Pagination) (*shared.Pagination, error)
}

type ServiceImpl struct {
	PostRepository PostRepository
}

func (s *ServiceImpl) Create(newPost Post) error {
	post := CreatePost(
		newPost.Title,
		newPost.Type,
		newPost.Coupon,
		newPost.Price,
		newPost.DueDate,
		newPost.Status,
		newPost.Link,
		newPost.Fixed,
	)

	err := s.PostRepository.Create(post)
	if err != nil {
		return err
	}

	return nil
}

func (s *ServiceImpl) GetAllPaginated(pagination *shared.Pagination) (*shared.Pagination, error) {
	posts, err := s.PostRepository.FindAllPaginated(pagination)
	if err != nil {
		return nil, err
	}

	return posts, nil
}
