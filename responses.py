import random

def get_response(message: str)-> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hello!'
    
    if p_message == 'birth':
        return 'Aún no tengo esa función :c'

    if message == 'roll':
        return str(random.randint(1,6))
    
    if p_message == 'help':
        return 'This is a help message'
    
    if p_message == 'bye':
        return 'Siokentiendo, c va*'
    
    return 'I didnt understand that'