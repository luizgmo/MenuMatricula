import sys

ra = []
nome_aluno = []
cpf = []
id_curso_nome = []

id_curso = []
nome_curso = []
duracao_curso = []

id_disciplina = []
nome_disciplina = []
disciplinas_por_curso = []
# id_curso

#Função menu principal
def menu_principal():

  print("")
  print("Menu Principal:")
  print("1 - Alunos")
  print("2 - Cursos")
  print("3 - Disciplinas")
  print("4 - Sair")
  
  while True:       
    escolha = input("Digite o número da opção desejada: ")       
    if escolha == '1':
      menu_alunos()
    elif escolha == '2':
      menu_cursos()
    elif escolha == '3':
      menu_disciplinas()
    elif escolha == '4':
      print("Saindo do programa!")
      sys.exit()
              
    else:
      print("Opção inválida. Por favor, escolha uma opção válida.")

#Função menu de alunos
def menu_alunos():
  print("")
  print("Menu de Alunos:")
  print("a. Incluir")
  print("b. Alterar(Buscar pelo RA)")
  print("c. Consultar dados do aluno(Dados, Curso e Disciplina)")
  print("d. Relatório completo(Alunos, Cursos e Disciplinas)")
  print("e. Excluir(Buscar pelo RA)")
  print("f. Voltar")

  escolha_aluno = input("Digite a letra da opção desejada: ")

#Funções dentro do menu de alunos
  def IncluirAluno():
    while True:
      print("")
      print("Incluir")
      ra_alunoV = input("Digite o RA do aluno: ")
      ra.append(ra_alunoV)
      nome_alunoV = input("Digite o nome do aluno: ")
      nome_aluno.append(nome_alunoV)
      cpfV = input("Digite o CPF do aluno: ")
      cpf.append(cpfV)
      
      while True:
        id_cursoV = input("Digite o ID do curso: ")
        if id_cursoV in id_curso:
          id_curso_nome.append(id_cursoV)
          break
        else:
            print("ID não encontrado. Por favor, digite um ID válido.")

      continuar = input("Deseja incluir outro aluno? (S/N): ")
      if continuar.lower() != 's':
          menu_principal()

  def AlterarAluno():
    while True:
      print("")
      print("Alterar")
      while True:
        ra_alunoV = input("Digite o RA do aluno: ")
        if ra_alunoV not in ra:
          print("RA inválido. Digite novamente.")
        else:
          break
      nome_aluno[ra.index(ra_alunoV)] = input("Digite o nome que será alterado: ")
      cpf[ra.index(ra_alunoV)] = input("Digite o CPF que será alterado: ")
      print(nome_aluno, cpf)
  
      continuar = input("Deseja alterar outro aluno? (S/N): ")
      if continuar.lower() != 's':
        menu_principal()

  def ConsultarAlunoRA():
    while True:
      print("")
      print("Consultar")
      while True:
        ra_alunoV = input("Digite o RA do aluno: ")
        if ra_alunoV not in ra:
          print("RA inválido. Digite novamente.")
        else:
          break
      posi = ra.index(ra_alunoV)
      print("Nome do aluno: ", nome_aluno[posi]) 
      print("Curso do aluno: ", nome_curso[posi])
      if nome_disciplina == []:
        print("Nenhuma disciplina foi encontrada.")
      else:
        print("Disciplinas do aluno: ", nome_disciplina[posi])
  
      continuar = input("Deseja consultar outro aluno? (S/N): ")
      if continuar.lower() != 's':
        menu_principal()

  def RelatorioAluno():
    while True:
      print("")
      print("Relatório")
      i = 0
      while i < len(nome_aluno):
        print("Nome do aluno:", nome_aluno[i])
        print("Curso:", nome_curso[i])
        if nome_disciplina == []:
          print("Nenhuma disciplina foi encontrada.")
        else:
          print("Disciplinas:", nome_disciplina[i])
        i = i + 1
  
      continuar = input("Deseja fazer outro relatório? (S/N): ")
      if continuar.lower() != 's':
        menu_principal()

  def ExcluirAluno():
    while True:
      print("")
      print("Excluir")
      while True:
        ra_alunoV = input("Digite o RA do aluno: ")
        if ra_alunoV not in ra:
          print("RA inválido. Digite novamente.")
        else:
          break
  
      posi = ra.index(ra_alunoV)
      nome_aluno.pop(posi)
      cpf.pop(posi)
      ra.pop(posi)

      continuar = input("Deseja excluir outro aluno? (S/N): ")
      if continuar.lower() != 's':
        menu_principal()
      


