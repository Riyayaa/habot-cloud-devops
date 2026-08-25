variable "project_id" {
  description = "Google Cloud project ID"
  type        = string
}

variable "region" {
  description = "Google Cloud region"
  type        = string
  default     = "asia-south1"
}

variable "bucket_name" {
  description = "D0 raw landing bucket name"
  type        = string
}

variable "dataset_id" {
  description = "D1 staged/enforced BigQuery dataset ID"
  type        = string
  default     = "d1_staged_enforced"
}

variable "security_principal" {
  description = "Principal used for least-privilege access"
  type        = string
}