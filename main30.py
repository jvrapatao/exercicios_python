class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        print('marca:', self.marca)
        print('Modelo:', self.modelo)


meu_carro = Carro('Toyota', 'Corolla')
meu_carro.exibir_info()
