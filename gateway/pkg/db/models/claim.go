package models

type ClaimScope string

const (
	ScopeCompany ClaimScope = "company"
	ScopeProduct ClaimScope = "product"
)

type ClaimPolarity string

const (
	PolarityPositive ClaimPolarity = "positive"
	PolarityNeutral  ClaimPolarity = "neutral"
	PolarityNegative ClaimPolarity = "negative"
)

type Claim struct {
	ID          uint          `pg:",pk"`
	QualityIDs  []int64       `pg:"quality_ids,notnull,array"`
	Code        string        `pg:"code,notnull"`
	Name        string        `pg:"name,notnull"`
	Description string        `pg:"description,notnull"`
	Scope       ClaimScope    `pg:"scope,notnull"`
	Polarity    ClaimPolarity `pg:"polarity,notnull"`
}

func (cl *Claim) TableName() string {
	return "claims"
}
