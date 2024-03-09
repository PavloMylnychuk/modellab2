import random

def generate_weather_states(num_days):
    states = ['Я']
    
    for _ in range(num_days - 1):
        current_weather = states[-1]
        
        # Ймовірності переходу від Я до інших станів
        transitions_prob = {'Я': {'Д': 0.5, 'С': 0.5},
                            'С': {'Я': 0.5, 'Д': 0.25, 'С': 0.25},
                            'Д': {'Я': 0.5, 'С': 0.25, 'Д': 0.25}}
        
        # Перевірка наявності ключа в словнику
        if current_weather not in transitions_prob:
            raise ValueError(f"Неправильний стан погоди: {current_weather}")
        
        # Вибір нового стану
        new_state = random.choices(['Я', 'С', 'Д'], [transitions_prob[current_weather].get(state, 0) for state in ['Я', 'С', 'Д']])[0]
        
        # Додавання нового стану
        states.append(new_state)
    
    return states

result_weather_states = generate_weather_states(20)
print(result_weather_states)