#Escolhas dentro do menu de alunos  
  if escolha_aluno == 'a':
    IncluirAluno()
  elif escolha_aluno == 'b':
    AlterarAluno()
  elif escolha_aluno == 'c':
    ConsultarAlunoRA()
  elif escolha_aluno == 'd':
    RelatorioAluno()
  elif escolha_aluno == 'e':
    ExcluirAluno()
  elif escolha_aluno == 'f':
    menu_principal()       
  else:
    print("Opção inválida. Por favor, escolha uma opção válida.")

#Função menu de cursos
def menu_cursos():
  print("")
  print("Menu de Cursos:")
  print("a. Incluir")
  print("b. Alterar(Buscar pelo ID)")
  print("c. Consultar pelo ID(Dados do Curso e Disciplina)")
  print("d. Relatório completo(Dados dos Cursos e Disciplinas)")
  print("e. Excluir(Buscar pelo ID)")
  print("f. Voltar")

  escolha_curso = input("Digite a letra da opção desejada: ")

#Funções dentro do menu de cursos
  def IncluirCurso():
    while True:
      print("")
      print("Incluir")
      id_cursoV = input("Digite o ID do curso: ")
      id_curso.append(id_cursoV)
      nome_cursoV = input("Digite o nome do curso: ")
      nome_curso.append(nome_cursoV)
      duracao_cursoV = input("Digite a duração do curso: ")
      duracao_curso.append(duracao_cursoV)

      continuar = input("Deseja incluir outro curso? (S/N): ")
      if continuar.lower() != 's':
          menu_principal()
            
  def AlterarCurso():
    while True:
      print("")
      print("Alterar")
      while True:
        id_cursoV = input("Digite o ID do curso: ")
        if id_cursoV not in id_curso:
          print("ID inválido. Digite novamente.")
        else:
          break
      nome_curso[id_curso.index(id_cursoV)] = input("Digite o nome do curso que será alterado: ")
      duracao_curso[id_curso.index(id_cursoV)] = input("Digite a duração que será alterado: ")
  
      continuar = input("Deseja alterar outro curso? (S/N): ")
      if continuar.lower() != 's':
        menu_principal()
        
  def ConsultarCursoID():
    while True:
      print("")
      print("Consultar")
      while True:
        id_cursoV = input("Digite o ID do curso: ")
        if id_cursoV not in id_curso:
          print("ID inválido. Digite novamente.")
        else:
          break
      posi = id_curso.index(id_cursoV)
      print("Nome do curso: ", nome_curso[posi]) 
      print("Duração do curso: ", duracao_curso[posi])
      if nome_disciplina == []:
        print("Nenhuma disciplina foi encontrada.")
      else:
        print("Disciplinas:", nome_disciplina[posi])
  
      continuar = input("Deseja consultar outro curso? (S/N): ")
      if continuar.lower() != 's':
        menu_principal()
        
  def RelatorioCurso():
    while True:
      print("")
      print("Relatório")
      i = 0
      while i < len(nome_curso):
        print("Nome do curso:", nome_curso[i])
        if nome_disciplina == []:
          print("Nenhuma disciplina foi encontrada.")
        else:
          print("Disciplinas:", nome_disciplina[i])
        i = i + 1
  
      continuar = input("Deseja fazer outro relatório? (S/N): ")
      if continuar.lower() != 's':
        menu_principal()
        
  def ExcluirCurso():
    while True:
      print("")
      print("Excluir")
      while True:
        id_cursoV = input("Digite o ID do curso: ")
        if id_cursoV not in id_curso:
          print("ID inválido. Digite novamente.")
        else:
          break
  
      posi = id_curso.index(id_cursoV)
      nome_curso.pop(posi)
      duracao_curso.pop(posi)
      id_curso.pop(posi)

      continuar = input("Deseja excluir outro curso? (S/N): ")
      if continuar.lower() != 's':
        menu_principal()

