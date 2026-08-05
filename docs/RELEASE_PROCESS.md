# Release process

## Before a public release

1. Finalise the paid package and Start Here roadmap.
2. Confirm product counts and page totals.
3. Update `product.yml`.
4. Update `docs/PACKAGE_MAP.md` when package contents changed.
5. Update `CHANGELOG.md`.
6. Run `python3 scripts/validate_repo.py`.
7. Compile and run the Java sample.
8. Review all placeholder warnings.
9. Confirm no paid files are staged.
10. Tag the repository with the matching semantic version.

## Release-note structure

Each release note should contain:

- what changed;
- who benefits;
- compatibility with the paid book version;
- corrections included;
- known limitations;
- upgrade instructions when required.

## Version policy

- Patch: corrections that do not change the package structure.
- Minor: meaningful new content or revised modules.
- Major: substantial restructuring or a new product generation.
