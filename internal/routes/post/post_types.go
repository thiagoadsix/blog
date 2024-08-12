package routes

import (
	"time"

	"posts/internal/domain/post"
)

type CustomTime struct {
	time.Time
}

const customTimeFormat = "2006-01-02"

func (ct *CustomTime) UnmarshalJSON(b []byte) (err error) {
	strInput := string(b)
	strInput = strInput[1 : len(strInput)-1]

	ct.Time, err = time.Parse(customTimeFormat, strInput)
	return
}

type CreatePostRequest struct {
	Title       string          `json:"title"`
	Type        post.TypeEnum   `json:"type"`
	Coupon      string          `json:"coupon"`
	Price       float32         `json:"price"`
	DueDate     CustomTime      `json:"dueDate"`
	Status      post.StatusEnum `json:"status"`
	Text        string          `json:"text"`
	Description string          `json:"description"`
	Link        string          `json:"link"`
	Fixed       bool            `json:"fixed"`
}
