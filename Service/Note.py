class Note:

    def __init__(self, id, header, text, date_time):
        self.__date_time = date_time
        self.__text = text
        self.__header = header
        self.__id = id

    @property
    def date_time(self):
        return self.__date_time

    @date_time.setter
    def date_time(self, date_time):
        self.__date_time = date_time


    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text):
        self.__text = text


    @property
    def header(self):
        return self.__header

    @header.setter
    def header(self, header):
        self.__header = header

    
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id

    def note_info(self):
        print(f"id:{self.__id} заголовок:{self.__header} тело заметки:{self.__text} дата,время создания:{self.__date_time}")

    def __str__(self) -> str:
        return f"{str(self.__id)};{self.__header};{self.__text};{str(self.__date_time)}"

#note = Note(1, "first", "fgblweqgfiwe",534)
#print(note)
