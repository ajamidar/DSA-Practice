def solution(S):
    # Count digit frequencies
    counts = [0] * 10
    for ch in S:
        counts[ord(ch) - 48] += 1

    left_parts = []
    nonzero_pairs = 0

    # Use non-zero pairs for the left half (from high to low)
    for d in range(9, 0, -1):
        pairs = counts[d] // 2
        if pairs:
            left_parts.append(str(d) * pairs)
            nonzero_pairs += pairs

    # If we have at least one non-zero pair, we can safely add zero pairs at the end
    if nonzero_pairs > 0:
        zero_pairs = counts[0] // 2
        if zero_pairs:
            left_parts.append('0' * zero_pairs)

        left = ''.join(left_parts)

        # Pick the highest digit with an odd count as the center (if any)
        center = ''
        for d in range(9, -1, -1):
            if counts[d] % 2 == 1:
                center = str(d)
                break

        right = left[::-1]
        return left + center + right

    # No non-zero pairs available -> best valid palindrome is a single highest digit
    for d in range(9, -1, -1):
        if counts[d] > 0:
            return str(d)

    # Should not reach here as S has at least one digit
    return ""