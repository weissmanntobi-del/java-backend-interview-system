# Publish this repository to GitHub

## 1. Customise the repository

Open [CUSTOMIZE_BEFORE_PUBLISHING.md](docs/CUSTOMIZE_BEFORE_PUBLISHING.md) and replace every placeholder.

At minimum, set:

- Gumroad product URL;
- GitHub username and final repository name;
- support email;
- security-report email;
- repository owner in `CODEOWNERS`.

## 2. Validate locally

```bash
python3 scripts/validate_repo.py
make sample
make clean
```

## 3. Create the GitHub repository

Suggested repository name:

```text
java-backend-interview-system
```

Suggested description:

```text
Public samples, study paths, errata and release notes for the Java Backend Interview System for engineers with 2–5 years of experience.
```

Suggested topics:

```text
java spring-boot backend interview-preparation postgresql system-design dsa sql performance-debugging
```

## 4. Push the files

```bash
git init
git branch -M main
git add .
git commit -m "Release public companion repository v1.0.0"
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/java-backend-interview-system.git
git push -u origin main
```

## 5. Create the release tag

```bash
git tag -a v1.0.0 -m "Java Backend Interview System public companion v1.0.0"
git push origin v1.0.0
```

Create a GitHub Release from tag `v1.0.0` and copy the relevant section from `CHANGELOG.md`.

## 6. Configure the repository

Recommended settings:

- enable Issues;
- enable Discussions only when you are ready to moderate them;
- protect the `main` branch;
- require the quality workflow before merging;
- disable wiki unless you intend to maintain duplicate documentation;
- add the Gumroad URL under the repository website field;
- upload your product banner as the social preview image.

## 7. Add the repository URL to the book

Use one stable URL:

```text
https://github.com/YOUR_GITHUB_USERNAME/java-backend-interview-system
```

Do not link the book to a branch-specific file that may later move.
