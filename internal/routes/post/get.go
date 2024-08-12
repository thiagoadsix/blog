package routes

import (
	"errors"
	"net/http"
	"strconv"

	shared "posts/internal/domain/shared/repository"
)

func (h *PostHandler) PostGetAllPaginated(w http.ResponseWriter, r *http.Request) (interface{}, int, error) {
	limit, _ := strconv.Atoi(r.URL.Query().Get("limit"))
	page, _ := strconv.Atoi(r.URL.Query().Get("page"))
	search := r.URL.Query().Get("search")

	pagination := &shared.Pagination{
		Limit: limit,
		Page:  page,
	}

	typeFilter := r.URL.Query()["type"]
	statusFilter := r.URL.Query()["status"]
	minPriceFilter := r.URL.Query()["minPrice"]
	maxPriceFilter := r.URL.Query()["maxPrice"]

	var filters []shared.Filter

	if len(typeFilter) > 0 {
		filters = append(filters, shared.Filter{
			Column: "type",
			Value:  typeFilter,
		})
	}

	if len(statusFilter) > 0 {
		filters = append(filters, shared.Filter{
			Column: "status",
			Value:  statusFilter[0],
		})
	}

	if len(minPriceFilter) > 0 || len(maxPriceFilter) > 0 {
		var minPrice, maxPrice float32
		var err error

		if len(minPriceFilter) > 0 {
			var minPrice64 float64
			minPrice64, err = strconv.ParseFloat(minPriceFilter[0], 32)
			if err != nil {
				return errors.New("Invalid minPrice value"), http.StatusBadRequest, nil
			}
			minPrice = float32(minPrice64)
		}

		if len(maxPriceFilter) > 0 {
			var maxPrice64 float64
			maxPrice64, err = strconv.ParseFloat(maxPriceFilter[0], 32)
			if err != nil {
				return errors.New("Invalid maxPrice value"), http.StatusBadRequest, nil
			}
			maxPrice = float32(maxPrice64)
		}

		filters = append(filters, shared.Filter{
			Column: "min_price",
			Value:  minPrice,
		})
		filters = append(filters, shared.Filter{
			Column: "max_price",
			Value:  maxPrice,
		})
	}

	pagination.Filters = filters
	pagination.Search = search

	posts, err := h.PostService.GetAllPaginated(pagination)
	if err != nil {
		return nil, http.StatusInternalServerError, err
	}

	return posts, http.StatusOK, nil
}
