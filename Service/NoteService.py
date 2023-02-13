from ast import List
import datetime
from Note import Note


class NoteService:
    

    def next_id(self, list):
        return  list[-1].id+1
    

    def now_date_time(self):
        return datetime.datetime.now()

l=[]        
id=NoteService() 
one=Note(1,"reqgre","qwee",3443) 
two=Note(2,"reqgre","qwee",3445)
print(two.id)
l.append(one)
l.append(two)  
three=l[-1]
print(three.id+1)
four=id.next_id(l)
print(four)
print(id.now_date_time())



 
 
