# pyqtforge/generator.py
import shutil
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

def generate_project(name: str):
    base_path = Path(__file__).parent
    template_dir = base_path / "templates" / "app"
    target_dir = Path.cwd() / name

    if target_dir.exists():
        print(f"⚠️ Folder '{name}' already exists.")
        return

    env = Environment(loader=FileSystemLoader(template_dir))

    for item in template_dir.rglob("*"):
        relative_path = item.relative_to(template_dir)
        target_path = target_dir / relative_path

        if item.is_dir():
            (target_dir / relative_path).mkdir(parents=True, exist_ok=True)
            # target_path.mkdir(parents=True, exist_ok=True)

        elif item.suffix == ".j2":
            output_path = target_path.with_suffix("")  # Remove .j2
            template = env.get_template(str(relative_path))
            rendered = template.render(project_name=name)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, "w") as f:
                f.write(rendered)
        else:

            target_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(item, target_path)

    print(f"✅ Project '{name}' created with UI and resources.")