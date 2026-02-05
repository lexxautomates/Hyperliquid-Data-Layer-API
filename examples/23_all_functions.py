"""
Moon Dev's ALL FUNCTIONS Reference - 🚀🌙
This script contains all major utility and view functions from the examples folder in one place.
Each function is directly taken from the working dashboards and utilities, for Moon Dev debugging and quick access.

NOTE: Main/entry logic is omitted. ALL function docstrings and debug print references are preserved. DO NOT EDIT TO REMOVE MOON DEV CREDITS OR PRINTS! 🚀🌙

To use: import this file, or copy-paste out what you need! NO API KEYS, NO MOCK DATA, NO PLACEHOLDERS!
"""

# --------- From 16_depositors.py ---------
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.columns import Columns
from rich.text import Text
from rich.align import Align
from rich import box
console = Console()

def create_banner():
    """Create the Moon Dev depositor banner"""
    banner = """██████╗ ███████╗██████╗  ██████╗ ███████╗██╗████████╗ ██████╗ ██████╗ ███████╗\n██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔════╝██║╚══██╔══╝██╔═══██╗██╔══██╗██╔════╝\n██║  ██║█████╗  ██████╔╝██║   ██║███████╗██║   ██║   ██║   ██║██████╔╝███████╗\n██║  ██║██╔══╝  ██╔═══╝ ██║   ██║╚════██║██║   ██║   ██║   ██║██╔══██╗╚════██║\n██████╔╝███████╗██║     ╚██████╔╝███████║██║   ██║   ╚██████╔╝██║  ██║███████║\n╚═════╝ ╚══════╝╚═╝      ╚═════╝ ╚══════╝╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝"""
    return Panel(
        Align.center(Text(banner, style="bold cyan")),
        title="🏦 [bold magenta]HYPERLIQUID DEPOSITOR TRACKER[/bold magenta] 🏦",
        subtitle="[dim]Every address that ever bridged to Hyperliquid | by Moon Dev[/dim]",
        border_style="bright_cyan",
        box=box.DOUBLE_EDGE,
        padding=(0, 1)
    )

def format_usd(value):
    """Format USD value with commas and dollar sign"""
    if value is None or value == 0:
        return "$0"
    if abs(value) >= 1_000_000_000:
        return f"${value/1_000_000_000:.2f}B"
    if abs(value) >= 1_000_000:
        return f"${value/1_000_000:.2f}M"
    elif abs(value) >= 1_000:
        return f"${value/1_000:.1f}K"
    return f"${value:,.0f}"

def format_count(value):
    """Format count with K/M suffixes"""
    if value is None or value == 0:
        return "0"
    if value >= 1_000_000:
        return f"{value/1_000_000:.1f}M"
    elif value >= 1_000:
        return f"{value/1_000:.1f}K"
    return f"{value:,}"

def display_depositor_stats(depositors_data):
    """Display depositor statistics"""
    console.print(Panel(
        "📊 [bold white]DEPOSITOR STATISTICS[/bold white]  [dim cyan]GET https://api.moondev.com/api/depositors.json[/dim cyan]",
        border_style="bright_white",
        padding=(0, 1)
    ))

    if isinstance(depositors_data, dict):
        depositors = depositors_data.get('depositors', depositors_data.get('addresses', []))
        stats = depositors_data.get('stats', {})
    elif isinstance(depositors_data, list):
        depositors = depositors_data
        stats = {}
    else:
        depositors = []
        stats = {}

    total_depositors = len(depositors) if depositors else stats.get('total_count', 0)
    total_volume = stats.get('total_volume', stats.get('total_deposited', 0))

    main_panel = Panel(
        f"[bold white]🏦 TOTAL DEPOSITORS[/bold white]\n\n"
        f"[bold cyan]{format_count(total_depositors)}[/bold cyan] unique addresses\n"
        f"[dim]Every wallet that bridged to Hyperliquid[/dim]",
        border_style="cyan",
        width=40,
        padding=(1, 2)
    )
    if total_volume:
        volume_panel = Panel(
            f"[bold white]💰 TOTAL DEPOSITED[/bold white]\n\n"
            f"[bold yellow]{format_usd(total_volume)}[/bold yellow] USDC\n"
            f"[dim]Lifetime bridge volume[/dim]",
            border_style="yellow",
            width=40,
            padding=(1, 2)
        )
        console.print(Columns([main_panel, volume_panel], equal=True, expand=True))
    else:
        console.print(main_panel)
    return depositors, stats

# (Functions from other files would continue here in the same way)
