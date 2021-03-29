from typing import Optional, List, Set
from datetime import datetime

class Myclothes:
    def __init__(self):
        
        self.clothes=set()

    def regist_clothes(self ) :
        pass
    def modify_clothes(self):
        pass

    def remove_closets(self, ref: str, qty: int):
        pass



class Closet:
    def __init__(self, id:str,name:str):
        self.id=id  
        self.name=name  #옷장이름
        self.parts=set() #옷칸
        self.clothes=set() #옷장내 옷    

    @property
    def number_of_clothes(self):
        pass

    @property
    def number_of_parts(self):
        pass

    def add_parts(self):
        pass

    def remove_parts(self):
        pass

#x:int,y:int,height:int, width:int
class Part:
    def __init__(self,x:int ,y:int):
        self.x=x
        self.y=y
        self.clothes=set()

    
    def in_clothes(self):
        pass

    def out_clothes(self):
        pass


class Clothes:
    def __init__(self,id:str, maker:str, serial:str, buydate:datetime,  rating:int):
        self.id=id
        self.maker=maker
        self.serial=serial
        self.buydate=buydate
        self.rating=rating
    



    
    
    
    