import random

def play_game():
    print("به بازی حدس عدد خوش آمدید!")
    print("من یک عدد بین ۱ تا ۱۰۰ انتخاب کرده‌ام. سعی کن آن را حدس بزنی.")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        guess = input("عدد خود را وارد کنید: ")
        
        if not guess.isdigit():
            print("لطفاً فقط یک عدد معتبر وارد کنید.")
            continue
            
        guess = int(guess)
        attempts += 1
        
        if guess < secret_number:
            print("بیشتر است! (عدد بزرگتر حدس بزن)")
        elif guess > secret_number:
            print("کمتر است! (عدد کوچکتر حدس بزن)")
        else:
            print(f"تبریک می‌گم! 🎉 عدد درست همین بود. شما موفق شدید در {attempts} تلاش آن را حدس بزنید.")
            break

play_game()
