package models

type Claim struct {
	ID          uint   `pg:",pk"`
	Code        string `pg:"code,notnull"`
	Name        string `pg:"name,notnull"`
	Description string `pg:"description,notnull"`
}

func (cl *Claim) TableName() string {
	return "claims"
}
