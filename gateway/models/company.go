package models

import (
	"time"
	"github.com/go-pg/v10"
)

type Company struct {
	ID		uint	`pg:"id,pk,default:nextval('companies_id_seq')"`
	Name	string	`pg:"name,notnull"`
}

func (c *Company) TableName() string {
	return "companies"
}