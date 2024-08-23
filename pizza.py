from ingredientes import vegetales, masa, proteinas

class Pizza:
    precio = 10000
    tamanio = "Familiar"
    
    
    def __init__(self, i_proteico=None, vegetal_1=None, vegetal_2=None, t_masa=None):
        """
        Genera las variables donde se almacenaran los ingredientes de cada tipo seleccionado por el usuario.

        Parametros:
        - i_proteico: str, Ingrediente proteico ingresado por el usuario
        - vegetal_1: str, Ingrediente vegetal numero 1 ingresado por el usuario
        - vegetal_2: str, Ingrediente vegetal numero 2 ingresado por el usuario
        - t_masa: str, Tipo de masa seleccionada por el usuario

        Return:
        - Campos vacios listos para que ser actualizados por el usuario
        """
        self.i_proteico = i_proteico
        self.vegetal_1 = vegetal_1
        self.vegetal_2 = vegetal_2
        self.t_masa = t_masa
        self.pizza_valida = None  # Se calculará después
        
        
    @staticmethod
    def casos_posibles(evaluacion,ingredientes: list):
        """
        Valida si los ingredientes ingresados estan dentro de la lista de ingredientes.

        Parametros:
        - evaluacion: str, Ingredientes seleccionados por el usuario
        - ingredientes: str, listado de ingredientes base para que el usuario seleccionara.

        Return:
        - Booleano True/False dependiendo si los ingredientes estan presentes en la lista base.
        """   

        if evaluacion in ingredientes:
            # print("Lo logre")
            return True
        # print("Hay un error en su pedido")
        return False
    
    
    def realizar_pedido(self):
        """
        Genera inputs para que el usuario pueda selecionar los ingredientes y valida que los ingredientes esten contenidos dentro de los disponibles.

        Return:
        - Mensaje basado en booleano True/False de acuerdo a la condicion de los ingredientes ingresados.
        """
        self.i_proteico = input("Por favor ingrese el tipo de proteína (pollo, uno, carne vegetal): ")
        self.vegetal_1 =  input("Por favor ingrese el primer ingrediente vegetal (tomates, aceitunas, champiñones): ")
        self.vegetal_2 =  input("Por favor ingrese el segundo ingrediente vegetal (tomates, aceitunas, champiñones): ")
        self.t_masa =  input("Por favor ingrese el tipo de masa (tradicional, delgada): ")
        
        v_1 = Pizza.casos_posibles(self.i_proteico, proteinas)
        v_2 = Pizza.casos_posibles(self.vegetal_1,vegetales)
        v_3 = Pizza.casos_posibles(self.vegetal_2, vegetales)
        v_4 = Pizza.casos_posibles(self.t_masa, masa)

        lista_respuesta = [v_1, v_2, v_3, v_4]

        if False in lista_respuesta:
            self.pizza_valida = "Su pedido tiene un error. Por favor verifique los ingredientes y vuelva a intentarlo."
            
        else:
            self.pizza_valida = "¡Su pedido está correcto! Gracias por su compra."
            
            #print(f"Resumen del pedido: \nProteína: {self.i_proteico}\nVegetales: {self.vegetal_1}, {self.vegetal_2}\nMasa: {self.t_masa}\nPrecio total: {Pizza.precio} pesos.")
    