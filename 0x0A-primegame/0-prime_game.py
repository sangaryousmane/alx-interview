#!/usr/bin/python3
""" Prime Game
determine who the winner of each game is
"""


def isWinner(x, nums):
    """ Main Function - determines the winner
    of each game
    """

    def is_prime(num):
        """ Check for prime numbers
        """
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    def get_primes_up_to(n):
        """ Get prime numbers upto certain number - n
        """
        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def play_game(n):
        """ Play the game
        """
        primes = get_primes_up_to(n)
        maria_turn = True
        while primes:
            if maria_turn:
                if not primes:
                    return "Ben"
                chosen_prime = primes[0]
                primes = [p for p in primes if p % chosen_prime != 0]
            else:
                if not primes:
                    return "Maria"
                chosen_prime = primes[0]
                primes = [p for p in primes if p % chosen_prime != 0]
            maria_turn = not maria_turn
        return "Ben" if maria_turn else "Maria"
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
