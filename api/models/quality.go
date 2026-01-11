package models

import (
	"time"
	"github.com/go-pg/v10"
)

type Quality struct {
	ID		uint	`pg:"id,pk,default:nextval('qualities_id_seq')"`
	Code	string	`pg:"code,notnull"`
	Name	string	`pg:"name,notnull"`
	Description	string	`pg:"description,notnull"`
}

func (q *Quality) TableName() string {
	return "qualities"
}