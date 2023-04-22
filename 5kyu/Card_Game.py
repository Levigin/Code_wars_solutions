def card_game(n):
    players = [0, 0]

    count = 0
    while n > 0:
        if n > 4 and n % 2 == 0:
            if n % 2 == 0 and (n // 2) % 2 == 0:
                players[count % 2] += 1
                n -= 1
            elif n % 2 == 0 and (n // 2) % 2 != 0:
                players[count % 2] += (n // 2)
                n //= 2
        elif n <= 4 and n % 2 == 0:
            players[count % 2] += (n // 2)
            n //= 2
        elif n % 2 != 0:
            players[count % 2] += 1
            n -= 1

        count += 1
    return players[0]


print(card_game(100000000000))
