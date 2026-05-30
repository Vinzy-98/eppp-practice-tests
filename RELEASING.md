# Release Checklist

Follow these steps every time you publish a new version of the app.

## Before you edit anything

- [ ] Make sure you are on the `main` branch:
  ```bash
  git checkout main
  git pull
  ```

## Make your changes

- [ ] Edit files inside `eppp_app/` as needed (questions, UI, style, etc.)
- [ ] Test locally by opening `eppp_app/index.html` in your browser

## Publish

```bash
git add .
git commit -m "Short description of what changed"
git push
```

## Verify

- [ ] Open https://github.com/Vinzy-98/eppp-practice-tests/actions
- [ ] Confirm the **Deploy EPPP App to GitHub Pages** workflow shows a green checkmark
- [ ] Open the live site and spot-check one test:
  https://vinzy-98.github.io/eppp-practice-tests/

## Done

The same link your users already have will automatically serve the new version.
No action needed from users — they just refresh the page.
