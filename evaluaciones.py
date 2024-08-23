from pizza import Pizza

# Imprimir atributos de la clase
#Requerimiento A
print(f"""Los atributos de la Pizza son: 
    precio: {Pizza.precio}
    tamaño: {Pizza.tamanio}\n""")


# Verificar si 'salsa de tomate' está en la lista de salsas

lista_salsas = ["salsa de tomate", "salsa bbq"]
print(f" El elemento -SALSA- si esta en la lista: {Pizza.casos_posibles('salsa de tomate',lista_salsas)}\n")


# Crear una instancia de Pizza
pedido = Pizza()


# Realizar pedido
pedido.realizar_pedido()


# Mostrar los ingredientes elegidos y si la pizza es válida
print(f"""Usted eligió los siguientes ingredientes:
    
    Proteína: {pedido.i_proteico}
    Vegetal 1: {pedido.vegetal_1}
    Vegetal 2: {pedido.vegetal_2}
    Tipo de masa: {pedido.t_masa}
    
    ¿Esta instancia es una pizza valida?: {pedido.pizza_valida}
    """)