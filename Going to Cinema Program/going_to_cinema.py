import math
card = 500
ticket = 15
perc = 0.90


def movie(card, ticket, perc):
    ticket_num = 0
    system_a = 0
    system_b = card
    system_b_prev = ticket
    while math.ceil(card) >= system_a:
        system_a += ticket
        system_b_prev *= perc
        card += system_b_prev
        ticket_num += 1
    return ticket_num


print(movie(card, ticket, perc))
