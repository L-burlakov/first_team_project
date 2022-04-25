from collections import UserDict
import pickle

class Subject:
    def __init__(self, subject):
        self.value = subject

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return self.value


class Note:
    def __init__(self, note):
        self.note = note

    def __str__(self) -> str:
        return self.note

    def __repr__(self) -> str:
        return self.note    

class Record_Note:
    
    def __init__(self, subject, *args):
        self.subject = subject
        self.notes = []
        self.add_note(*args)
                
    def add_note(self, *args) -> None:                
        for item in args:             
                                
            if item.note != '' and isinstance (item, Note) and item not in self.notes:      
                #print (f'{self.subject}, {item.note}')
                self.notes.append(item)

    def delete_note(self, index) -> str:
        try:
            #print(index)
            note = self.notes.pop(index)
            
            return print(f"note {note} deleted from subject {self.subject}")
        except IndexError:
            return f"Sorry, there is no note with the index {index}"
        

    def edit_note(self, index, new_note: Note) -> str:
        try:
            self.notes[index] = new_note
        except IndexError:
            return f"Sorry, there is no note to change with the index {index}"
        return print(f"""Note with index {index} in record with name {self.subject} changed on note {new_note}""" )                     

    def __str__(self) -> str:
        return f"Subject: {self.subject}, notes : {', '.join([str(p.note) for p in self.notes])}"

    def __repr__(self) -> str:
        return f"Subject: {self.subject}, notes : {', '.join([str(p.note) for p in self.notes])}"   

class NotesBook(UserDict):
    a=[]
    index=0
    filename = "Notes.bin"

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)            
        return content


    def add_record(self, obj):
        
        if isinstance(obj, Record_Note):
            if obj.subject.value in self.data.keys():
                #print(f'{obj.subject.value} {obj.notes}')
                self.data.update({obj.subject.value: obj})
                self.save_to_file()
                #print ("aaa")
            else:
                #print(f'{obj.subject.value} {obj.notes}')
                self.data[obj.subject.value] = obj  # , print("bbb")
                self.save_to_file()
                #print (self.data)

    def del_record(self, obj):
        del self.data[obj.subject.value]
        self.save_to_file()
    def delete_record(self, subject: Subject):
        print( f"Record with name {subject} deleted from NoteBook")
        self.data.pop(subject)
        self.save_to_file()

    def __str__(self) -> str:
        result = "\n".join([str(rec) for rec in self.data.values()])
        
        return result

    def __iter__ (self):          
        
        self.data.update(self.read_from_file().data)
        return self

    def __next__(self): 
      
        if len(self.data.values()) > self.index: 
            for i in self.data.values():
                self.a.append(i)
            
            c=self.a[self.index]
            self.index+=1       
            return f"Subject: {c.subject}, notes : {', '.join([str(p.note) for p in c.notes])}" 

        elif len(self.data.values()) <= self.index: 
            print ('NoteBook is ended')
            self.index=0  

def input_error(get_handler):
    def inner(command1):
        try:
            get_handler(command1)
            return get_handler(command1)
        except ValueError as e:
            print(e)
            command1 = "help"
        except IndexError as e:
            print(e)
            command1 = "help"
        except TypeError as e:
            print(e)
            command1 = "help"
        except KeyError as e:
            print(e)
            command1 = "help"
        return command1

    return inner


def input_():
    while True:
        user_command1 = input("Please, give me a command:")
        if (

            "add" in user_command1
            or "show all" in user_command1
            or "add_note" in user_command1
            or "del_note" in user_command1
            or "edit_note" in user_command1
            or "del_subject" in user_command1
            or "add_birthday" in user_command1
            or "find"  in user_command1 
                     
        ):
            return user_command1
        continue

def normalization(user_command1):
    user_command1.casefold()
    user_command1_norm = user_command1
    return user_command1_norm


def input_error_2(parser):
    def inner(user_command1_norm):
        a = 0
        while a < 10:
            try:
                subject, note, command1, new_note = parser(user_command1_norm)
                a += 1
                return subject, note, command1, new_note
            except TypeError:
                print("Give me subject and note please")

            except IndexError:

                print("Give me subject and note please")

                while True:
                    user_command1 = input_()
                    user_command1_norm = normalization(user_command1)
                    subject, note, command1, new_note= parser(user_command1_norm)
                    a += 1
                    return subject, note, command1, new_note
    return inner

