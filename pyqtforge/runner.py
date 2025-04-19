# pyqtforge/runner.py
import subprocess
from pathlib import Path
import os

def run_project(name: str, use_venv: bool = False, debug: bool = False):
    project_dir = Path.cwd() / name
    main_file = project_dir / "main.py"

    if not main_file.exists():
        print(f"❌ Could not find 'main.py' in {project_dir}")
        return

    if use_venv:
        venv_path = project_dir / ".venv"
        python_exec = venv_path / "bin" / "python" if os.name != 'nt' else venv_path / "Scripts" / "python.exe"

        if not python_exec.exists():
            print("❌ No virtual environment found in the project.")
            return
    else:
        python_exec = "python"

    cmd = [str(python_exec), str(main_file)]

    if debug:
        print(f"[DEBUG] Running command: {' '.join(cmd)}")

    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError:
        print("❌ Error while running the app.")
