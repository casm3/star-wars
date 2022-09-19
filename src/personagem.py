from src.personagem_interface import PersonagemInterface


class Personagem(PersonagemInterface):
    """Modela um Personagem Genérico do Universo Star Wars"""
    def __init__(self, nome: str, especie: str, hp: int) -> None:
        self.nome = nome
        self.especie = especie
        self.__hp = hp

    def get_hp(self) -> int:
        return self.__hp

    def set_hp(self, dano: int):
        self.__hp -= dano

    def __repr__(self) -> str:
        return f"Me chamo {self.nome}, sou {self.especie} e HP {self.get_hp()}"

    def falar(self) -> str:
        return "Que a força esteja com você!"
