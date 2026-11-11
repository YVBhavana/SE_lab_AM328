TOPPINGS = {"cheese": 40, "olives": 30, "onion": 20, "paneer": 50}
SIZES = {"S": 8, "M": 10, "L": 12}

def toppings_price(toppings_csv):
    total = 0
    for t in toppings_csv.split(','):
        t = t.strip().lower()
        if t in TOPPINGS:
            total += TOPPINGS[t]
    return total

def pizza_inches(size):
    size = size.strip().upper()
    if size in SIZES:
        return SIZES[size]
    return None

def split_bill(text):
    try:
        total, people = text.split('/')
        if int(people) == 0:
            return None
        return round(int(total) / int(people), 2)
    except (ValueError, ZeroDivisionError):
        return None

def main():
    print("==== Running toppings_price ====")
    user_input = input("Enter toppings as CSV (e.g. cheese,olives): ")
    result = toppings_price(user_input)
    print("Toppings Price:", result)

    print("\n==== Running pizza_inches ====")
    user_input = input("Enter pizza size (S/M/L): ")
    result = pizza_inches(user_input)
    print("Size in Inches:", result)

    print("\n==== Running split_bill ====")
    user_input = input("Enter total and people (e.g. 900/3): ")
    result = split_bill(user_input)
    print("Per Person:", result)

if __name__ == "__main__":
    main()