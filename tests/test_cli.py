
ui_name = "mainwindo"
ui_template = '''<?xml version="1.0" encoding="UTF-8"?>
    <ui version="4.0">
     <class>{}</class>
     <widget class="QMainWindow" name="MainWindow">
      <property name="windowTitle">
       <string>{}</string>
      </property>
      <widget class="QWidget" name="centralwidget"/>
     </widget>
     <resources/>
     <connections/>
    </ui>
    '''.format(ui_name.capitalize(), ui_name.capitalize())

print(ui_template)