"""
Proyecto python y MySQL:
- Abrir asistente.
- Login o registro.
- Si seleccionamos registro, creará un usuario en la ddbb.
- Si seleccionamos login, identificará al usuario.
- Crear notas, mostrar notas, borrarlas.
"""
from users import actions

wellcoming = "¡¡¡WELLCOME TO @PW PROYECT!!!"
menu = """
Available actions:
Select a number:
1. Register 
2. Login
"""

print(f"\n{wellcoming}")

make = actions.Actions()
action = input(menu)

if action == "1":
    make.register()
    
elif action == "2":
    make.login()
