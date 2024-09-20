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
    
def generate_object_set(min, max):
        obj = []
        n = random.randint(min, max)
        for i in range(n):
            obj.append(Objeto(random.randint(1, 100), random.randint(1, 100)))
        return obj


class Mochila:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.objetos = generate_object_set(10, 40)
    
    def agregar_objeto(self, objeto):
        self.objetos.append(objeto)
    
    def get_capacidad(self):
        return self.capacidad
    
    def get_objetos(self):
        return self.objetos
    
    def print_objetos(self):
        for objeto in self.objetos:
            print(objeto.__str__())
    
    def __str__(self):
        return f"Mochila(capacidad={self.capacidad}, cantidad de objetos={len(self.objetos)})"

print(Mochila(100).__str__())