#Escolhas dentro do menu de cursos    
  if escolha_curso == 'a':
    IncluirCurso()
  elif escolha_curso == 'b':
    AlterarCurso()
  elif escolha_curso == 'c':
    ConsultarCursoID()
  elif escolha_curso == 'd':
    RelatorioCurso()
  elif escolha_curso == 'e':
    ExcluirCurso()
  elif escolha_curso == 'f':
    menu_principal()       
  else:
    print("Opção inválida. Por favor, escolha uma opção válida.")

#Função menu de disciplinas
def menu_disciplinas():
  print("")
  print("Menu de Disciplinas:")
  print("a. Incluir")
  print("b. Alterar(Buscar pelo ID)")
  print("c. Consultar pelo ID")
  print("d. Relatório completo(Disciplinas)")
  print("e. Excluir(Buscar pelo ID)")
  print("f. Voltar")

  escolha_disciplina = input("Digite a letra da opção desejada: ")
  
  #Funções dentro do menu de disciplinas
  def IncluirDisciplina():
    while True:
        print("")
        print("Incluir")
        id_disciplinaV = input("Digite o ID da disciplina: ")
        nome_disciplinaV = input("Digite o nome da disciplina: ")
        
        while True:
          id_cursoV = input("Digite o ID do curso: ")
          if id_cursoV not in id_curso:
            print("ID inválido. Digite novamente.")
          else:
            posi = id_curso.index(id_cursoV)
            id_disciplina.insert(posi, id_disciplinaV)
            nome_disciplina.insert(posi, nome_disciplinaV)
            break
        
  
        continuar = input("Deseja incluir outra disciplina? (S/N): ")
        if continuar.lower() != 's':
            menu_principal()
    
  def AlterarDisciplina():
    while True:
      print("")
      print("Alterar")
      while True:
        id_disciplinaV = input("Digite o ID da disciplina: ")
        if id_disciplinaV not in id_disciplina:
          print("ID inválido. Digite novamente.")
        else:
          break
      nome_disciplina[id_disciplina.index(id_disciplinaV)] = input("Digite o nome da disciplina que será alterada: ")
      print(nome_disciplina)
  
      continuar = input("Deseja alterar outra disciplina? (S/N): ")
      if continuar.lower() != 's':
        menu_principal()

  def ConsultarDisciplinaID():
    while True:
      print("")
      print("Consultar")
      while True:
        id_disciplinaV = input("Digite o ID da disciplina: ")
        if id_disciplinaV not in id_disciplina:
          print("ID inválido. Digite novamente.")
        else:
          break
      posi = id_disciplina.index(id_disciplinaV)
      print("Nome da disciplina: ", nome_disciplina[posi]) 
  
      continuar = input("Deseja consultar outra disciplina? (S/N): ")
      if continuar.lower() != 's':
        menu_principal()
        
  def RelatorioDisciplina():
    print("")
    print("Relatório")
    i = 0
    while i < len(nome_disciplina):
      print("Nome da disciplina:", nome_disciplina[i])
      i = i + 1
  
    continuar = input("Deseja fazer outro relatório? (S/N): ")
    if continuar.lower() != 's':
      menu_principal()
        
      
        
  def ExcluirDisciplina():
    while True:
      print("")
      print("Excluir")
      while True:
        id_disciplinaV = input("Digite o ID da disciplina: ")
        if id_disciplinaV not in id_disciplina:
          print("ID inválido. Digite novamente.")
        else:
          break
  
      posi = id_disciplina.index(id_disciplinaV)
      nome_disciplina.pop(posi)
      id_disciplina.pop(posi)

      continuar = input("Deseja excluir outra disciplina? (S/N): ")
      if continuar.lower() != 's':
        menu_principal()
  
  if escolha_disciplina == 'a':
    IncluirDisciplina()
  elif escolha_disciplina == 'b':
    AlterarDisciplina()
  elif escolha_disciplina == 'c':
    ConsultarDisciplinaID()
  elif escolha_disciplina == 'd':
    RelatorioDisciplina()
  elif escolha_disciplina == 'e':
    ExcluirDisciplina()
  elif escolha_disciplina == 'f':
    menu_principal()       
  else:
    print("Opção inválida. Por favor, escolha uma opção válida.")

#Inicie o programa chamando o menu principal
menu_principal()
