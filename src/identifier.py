def identifier(entrada):
    if entrada is None:
        return "inválido"

    if len(entrada) < 1 or len(entrada) > 6:
        return "inválido"

    if not entrada[0].isalpha():
        return "inválido"

    if not entrada.isalnum():
        return "inválido"

    return "válido"