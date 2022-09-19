from src.personagem import Personagem
from src.light_saber import SabreDeLuz


class Sith(Personagem):
    def __init__(self, nome: str, especie: str, hp: int):
        super().__init__(nome, especie, hp)
        self.light_saber = SabreDeLuz("vermelho", 50)

    def atacar(self, personagem):
        if not personagem.defender():
            personagem.set_hp(self.light_saber.forca)

    def falar(self):
        if self.get_hp() <= 0:
            print(f"{self.nome} morreu")
        return "EU SOU SEU PAI!"
