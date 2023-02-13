import datetime


class Note:

    def __init__(self, id, header, text, date_time=datetime.now):
        self.__date_time = date_time
        self.__text = text
        self.__header = header
        self.__id = id

    def set_date_time(self, date_time):
        self.__date_time = date_time

    def get_date_time(self):
        return self.__date_time

    def set_text(self, text):
        self.__text = text

    def get_text(self):
        return self.__text

    def set_header(self, header):
        self.__header = header

    def get_header(self):
        return self.__header

    def set_id(self, id):
        self.__id

    def get_id(self):
        return self.__id

    def note_info(self):
        print(f"id:{self.__id} заголовок:{self.__header} тело заметки:{self.__text} дата,время создания:{self.__date_time}")


note = Note(1, "first", "fgblweqgfiwe")
note.note_info()
