import random


def fibonacci_sequence(n=15, start1=2, start2=2):
    fib_sequence = [start1, start2]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[1:n]


def result_roulette():
    return random.randint(0, 35)


def is_pair(result):
    if result == 0:
        return 0.5
    if result % 2 == 0:
        return 2
    else:
        return 0


def play_roulette_fibonacci():
    fibonacci_bets = fibonacci_sequence()
    current_position = 0
    balance = 400  # Solde initial
    objectif = balance * 1.5
    bet_history = []
    games_lost = 0
    rounds = 0

    while balance > 0 and balance < objectif:
        if current_position >= len(fibonacci_bets):
            current_position = len(fibonacci_bets) - 1

        bet_amount = fibonacci_bets[current_position]
        balance -= bet_amount  # Placer le pari
        outcome = random.randint(0, 36)  # Simuler la roulette

        result = is_pair(outcome)
        win_or_lose = "Win" if result == 2 else "Lose"

        if result == 2:  # Gagner le pari
            balance += bet_amount * 2  # Recevoir le double du pari
            if current_position >= 2:
                current_position -= 2  # Reculer de deux positions dans la séquence
            else:
                current_position = 0
        else:  # Perdre le pari
            current_position += 1  # Avancer d'une position dans la séquence

        bet_history.append((win_or_lose, outcome, bet_amount, balance))
        rounds += 1  # Incrémenter le nombre de tours

        if balance <= 0:
            games_lost += 1
            break

    return bet_history, balance, games_lost, rounds

def stat_casino():

    total_games = 10000

    all_game_results = []
    total_games_lost = 0
    total_time_minutes = 0

    for game_number in range(total_games):
        history, final_balance, games_lost, rounds = play_roulette_fibonacci()
        all_game_results.append((game_number + 1, final_balance, games_lost, rounds))
        total_games_lost += games_lost
        total_time_minutes += rounds  # Ajouter le temps en minutes pour chaque jeu

    print(f"\nSolde initial: {total_games*400}")
    print(f"Chiffre d'affaires: {(total_games_lost*100/total_games)*-400 + (100 - (total_games_lost*100/total_games))*200} euros")
    print(f"\nNombre total de jeux perdus: {total_games_lost*100/total_games}%")
    print(f"moyenne heure/jeu: {(total_time_minutes/60)/total_games:.1f} heure")