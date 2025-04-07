import typer

app = typer.Typer()

@app.command()
def create(name: str):
    typer.echo(f"🔧 Creating new PyQt app: {name}")


if __name__ == "__main__":
    app()