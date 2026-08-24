resource "google_storage_bucket" "d0_raw_landing" {
  name                        = var.bucket_name
  project                     = var.project_id
  location                    = var.region
  storage_class               = "STANDARD"
  uniform_bucket_level_access = true
  public_access_prevention    = "enforced"

  versioning {
    enabled = true
  }

  labels = {
    layer       = "d0"
    environment = "staging"
    purpose     = "raw-landing"
  }
}

resource "google_bigquery_dataset" "d1_staged_enforced" {
  dataset_id = var.dataset_id
  project    = var.project_id
  location   = var.region

  labels = {
    layer       = "d1"
    environment = "staging"
    purpose     = "staged-enforced"
  }
}

resource "google_bigquery_table" "student_staging" {
  project    = var.project_id
  dataset_id = google_bigquery_dataset.d1_staged_enforced.dataset_id
  table_id   = "student_staging"

  deletion_protection = false

  schema = jsonencode([
    {
      name = "student_id"
      type = "STRING"
      mode = "REQUIRED"
    },
    {
      name = "student_name"
      type = "STRING"
      mode = "REQUIRED"
    },
    {
      name = "region"
      type = "STRING"
      mode = "REQUIRED"
    },
    {
      name = "requires_support"
      type = "BOOL"
      mode = "REQUIRED"
    }
  ])
}

resource "google_bigquery_row_access_policy" "region_filter" {
  project    = var.project_id
  dataset_id = google_bigquery_dataset.d1_staged_enforced.dataset_id
  table_id   = google_bigquery_table.student_staging.table_id

  policy_id = "region_filter"

  filter_predicate = "region = 'IN-WEST'"

  grantees = [
    var.security_principal
  ]
}

resource "google_bigquery_dataset_iam_member" "staging_reader" {
  project    = var.project_id
  dataset_id = google_bigquery_dataset.d1_staged_enforced.dataset_id
  role       = "roles/bigquery.dataViewer"
  member     = var.security_principal

  condition {
    title       = "AssessmentWindowAccess"
    description = "Temporary read access to the D1 staged dataset."
    expression  = "request.time < timestamp('2026-09-30T23:59:59Z')"
  }
}
resource "google_storage_bucket_iam_member" "conditional_object_viewer" {
  bucket = google_storage_bucket.d0_raw_landing.name
  role   = "roles/storage.objectViewer"
  member = var.security_principal

  condition {
    title       = "AssessmentWindowAccess"
    description = "Temporary read access to the D0 raw landing bucket."
    expression  = "request.time < timestamp('2026-09-30T23:59:59Z')"
  }
}