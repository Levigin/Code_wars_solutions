def generate_hashtag(s: str):
    if s == "":
        return False
    s = s.lower()
    s = s.split()
    new_list = []
    for i in s:
        new_list.append(i[0].upper() + i[1:])
    print(new_list)
    new_s = '#' + ''.join(new_list)
    if len(new_s) > 140:
        return False
    return new_s

print(generate_hashtag('PwUtUCS ATx FMAAHJLdhVW UyUNrmSNQxk'))
