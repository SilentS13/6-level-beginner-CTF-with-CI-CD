# Contributing to the Web CTF Project

Welcome to the team! To keep our development organized, please follow these guidelines.

## Team Roles
- **Project Lead:** Overall coordination and GitHub repository management.
- **Security Researchers:** Designing and implementing the vulnerabilities (Levels 1-6).
- **QA/Testers:** Verifying that flags are reachable and the "hints" are helpful.
- **Documentation Lead:** Maintaining the README and solution guides.

## Workflow
1. **Branching:** Create a new branch for each feature or level (e.g., `feature/level-7` or `fix/typos`).
2. **Pull Requests:** Submit a PR for any changes. At least one other team member must review it.
3. **Testing:** Ensure the GitHub Action passes before merging.

## Adding New Levels
1. Create a new folder `level-X`.
2. Add an `index.html` or necessary server code.
3. Update the main `README.md` with the new level description and flag.
