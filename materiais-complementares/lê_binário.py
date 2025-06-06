def lê_binário():
    try:
        with open("binary.jpg" ,"rb") as fs1:
            dados=fs1.read()
            print(type(dados))
        with open("cópia.jpg" ,"wb") as fs2:
            fs2.write(dados)
    except FileNotFoundError as e:
        print('Arquivo não existe! -_-|||', e)
    except IOError as e:
        print('Deu algo errado @_@') 
    print("OK! ~_~")
lê_binário()

