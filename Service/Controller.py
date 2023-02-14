from NoteService import NoteService
from FileService import FileService
from Note import Note


class Controller:

    file ="note.csv"
    note_serv = NoteService()
    file_serv = FileService()

    def add(self):
        note_serv = NoteService()
        file_serv = FileService()
        file = "note.csv"
        header= input("Введите заголовок заметки: ")
        text = input("Введите тело заметки: ")
        list = file_serv.read_all_lines(file)
        note = note_serv.create_note(list, header, text)
        file_serv.write_file(file, note)
        print("Заметка успешно сохранена")




    '''
    file="note.csv"
    list=[]
    header='заголовок'
    text='текст заметки'
    exit
    list2=file_serv.read_all_lines(file)
    #list3=file_serv.read_note(list2)
    for n in list2:
        print(n)

    #note=note_serv.create_note(list2,header, text)
    file_serv.write_file(file, note)
'''
