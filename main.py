import typer


def main(name: str) -> None:
    """Welcome to our awesome CLI!
    
    Put in your name to get greeted :)"""
    typer.echo(f"Hello, {name}!")


if __name__ == "__main__":
    typer.run(main)
