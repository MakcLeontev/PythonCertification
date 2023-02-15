from ast import List
from datetime import date
from Note import Note


class NoteService :
    

    def next_id(self, list):
        if len(list)!=0:
            return  int(list[-1].id)+1
        else:
            return 1
    
    def now_date_time(self):
        return date.today()

    def create_note(self, list, header, text):
        note_service=NoteService()
        id=note_service.next_id(list)
        date_time=note_service.now_date_time()
        return Note(id, header, text, date_time)
    
    






 
 
