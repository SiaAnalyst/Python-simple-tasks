def solve_riddle(riddle, word_length, start_letter, reverse=False):
    if riddle.find(start_letter) == -1:
        return ""
    else:
        if reverse:
            word = riddle[riddle.index(start_letter)-word_length+1:riddle.index(start_letter)+1]
            word = word[::-1]
            return word
        else:
            word = riddle[riddle.index(start_letter):riddle.index(start_letter)+word_length]
            return word