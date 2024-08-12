include .env

create_migration:
	migrate create -ext=sql -dir=internal/infra/database/migrations -seq $(name)

migrate_up:
	migrate -path=internal/infra/database/migrations -database "postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}?sslmode=disable" -verbose up

migrate_down:
	migrate -path=internal/infra/database/migrations -database "postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}?sslmode=disable" -verbose down

.PHONY: create_migration migrate_up migrate_down