# pyqtforge/cli.py
import typer
from generator import generate_project
from envmanager import create_venv, install_packages
from runner import run_project

app = typer.Typer()

@app.command("createproject")
def create_project(name: str):
    """Create a new PyQt project with the given name."""
    generate_project(name)

    # Step 1: Virtual environment setup
    use_venv = typer.confirm("🧪 Create a virtual environment in this project?", default=False)
    venv_path = None
    if use_venv:
        venv_path = create_venv(name)

    # Step 2: Install PyQt packages
    if typer.confirm("📦 Install recommended packages (pyqt5, pyqt5-tools)?", default=True):
        install_packages(["pyqt5", "pyqt5-tools"], venv_path)

    # Step 3: Setup PyInstaller
    if typer.confirm("📦 Set up PyInstaller for packaging your app?", default=False):
        install_packages(["pyinstaller"], venv_path)

    print("🎉 Project setup complete!")



# @app.command("runproject")
# def run_project_command(name: str):
#     """Run a PyQt project by its folder name."""
#     run_project(name)

@app.command("runproject")
def run_project_command(
    name: str,
    venv: bool = typer.Option(False, help="Use virtual environment in the project folder."),
    debug: bool = typer.Option(False, help="Enable debug mode (prints commands).")
):
    """Run a PyQt project by its folder name."""
    run_project(name, use_venv=venv, debug=debug)

if __name__ == "__main__":
    app()
