import random
import time


print(("-=-" * 20), "\033[32mGAME: Pedra Papel e Tesoura\033[m", ("-=-" * 20))

print(("-=-" * 5), "\033[1mSuas opções\033[m", ("-=-" * 5))

print()
print("\033[1m[\033[m \033[32m1\033[m \033[1m] PEDRA\033[m")
print("\033[1m[\033[m \033[33m2\033[m \033[1m] PAPEL\033[m")
print("\033[1m[\033[m \033[34m3\033[m \033[1m] TESOURA\033[m")

print()

jogada = int(input("\033[1mInforme a sua jogada (1 à 3): "))

opcoes = ["PEDRA", "PAPEL", "TESOURA"]
computador = random.choice(opcoes)

print("\033[m\033[1;32mJO\033[m\033[1m...\033[m")
time.sleep(0.70)

print("\033[1;32mJO\033[m\033[1;33mKEN\033[m\033[1m..\033[m")
time.sleep(0.70)

print("\033[1;32mJO\033[m\033[1;33mKEN\033[m\033[1;34mPO\033[m\033[1m!\033[m")
time.sleep(0.5)

if jogada == 1:
    print(("\033[1;44;31m-=-"), "VOCÊ JOGOU PEDRA", ("-=-" * 6))

    print("\033[m")
    time.sleep(0.25)

    print(("\033[1;41;34m-=-" * 3), f"O COMPUTADOR JOGOU {computador}", "-=-=")

    print("\033[m")

    if computador == "TESOURA":
        print(
            ("\033[1m-=-\033[m" * 5),
            "\033[1;32mVocê Venceu!\033[m",
            ("\033[1m-=-\033[m" * 5),
        )
    elif computador == "PAPEL":
        print(
            ("\033[1m-=-\033[m" * 5),
            "\033[1;31mO computador venceu.\033[m",
            ("\033[1m-=-\033[m" * 5),
        )
    else:
        print(
            ("\033[1m-=-\033[m" * 5),
            "\033[1;33mFoi um empate!\033[m",
            ("\033[1m-=-\033[m" * 5),
        )
elif jogada == 2:
    print(("\033[1;44;31m-=-"), "VOCÊ JOGOU PAPEL", ("-=-" * 6))

    print("\033[m")
    time.sleep(0.25)

    print(("\033[1;41;34m-=-" * 3), f"O COMPUTADOR JOGOU {computador}", "-=-=")

    print("\033[m")

    if computador == "PEDRA":
        print(
            ("\033[1m-=-\033[m" * 5),
            "\033[1;32mVocê Venceu!\033[m",
            ("\033[1m-=-\033[m" * 5),
        )
    elif computador == "TESOURA":
        print(
            ("\033[1m-=-\033[m" * 5),
            "\033[1;31mO computador venceu.\033[m",
            ("\033[1m-=-\033[m" * 5),
        )
    else:
        print(
            ("\033[1m-=-\033[m" * 5),
            "\033[1;33mFoi um empate!\033[m",
            ("\033[1m-=-\033[m" * 5),
        )
elif jogada == 3:
    print(("\033[1;44;31m-=-"), "VOCÊ JOGOU TESOURA", ("-=-" * 6))

    print("\033[m")
    time.sleep(0.25)

    print(("\033[1;41;34m-=-" * 3), f"O COMPUTADOR JOGOU {computador}", "-=-=")

    print("\033[m")

    if computador == "PAPEL":
        print(
            ("\033[1m-=-\033[m" * 5),
            "\033[1;32mVocê Venceu!\033[m",
            ("\033[1m-=-\033[m" * 5),
        )
    elif computador == "PEDRA":
        print(
            ("\033[1m-=-\033[m" * 5),
            "\033[1;31mO computador venceu.\033[m",
            ("\033[1m-=-\033[m" * 5),
        )
    else:
        print(
            ("\033[1m-=-\033[m" * 5),
            "\033[1;33mFoi um empate!\033[m",
            ("\033[1m-=-\033[m" * 5),
        )
else:
    print("\033[31;4mEscolha uma opção válida. (1 à 3)\033[m")
