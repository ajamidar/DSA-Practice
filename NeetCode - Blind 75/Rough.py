import sys

def is_valid(s: str) -> bool:
    s = s.strip()
    if not s or not s.isdigit():
        return False
    total = 0
    double = False
    for ch in reversed(s):
        d = int(ch)
        if double:
            d *= 2
            if d > 9:
                d -= 9
        total += d
        double = not double
    return total % 10 == 0

def main():
    data = sys.stdin.read().strip()
    print("True" if is_valid(data) else "False")

if __name__ == "__main__":
    main()

# Luhn Algorithm - Used to validate Tesco's clubcard numbers.