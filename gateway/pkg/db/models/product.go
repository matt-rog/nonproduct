package models

import (
)

type Product struct {
	ID          uint   `pg:",pk"`
	Name		string	`pg:"name,notnull"`
	CompanyIDs	[]int64 `pg:"company_ids,notnull,array"`
	
}

func (p *Product) TableName() string {
	return "products"
}