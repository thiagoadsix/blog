package shared

type Filter struct {
	Column string
	Value  interface{}
}

type Pagination struct {
	Limit      int         `json:"limit" query:"limit" validate:"omitempty"`
	Page       int         `json:"page" query:"page" validate:"omitempty"`
	Filters    []Filter    `json:"filters" query:"filters" validate:"omitempty,dive"`
	Search     string      `json:"search" query:"search" validate:"omitempty"`
	TotalRows  int64       `json:"totalRows"`
	TotalPages int         `json:"totalPages"`
	Rows       interface{} `json:"rows"`
}

func (p *Pagination) GetOffset() int {
	return (p.GetPage() - 1) * p.GetLimit()
}

func (p *Pagination) GetLimit() int {
	if p.Limit == 0 {
		p.Limit = 10
	}
	return p.Limit
}

func (p *Pagination) GetPage() int {
	if p.Page == 0 {
		p.Page = 1
	}
	return p.Page
}
