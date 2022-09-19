from src.light_saber import SabreDeLuz


def test_light_saber():
    light_saber = SabreDeLuz(cor="rosa", forca=100)
    assert light_saber.cor == "rosa"
    assert light_saber.forca == 100
