package repository

import (
	"context"
	"fmt"
	"time"

	"github.com/jackc/pgx/v5/pgtype"

	"posts/internal/domain/post"
	shared "posts/internal/domain/shared/repository"
	db "posts/internal/infra/database/config"
)

type PostRepository struct {
	Queries *db.Queries
	Ctx     context.Context
}

func (pr *PostRepository) Create(post *post.Post) error {
	now := time.Now()
	post.CreatedAt = now
	post.UpdatedAt = now

	_, err := pr.Queries.CreatePost(pr.Ctx, db.CreatePostParams{
		ID:        pgtype.UUID{Bytes: post.ID.Bytes(), Status: pgtype.Present},
		Title:     pgtype.Text{String: post.Title, Status: pgtype.Present},
		Type:      pgtype.Text{String: string(post.Type), Status: pgtype.Present},
		Coupon:    pgtype.Text{String: post.Coupon, Status: pgtype.Present},
		Price:     pgtype.Numeric{Float: float64(post.Price), Status: pgtype.Present},
		DueDate:   pgtype.Timestamptz{Time: post.DueDate, Status: pgtype.Present},
		Status:    pgtype.Text{String: string(post.Status), Status: pgtype.Present},
		Link:      pgtype.Text{String: post.Link, Status: pgtype.Present},
		Fixed:     pgtype.Bool{Bool: post.Fixed, Status: pgtype.Present},
		CreatedAt: pgtype.Timestamptz{Time: post.CreatedAt, Status: pgtype.Present},
		UpdatedAt: pgtype.Timestamptz{Time: post.UpdatedAt, Status: pgtype.Present},
		DeletedAt: pgtype.Timestamptz{Time: post.DeletedAt.Time, Status: post.DeletedAt.Status},
	})

	if err != nil {
		return err
	}

	return nil
}

func (pr *PostRepository) FindAllPaginated(pagination *shared.Pagination) (*shared.Pagination, error) {
	offset := pagination.GetOffset()
	limit := pagination.GetLimit()

	searchText := pgtype.Text{
		String: pagination.Search,
		Valid:  pagination.Search != "",
	}

	params := db.SearchPostsParams{
		FilterByType:  false,
		FilterByPrice: false,
		Limit:         int32(limit),
		Offset:        int32(offset),
		Search:        searchText,
	}

	for _, filter := range pagination.Filters {
		switch filter.Column {
		case "type":
			if val, ok := filter.Value.([]string); ok {
				params.Types = val
				params.FilterByType = true
			}
		case "min_price":
			if val, ok := filter.Value.(float32); ok {
				params.MinPrice = val
				params.FilterByPrice = true
			}
		case "max_price":
			if val, ok := filter.Value.(float32); ok {
				params.MaxPrice = val
				params.FilterByPrice = true
			}
		default:
			fmt.Printf("Unsupported filter supplied, Column: %s, Value: %v\n", filter.Column, filter.Value)
		}
	}

	posts, err := pr.Queries.SearchPosts(pr.Ctx, params)

	if err != nil {
		return nil, err
	}

	totalRows, err := pr.Queries.CountPosts(pr.Ctx)
	if err != nil {
		return nil, err
	}

	pagination.Rows = posts
	pagination.TotalRows = totalRows
	pagination.TotalPages = int((totalRows + int64(limit) - 1) / int64(limit))

	return pagination, nil
}
