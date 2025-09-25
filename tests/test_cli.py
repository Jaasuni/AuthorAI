from pathlib import Path
import subprocess
import sys

def run_cli(*a):
    return subprocess.run([sys.executable, "-m", "authorai.cli", *a], capture_output=True, text=True)

def test_init(tmp_path: Path):
    p = tmp_path / "demo"
    r = run_cli("init", str(p))
    assert r.returncode == 0
    assert (p / "drafts").exists()

def test_generate(tmp_path: Path):
    out = tmp_path / "drafts" / "file.md"
    r = run_cli("generate", "--prompt", "idea", "--out", str(out))
    assert r.returncode == 0
    assert out.exists()
