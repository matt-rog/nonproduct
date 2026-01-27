package models

type Company struct {
	ID   uint   `pg:",pk"`
	Name string `pg:"name,notnull"`
}

func (c *Company) TableName() string {
	return "companies"
}
