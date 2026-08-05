# Book-to-repository linking

Use this repository as the public technical home of the Java Backend Interview System.

## Link from the book to GitHub

Add the stable repository URL to:

1. the copyright or product-information page;
2. the Start Here roadmap;
3. the SQL lab introduction;
4. the companion-project guide;
5. the final page or support section.

Recommended wording:

> Public samples, release notes, errata, and updates: `https://github.com/YOUR_GITHUB_USERNAME/java-backend-interview-system`

Do not link to `main/README.md`, a raw file, or a branch-specific URL. The repository root is more stable.

## Link from GitHub to Gumroad

Place the Gumroad URL in:

- the first call to action in `README.md`;
- the GitHub repository website field;
- `.github/FUNDING.yml`;
- `product.yml`;
- `CITATION.cff`;
- release descriptions where appropriate.

Recommended wording:

> Get the complete Java Backend Interview System, including all 17 PDFs, the SQL laboratory, diagrams, and companion project.

## Keep versions aligned

For each product release:

1. update the book version;
2. update `product.yml`;
3. update `CHANGELOG.md`;
4. create the matching Git tag;
5. create a GitHub Release;
6. publish the same high-level change summary on Gumroad.

Recommended mapping:

```text
Book v1.0 -> Repository tag v1.0.0
Book v1.1 -> Repository tag v1.1.0
Book v1.1.1 -> Repository tag v1.1.1
```

## Protect paid content

Do not commit:

- paid PDFs;
- source DOCX files;
- customer-download archives;
- Gumroad customer data;
- private support conversations;
- complete answer banks;
- private companion-project source unless you intentionally make it public.

The root `.gitignore` blocks common paid-file formats, but you should still inspect every commit.

## Recommended buyer journey

```text
Medium or LinkedIn article
        ↓
GitHub public companion repository
        ↓
Free technical sample and package map
        ↓
Gumroad product page
        ↓
Paid Java Backend Interview System
        ↓
GitHub errata, updates, and release notes
```
