# Bowling game rules: 
# 300 Max score
# 10 Frames = 20 rolls except when the score reaches 300 first
# 10 points for "strike"
# 10 points plus the following score of the next frame for "Spare" (Got 10 points from two rolls. e.g. 1st roll = 6, 2nd roll = 4)
# If not "strike" nor "spare", just add the score based on how many pins tumbled.

# Logic
def bowling_score(frames):
    for frame in frames:
        if not isinstance(frame, (list, tuple)):
            raise ValueError("Invalid frame")
        if len(frame) < 1 or len(frame) > 3:
            raise ValueError("Invalid frame length")
        for pins in frame:
            if pins < 0 or pins > 10:
                raise ValueError("Impossible roll")
        if len(frame) >= 2 and frame[0] != 10 and frame[0] + frame[1] > 10:
            raise ValueError("Invalid frame total")

    rolls = []
    for frame in frames:
        for r in frame:
            rolls.append(r)

    score = 0
    ri = 0
    frames_to_score = min(10, len(frames))
    for _ in range(frames_to_score):
        if ri >= len(rolls):
            break
        if rolls[ri] == 10:
            b1 = rolls[ri+1] if ri+1 < len(rolls) else 0
            b2 = rolls[ri+2] if ri+2 < len(rolls) else 0
            score += 10 + b1 + b2
            ri += 1
        elif ri+1 < len(rolls) and rolls[ri] + rolls[ri+1] == 10:
            b = rolls[ri+2] if ri+2 < len(rolls) else 0
            score += 10 + b
            ri += 2
        else:
            a = rolls[ri]
            b = rolls[ri+1] if ri+1 < len(rolls) else 0
            score += a + b
            ri += 2
    return score

assert bowling_score([[0,0]]*10) == 0
assert bowling_score([[3,3]]*10) == 60
assert bowling_score([[10]]*12) == 300
assert bowling_score([[5,5]]*9 + [[5,5,5]]) == 150
assert bowling_score([[5,3],[10],[4,6]]) == 38
assert bowling_score([[3,4]]) == 7
assert bowling_score([[10],[5,5],[3,2],[10],]) == 48
assert bowling_score([[0,0]]*9 + [[10,7,3]]) == 20
assert bowling_score([[0,0]]*9 + [[7,3,5]]) == 15
assert bowling_score([[5,3],[10],[4,6],[0,0],[8,1],[10],[6,3],[7,2],[10],[10,10,10]]) == 144
assert bowling_score([[5,4],[3,3],[7,3],[10]]) == 45

try:
    bowling_score([[15,5]])
    assert False, "should have raised ValueError for impossible roll"
except ValueError:
    pass

try:
    bowling_score([[5,8]])
    assert False, "should have raised ValueError for invalid frame total"
except ValueError:
    pass

print("All tests passed!")
