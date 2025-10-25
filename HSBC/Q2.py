def solution(S, T):
    N = len(S)
    moves = 0

    # Calculate the difference between S and T
    for i in range(N - 1):
        s_digit = int(S[i])
        t_digit = int(T[i])
        # Calculate the required increment
        increment = (t_digit - s_digit + 10) % 10
        
        # If we need to increment, we apply it to the current and next digit
        if increment > 0:
            moves += increment
            # Update the next digit in S to reflect the increment
            S = S[:i] + str((s_digit + increment) % 10) + str((int(S[i + 1]) + increment) % 10) + S[i + 2:]

    # Check the last digit
    if int(S[-1]) != int(T[-1]):
        return -1

    return moves