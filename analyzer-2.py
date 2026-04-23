print("=== Analyzer part 2 ===")

data = []

def average(data):
    if len(data) == 0:
        return 0

    total = 0
    count = 0

    for i in data:
        count += 1
        total += i

    return total / count


def per_pos(data):
    if len(data) == 0:
        return 0

    pos = 0
    for i in data:
        if i > 0:
            pos += 1

    return pos / len(data) * 100


def per_neg(data):
    if len(data) == 0:
        return 0

    neg = 0
    for i in data:
        if i < 0:
            neg += 1

    return neg / len(data) * 100


while True:
    x = input("give me a value (digit stop for exit): ").lower().strip()

    if x == "stop":
        print("\n--- RESULTS ---")
        print("average:", average(data))
        print("positive %:", per_pos(data))
        print("negative %:", per_neg(data))
        break

    try:
        data.append(int(x))
    except ValueError:
        print(x, "is not a valid number")
