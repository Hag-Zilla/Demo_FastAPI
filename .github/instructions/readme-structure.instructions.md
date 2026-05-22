---
applyTo: "**/README.md,**/CHANGELOG.md"
---

## Purpose

Enforce a consistent README structure so every project exposes the same navigation
pattern and minimum required information.

## Required Sections (in order)

1. **Title + Badges** — Project name as H1; shields.io badges for CI, release, license,
   and any relevant tool (Copilot, pre-commit, etc.).
2. **Table of Contents** — Linked list matching the actual headings below.
3. **About** — One paragraph: what the project does, the problem it solves, and the
   target audience.
4. **Key Features** — Bulleted list of the main capabilities (5–8 items max).
5. **Quick Start** — Numbered steps: clone → environment setup → run.
   Include the minimum commands to get a working state.
6. **Architecture** — Layer model or component interaction description. No file tree.
7. **Repository Structure** — Tree view of the project layout
   (reference `project-structure.instructions.md`).
8. **Configuration & Customization** — How to adapt the project (env vars, config
   files, instruction files). Include language and branch strategy tables.
9. **Roadmap** — Optional. Planned features not yet implemented; omit if empty.
10. **Contributing** — Link to `CONTRIBUTING.md`; one-sentence summary of the workflow.
11. **License** — License name and link to `LICENSE`.

## Guidelines

- Do not add sections that are empty or contain only "Coming soon."
- Keep the **About** section under 5 sentences.
- **Quick Start** must be self-contained: a reader with a clean environment should reach
  a working state following only those steps.
- Use ATX headings only (`##`, `###`), never setext (underline-style).
- Fenced code blocks must specify a language (` ```bash `, ` ```python `, ` ```text `).
- Lists must be surrounded by blank lines (markdownlint MD032).
- Line length limit: follow the value set in `.github/.markdownlint.json`.
- The interaction language of the README must match the `Interaction language` setting
  in `.github/copilot-instructions.md`.

## Badges (standard set)

```markdown
![CI](https://github.com/<org>/<repo>/actions/workflows/quality.yml/badge.svg)
![GitHub release](https://img.shields.io/github/v/release/<org>/<repo>)
![License](https://img.shields.io/badge/License-<SPDX>-lightgrey.svg)
![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen.svg)
```

Replace `<org>`, `<repo>`, and `<SPDX>` with actual values.

## Examples

````markdown
# MyProject — Short tagline

![CI](https://github.com/org/myproject/actions/workflows/quality.yml/badge.svg)
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)

## About

MyProject does X to solve Y for Z audience.

## Key Features

- Feature A.
- Feature B.

## Quick Start

```bash
git clone https://github.com/org/myproject.git
cd myproject
uv sync --group dev
uv run pre-commit install
```

## Architecture

Describe the layered model or component diagram here.

## Repository Structure

```text
project-root/
├── src/<package>/
├── tests/
└── .github/
```

## Configuration and Customization

Describe env vars, config files, and instruction files here.

## Roadmap

- Planned feature A.

## CHANGELOG.md

Maintain a CHANGELOG.md file following the **[Keep a Changelog](https://keepachangelog.com/)**
format with [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

### Standard Sections

- **Unreleased** — Changes currently in development.
- **Added** — New features and capabilities.
- **Changed** — Updates to existing functionality.
- **Deprecated** — Features marked for removal.
- **Removed** — Deleted or archived features.
- **Fixed** — Bug fixes and corrections.
- **Security** — Security patches and vulnerability fixes.

### Guidelines

- Update CHANGELOG.md with each notable change before release.
- Use semantic versioning for version numbers (e.g., `0.1.0`, `1.2.3`).
- Include links to GitHub compare views for each released version.
- Keep entries concise and user-focused; avoid implementation details.

### Example

```markdown
## [Unreleased]

### Added
- New authentication module with OAuth2 support
- Database migration system with Alembic

### Fixed
- Critical bug in expense calculations

## [0.1.0] - 2026-05-22

### Added
- Initial project setup with FastAPI

[Unreleased]: https://github.com/owner/repo/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/owner/repo/releases/tag/v0.1.0
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Licensed under [MIT](LICENSE).
````
