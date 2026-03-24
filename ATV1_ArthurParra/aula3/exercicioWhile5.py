pessoas = 1
pontos_totais = 0

while pessoas <= 4:
    questao = 1
    while questao <= 3:
        resposta = input(f"Pessoa {pessoas}, Questão {questao}: ")
        
        if questao == 1:
            if resposta == "A":
                pontos_totais += 1
        elif questao == 2:
            if resposta == "C":
                pontos_totais += 1
        elif questao == 3:
            if resposta == "D":
                pontos_totais += 1
        
        questao += 1
    
    pessoas += 1

print(f"Pontuação total: {pontos_totais}")