@input_error_2
def parser(user_command1_norm):
    if user_command1_norm in ["hello", "exit", "close", "good bye", "show all"]:
        command1 = user_command1_norm
        #print( command1)
        return "", "", command1, ""

    elif "add_note" in user_command1_norm:
        c = user_command1_norm.split(" ")
        
        subject = c[1]
        command1 = c[0]
        if len(c) <= 2:
            note = "no"
        else:
            note = c[2]

        return subject, note, command1, ""

 

    elif "del_subject" in user_command1_norm:
        c = user_command1_norm.split(" ")
        
        subject = c[1]
        command1 = c[0]
        if len(c) <= 2:
            note = "no"
        else:
            note = c[2]

        return subject, note, command1, "" 


    elif "del_note" in user_command1_norm:
        c = user_command1_norm.split(" ")
        
        subject = c[1]
        command1 = c[0]
        note = c[2]

        return subject, note, command1, ""    


    elif "edit_note" in user_command1_norm:
        c = user_command1_norm.split(" ")
        
        subject = c[1]
        command1 = c[0]
        if len(c) <= 2:
           note = "no"
        else:
            note = c[2]
            new_note = c[3]           

        return subject, note, command1, new_note 


    elif "find_note" in user_command1_norm:
        c = user_command1_norm.split(" ")
        subject = c[1]
        command1 = c[0]
               
        
        return subject, "", command1, ""

    elif "add" in user_command1_norm:
        c = user_command1_norm.split(" ")
        subject  = c[1]
        command1 = c[0]
        if len(c) <= 2:
            note = "no"
        else:
            note = c[2]
        return subject, note, command1, ""

    elif "note" in user_command1_norm:
        b = user_command1_norm.split("note ")
        subject = b[-1]
        command1 = "note"
        return subject, "", command1, "" 

    else:
        subject = ""
        note = ""
        command1 = "help"
        new_note = ""
        return subject, note, command1, new_note



def main():
    def close_func():
        print("Good bye!")

    def show_func(N=2):
        #print('iiii')
        for i in range (0, N):           
           print(next(n_b))

    def phone_func():
        if subject in n_b.data.keys():
            jjj=[]
            for i in n_b.get(subject).notes:
                jjj.append(i.note)
                #print(len(c_b.get(name).phones))
                print(f"Subject is {subject}, notes are {jjj} ")

    def add_func():
        if subject in n_b.data.keys():
            
            add_note_func()
        else:                        
            subject1 = Subject(subject)
            note1 = Note(note)           
            record = Record_Note(subject1, note1)
            #print('ddd')
            n_b.add_record(record)
            

    def del_subject_func():     
        n_b.delete_record(subject)
           

    def hello_func():
        print("How can I help you?")

    def add_note_func():
        if subject not in n_b.data.keys():
            subject1 = Subject(subject)
            note1 = Note(note)           
            record = Record_Note(subject1, note1)
            n_b.add_record(record)
        if subject in n_b.data.keys():
            record=n_b.data.get(subject)
            note1 = Note(note)
            record.add_note(note1)
            n_b.add_record(record)
            

    def del_note_func():
        record=n_b.data.get(subject)        
        for i, j in enumerate(record.notes):                       
            if note == str(j) and j != None:                  
                record.delete_note(i)
                n_b.add_record(record)

    def edit_note_func():
        record=n_b.data.get(subject)
       
        note1 = Note(new_note)           
        
        
        
        #note1.note=new_note
        #record.new_phone = new_phone
        for i, j in enumerate(record.notes):                       
            if note == str(j) and j != None:                  
                #new_note = Note(note.1)
                record.edit_note(i, note1)
                n_b.add_record(record) 

   
    def find_note_func():             
        find_notes=[]       
        if subject in str(n_b.data.items()):          
            #print('ffff')
            for k,v in n_b.data.items():
                for i in v.notes:               
                    if subject in k or subject in i.note:                    
                        print(f"Subject is {k}, notes are {n_b.get(k).notes}")               

    command1S = {
        "good bye": close_func,
        "close": close_func,
        "exit": close_func,
        "show all": show_func,
        "phone": phone_func,
        "change": add_func,       
        "add_note": add_note_func,
        "hello": hello_func,        
        "edit_note": edit_note_func,
        "del_note": del_note_func,
        "del_subject": del_subject_func,
       
        "add": add_func,
        "find_note": find_note_func,
        
    }

    @input_error
    def get_handler(command1):
        return command1S[command1]

    
    n_b = NotesBook()
    while True:
        try:
            n_b=n_b.read_from_file()            
        except EOFError: 
            n_b = NotesBook()
        except FileNotFoundError:
            n_b = NotesBook()
        #print(type(c_b))
        user_command1 = input_()

        if user_command1 in ["close", "good bye", "exit"]:
            close_func()
            break

        user_command1_norm = normalization(user_command1)

        subject, note, command1, new_note  = parser(user_command1_norm)
        
        #print(command1)
        #print(subject)
        #print(record)




        if command1 is not None:

            a = get_handler(command1)
            a()
            #print(command1)
            #paginator = iter(c_b)
        n_b.save_to_file()
if __name__ == "__main__":

    main()

