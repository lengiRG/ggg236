def texto_valido(texto):
    return texto.strip() != ""

def email_valido(email):
    email = email.strip()
    return email.count("@") == 1 and "." in email.split("@")[1]
