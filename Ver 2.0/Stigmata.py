# %%
class StigmataSet:
    """Class for Stigmata Objects"""

    def __init__(self,name,set2,set3):
        self.name   = name
        self.set2   = set2
        self.set3   = set3

    def __setattr__(self,setability2,setability3):
        self.setbility.update(
            {
                2:setability2,
                3:setability3
            }
        )
        return print(setability)

    def __getattr__(self):
        print(setability)

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
red = StigmataSet('霄雲紅')

# %%
