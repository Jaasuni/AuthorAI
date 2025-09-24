import json
from pathlib import Path
import typer
from rich import print

app = typer.Typer(no_args_is_help=True)

def _safe_mkdir(p: Path):
    p.mkdir(parents=True, exist_ok=True)

@app.command()
def init(project: str, json_out: bool = typer.Option(False, "--json", help="JSON output")):
    root = Path(project)
    _safe_mkdir(root / "drafts"); _safe_mkdir(root / "prompts")
    (root / "README.md").write_text(f"# {project}\n")
    if json_out:
      print(json.dumps({"ok": True, "action": "init", "project": str(root)}))
    else:
      print(f"[bold green]Initialized[/] {root}")

@app.command()
def generate(
    prompt: str,
    out: str = typer.Option("drafts/draft_001.md", "--out"),
    json_out: bool = typer.Option(False, "--json", help="JSON output"),
):
    out_path = Path(out)
    if out_path.is_dir():
        raise typer.BadParameter("--out points to a directory; provide a file path.")
    _safe_mkdir(out_path.parent)
    out_path.write_text(f"# Draft\n\nPrompt: {prompt}\n\n(Coming soon)")
    if json_out:
      print(json.dumps({"ok": True, "action": "generate", "out": str(out_path)}))
    else:
      print(f"[bold cyan]Wrote[/] {out_path}")

if __name__ == "__main__":
    app()
