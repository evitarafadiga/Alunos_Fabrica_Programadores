import itertools
import string

def adivinhar_senha_educacional(senha_alvo):
    caracteres = string.ascii_lowercase  # Tenta apenas letras minúsculas (a-z)
    max_comprimento = len(senha_alvo) # Define o comprimento máximo para ser o da senha que será descoberta

    print("Tentando adivinhar a senha '%s'..." % senha_alvo)

    for comprimento in range(1, max_comprimento + 1):
        for combinacao_tupla in itertools.product(caracteres, repeat=comprimento):
            tentativa = "".join(combinacao_tupla)
            print(f"Tentando: {tentativa}")
            if tentativa == senha_alvo:
                print("\n🎉 Senha encontrada! A senha é: %s" % tentativa)
                return True
    print("\nSenha não encontrada neste conjunto de caracteres e comprimento.")
    return False

# --- Exemplo de uso (troque 'abc' pela senha que você quer que o código "encontre") ---
senha_para_tentar = "mew" # Mude esta senha para experimentar! Tente senhas curtas.
adivinhar_senha_educacional(senha_para_tentar)