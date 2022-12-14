def formatted_numbers():
    list = []
    list.append(f'|{"decimal":^10}|{"hex":^10}|{"binary":^10}|')
    for i in range(0,16):
        list.append(f'|{i:<10}|{i:^10x}|{i:>10b}|')
    return list