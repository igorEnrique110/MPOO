class Endereco:
    def __init__(self, rua, numero, cidade, estado, cep):
        self.rua = rua
        self.numero = numero
        self.cidade = cidade
        self.estado = estado
        self.cep = cep

class Pessoa:
    def __init__(self, nome, cpf, endereco):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco

class Aluno(Pessoa):
    def __init__(self, nome, cpf, endereco, curso, sala):
        super().__init__(nome, cpf, endereco)
        self.curso = curso
        self.sala = sala

class Professor(Pessoa):
    def __init__(self, nome, cpf, endereco, disciplinas):
        super().__init__(nome, cpf, endereco)
        self.disciplinas = disciplinas

class Curso:
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo

class Disciplina:
    def __init__(self, nome, codigo, carga_horaria):
        self.nome = nome
        self.codigo = codigo
        self.carga_horaria = carga_horaria

class Sala:
    def __init__(self, numero, capacidade):
        self.numero = numero
        self.capacidade = capacidade

class Servidor(Pessoa):
    def __init__(self, nome, cpf, endereco, cargo):
        super().__init__(nome, cpf, endereco)
        self.cargo = cargo

class Diretor(Servidor):
    def __init__(self, nome, cpf, endereco, cargo):
        super().__init__(nome, cpf, endereco, cargo)

class Coordenador(Servidor):
    def __init__(self, nome, cpf, endereco, cargo):
        super().__init__(nome, cpf, endereco, cargo)


aluno1Curso = Curso("SI", "001")
aluno1Endereco = Endereco("Rua 08", "Nº42", "Serra T.", "Pernambuco", "54896")
aluno1Sala = Sala("Nº14", "25")
aluno1 = Aluno("João", "5558877", aluno1Endereco, aluno1Curso, aluno1Sala)

professor1Disciplina = Disciplina("Programção", "004", "60 horas")
professor1 = Professor("José", "11226644", "Rua 10", "Programação")


print("Aluno:")
print("Nome:", aluno1.nome)
print("CPF:", aluno1.cpf)
print("Curso:", aluno1.curso.codigo)
print("Endereço:", aluno1.endereco.rua, aluno1.endereco.numero, aluno1.endereco.cidade, aluno1.endereco.estado, aluno1.endereco.cep)
print("Sala:", aluno1.sala.numero, "| Capacidade", aluno1.sala.capacidade)

print("/-/-/"*10)

print("Professor:")
print("Nome do professor:", professor1.nome)
print("Matéria:", professor1.disciplinas, "Carga horária:", professor1Disciplina.carga_horaria, "| Código:", professor1Disciplina.codigo)