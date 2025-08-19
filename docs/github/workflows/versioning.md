# 📦 Automated Versioning with Release Please

This repository uses [release-please](https://github.com/googleapis/release-please) to manage versioning and releases.

## 🔀 Branching Workflow

- `develop` → feature integration branch.
  - Each merge into `develop` generates a **pre-release** with suffix `-dev.N`.
  - Example: `0.11.0-dev.1`.

- `main` → stable branch.
  - When `develop` is merged into `main`, release-please opens a Release PR.
  - Once that PR is merged, a **stable release** with tag and changelog is created.
  - Example: `0.11.0`.

After each release on `main`, it is recommended to do a reverse merge to keep branches in sync:

```bash
git checkout develop
git merge main
```

## ⚙️ Configuration

The release-please configuration lives in:

- `.github/workflows/release.yml`
- `.github/release-please-config.json`

### `.github/workflows/release.yml`

```yaml
name: 📦 Release Please

on:
  push:
    branches:
      - main
      - develop

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: googleapis/release-please-action@v4
        with:
          config-file: .github/release-please-config.json
          token: ${{ secrets.GITHUB_TOKEN }}
```

### `.github/release-please-config.json`

```json
{
  "branches": [
    {
      "branch": "develop",
      "release-type": "python",
      "prerelease": true,
      "prerelease-type": "dev",
      "packages": {
        ".": {
          "package-name": "sakugaflow"
        }
      }
    },
    {
      "branch": "main",
      "release-type": "python",
      "packages": {
        ".": {
          "package-name": "sakugaflow"
        }
      }
    }
  ]
}
```

## 📝 Commit Convention

Release Please uses commit messages to determine the version bump:

- `feat:` → **minor** (`0.11.0 → 0.12.0`)
- `fix:` → **patch** (`0.11.0 → 0.11.1`)
- `BREAKING CHANGE:` in the body → **major** (`0.11.0 → 1.0.0`)
- Other types (`docs:`, `chore:`, `ci:`, etc.) do not affect version numbers.

## ✅ Summary

- `develop` → pre-release tags (`-dev.N`).
- `main` → stable tags + GitHub Releases.
- Automatic versioning based on Conventional Commits.
