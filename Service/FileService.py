from NoteService import NoteService
from Note import Note


class FileService:
    file = "note.csv"

    def __init__(self) -> None:
        pass

    def write_file(self, file, note):
        with open(file, "a", encoding='utf-8') as f:
            f.write(f"{note}\n")

    def read_all_lines(self, file):
        list_note = []
        with open(file, "r", encoding='utf-8') as f:
            line = f.readline()
            while line:
                list = line.split(";")
                note = Note(list[0], list[1], list[2], list[3])
                list_note.append(note)
                line = f.readline()
            return list_note

    def select_note(id, list_note):
        for n in list_note:
            n.id
