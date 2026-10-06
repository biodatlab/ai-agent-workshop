"""Local workshop setup for Windows, macOS and Linux (Python 3.11)."""
import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time
import urllib.request
import venv

ROOT = Path(__file__).resolve().parent


def environment_python(folder, windows=None):
    windows = os.name == "nt" if windows is None else windows
    return folder / ("Scripts/python.exe" if windows else "bin/python")


def find_ollama():
    executable = shutil.which("ollama")
    if executable:
        return executable
    candidates = [Path("/Applications/Ollama.app/Contents/Resources/ollama")]
    if os.name == "nt":
        candidates.insert(0, Path(os.environ.get("LOCALAPPDATA", "")) / "Programs/Ollama/ollama.exe")
    for candidate in candidates:
        if candidate.is_file():
            return str(candidate)
    raise RuntimeError("Install Ollama from https://ollama.com/download and rerun setup.")


def ollama_ready():
    try:
        # Ignore proxy settings for this local endpoint.
        opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
        with opener.open("http://127.0.0.1:11434/api/version", timeout=2) as response:
            return bool(json.load(response).get("version"))
    except (OSError, ValueError):
        return False


def run(*args):
    subprocess.run([str(arg) for arg in args], cwd=ROOT, check=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--no-launch", action="store_true", help="Prepare without opening JupyterLab")
    args = parser.parse_args()
    print("[1/5] Preparing Python 3.11", flush=True)
    if sys.version_info[:2] != (3, 11):
        raise RuntimeError("Run with Python 3.11: py -3.11 setup.py (Windows) or python3.11 setup.py (macOS/Linux).")
    ollama = find_ollama()
    print("[2/5] Preparing .venv and Jupyter", flush=True)
    folder = ROOT / ".venv"
    python = environment_python(folder)
    if folder.exists():
        if not python.is_file():
            raise RuntimeError("Existing .venv belongs to another OS or is incomplete. Rename it and rerun setup.")
        run(python, "-c", "import sys; assert sys.version_info[:2] == (3, 11), 'Existing .venv must use Python 3.11'")
    else:
        venv.EnvBuilder(with_pip=True).create(folder)
    run(python, "-m", "pip", "install", "--upgrade", "pip")
    run(python, "-m", "pip", "install", "jupyterlab>=4,<5", "ipykernel>=7,<8")
    run(python, "-m", "ipykernel", "install", "--prefix", folder,
        "--name", "python3", "--display-name", "Python 3.11 (workshop)")
    run(python, "-c", "import pip, jupyterlab, ipykernel; import sys; assert sys.prefix != sys.base_prefix")
    print("[3/5] Starting Ollama if needed", flush=True)
    if not ollama_ready():
        log_path = ROOT / "ollama-setup.log"
        options = {"creationflags": subprocess.CREATE_NO_WINDOW | subprocess.DETACHED_PROCESS} if os.name == "nt" else {"start_new_session": True}
        env = dict(os.environ, OLLAMA_HOST="127.0.0.1:11434")
        with log_path.open("ab") as log:
            process = subprocess.Popen([ollama, "serve"], stdin=subprocess.DEVNULL, stdout=log, stderr=log, env=env, **options)
        deadline = time.monotonic() + 60
        while not ollama_ready():
            if process.poll() is not None or time.monotonic() >= deadline:
                raise RuntimeError(f"Ollama did not start. See {log_path} or run ollama serve.")
            time.sleep(0.5)
    print("[4/5] Downloading workshop models", flush=True)
    # Match the endpoint used by the notebooks, even if a custom host is configured.
    os.environ["OLLAMA_HOST"] = "127.0.0.1:11434"
    for model in ("qwen3:4b", "bge-m3"):
        run(ollama, "pull", model)
    if not ollama_ready():
        raise RuntimeError("Ollama stopped before setup completed. Run setup again.")
    print("[5/5] Ready: open notebook 03, 08 or 12 and select Run > Run All Cells", flush=True)
    if not args.no_launch:
        run(python, "-m", "jupyterlab", "--notebook-dir", ROOT, "--MappingKernelManager.default_kernel_name=python3")


if __name__ == "__main__":
    try:
        main()
    except (OSError, RuntimeError, subprocess.CalledProcessError) as error:
        print(f"Setup failed: {error}", file=sys.stderr)
        sys.exit(1)
