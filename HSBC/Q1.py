# ...existing code...
def solution(S):
    # Count parity (odd/even) per letter and sum odds
    parity = [0] * 26
    for ch in S:
        parity[ord(ch) - 97] ^= 1  # toggle between 0 and 1
    return sum(parity)
# ...existing code...