package post

import (
	"time"
)

type TypeEnum string

const (
	COUPON TypeEnum = "COUPON"
	OFFER  TypeEnum = "OFFER"
)

type StatusEnum string

const (
	DELETED   StatusEnum = "DELETED"
	EXPIRED   StatusEnum = "EXPIRED"
	PUBLISHED StatusEnum = "PUBLISHED"
)

type Post struct {
	ID        string     `json:"id" `
	Title     string     `json:"title"`
	Type      TypeEnum   `json:"type"`
	Coupon    string     `json:"coupon"`
	Price     float32    `json:"price"`
	DueDate   time.Time  `json:"dueDate"`
	Status    StatusEnum `json:"status" validate:"status_enum"`
	Link      string     `json:"link"`
	Fixed     bool       `json:"fixed"`
	CreatedAt time.Time  `json:"createdAt"`
	UpdatedAt time.Time  `json:"updatedAt"`
	DeletedAt time.Time  `json:"deletedAt"`
}

type Status struct {
	Status StatusEnum `json:"status" validate:"required,status_enum"`
}

func CreatePost(
	title string,
	postType TypeEnum,
	coupon string,
	price float32,
	dueDate time.Time,
	status StatusEnum,
	link string,
	fixed bool,
) *Post {
	post := &Post{
		Title:     title,
		Type:      postType,
		Coupon:    coupon,
		Price:     price,
		DueDate:   dueDate,
		Status:    status,
		Link:      link,
		Fixed:     fixed,
		CreatedAt: time.Now(),
	}

	return post
}
