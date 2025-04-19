import typer
from generator import generate_project
from runner import run_project
from envmanager import create_venv , install_packages
app = typer.Typer()



@app.command("createproject")
def create_project(name: str):
    """Create a new PyQt project with the given name."""
    generate_project(name)

    # Step 1: Venv
    use_venv = typer.confirm("🧪 Create a virtual environment in this project?", default=False)
    venv_path = None
    if use_venv:
        venv_path = create_venv(name)

    # Step 2: Install packages
    if typer.confirm("📦 Install recommended packages (PyQt5, tools)?", default=True):
        packages = ["pyqt5", "pyqt5-tools"]
        install_packages(packages, venv_path)

    # Step 3: PyInstaller
    if typer.confirm("📦 Set up PyInstaller for building executables?", default=False):
        install_packages(["pyinstaller"], venv_path)




@app.command("runproject")
def run_project_command(name: str):
    """Run a PyQt project by its folder name."""
    run_project(name)

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
