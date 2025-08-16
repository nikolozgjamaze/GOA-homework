def sum_mix(arr):
    return sum(map(int, arr))


def smash(words):
    return ' '.join(words)




def simple_multiplication(n):
    return n * 8 if n % 2 == 0 else n * 9




def count_positives_sum_negatives(arr):
    if not arr:
        return []
    pos = sum(1 for x in arr if x > 0)
    neg = sum(x for x in arr if x < 0)
    return [pos, neg]



def count_positives_sum_negatives(arr):
    if not arr:
        return []
    pos = sum(1 for x in arr if x > 0)
    neg = sum(x for x in arr if x < 0)
    return [pos, neg]




def reverse_seq(n):
    return list(range(n, 0, -1))





def opposite(number):
    return -number




def number_to_string(num):
    return str(num)
