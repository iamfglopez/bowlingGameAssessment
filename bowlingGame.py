# Bowling game rules: 
# 300 Max score
# 10 Frames = 20 rolls except when the score reaches 300 first
# 10 points for "strike"
# 10 points plus the following score of the next frame for "Spare" (Got 10 points from two rolls. e.g. 1st roll = 6, 2nd roll = 4)
# If not "strike" nor "spare", just add the score based on how many pins tumbled.

# Logic

frames = [(5, 2),10,(4, 6)]
# Flatten collected score from the list (frames)
rolls = []
for frame in frames:
    if isinstance(frame, int):
        rolls.append(frame)
    else:
        rolls.extend(frame)


score = 0
index = 0

# Loop over 10 frames max or however many frames are given
for frame in range(10):
    # Stop if no more rolls
    if index >= len(rolls):
        break
    # Srike
    if rolls[index] == 10:
        score += 10
        if index + 1 < len(rolls):
            score += rolls[index + 1]
        if index + 2 < len(rolls):
            score += rolls[index + 2]
        index += 1
    # Spare
    elif index + 1 < len(rolls) and rolls[index] + rolls[index + 1] == 10:
        score += 10
        if index + 2 < len(rolls):
            score += rolls[index + 2]
        index += 2
    # Open frame
    else:
        score += rolls[index]
        if index + 1 < len(rolls):
            score += rolls[index + 1]
        index += 2

print("Final Score:", score)