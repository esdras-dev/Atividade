# Resolução 2 Filas

from collections import deque 
 
# Passo 1: Criar a Fila
fila_de_pedidos = deque()

# Passo 2: Adicionar Pedidos
def adicionar_pedido(fila, pedido):
    fila.append(pedido)

# Adicionando os pedidos
adicionar_pedido(fila_de_pedidos, "Martelo Encantado")
adicionar_pedido(fila_de_pedidos, "Pinça Teleportadora")
adicionar_pedido(fila_de_pedidos, "Chave de Fenda Sônica")

# Passo 3: Visualizar a Fila
print("Fila de Pedidos Atual:")
print(fila_de_pedidos)

# Passo 4: Processar Pedido
def processar_pedido(fila):
    return fila.popleft()

# Processando o próximo pedido
pedido_atendido = processar_pedido(fila_de_pedidos)
print(f"Pedido atendido: {pedido_atendido}")

# Passo 5: Verificar Fila Vazia
def fila_vazia(fila):
    return len(fila) == 0

# Verificando se ainda há pedidos na fila
print(f"Ainda há pedidos na fila? {not fila_vazia(fila_de_pedidos)}")

# Passo 6: Visualizar Fila Restante
print("Fila de Pedidos Restante:")
print(fila_de_pedidos)

# Passo 7: Processar Pedidos Restantes
print("Processando pedidos restantes:")
while not fila_vazia(fila_de_pedidos):
    pedido = processar_pedido(fila_de_pedidos)
    print(f"Pedido atendido: {pedido}")

# Verificando se a fila está vazia ao final
print(f"Todos os pedidos foram processados? {fila_vazia(fila_de_pedidos)}")
