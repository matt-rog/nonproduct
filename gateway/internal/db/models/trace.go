package models

type Trace struct {
	ID uint `pg:",pk"`
}

func (t *Trace) TableName() string {
	return "traces"
}
