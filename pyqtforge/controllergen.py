import subprocess
import os
import sys
from pathlib import Path


def create_controller_file(name: str):
    camel_file = ''.join(word.capitalize() for word in name.split('_'))
    className = f"Cls{camel_file}"
    fileName = f"Cls{camel_file}.py"


    controllers_dir = Path("controller")
    controllers_dir.mkdir(exist_ok=True)

    controller_path = controllers_dir / fileName
    if controller_path.exists():
        print(f"⚠️ Controller '{fileName}' already exists.")
        return

    controller_code = f'''
    from PyQt5.QtWidgets import QMainWindow
    class {className}:
    def __init__(self):
         print("c{className} controller initialized.")
         super({className} , self).__init__()
    '''

    controller_path.write_text(controller_code)
    print(f"✅ Created controller: {controller_path}")


def generate_controller(view_name:str):
    view_file = Path("views") / f"{view_name}.py"
    if not view_file.exists():
        print(f"❌ View file '{view_file}' does not exist.")
        return
    class_name = f"Cls{view_name.capitalize()}"
    controller_dir = Path("controllers")
    controller_dir.mkdir(exist_ok=True)
    controller_file = controller_dir / f"{class_name}.py"
    if controller_file.exists():
        print(f"⚠️ Controller '{controller_file}' already exists.")
        return

    content = f"""from views.{view_name} import {view_name.capitalize()}
    class {class_name}():
        def __init__(self):
            self.ui = {view_name.capitalize()}()
            self.setup_connections()

        def setup_connections(self):
            # Connect UI elements to slots here
            pass
    """

    controller_file.write_text(content)
    print(f"✅ Created controller: {controller_file}")

