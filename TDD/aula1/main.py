def cpf(cpf_number):
    if len(cpf_number) != 11:
        raise Exception("CPF Inválido")
    return f'{cpf_number[0:3]}.{cpf_number[3:6]}.{cpf_number[6:9]}-{cpf_number[9:11]}'

def telefone(telefone_number):
    if len(telefone_number) != 11:
        raise Exception("Telefone Inválido")
    return f'({telefone_number[0:2]}){telefone_number[2:7]}-{telefone_number[7:11]}'