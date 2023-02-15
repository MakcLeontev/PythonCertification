from NoteService import NoteService
from FileService import FileService
from Note import Note
from datetime import datetime
from datetime import date



class Controller:

    file = "note.csv"
    note_serv = NoteService()
    file_serv = FileService()

    def add(self):
        note_serv = NoteService()
        file_serv = FileService()
        file = "note.csv"
        header= input("Введите заголовок заметки: ")
        text = input("Введите тело заметки: ")
        try:
            list = file_serv.read_all_lines(file)
        except:
            list=[]
        note = note_serv.create_note(list, header, text)
        try:
            file_serv.write_file(file, note)
        except:
            print("не удалось сохранить заметку")
            return
        print("Заметка успешно сохранена")

    def read(self):
        file_serv = FileService()
        file = "note.csv"
        try:
            list_note = file_serv.read_all_lines(file)
        except:
            print("нет ни одной заметки")
            return
        for n in list_note:
            print(n)
    def date(self):
        file_serv = FileService()
        file = "note.csv"
        list_note = file_serv.read_all_lines(file)
        list_sort = []
        date_note = input("Введите дату для сортировки по дате в формате ГГГГ-ММ-ДД: ")
        format = "%Y-%m-%d"
        res=True
        try:
            res = bool(datetime.strptime(date_note, format))
        except ValueError:
            print("неверный формат")
            return

        for n in list_note:
            if(date_note in n.date_time):
                list_sort.append(n)

        if (len(list_sort) !=0):
            print("Список заметок с выбранной датой: \n")
            for n in list_sort:
                print(n)
        else:
            print("Нет заметок с такой датой")

    def select(self):
        try:
            id = int(input("Введите id заметки, которую хотите просмотреть: "))
        except:
            print("неверный формат")
            return
        file_serv = FileService()
        file = "note.csv"
        try:
            list_note = file_serv.read_all_lines(file)
        except:
            print("не удалось прочесть файл")
            return
        note_id = None
        for n in list_note:
            if(str(id) == n.id):
                note_id=n
        if(note_id != None):
            print(note_id)
        else:
            print("заметки с таким id не найдено")

    def delete(self):
        try:
            id = int(input("Введите id заметки, которую хотите УДАЛИТЬ: "))
        except:
            print("неверный формат")
            return
        file_serv = FileService()
        file = "note.csv"
        try:
            list_note = file_serv.read_all_lines(file)
        except:
            print("не удалось прочесть файл")
            return
        note_index = None
        for n in list_note:
            if (str(id) == n.id):
                try:
                    note_index = list_note.index(n)
                except:
                    print("индекс не найден")
                    return
        if (note_index != None):
            list_note.pop(note_index)
        else:
            print("заметки с таким id не найдено")
        try:
            file_serv.rewrite_file(file,list_note)
            print("запись удалена")
        except:
            print("ошибка удаления")
            return

    def edit(self):
        try:
            id = int(input("Введите id заметки, которую хотите изменить: "))
        except:
            print("неверный формат")
            return
        file_serv = FileService()
        file = "note.csv"
        try:
            list_note = file_serv.read_all_lines(file)
        except:
            print("не удалось прочесть файл")
            return
        note_index = None
        for n in list_note:
            if (str(id) == n.id):
                try:
                    note_index = list_note.index(n)
                except:
                    print("индекс не найден")
                    return
        if (note_index != None):
            header = input("Введите заголовок заметки: ")
            text = input("Введите тело заметки: ")
            note = list_note[note_index]
            note.header=header
            note.text=text
            note.date_time=str(date.today())+"\n"
            list_note[note_index]=note
        else:
            print("заметки с таким id не найдено")
        try:
            file_serv.rewrite_file(file,list_note)
            print("изменение прошло успешно")
        except:
            print("ошибка изменения")
            return

    def help(self):
        print("Список команд для работы с программой:\n" 
                "ADD - добавление заметки\n"
                "EXIT - выход из программы\n"
                "READ - чтение всех заметок\n"
                "DATE - сортировка по дате\n"
                "SELECT - просмотр заметки по id\n"
                "DELETE - удаление заметки по id\n"
                "EDIT - изменение заметки по id")



