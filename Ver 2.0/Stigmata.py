# %%
class StigmataSet:
    """Class for Stigmata Objects"""

    setability={
        2:None,
        3:None
    }

    def __init__(self,name,setability2,setability3):
        self.name           = name
        self.setability2    = setability2
        self.setability3    = setability3

    def setability(self,pieces,ability):

    def __setattr__
        self.
        __setattr__
        (setability2,ability)


    def getability(self,pieces:in
        setability = {
            1:None,
            2:self.setability2,
            3:self.setability3
        }
        return setability.get(pieces)

class Stigmata(StigmataSet):

    def __init__(self,name,pos,hp,sp,atk,dfs,crt,ability,setability2,setability3):

        super().__init__(self,setability2,setability3)
        self.name   = name
        self.pos    = pos
        self.hp     = hp
        self.sp     = sp
        self.atk    = atk
        self.dfs    = dfs
        self.crt    = crt    

# %%