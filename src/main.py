from personagem import Personagem
from jedi import Jedi
from sith import Sith


if __name__ == "__main__":
    padme = Personagem("Padmé", "Humana", 50)
    luke = Jedi("Luke", "Humano", 200)
    vader = Sith("Vader", "Humano", 200)
    print(
        padme, "\n",
        luke, "\n",
        vader, "\n"
    )
    while luke.get_hp() >= 0 or vader.get_hp() >= 0:
        if vader.get_hp() >= 0:
            vader.atacar(luke)
            print(vader.falar())
        else:
            break
        if luke.get_hp() >= 0:
            print(luke.falar())
            luke.contra_atacar(vader)
        else:
            break
