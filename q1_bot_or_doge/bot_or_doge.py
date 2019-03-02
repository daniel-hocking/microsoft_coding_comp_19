def is_bot(user):
    unique = set()
    for c in user:
        unique.add(c)
    if len(unique) % 2:
        print('BOT')
    else:
        print('DOGE')
        
testin = input()
is_bot(testin)
