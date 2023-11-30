import random

def complimenten_generator (naam: str) -> str:
    COMPLIMENTEN = ('je bent geweldig ', 'je bent mooi ', 'je bent de beste ')
    random_compliment = random.choice(COMPLIMENTEN)
    return random_compliment + naam


print (complimenten_generator ('taym')) 