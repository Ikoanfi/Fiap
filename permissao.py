acesso = input("Informe seu nivel de acesso (ADM, USR ou GUEST) ").upper()
sexo = input("Informe seu sexo M(Masculino ou F(Feminino) ").upper()

if acesso == "ADM" or acesso == "URS" or acesso == "GUEST":
    if acesso == "ADM":
        if sexo == "M":
            print("Ola administrador ")
        elif sexo == "F":
            print("Ola administradora")
    elif acesso == "URS":
        if sexo == "M":
            print("Ola usuario")
        elif sexo == "F":
            print("Ola usuaria")
    elif acesso == "GUEST":
        print("Ola visitante")    

else:
    print("Ola desconhecido ")



