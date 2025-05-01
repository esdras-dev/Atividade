# Resolução 1 Listas

catalogo_magico = []

# Passo 2: Adicionar Livros
def adicionar_livro(catalogo, livro):
    catalogo.append(livro)

# Adicionando os livros ao catálogo
adicionar_livro(catalogo_magico, "O Feitiço da Lua Crescente")
adicionar_livro(catalogo_magico, "A Jornada do Unicórnio Perdido")
adicionar_livro(catalogo_magico, "Segredos da Floresta Encantada")

# Passo 3: Visualizar o Catálogo
print("Catálogo Mágico Atual:")
print(catalogo_magico)

# Passo 4: Buscar Livro por Posição
def buscar_livro(catalogo, indice):
    return catalogo[indice]

# Buscar o livro na posição 1
livro_encontrado = buscar_livro(catalogo_magico, 1)
print(f"\n Livro na posição 1: {livro_encontrado}")

# Passo 5: Remover Livro
catalogo_magico.remove("A Jornada do Unicórnio Perdido")

# Passo 6: Visualizar Catálogo Atualizado
print("\n Catálogo Mágico Após Remoção:")
print(catalogo_magico)

# Passo 7: Verificar Presença
def verificar_livro(catalogo, livro):
    return livro in catalogo

# Verificando se "Segredos da Floresta Encantada" está no catálogo
presente = verificar_livro(catalogo_magico, "Segredos da Floresta Encantada")
print(f"\n'Segredos da Floresta Encantada' está no catálogo? {presente}")
