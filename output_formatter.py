# output_formatter.py
import sys
import time
from rich.console import Console
from rich.panel import Panel
from rich import box

console = Console()

def type_out_text(text, delay=0.02):
    """Simulate live typing effect by printing each character with a delay."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def print_panel(content, title="", style="bold magenta"):
    """Print content inside a rich Panel."""
    panel = Panel(content, title=title, style=style, box=box.ROUNDED)
    console.print(panel)