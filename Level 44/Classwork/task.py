
def sum_mix(arr):
    return sum(int(n) for n in arr)



def reverse_seq(n):
    return list(range(n, 0, -1))





def remove_exclamation_marks(s):
    return s.replace('!', '')




def points(games):
    total = 0
    for game in games:
        x, y = map(int, game.split(':'))
        if x > y:
            total += 3
        elif x == y:
            total += 1
    return total





def count_positives_sum_negatives(arr):
    if not arr:
        return []
    pos = sum(1 for x in arr if x > 0)
    neg = sum(x for x in arr if x < 0)
    return [pos, neg]







def smash(words):
    return ' '.join(words)


def simple_multiplication(n):
    return n * 8 if n % 2 == 0 else n * 9




