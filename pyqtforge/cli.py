import typer
from generator import generate_project
from runner import run_project

app = typer.Typer()

#
#
# @app.command()
# def create(name: str):
#     """start project"""
#     typer.echo(f"🔧 Creating new PyQt app: {name}")

@app.command("createproject")
def create_project(name: str):
    """Create a new PyQt project with the given name."""
    generate_project(name)

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
