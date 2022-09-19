from src.personagem import Personagem
from src.light_saber import SabreDeLuz
from random import choice


class Jedi(Personagem):
    def __init__(self, nome: str, especie: str, hp: int) -> None:
        super().__init__(nome, especie, hp)
        self.light_saber = SabreDeLuz("verde", 50)

    def defender(self) -> bool:
        defesa = choice([True, False])
        if defesa:
            print(f"{self.nome} defendeu!")
        return defesa

    def contra_atacar(self, personagem):
        personagem.set_hp(self.light_saber.forca)

    def falar(self) -> str:
        if self.get_hp() <= 0:
            print(f"{self.nome} morreu")
        return "NOOOOOOOOO!"
