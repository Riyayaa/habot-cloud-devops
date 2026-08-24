# HabotConnect – Task 1: Terraform Secure Staging Provisioning

## Candidate
Riya Choudhary

## Objective
Securely provision the D0 Raw Landing GCS bucket and D1 Staged/Enforced BigQuery environment using Terraform.

## Infrastructure

### D0 Raw Landing – Google Cloud Storage
- Standard storage class
- Region: asia-south1
- Uniform bucket-level access enabled
- Public access prevention enforced
- Object versioning enabled
- Time-bound storage.objectViewer IAM access

### D1 Staged/Enforced – BigQuery
- Dataset: d1_staged_enforced
- Region: asia-south1
- Table: student_staging
- Required student staging schema
- Time-bound bigquery.dataViewer IAM access
- Row-Level Security restricting access to region = 'IN-WEST'

## Validation
- Terraform validate: successful
- Terraform apply: successful
- Final terraform plan: No changes

## RLS Verification Note
The RLS policy was verified structurally and its enforcement was confirmed by BigQuery rejecting an INSERT attempt from the policy subject. A live SELECT-filtering demonstration requires a second unrestricted identity, which was not available in this environment.