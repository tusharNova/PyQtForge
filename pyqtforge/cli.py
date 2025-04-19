
from typing import Optional

import typer
from generator import generate_project
from envmanager import create_venv, install_packages
from runner import run_project
import os
from pathlib import Path
import subprocess
from pathlib import Path

app = typer.Typer()

@app.command("createproject")
def create_project(
    name: str,
    no_prompt: bool = typer.Option(False, "--no-prompt", help="Run setup without any questions"),
):
    """Create a new PyQt project with the given name."""
    from envmanager import create_venv, install_packages
    from generator import generate_project

    generate_project(name)

    venv_path = None
    if no_prompt:
        print("⚙️ Running in no-prompt mode.")
        venv_path = create_venv(name)
        install_packages(["pyqt5", "pyqt5-tools"], venv_path)
        install_packages(["pyinstaller"], venv_path)
    else:
        use_venv = typer.confirm("🧪 Create a virtual environment in this project?", default=False)
        if use_venv:
            venv_path = create_venv(name)

        if typer.confirm("📦 Install recommended packages (pyqt5, pyqt5-tools)?", default=True):
            install_packages(["pyqt5", "pyqt5-tools"], venv_path)

        if typer.confirm("📦 Set up PyInstaller for packaging your app?", default=False):
            install_packages(["pyinstaller"], venv_path)

    print("🎉 Project setup complete!")

@app.command("runproject")
def run_project_command(
    name: str,
    venv: bool = typer.Option(False, help="Use virtual environment in the project folder."),
    debug: bool = typer.Option(False, help="Enable debug mode (prints commands).")
):
    """Run a PyQt project by its folder name."""
    run_project(name, use_venv=venv, debug=debug)



@app.command()
def createui(
    ui_name: str = typer.Argument(..., help="The name of the UI file (without .ui)"),
):
  pass


if __name__ == "__main__":
    app()
