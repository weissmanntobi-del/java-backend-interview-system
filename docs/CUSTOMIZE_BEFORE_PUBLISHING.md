# Customise before publishing

Replace the following placeholders throughout the repository:

| Placeholder | Replace with |
| --- | --- |
| `YOUR_GUMROAD_URL` | Final Gumroad product URL |
| `YOUR_GITHUB_USERNAME` | GitHub account or organisation |
| `YOUR_SUPPORT_EMAIL` | Private support email |
| `YOUR_SECURITY_EMAIL` | Private security-report email |

Also update:

- `.github/CODEOWNERS` with your GitHub username;
- `.github/FUNDING.yml` with the real product URL;
- repository description and topics;
- product banner or social preview image;
- `CITATION.cff` repository URL;
- `product.yml` URLs and email;
- `SECURITY.md` supported versions when new versions are released.

Run:

```bash
python3 scripts/validate_repo.py
```

The script reports every remaining placeholder. It treats placeholders as warnings until you publish.
