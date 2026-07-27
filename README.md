<h1 align="center">🤖 Automation OpenPR</h1>

<p align="center">
  <b>Open the Simulink models changed in a pull request — automatically, straight from the PR link.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.6+-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/MATLAB%2FSimulink-E16737?style=flat-square&logo=mathworks&logoColor=white" alt="MATLAB/Simulink" />
  <img src="https://img.shields.io/badge/GitHub%20CLI-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub CLI" />
</p>

---

## 📌 What it does

Reviewing model-based (Simulink) pull requests by hand is repetitive: open the PR, read the diff, figure out **which `.slx` / `.sldd` files changed**, find each one in your local workspace, and open them one by one in MATLAB.

**Automation OpenPR turns that whole routine into a single command.** Give it a pull request URL and it opens every changed Simulink model (`.slx`) and data dictionary (`.sldd`) for you, ready to review.

### Manual → Automated

| Step | Manual | With Automation OpenPR |
|---|---|---|
| Find changed models | Read the PR diff, file by file | Done for you |
| Locate them locally | Navigate the workspace by hand | Resolved from your repo path |
| Open in MATLAB | One model at a time | All of them at once |
| Effort per review | Several manual steps | `openpr <pr_url>` |

## ⚙️ How it works

1. Uses the **GitHub CLI (`gh`)** to fetch the pull request and list its changed files.
2. Filters for Simulink artifacts (`.slx`, `.sldd`).
3. Opens each one in **MATLAB** from your configured local repository path.

## ✅ Requirements

- **Python 3.6+** — https://www.python.org/
- **GitHub CLI (`gh`)** — https://cli.github.com/
- **MATLAB** (with Simulink)
- Access to the target GitHub repository *(connect to your VPN first if it lives on an internal / enterprise GitHub host)*

## 🚀 Setup

> Replace the placeholders (`<...>`) with your own values.

**1. Install Python and the GitHub CLI** (links above).

**2. Authenticate the GitHub CLI** against your GitHub host — run in PowerShell (VPN on if the host is internal):

```powershell
$env:GH_HOST="<YOUR_GITHUB_HOST>"
gh.exe auth login -h $env:GH_HOST
```

Follow the browser flow when prompted.

**3. Confirm the tools are available** — in Git Bash:

```bash
gh --version
python --version
```

If both print a version, you're good to go.

**4. Configure your local path** — open `local_config.py` and set the path to your local model repository.

## ▶️ Usage

Run the script with a PR URL:

```bash
python /c/<your-path>/script.py <your_pr_url>
```

### Optional: a shorter command

Create an alias so you can call it from anywhere. In Git Bash:

```bash
nano ~/.bashrc
```

Add this line:

```bash
alias openpr='python /c/<your-path>/script.py'
```

Save (`Ctrl + O`, then `Enter`) and exit (`Ctrl + X`), then reload:

```bash
source ~/.bashrc
```

Now you can simply run:

```bash
openpr <your_pr_url>
```

**Enjoy! 🚀**

---

## 💡 Why it exists

Model-based design reviews happen constantly, and the manual "find-and-open" step adds friction to every one of them. Automating it keeps the reviewer focused on **the models**, not on hunting for files around them — saving time on every single PR.
