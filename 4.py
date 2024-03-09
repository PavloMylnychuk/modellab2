import random

def simulate_insurance_bankruptcy_probability(num_simulations, num_years):
    bankruptcies = 0
    
    for _ in range(num_simulations):
        states = [3]
        
        for _ in range(num_years):
            current_assets = states[-1]
            
            # Ймовірності виплати премій та страхових виплат
            premium_prob = 0.4
            claim_probs = [0.35, 0.25]
            
            # Вибір події (премія або виплата)
            event = random.choices(['premium', 'claim'], weights=[premium_prob, 1 - premium_prob])[0]
            
            if event == 'premium':
                current_assets += 2
            else:
                # Вибір суми виплати з відповідними ймовірностями
                claim_amount = random.choices([1, 2, 4], weights=claim_probs, k=1)[0]
                current_assets -= claim_amount
            
            # Перевірка умов банкрутства та виплати дивідендів
            if current_assets > 3:
                dividend = current_assets - 3
                current_assets = 3
            elif current_assets <= 0:
                bankruptcies += 1
                break  # Компанія банкрутує
            
            # Додавання нового стану
            states.append(current_assets)
    
    bankruptcy_probability = bankruptcies / num_simulations
    return bankruptcy_probability

# Задати кількість симуляцій та кількість років
num_simulations = 10000
num_years = 5

# Обчислити ймовірність банкрутства протягом перших 5 років
probability_of_bankruptcy = simulate_insurance_bankruptcy_probability(num_simulations, num_years)
print(f"Ймовірність банкрутства компанії протягом перших {num_years} років: {probability_of_bankruptcy}")
