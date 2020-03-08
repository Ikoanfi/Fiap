nome = input("Nome do paciente: ")
idade = int(input("Idade do paciente: "))
risco = input("Eh grupo de risco? (sim ou nao) ").upper()

if risco != "SIM" and risco != "NAO":
    risco = input("Entre somente com sim ou nao ").upper()
else:
    if idade < 15 or idade > 60:
        print("Paciente: ", nome.title(), " prioridade")
    elif risco == "SIM":
        print("Paciente: ", nome.title(), " prioridade")
    else:
        print("Paciente: ", nome.title(), " segue na fila")

        
        
        
        
        
        
