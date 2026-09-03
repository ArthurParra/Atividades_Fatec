import random
 
alunos=[
    "Ana","Bruno","Carlos","Daniela","Eduardo","Fernanda","Gabriel","Helena","Igor","Julia"
]
 
random.seed(42)
 
amostra= random.sample(alunos, 3)
print(amostra)