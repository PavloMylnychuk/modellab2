import random

def generate_states(t, num_experiments):
    states = [t]
    
    for _ in range(num_experiments - 1):
        white_balls = states[-1]
        prob_black = white_balls / (white_balls + 1) if white_balls > 0 else 0
        chosen_ball = random.choices(['white', 'black'], [1 - prob_black, prob_black])[0]
        white_balls = white_balls + 1 if chosen_ball == 'black' else white_balls - 1
        states.append(white_balls)
    
    return states

result_states = generate_states(2, 20)
print(result_states)
