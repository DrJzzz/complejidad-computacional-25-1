import random

class Objeto:
    def __init__(self, peso, valor):
        self.peso = peso
        self.valor = valor
    
    def __str__(self):
        return f"Objeto(peso={self.peso}, valor={self.valor})"
    
    def get_peso(self):
        return self.peso
    
    def get_valor(self):
        return self.valor
    

class InstancaProblema:
    def __init__(self, capacidad):
        self.objetos = self.generate_object_set(10, 40)
        self.capacidad = self.generate_random_k_or_C(False)
        self.k = self.generate_random_k_or_C(True)

    def generate_object_set(self, min, max):
        obj = []
        n = random.randint(min, max)
        for i in range(n):
            obj.append(Objeto(random.randint(1, 100), random.randint(1, 100)))
        return obj

    def generate_random_k_or_C(self, k:bool):
        c = 4
        if k:
            c = 5
        acc = 0
        for o in self.objetos:
            acc += o.get_valor()
        return random.randint((acc // 4), (acc // 6) * c) 
    
    def get_capacidad(self):
        return self.capacidad

    def get_objetos(self):
        return self.objetos
    
    def print_objetos(self):
        for objeto in self.objetos:
            print(objeto.__str__())


    def print_problem_input(self):
        print("Instancia del problema:")
        print(f"Capacidad: {self.capacidad}")
        print(f"K: {self.k}")
        print("Objetos:")
        self.print_objetos()
        print()

    def algoritmo_mochila(self):
        ## Fase adivinadora
        S = []
        acc = 0
        for objeto in self.objetos:
            if acc + objeto.get_peso() > self.capacidad:
                break
            ## Paso no determinista
            if random.randint(0, 1) == 1:
                S.append(objeto)
                acc += objeto.get_peso()

        ## Fase verificadora 
        acc_valor = 0
        for objeto in S:
            acc_valor += objeto.get_valor()

        ## Imprimimos candidato
        print("Candidato a solucion:")
        for objeto in S:
            print(objeto.__str__())
        print(f"Valor total: {acc_valor}")
        print(f"Peso total: {acc}")
        print()

        if acc_valor >= self.k:
            return "YES"
        else:
            return "NO"



instancaProblema = InstancaProblema(100)
instancaProblema.print_problem_input()
print(instancaProblema.algoritmo_mochila())
