# Java Backend Interview System

**Public companion repository for the Java Backend Interview System for Engineers with 2–5 Years of Experience**

[![Version](https://img.shields.io/badge/version-1.0.0-blue)](CHANGELOG.md)
[![Java](https://img.shields.io/badge/Java-17%2B-orange)](samples/dsa/README.md)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14%2B-336791)](samples/sql/README.md)
[![Content](https://img.shields.io/badge/PDFs-17-informational)](docs/PACKAGE_MAP.md)
[![Pages](https://img.shields.io/badge/pages-1%2C049-informational)](docs/PACKAGE_MAP.md)

By **Tobias Weissmann**

## Get the complete interview system

**[Get the Complete Java Backend Interview System](https://tobiweissmann.gumroad.com/l/rntcs)**

The complete product contains the structured books, question banks, production scenarios, SQL laboratory, architecture diagrams, study plans, scorecards, and Java companion project. This public repository provides selected samples, product documentation, release information, and a transparent errata channel. It does **not** contain the complete paid PDF collection.

## What the complete system contains

- 17 PDFs with 1,049 pages
- 100 Java-focused DSA problems
- Top 100 must-master Java backend questions
- 350-question Java backend reference bank
- Spring Boot and Spring Security preparation
- production debugging scenarios with logs
- mock interview transcripts and scorecards
- eight-file PostgreSQL performance laboratory
- ten standalone architecture diagrams
- Java backend companion project
- 7-day, 14-day, and 30-day study plans

See the [package map](docs/PACKAGE_MAP.md) for the exact structure.

## Free material in this repository

| Area | Sample |
| --- | --- |
| DSA | [Solve one problem using three approaches](samples/dsa/README.md) |
| SQL | [Compare deep OFFSET with keyset pagination](samples/sql/README.md) |
| Spring Boot | [Weak, acceptable, and strong interview answer](samples/interview/transactional-answer.md) |
| Architecture | [Spring Boot request-flow practice diagram](samples/architecture/spring-boot-request-flow.md) |
| Mock practice | [Mini Java backend mock interview](samples/mock/mini-mock.md) |

## Choose your study path

- **Interview in seven days:** diagnose first, prioritise weak areas, practise aloud, and complete one scored mock.
- **Interview in fourteen days:** combine Java, DSA, Spring Boot, security, SQL, debugging, and two scored mocks.
- **Interview in thirty days:** build foundations, complete practical labs, defend project decisions, and run four scored mocks.

Read the [study paths](docs/STUDY_PATHS.md) for a concise plan.

## Repository purpose

This repository is designed to:

1. give buyers a stable public URL to place inside the book;
2. publish samples without exposing the complete paid content;
3. maintain version history and release notes;
4. collect corrections through a public errata process;
5. make product scope and file structure transparent;
6. provide a professional technical home for the interview system.

## Recommended linking model

Use a two-way link:

- the PDF roadmap links to this GitHub repository;
- this GitHub repository links to the Gumroad product page.

Follow [Book-to-repository linking](docs/BOOK_TO_REPO_LINKING.md) before publishing.

## Quick start for repository samples

Compile and run the Java sample:

```bash
javac samples/dsa/TwoSumThreeApproaches.java
java -cp samples/dsa TwoSumThreeApproaches
```

Review the SQL sample:

```bash
cat samples/sql/README.md
```

Run repository validation:

```bash
python3 scripts/validate_repo.py
```

## Version compatibility

| Book release | Repository tag | Status |
| --- | --- | --- |
| Java Backend Interview System v1.0 | `v1.0.0` | Initial public companion release |

For future updates, keep the book version, Gumroad release note, and GitHub tag aligned.

## Corrections and support

- Report a confirmed content problem through the [content-correction issue form](https://github.com/weissmann-tobi/java-backend-interview-system/issues/new?template=content_correction.yml).
- Check [ERRATA.md](docs/ERRATA.md) before reporting a known issue.
- For purchase or account questions, use `YOUR_SUPPORT_EMAIL` rather than a public GitHub issue.

## Important boundaries

Do not open GitHub issues containing:

- paid PDF pages or complete answer sections;
- order numbers, email addresses, or payment information;
- employer-confidential interview questions;
- leaked or proprietary company material.

## Disclaimer

This is an independent interview-preparation resource. It does not contain leaked interview questions, confidential company information, or a guarantee of employment. Interview formats vary by role, company, location, and experience level.

## Licensing

Sample source code is available under the [MIT License](LICENSE). Written product descriptions, sample interview content, diagrams, and book-related material remain subject to [CONTENT_LICENSE.md](CONTENT_LICENSE.md).
