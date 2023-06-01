def is_less_dict(x, y):
    alphabet = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    x = x.lower()
    y = y.lower()
    
    diff = len(x) - len(y)

    if diff < 0:
        diff = diff*(-1)
        x = x+" "*diff

    if diff > 0:
        y = y+" "*diff

    for i in range(len(x)):
        if alphabet.index(x[i]) < alphabet.index(y[i]):
            return True
        if alphabet.index(x[i]) < alphabet.index(y[i]):
            return False

    return False

def is_less_str(x, y):
    alphabet = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    x = x.lower()
    y = y.lower()
    
    if len(x) < len(y):
        return True
    if len(y) < len(x):
        return False

    for i in range(len(x)):
        if alphabet.index(x[i]) < alphabet.index(y[i]):
            return True
        if alphabet.index(x[i]) < alphabet.index(y[i]):
            return False

    return False
            
