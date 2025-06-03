import random

def main():
    print("Добре дошли в играта 'Познай числото'!")
    play_again = True
    while play_again:
        secret = random.randint(1, 100)
        attempts = 0
        while True:
            try:
                guess = int(input("Познайте число между 1 и 100: "))
            except ValueError:
                print("Моля, въведете валидно цяло число.")
                continue
            attempts += 1
            if guess < secret:
                print("По-голямо!")
            elif guess > secret:
                print("По-малко!")
            else:
                print(f"Познахте! Числото беше {secret}. Опитахте {attempts} пъти.")
                break
        choice = input("Играте ли отново? (y/n): ")
        play_again = choice.lower().startswith('y')
    print("Благодаря за играта!")

if __name__ == "__main__":
    main()
