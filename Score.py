def add_score(difficulty: int):
    try:
        f = open('scores.txt', 'r')
        number = int(f.read())
        new_score = (difficulty * 3) + 5 + number
    except ValueError:
        print('The data stores in Scores.txt is not an instence of int, creating new counter..')
        new_score = (difficulty * 3) + 5
    finally:
        f = open('scores.txt', 'w')
        f.write(str(new_score))