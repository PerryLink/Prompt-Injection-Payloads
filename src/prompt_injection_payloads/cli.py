"""CLI commands using Click"""

import click
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.syntax import Syntax

from prompt_injection_payloads.core import PayloadDatabase


console = Console()
db = PayloadDatabase()


@click.group()
@click.version_option(version="0.1.0")
def main():
    """Prompt Injection Payloads - AI Security Testing Tool"""
    pass


@main.command()
@click.option("--category", "-c", help="Filter by category")
@click.option("--search", "-s", help="Search by keyword")
@click.option("--severity", help="Filter by severity (high/medium/low)")
def list(category, search, severity):
    """List all available payloads"""
    try:
        if category:
            payloads = db.filter_by_category(category)
        elif search:
            payloads = db.search(search)
        elif severity:
            payloads = db.filter_by_severity(severity)
        else:
            payloads = db.get_all_payloads()

        if not payloads:
            console.print("[yellow]No payloads found.[/yellow]")
            return

        console.print(f"\n[green]Found {len(payloads)} payload(s):[/green]\n")

        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("ID", style="cyan")
        table.add_column("Name", style="green")
        table.add_column("Category", style="yellow")
        table.add_column("Severity", style="red")

        for payload in payloads:
            table.add_row(
                payload.get("id", ""),
                payload.get("name", ""),
                payload.get("category_name", ""),
                payload.get("severity", "")
            )

        console.print(table)
        console.print(f"\n[dim]Use 'pipayloads show <id>' to view full payload details[/dim]\n")

    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")


@main.command()
@click.argument("payload_id")
def show(payload_id):
    """Show detailed information about a specific payload"""
    try:
        payload = db.get_payload_by_id(payload_id)

        if not payload:
            console.print(f"[red]Payload '{payload_id}' not found.[/red]")
            return

        console.print(f"\n[bold cyan]ID:[/bold cyan] {payload.get('id', '')}")
        console.print(f"[bold cyan]Name:[/bold cyan] {payload.get('name', '')}")
        console.print(f"[bold cyan]Category:[/bold cyan] {payload.get('category_name', '')} ({payload.get('category_id', '')})")
        console.print(f"[bold cyan]Severity:[/bold cyan] {payload.get('severity', '')}")
        console.print(f"[bold cyan]Description:[/bold cyan] {payload.get('description', '')}")

        if payload.get('tags'):
            console.print(f"[bold cyan]Tags:[/bold cyan] {', '.join(payload.get('tags', []))}")

        console.print("\n[bold cyan]Payload:[/bold cyan]")
        panel = Panel(
            payload.get('payload', ''),
            border_style="green",
            padding=(1, 2)
        )
        console.print(panel)

        if payload.get('references'):
            console.print("\n[bold cyan]References:[/bold cyan]")
            for ref in payload.get('references', []):
                console.print(f"  - {ref}")

        console.print()

    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")


@main.command()
@click.option("--category", "-c", help="Get random payload from specific category")
def random(category):
    """Get a random payload"""
    try:
        payload = db.get_random_payload(category)

        if not payload:
            console.print("[yellow]No payloads available.[/yellow]")
            return

        console.print(f"\n[bold green]Random Payload:[/bold green]\n")
        console.print(f"[bold cyan]ID:[/bold cyan] {payload.get('id', '')}")
        console.print(f"[bold cyan]Name:[/bold cyan] {payload.get('name', '')}")
        console.print(f"[bold cyan]Category:[/bold cyan] {payload.get('category_name', '')}")

        console.print("\n[bold cyan]Payload:[/bold cyan]")
        panel = Panel(
            payload.get('payload', ''),
            border_style="green",
            padding=(1, 2)
        )
        console.print(panel)
        console.print()

    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")


if __name__ == "__main__":
    main()
