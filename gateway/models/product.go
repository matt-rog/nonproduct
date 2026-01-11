package models

import (
	"time"
	"github.com/go-pg/v10"
)

type Product struct {
	ID			uint	`pg:"id,pk,default:nextval('products_id_seq')"`
	Name		string	`pg:"name,notnull"`
	CompanyIDs	[]int64 `pg:"company_ids,notnull,array"`
	
}

func (p *Product) TableName() string {
	return "products"
}