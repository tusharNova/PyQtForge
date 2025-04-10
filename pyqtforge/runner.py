import subprocess
from pathlib import Path


def run_project(name: str):
    project_dir  = Path.cwd() / name
    main_file = project_dir / 'main.py'

    if not main_file.exists():
        print(f"❌ Could not find 'main.py' in {project_dir}")
        return
    print(f"🚀 Running {main_file}...\n")

    try:
        subprocess.run(["python", str(main_file)], check=True)
    except subprocess.CalledProcessError:
        print("❌ Error while running the app.")