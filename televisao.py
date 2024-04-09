class Televisao:
    def __init__(self, estado):
        self.volume = 10
        self.estado = estado

    def modeOnOff(self):
        if self.estado == "ligar":
            self.estado = "Ligada"
            print("Televisão ligada")
        else:
            self.estado = "Desligada"
            print("Televisão desligada")

    def aumentarVolume(self):
        self.volume = self.volume + 1

        print(self.volume)


    def diminuirVolume(self):
        self.volume = self.volume - 1

        print(self.volume)




televisao1 = Televisao("ligar")
televisao1.modeOnOff()
print(televisao1.estado)
#print(televisao1.aumentarVolume())
print(televisao1.diminuirVolume())


