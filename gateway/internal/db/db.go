package db

import (
	"fmt"
	"log"
	"os"

	"gateway/internal/db/models"

	"github.com/go-pg/pg/v10"
	"github.com/go-pg/pg/v10/orm"
	"github.com/stretchr/testify/assert/yaml"
)

type SeedData struct {
	Qualities []models.Quality `yaml:"qualities"`
	Claims    []models.Claim   `yaml:"claims"`
}

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

	// Seed data
	data, err := os.ReadFile("pkg/db/seed.yaml")
	if err != nil {
		fmt.Println(err)
	}
	var seedData SeedData

	err = yaml.Unmarshal(data, &seedData)
	if err != nil {
		fmt.Println(err)
		return db, err
	}

	for _, q := range seedData.Qualities {
		_, err = db.Model(&q).Insert()
		if err != nil {
			fmt.Println(err)
		}
	}

	for _, c := range seedData.Claims {
		_, err = db.Model(&c).Insert()
		if err != nil {
			fmt.Println(err)
		}
	}

	return db, err

}
