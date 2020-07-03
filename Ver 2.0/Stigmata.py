# %%
class StigmataSet:
    """Class for Stigmata Objects"""


    def __init__(self,name,setability2,setability3):
        self.name           = name
        self.setability2    = setability2
        self.setability3    = setability3

    def getability(self,pieces):
        ability = [ability for ability in ]

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