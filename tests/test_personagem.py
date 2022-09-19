from src.personagem import Personagem
from src.jedi import Jedi
from src.sith import Sith


def test_cria_personagem():
    personagem = Personagem(
        nome="Padmé",
        especie="Humana",
        hp=50
    )

    assert personagem.nome == "Padmé"
    assert personagem.especie == "Humana"
    assert personagem.get_hp() == 50


def test_cria_jedi():
    jedi = Jedi(
        nome="Luke",
        especie="Humano",
        hp=100
    )

    assert jedi.nome == "Luke"
    assert jedi.especie == "Humano"
    assert jedi.get_hp() == 100
    assert jedi.light_saber.forca == 50
    assert jedi.light_saber.cor == "verde"


def test_cria_sith():
    sith = Sith(
        nome="Vader",
        especie="Humano",
        hp=300
    )

    assert sith.nome == "Vader"
    assert sith.especie == "Humano"
    assert sith.get_hp() == 300
    assert sith.light_saber.forca == 50
    assert sith.light_saber.cor == "vermelho"
