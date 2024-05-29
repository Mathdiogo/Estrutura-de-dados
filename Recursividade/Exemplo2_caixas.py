from typing import List
from collections import namedtuple

Box = namedtuple('Box', 'have_key') #"tem chave"

#recebe uma lista de caixas e pode receber um index para saber em qual caixa que estou
def find_key(Boxes: List[Box], index: int = 0) -> Box:
    #Caso base
    if len(Boxes) <= index:
        return Box(False)
    
    Box = boxes[index]
    
    #caso base 2
    if Boxes.have_key:
        return Box

if __name__ == "__main__":
    boxes: List[Box] = [
        Box(False), Box(False), Box(False),
        Box(False), Box(False), Box(False),
        Box(False), Box(False), Box(False),
        Box(False), Box(True), Box(False),
    ]
    
    print(find_key(boxes))