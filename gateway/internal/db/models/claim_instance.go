package models

type ClaimInstanceApplies string

const (
	ClaimInstanceAppliesTrue   ClaimInstanceApplies = "true"
	ClaimInstanceAppliesUnsure ClaimInstanceApplies = "unsure"
	ClaimInstanceAppliesFalse  ClaimInstanceApplies = "false"
)

type ClaimInstanceConfidence string

const (
	ClaimInstanceConfidenceHigh   ClaimInstanceConfidence = "high"
	ClaimInstanceConfidenceMedium ClaimInstanceConfidence = "medium"
	ClaimInstanceConfidenceLow    ClaimInstanceConfidence = "low"
)

type ClaimInstance struct {
	ID         uint                    `pg:",pk"`
	ClaimID    int64                   `pg:"claim_id,notnull"`
	ProductID  int64                   `pg:"product_id"`
	CompanyID  int64                   `pg:"company_id"`
	TraceID    int64                   `pg:"trace_id"`
	Applies    ClaimInstanceApplies    `pg:"applies,notnull"`
	Confidence ClaimInstanceConfidence `pg:"confidence,notnull"`
}

func (cl *ClaimInstance) TableName() string {
	return "claim_instances"
}
