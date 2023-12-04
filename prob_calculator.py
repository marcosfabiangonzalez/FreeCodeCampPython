import copy
import random

class Hat:
    contents: list
    
    def __init__(self, **args) -> None:
        self.contents = ''.join(map(lambda i: f"{i} " * args[i], args)).strip().split(' ')
        
    def draw(self, balls: int) -> list:
        total = len(self.contents) if balls > len(self.contents) else balls
        draw_balls = list()
        for _ in range(total):
            rnd_inx = random.randrange(len(self.contents))
            draw_balls.append(self.contents[rnd_inx])
            self.contents.remove(self.contents[rnd_inx])
            
        draw_balls.sort()
        return ' '.join(draw_balls).split(' ')

def experiment(hat, expected_balls: list, num_balls_drawn: int, num_experiments: int) -> float:
    #expected_balls={"red":2,"green":1},
    match = 0
    match_2 = 0
    for _ in range(1, num_experiments):
        copy_hat = copy.deepcopy(hat)
        balls_drawn = copy_hat.draw(num_balls_drawn)
        balls_req = sum([1 for k, v in expected_balls.items() if balls_drawn.count(k) >= v])
        match_2 += 1 if balls_req == len(expected_balls) else 0
        length = 0
        for k, v in expected_balls.items():
            length += 1 if balls_drawn.count(k) >= v else 0
            
        match += 1 if length == len(expected_balls) else 0

    return match / num_experiments