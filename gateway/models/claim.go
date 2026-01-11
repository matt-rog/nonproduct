package models

import (
	"time"
	"github.com/go-pg/v10"
)

type Claim struct {
	ID		uint	`pg:"id,pk,default:nextval('claims_id_seq')"`
	Code	string	`pg:"code,notnull"`
	Name	string	`pg:"name,notnull"`
	Description	string	`pg:"description,notnull"`
}

func (cl *Claim) TableName() string {
	return "claims"
}