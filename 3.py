import random

def generate_insurance_states(num_years):
    states = [3]
    
    for _ in range(num_years):
        current_assets = states[-1]
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
            break  # Компанія банкрутує
        
        # Додавання нового стану
        states.append(current_assets)
    
    return states

# Генерувати можливі стани для компанії протягом 10 років
result_insurance_states = generate_insurance_states(10)
print(result_insurance_states)
