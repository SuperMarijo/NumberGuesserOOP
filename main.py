import datetime
import random
import json

class Scores:
    def __init__(self, attempts, player_name, date, secret_num):
        self.attempts = attempts
        self.player_name = player_name
        self.date = date
        self.secret_num = secret_num

def play():
    secret = random.randint(1, 99)
    attempts = 0
    player = input("What's your name? ")
    data_list = get_data_list()

    while True:
        guess = int(input("Guess the secret number (between 1 and 99): "))
        attempts += 1

        if guess == secret:
            scores_list = Scores(attempts=attempts, player_name=player, date=str(datetime.datetime.now()), secret_num=secret)

            data_list.append(scores_list.__dict__)

            with open("data_list.json", "w") as data_file:
                data_file.write(json.dumps(data_list))

            print("You've guessed it - congratulations! It's number " + str(secret))
            print("Attempts needed: " + str(attempts))
            break
        elif guess > secret:
            print("Your guess is not correct... try something smaller")
        elif guess < secret:
            print("Your guess is not correct... try something bigger")

        wrong_guesses.append({"wrong_guesses": guess})

def get_data_list():
    with open("data_list.json", "r") as data_file:
        data_list = json.loads(data_file.read())
        return data_list

def get_top_scores():
    data_list = get_data_list()
    ordered_list = sorted(data_list, key=lambda x: x["attempts"])[:3]
    return ordered_list


while True:
    play_again = input("Would you like to A) play a new game, B) see the best scores, or C) quit? ")

    if play_again.upper() == "A":
        play()
    elif play_again.upper() == "B":
        for scores_dict in get_top_scores():
            scores_list = Scores(attempts=scores_dict.get("attempts"), player_name=scores_dict.get("player_name"), date=scores_dict.get("date"),
                            secret_num=scores_dict.get("secret_num"))
            results = "Player {player} guessed correctly it was number {secret_num} in {attempts} tries on {date}." \
                .format(player=scores_list.player_name,
                        secret_num=scores_list.secret_num,
                        attempts=scores_list.attempts,
                        date=scores_list.date,)
        print(results)
    else:
        break
