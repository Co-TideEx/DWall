from random import Random

CHUTES_LADDERS = {1:38, 4:14, 9:31, 16:6, 21:42, 28:84, 36:44,
                  47:26, 49:11, 51:67, 56:53, 62:19, 64:60,
                  71:91, 80:100, 87:24, 93:73, 95:75, 98:78}

def simulate_cl_game(rseed=None, max_roll=6):

    rand = Random(rseed)
    position = 0
    turns = 0
    while position < 100:
        turns += 1
        roll = rand.randint(1, max_roll)

        if position + roll > 100:
            continue

        position += roll

        position = CHUTES_LADDERS.get(position, position)
    return turns
print(simulate_cl_game())