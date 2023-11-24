import block_library

class Goodblock(block_library.Block):
     def __init__(self, filename:str ,width:int, height:int):
            super().__init__(filename,width,height)

            