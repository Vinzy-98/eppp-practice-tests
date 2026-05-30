# EPPP Practice Tests

Interactive practice tests for the Examination for Professional Practice in Psychology (EPPP).

## Quick Start

### Option 1: Double-click (no server needed)
Simply open `index.html` in your web browser. The app works directly from the file system.

> On some Windows Chrome setups, local `file://` restrictions can prevent test files from loading.
> If that happens, use Option 2 (`start.bat`) instead.

### Option 2: Local server (recommended for best experience)

**macOS / Linux:**
```bash
cd eppp_app
python3 -m http.server 8080
# Open http://localhost:8080 in your browser
```
Or just run:
```bash
./start.sh
```

**Windows (Command Prompt):**
```cmd
cd eppp_app
start.bat
```

**Windows (PowerShell):**
```powershell
cd eppp_app
.\start.ps1
```

> **Note:** On Windows, Python is usually invoked as `python` rather than `python3`. The startup scripts handle this automatically.

## Features

- **21 practice tests** (9 category tests + 12 full tests) with 3,250+ questions
- **Timer** showing elapsed time during each test
- **Question navigator** — jump to any question, see which ones are answered
- **Instant scoring** — absolute score and percentage after submission
- **Detailed review** — see your answer, correct answer, and full explanation for each question
- **Progress tracking** — all attempt history stored in your browser's localStorage
- **Multiple attempts** — retake any test; each attempt is recorded separately
- **Dashboard** — overall stats, best scores, and recent attempt history

## Sharing

To share with someone else:
1. Zip or tar the entire `eppp_app` folder
2. The recipient just unzips and opens `index.html`
3. Their progress will be stored locally on their own machine

## Host On GitHub Pages (Free)

This option gives you one permanent link and easy updates.

- Users do **not** need a GitHub account.
- Users can open one public URL and start practicing immediately.
- Each user keeps their own progress in their own browser localStorage.

### One-time setup

1. Create a new GitHub repository (public) named, for example, `eppp-practice-tests`.
2. In a terminal, run from the parent folder (`Practice_tests_EPPP`):

```bash
git init
git add .
git commit -m "Initial publish: EPPP app"
git branch -M main
git remote add origin https://github.com/<your-username>/eppp-practice-tests.git
git push -u origin main
```

3. In GitHub, open the repository and go to **Settings -> Pages**.
4. Under **Build and deployment**, set **Source** to **GitHub Actions**.
5. Wait for the workflow named **Deploy EPPP App to GitHub Pages** to finish.
6. Your site URL will look like:

```text
https://<your-username>.github.io/eppp-practice-tests/
```

### Future updates

Whenever you change app files, run:

```bash
git add .
git commit -m "Update app content"
git push
```

The same public URL will serve the new version automatically after the action completes.

### Data persistence notes

- Progress is stored per browser and per device.
- Browser cache clears or private/incognito mode can remove progress.
- Keeping the same GitHub Pages URL preserves users' saved progress across app updates.

## Data Storage

All progress is stored in your browser's `localStorage` under the key `eppp_progress`. 
- Data persists across browser sessions
- Data is per-browser (different browsers = different progress)
- Clearing browser data will reset progress
