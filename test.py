def bowling_score(frames):
    # Flatten frames
    rolls = []
    for frame in frames:
        if isinstance(frame, int):
            rolls.append(frame)
        else:
            rolls.extend(frame)

    score = 0
    roll_index = 0

    for frame in range(10):
        if roll_index >= len(rolls):
            break

        if rolls[roll_index] == 10:  # Strike
            score += 10
            if roll_index + 1 < len(rolls):
                score += rolls[roll_index + 1]
            if roll_index + 2 < len(rolls):
                score += rolls[roll_index + 2]
            roll_index += 1

        elif roll_index + 1 < len(rolls) and rolls[roll_index] + rolls[roll_index + 1] == 10:  # Spare
            score += 10
            if roll_index + 2 < len(rolls):
                score += rolls[roll_index + 2]
            roll_index += 2

        else:  # Open frame
            score += rolls[roll_index]
            if roll_index + 1 < len(rolls):
                score += rolls[roll_index + 1]
            roll_index += 2

    return score
