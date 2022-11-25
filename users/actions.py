# Importamos el método user del módulo users como "model" para definir nuestras acciones
#   (registrarse, loguearse, crear notas, mostrarlas, etc.)

import users.user as model
import notes.actions

class Actions:
     
    def register(self):

        print(f"OK! Let´s register your count:")
        name = input("What´s your name?      ")
        last_name = input("What´s your last name?     ")
        email = input("What´s your email? ")
        password = input("Create your password: ")

        user = model.User(name.capitalize(), last_name.capitalize(), email, password)
        register = user.regiser()

        if register[0] >= 1:
            print(f"\nPerfect! {register[1].name} you have registered with the email {register[1].email}")
            
            #### PROBANDO... PROBANDO... ####
            user = model.User("", "", email, password)
            login = user.login_data()
            
            self.next_actions(login)
            #### PROBANDO... PROBANDO... ####
        else:
            print("\nYou haven´t registered correctly")
            
    def login(self):
        print("Ok! Please enter this information: " )
        
        try:
            email = input("Your email: ")
            password = input("Your password: ")

            user = model.User("", "", email, password)
            login = user.login_data()

            if email == login[3]:
                print (f"Wellcome {login[1]}, you are with us since {login[5]}")
                self.next_actions(login)
        
        except Exception as e:
            print (f"Incorrect login '{type(e)}' Try again later")
    
    def next_actions (self, user):
        print("""
        Notes Manager:
        
        1. New note
        2. Show note
        3. Delete note
        4. Exit
        """)
        action = input("Select a number: ")
        make = notes.actions.Actions()

        if action == "1":
            make.create(user)
            self.next_actions(user)

        elif action == "2":
            make.show(user)
            self.next_actions(user)

        elif action == "3":
            make.delete(user)
            self.next_actions(user)

        elif action == "4":
            print(f"Ok {user[1]}! See you soon!")
            exit()