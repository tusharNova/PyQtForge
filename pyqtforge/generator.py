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

    # Create the new project directory
    target_dir.mkdir(parents=True)
    # shutil.copytree(template_dir, target_dir)

    # Set up Jinja
    env = Environment(loader=FileSystemLoader(template_dir))

    # Render template files
    for template_file in template_dir.glob("**/*.j2"):
        relative_path = template_file.relative_to(template_dir)
        output_path = target_dir / relative_path.with_suffix('')  # Remove .j2

        output_path.parent.mkdir(parents=True, exist_ok=True)

        template = env.get_template(str(relative_path))
        rendered = template.render(project_name=name)

        with open(output_path, 'w') as f:
            f.write(rendered)

    print(f"✅ Created PyQt project: {target_dir}")
