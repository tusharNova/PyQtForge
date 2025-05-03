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
