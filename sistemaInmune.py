import random

class CelulaInmune:
    def __init__(self, identificador):
        self.identificador = identificador

    def detectar_patogeno(self, patogeno):
        if random.random() < 0.5:  # Probabilidad de detectar un patógeno
            print(f"Célula {self.identificador} ha detectado el patógeno {patogeno}")
            return True
        else:
            return False

    def eliminar_patogeno(self, patogeno):
        print(f"Célula {self.identificador} ha eliminado el patógeno {patogeno}")


class SistemaInmune:
    def __init__(self, num_celulas):
        self.celulas = [CelulaInmune(i) for i in range(num_celulas)]

    def atacar_patogeno(self, patogeno):
        for celula in self.celulas:
            if celula.detectar_patogeno(patogeno):
                celula.eliminar_patogeno(patogeno)
                return True
        print("Ninguna célula pudo detectar el patógeno")
        return False


# Uso del sistema inmune
sistema = SistemaInmune(10)  # Creamos un sistema inmune con 10 células
patogeno = "Virus"

print("Patógeno introducido:", patogeno)
sistema.atacar_patogeno(patogeno)