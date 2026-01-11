package models

import (
)

type Quality struct {
	ID          uint   `pg:",pk"`
	Code	string	`pg:"code,notnull"`
	Name	string	`pg:"name,notnull"`
	Description	string	`pg:"description,notnull"`
}

func (q *Quality) TableName() string {
	return "qualities"
}