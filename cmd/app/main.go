package main

import (
	"context"
	"log"
	"net/http"
	"os"

	"github.com/go-chi/chi"
	"github.com/go-chi/chi/middleware"
	"github.com/jackc/pgx/v5"
	"github.com/joho/godotenv"

	"posts/internal/domain/post"
	db "posts/internal/infra/database/config"
	postRepository "posts/internal/infra/repository/post"
	"posts/internal/routes"
	postRoutes "posts/internal/routes/post"
)

func main() {
	err := godotenv.Load()

	if err != nil {
		log.Fatalf("Error loading .env file: %s", err.Error())
		panic("Error loading .env file")
	}

	r := chi.NewRouter()

	r.Use(middleware.RequestID)
	r.Use(middleware.RealIP)
	r.Use(middleware.Logger)
	r.Use(middleware.Recoverer)

	dsn := os.Getenv("DATA_BASE_URL")
	config, err := pgx.ParseConfig(dsn)
	if err != nil {
		log.Fatalf("Unable to parse database URL: %v\n", err)
	}

	dbPool, err := pgx.ConnectConfig(context.Background(), config)
	if err != nil {
		log.Fatalf("Unable to create connection pool: %v\n", err)
	}
	defer dbPool.Close(context.Background())

	sqlcQueries := db.New(dbPool)

	postService := post.ServiceImpl{
		PostRepository: &postRepository.PostRepository{Queries: sqlcQueries, Ctx: context.Background()},
	}
	postHandler := postRoutes.PostHandler{
		PostService: &postService,
	}

	r.Route("/posts", func(r chi.Router) {
		r.Post("/", routes.HandlerError(postHandler.PostPost))
		r.Get("/", routes.HandlerError(postHandler.PostGetAllPaginated))
	})

	http.ListenAndServe(":3000", r)
}
