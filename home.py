print("Вгадай число")
nu = 0
att = 0
guess = None

while guess !=nu:

    guess = int(input("Впиши вгадане число: "))
    att += 1
    if guess > nu:
        print("Менше")

print(f"Вгадав! Витрачено спроб: {att}")