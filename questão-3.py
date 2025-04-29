# Resolução 3 Pilhas

torre_de_cristais = []

# Passo 2: Empilhar Cristal
def empilhar_cristal(pilha, cristal):
    pilha.append(cristal)

# Adicionando os cristais à pilha
empilhar_cristal(torre_de_cristais, "Cristal do Passado")
empilhar_cristal(torre_de_cristais, "Cristal do Presente")
empilhar_cristal(torre_de_cristais, "Cristal do Futuro")

# Passo 3: Visualizar a Pilha
print("Torre de Cristais Atual (topo no final):")
print(torre_de_cristais)

# Passo 4: Desempilhar Cristal
def desempilhar_cristal(pilha):
    return pilha.pop()

# Utilizando o cristal do topo em um ritual
cristal_usado = desempilhar_cristal(torre_de_cristais)
print(f"\n Cristal utilizado no ritual: {cristal_usado}")

# Passo 5: Verificar Pilha Vazia
def pilha_vazia(pilha):
    return len(pilha) == 0

# Verificando se ainda há cristais
print(f"\nAinda há cristais na torre? {not pilha_vazia(torre_de_cristais)}")

# Passo 6: Visualizar Pilha Restante
print("\n Torre de Cristais Restante:")
print(torre_de_cristais)

# Passo 7: Desempilhar Cristais Restantes
print("\nUtilizando cristais restantes:")
while not pilha_vazia(torre_de_cristais):
    cristal = desempilhar_cristal(torre_de_cristais)
    print(f" Cristal utilizado: {cristal}")

# Verificando se a pilha está vazia ao final
print(f"\n Todos os cristais foram utilizados? {pilha_vazia(torre_de_cristais)}")
