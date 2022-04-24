#saving notes with text information

def __create_note(self) -> str:
    text = ""
    while True:
        row = input()
        if row:
            text += row + "\n"
        else:
            break
    return text

def add_note(self) -> None:
    print("Write your note please:")
    text = self.__create_note()

    if text == "":
        return
    text_tags = input("Write tags to this note: ")
    
#if needs the redaction, having other text option:
#deleting space at the start and end of the word
#saving data after correction --->
    if text_tags != "":
        tags = text_tags.split(",")
        tags = [tag.strip() for tag in tags]
        self.notepad.add_note(text, tags)
        self.notepad.save_data()
    else:
        self.notepad.add_note(text, [])
        self.notepad.save_data()

def find_note(self, value: str) -> None:
    notes = self.notepad.find_note(value)
    for note in notes:
        print(note)
#if note is not exist yet -->
def show_notes(self,) -> None:
    if len(self.notepad.data) == 0:
        print("Can not find any of your notes, please add some")
        return
    for note in self.notepad.data:
        print(note)
