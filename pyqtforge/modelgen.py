# pyqtforge/modelgen.py

from pathlib import Path

MODEL_TEMPLATE = '''
from pyqtforge.db.orm import Model

class {class_name}(Model):
    table_name = "{table_name}"
    fields = {{
        "name": "TEXT",
        "created_at": "TEXT"
    }}
'''


def generate_model(model_name: str):
    class_name = model_name.capitalize()
    table_name = model_name.lower()

    model_dir = Path("models")
    model_dir.mkdir(exist_ok=True)

    file_path = model_dir / f"{table_name}.py"
    if file_path.exists():
        print(f"⚠️ Model '{file_path}' already exists.")
        return

    with open(file_path, "w") as f:
        f.write(MODEL_TEMPLATE.format(class_name=class_name, table_name=table_name))

    print(f"✅ Created model: {file_path}")
