# PyQtForge 🛠️

**PyQtForge** is a lightweight framework and CLI tool that helps you quickly scaffold, manage, and run PyQt5 desktop applications — with ease and flexibility.

---

## ✨ Features

- 📁 Create new PyQt5 project structure instantly
- 🧠 Template rendering with Jinja2
- 📦 Includes UI files, resource folders, and ready-to-run `main.py`
- ⚙️ Run projects with a single command (`runproject`)
- 🐍 Choose between global Python or virtual environments
- 🧪 Debug mode for deeper visibility into commands

---

## 🚀 Installation

```bash
git clone https://github.com/yourusername/pyqtforge.git
cd pyqtforge
pip install -r requirements.txt
```

# 🧪 Commands

## 📦 Create a New Project
```bash
 python pyqtforge/cli.py createproject myapp
```

## 🚀 Run a Project
```bash
 python pyqtforge/cli.py runproject myapp
```

### Options:
```bash
 --venv       Use .venv inside the project (if exists)
 --debug      Print command details
```

#### Example:
```bash
 python pyqtforge/cli.py runproject myapp --venv true --debug

```

# 📁 Project Structure Example
```css
myapp/
├── main.py
├── ui/
│   └── main_window.ui
└── resources/
    └── .keep
```

# 📌 Requirements
- Python 3.7+
- PyQt5
- Typer
- Jinja2

#### Install via:
```bash
 pip install -r requirements.txt
```

# 📄 License
MIT License — feel free to use, improve, and share.

# ❤️ Contribute

This project is just getting started! PRs, ideas, and issues are welcome 🙌
Let’s make PyQt development smoother for everyone.

```yaml

---

Let me know if you want to add author info, link a logo/icon, or mention future roadmap!

```
