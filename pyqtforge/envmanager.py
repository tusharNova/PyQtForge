import subprocess
from pathlib import Path
import sys

def create_vene(project_name : str):
    venv_path = Path.cwd() / project_name / ".venv"

    if venv_path.exists():
        print("⚠️ Virtual environment already exists.")
        return

    print("📦 Creating virtual environment...")
    subprocess.run([sys.executable, "-m", "venv", str(venv_path)], check=True)

    print(f"✅ Virtual environment created at '{venv_path}'")