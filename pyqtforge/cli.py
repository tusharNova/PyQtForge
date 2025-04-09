import typer
from generator import generate_project
app = typer.Typer()



@app.command()
def create(name: str):
    """start project"""
    typer.echo(f"🔧 Creating new PyQt app: {name}")

@app.command("createproject")
def create_project(name: str):
    """Create a new PyQt project with the given name."""
    generate_project(name)



if __name__ == "__main__":
    app()
