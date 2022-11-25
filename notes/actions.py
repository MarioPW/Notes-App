import notes.note as model

class Actions:

    def create(self, user):
        print (f"Ok! Let´s make a new note!")

        tittle = input("Fill in the tittle: ")
        description = input("Note: ")

        note = model.Note(user[0], tittle, description)
        save = note.save()

        if save[0] >= 1:
            print(f"\nPerfect!!! Youre note {note.tittle} has bin saved!!")
        
        else:
            print(f"Sorry, incorrect saving... {user[1]}")
    
    def show (self, user):
        print (f"Ok {user[1]}!!! These are your notes: ")

        note = model.Note(user[0])
        notes = note.get_ready()

        for note in notes:

            print("\n*****************************")
            print(note[2])
            print(note[3])
            print("\n*****************************")
    
    def delete (self, user):
        print(f"Ok {user[1]}! Let's eliminate some notes: ")

        tittle = input("Enter the note's tittle to eliminate: ")
        note = model.Note(user[0], tittle)
        delete = note.delete()

        if delete[0] >= 1:
            print(f"Note deleted: {note.tittle}")
        
        else:
            print("Note not deleted... Try leter...")
