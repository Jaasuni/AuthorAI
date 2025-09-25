from pathlib import Path
import json
import subprocess
import sys

def run_cli(*a):
    return subprocess.run([sys.executable, "-m", "authorai.cli", *a], capture_output=True, text=True)

def test_init_json(tmp_path: Path):
    p = tmp_path / "demo"
    r = run_cli("init", str(p), "--json")
    payload = json.loads(r.stdout.strip())
    assert payload["ok"] and payload["action"] == "init"

def test_generate_json(tmp_path: Path):
    out = tmp_path / "drafts" / "file.md"
    r = run_cli("generate", "--prompt", "idea", "--out", str(out), "--json")
    payload = json.loads(r.stdout.strip())
    assert payload["ok"] and Path(payload["out"]).name == "file.md"
    assert out.exists()
