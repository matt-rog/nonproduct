package models

type Quality struct {
	ID          uint   `pg:",pk" yaml:"id"`
	Name        string `pg:"name,notnull" yaml:"name"`
	Description string `pg:"description,notnull" yaml:"description"`
}

func (q *Quality) TableName() string {
	return "qualities"
}
