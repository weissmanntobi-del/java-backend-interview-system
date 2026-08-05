# SQL sample: deep OFFSET versus keyset pagination

This small PostgreSQL sample demonstrates one concept from the complete SQL performance laboratory.

## Requirements

- PostgreSQL 14 or later
- `psql`
- a disposable local database

## Run the sample

```bash
createdb java_interview_sample
psql -d java_interview_sample -f samples/sql/01_sample_schema.sql
psql -d java_interview_sample -f samples/sql/02_deep_offset.sql
psql -d java_interview_sample -f samples/sql/03_keyset_fix.sql
```

## What to compare

For both queries, inspect:

- execution time;
- rows scanned or discarded;
- scan type;
- explicit sort operations;
- shared-buffer activity;
- whether the ordering is deterministic.

Deep OFFSET remains logically valid, but the database must still locate and skip the earlier rows. Keyset pagination starts after a known `(created_at, id)` cursor and avoids repeatedly discarding the complete prefix.

The exact plan depends on PostgreSQL version, data statistics, cache state, and hardware.
