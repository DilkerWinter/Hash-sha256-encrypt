import hashlib

def encriptar(senha):
    senha_encoded = senha.encode('utf-8')
    senhaCriptografada = hashlib.sha256(senha_encoded).hexdigest()
    return senhaCriptografada


def main():
    senha = input("Digite uma senha para encriptar: ")
    print(encriptar(senha))


if __name__ == "__main__":
    main()


