# Put this project on GitHub

**Requested owner:** `phoitran`. **Suggested repository name:** `natures-mossy-friends`.

The source package is prepared for that destination. A username alone does not grant write access. Do not put this project into another person's account merely because that account happens to be connected.

## What to upload

Extract the ZIP. Upload the **contents of the Natures-Mossy-Friends folder**, including `README.md`, `LICENSE`, documentation, source, public media and hidden configuration/example files. Do not upload only the ZIP: GitHub must be able to display the code and documentation for review.

The archive has no `.git` directory or old repository history. This gives the new repository a clean initial source commit while `EXPORT_METADATA.json` records the original Sites commit. No dependency folder, production database or visitor uploads are included.

## Straightforward route: GitHub Desktop

1. Sign into GitHub Desktop as `phoitran`.
2. Create a new local repository named `natures-mossy-friends` in an empty folder. Avoid selecting a replacement license or README; this package already supplies them.
3. Copy all extracted project contents into that new repository folder, including dotfiles such as `.gitignore`, `.dev.vars.example`, `.openai` and `.github`. On macOS, Command+Shift+Period reveals hidden files in Finder.
4. Review the changes. There should be application code, docs and media, with no credentials or generated dependency/build folders. Commit with a message such as `Add Natures Mossy Friends source and documentation`.
5. Publish the repository under `phoitran`. Private is a sensible starting setting; add the instructor as a collaborator if the course accepts private submissions. If public access is required, confirm media licensing and the instructor's requirement before changing visibility.
6. Open the repository on GitHub and confirm the README renders, the license and docs open, and the source directories are present. Check Actions for test results; a queued or failed run is not a pass.
7. Submit the repository URL, plus the live-site URL if the assignment requests it. A local ZIP alone does not satisfy “documented on GitHub.”

## Command-line route

Create an **empty** repository under `phoitran` first, with no automatically generated README, license or gitignore. From inside the extracted folder:

```sh
git init -b main
git add .
git status --short
git commit -m "Add Natures Mossy Friends source and documentation"
git remote add origin https://github.com/phoitran/natures-mossy-friends.git
git push -u origin main
```

The example remote is a proposed destination, not proof that the repository exists. Use the URL returned by GitHub if a different name was chosen. Authenticate through GitHub Desktop or the supported credential flow; do not paste a token into a remote URL or chat. If a repository already has commits, clone it and add these files on a branch instead of force-pushing over it.

All shipped files were below GitHub's individual-file limit when packaged. The many assets make a Git/Desktop push easier than a browser upload. Keep media in the repository for this full-source handoff; optimize distribution separately if it grows.

## Official help

- [Add locally hosted code](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github)
- [Add a repository to GitHub Desktop](https://docs.github.com/en/desktop/adding-and-cloning-repositories/adding-a-repository-from-your-local-computer-to-github-desktop)
- [GitHub large-file limits](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github)
