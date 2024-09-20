import random

class Objeto:
    def __init__(self, size):
        self.size = size

    def __str__(self):
        return f"Objeto(tamaño={self.size})"

class InstanciaProblema:
    def __init__(self):
        self.objetos = self.generate_object_set(15, 45)
        self.t = self.generate_random_t_or_k(True)
        self.k = self.generate_random_t_or_k(False)

    def generate_object_set(self, min, max):
        obj = []
        n = random.randint(min, max)
        for i in range(n):
            obj.append(Objeto(random.randint(1, 200)))
        return obj

    def generate_random_t_or_k(self, t:bool):
        acc = 1
        seed = random.randint(3, 5)
        if t:
            seed = random.randint(5, 8)
        for o in self.objetos:
            if o.size % seed != 0:
                acc *= o.size
        return acc

    def print_objetos(self):
        for objeto in self.objetos:
            print(objeto.__str__())

    def print_problem_input(self):
        print("Instancia del problema:")
        print(f"Cota de tamaño: {self.t}")
        print(f"k: {self.k}")
        print("Objetos:")
        self.print_objetos()
        print()

    def algoritmo_subconjunto(self):
        ## Fase adivinadora
        A = []
        acc = 1
        for objeto in self.objetos:
            if acc * objeto.size > self.t:
                break
            ## Paso no determinista
            if random.randint(0, 1) == 1:
                A.append(objeto)
                acc *= objeto.size
        print()
        print("Candidato a solucion:")
        for objeto in A:
            print(objeto.__str__())
        print(f"Acomulado: {acc}")
        ## Fase verificadora
        if acc >= self.k:
            return "YES"
        return "NO"


def main():
    problema = InstanciaProblema()
    problema.print_problem_input()
    print(problema.algoritmo_subconjunto())


if __name__ == "__main__":
    main()
        