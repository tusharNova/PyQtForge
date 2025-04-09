# pyqtforge/generator.py
import shutil
from pathlib import Path

def generate_project(name: str):
    base_path = Path(__file__).parent
    template_path = base_path / "templates" / "app"
    target_path = Path.cwd() / name

    if target_path.exists():
        print(f"⚠️  Folder '{name}' already exists.")
        return

    shutil.copytree(template_path, target_path)
    print(f"✅ Created PyQt project at: {target_path}")
