# pyqtforge/envmanager.py
import subprocess
import os
import sys
from pathlib import Path

def create_venv(project_name: str) -> Path:
    venv_path = Path.cwd() / project_name / ".venv"

    if venv_path.exists():
        print("⚠️ Virtual environment already exists.")
        return venv_path

    print("📦 Creating virtual environment...")
    subprocess.run([sys.executable, "-m", "venv", str(venv_path)], check=True)
    print(f"✅ Virtual environment created at '{venv_path}'")
    return venv_path

def install_packages(packages: list[str], venv_path: Path = None):
    if venv_path:
        pip_path = venv_path / "bin" / "pip" if os.name != 'nt' else venv_path / "Scripts" / "pip.exe"
    else:
        pip_path = "pip"

    print(f"📥 Installing: {', '.join(packages)}")
    try:
        subprocess.run([str(pip_path), "install"] + packages, check=True)
        print("✅ Packages installed successfully.")
    except subprocess.CalledProcessError:
        print("❌ Package installation failed.")
