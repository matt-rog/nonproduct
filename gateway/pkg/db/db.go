package db

import (
	"log"
	"os"

	"gateway/pkg/db/models"

	"github.com/go-pg/pg/v10"
	"github.com/go-pg/pg/v10/orm"
)

func StartDB() (*pg.DB, error) {
	var (
		opts *pg.Options
		err  error
	)

	opts, err = pg.ParseURL(os.Getenv("DATABASE_URL"))
	if err != nil {
		return nil, err
	}

	db := pg.Connect(opts)

	var models = []interface{}{
		&models.Claim{},
		&models.Company{},
		&models.Product{},
		&models.Quality{},
		&models.ClaimInstance{},
		&models.Trace{},
	}

	for _, m := range models {
		if err := db.Model(m).CreateTable(&orm.CreateTableOptions{IfNotExists: true}); err != nil {
			log.Fatalf("Failed to create table %T: %v", m, err)
		}
	}

	return db, err

}
