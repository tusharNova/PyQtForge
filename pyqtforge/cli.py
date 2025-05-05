from typing import Optional
import click
import typer
from pyqtforge.runner import run_project
import subprocess
from pathlib import Path

app = typer.Typer()


@app.callback()
@click.version_option(version="0.1.0")
def main_callback():
    """
    🚀 PyQtForge — A CLI tool to manage and build PyQt5 apps easily.

    Commands:
    - createproject <name> : Create a new project
    - runproject            : Run the app from current folder
    - createui <name>       : Open Designer to create UI
    - ui2py <name>/(--all)         : Convert .ui files to Python
    """
    pass


@app.command("createproject")
def create_project(
    name: str,
    no_prompt: bool = typer.Option(False, "--no-prompt", help="Run setup without any questions"),
):
    """Create a new PyQt project with the given name."""
    from pyqtforge.envmanager import create_venv, install_packages
    from pyqtforge.generator import generate_project

    generate_project(name)

    venv_path = None
    if no_prompt:
        print("⚙️ Running in no-prompt mode.")
        venv_path = create_venv(name)
        install_packages(["pyqt5", "pyqt5-tools"], venv_path)
        # install_packages(["pyinstaller"], venv_path)
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
    venv: bool = typer.Option(False, help="Use virtual environment in the project folder."),
    debug: bool = typer.Option(False, help="Enable debug mode (prints commands).")
):
    """Run a PyQt project from the current folder."""
    run_project(use_venv=venv, debug=debug)




@app.command()
def createui(
    name: str = typer.Argument(..., help="Name for the UI file (used for suggestion only)")
):
    """
    Open Qt Designer to let the user create a new UI file manually.
    Suggest saving it as: ui/<name>.ui
    """
    ui_dir = Path("ui")
    ui_dir.mkdir(exist_ok=True)

    try:
        typer.echo(f"🔧 Opening Qt Designer... Save your file as: ui/{name}.ui")
        subprocess.run(["pyqt5-tools", "designer"], check=True)
    except FileNotFoundError:
        typer.echo("❌ Qt Designer not found. Make sure pyqt5-tools is installed.")
    except subprocess.CalledProcessError:
        typer.echo("❌ Failed to launch Qt Designer.")


@app.command()
def ui2py(
    ui_file: str = typer.Argument(None, help="Path to the .ui file to convert (or use --all)"),
    all: bool = typer.Option(False, "--all", help="Convert all .ui files in the 'ui/' directory."),
):
    """
    Convert a .ui file into a Python .py file using pyuic5.
    Use ui file to covert or
    Use --all to convert all .ui files in the ui/ folder.
    """
    from pathlib import Path
    import subprocess

    ui_dir = Path("ui")
    views_dir = Path("views")
    views_dir.mkdir(exist_ok=True)

    files_to_convert = []

    if all:
        if not ui_dir.exists():
            typer.echo("❌ 'ui/' directory not found.")
            raise typer.Exit()
        files_to_convert = list(ui_dir.glob("*.ui"))
        if not files_to_convert:
            typer.echo("⚠️ No .ui files found in 'ui/' directory.")
            raise typer.Exit()
    else:
        if not ui_file:
            typer.echo("❌ Please provide a .ui file or use --all.")
            raise typer.Exit()
        ui_path = Path(ui_file)
        if not ui_path.exists():
            typer.echo(f"❌ UI file '{ui_file}' does not exist.")
            raise typer.Exit()
        files_to_convert = [ui_path]

    for file in files_to_convert:
        output_file = views_dir / f"{file.stem}.py"
        try:
            subprocess.run([
                "pyuic5", str(file),
                "-o", str(output_file)
            ], check=True)
            typer.echo(f"✅ Converted {file} -> {output_file}")
        except FileNotFoundError:
            typer.echo("❌ 'pyuic5' not found. Make sure PyQt5 is installed.")
        except subprocess.CalledProcessError:
            typer.echo(f"❌ Failed to convert: {file}")


@app.command("mkctrl")
def make_controller(
    name: str = typer.Argument(..., help="Name of the view (without .py) to base controller on")
):
    """
    Create a controller class based on an existing view.
    """
    from pyqtforge.controllergen import generate_controller
    generate_controller(name)


@app.command("initdb")
def init_database():
    """
    Initialize the database by creating the default DB file.
    """
    from pyqtforge.db.config import DB_PATH
    if DB_PATH.exists():
        typer.echo(f"✅ Database already exists at: {DB_PATH}")
    else:
        DB_PATH.touch()
        typer.echo(f"🎉 New database created at: {DB_PATH}")


@app.command("mkmodel")
def make_model(model_name: str = typer.Argument(..., help="Name of the model (e.g. user)")):
    """
    Create a new database model inside the 'models/' folder.
    """
    from pyqtforge.modelgen import generate_model
    generate_model(model_name)



# ✅ This is your main entry point for scripts and setup.py console entry
def main():
    app()

if __name__ == "__main__":
    main()

