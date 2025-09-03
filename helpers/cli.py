from rich.console import Console
from rich.traceback import install

install(show_locals=False)
console = Console()
err_console = Console(stderr=True)


def print_ok(message):
    console.print(f"[bold green]OK[/] {message}")


def print_err(message):
    err_console.print(f"[bold red]ERROR[/] {message}")


def print_warn(message):
    console.print(f"[bold yellow]WARN[/] {message}")


def print_info(message):
    console.print(f"[bold blue]INFO[/] {message}")
