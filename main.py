# main.py
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from agent import ManagerAgent

def main():
    console = Console()
    console.print(Panel("Welcome to the Hierarchical Reasoning Agent", style="bold cyan"))
    
    # The API key is loaded automatically from the .env file via groq_client.py.
    manager = ManagerAgent()
    while True:
        user_input = Prompt.ask("[bold yellow]Enter your problem statement (or type 'exit' to quit)[/bold yellow]")
        if user_input.lower() in ["exit", "quit"]:
            console.print("[bold red]Exiting the Hierarchical Reasoning Agent. Goodbye![/bold red]")
            break
        manager.execute(user_input)

if __name__ == '__main__':
    main()
