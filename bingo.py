def PromptNb(mini, maxi) :
    nb = input(f"Please enter a number between {mini} and {maxi} :\n")
    while not nb.isnumeric() or not mini <= int(nb) or not int(nb) <= maxi :
        nb = input(f"Please enter a number between {mini} and {maxi} and not a word :\n")
    return int(nb)

class Bingo :
    def __init__(self, board=None) :
        self.board = board if board else [[(0, False)]*5 for _ in range(5)]
        if not board :
            self.fill()

    def fill(self) :
        limits = [(1, 19), (20, 39), (40, 59), (60, 79), (80, 99)]
        for i in range(5) :
            for j in range(5) :
                print(self)
                if i == 2 and j == 2 :
                    self.board[2][2] = (0, True)
                else :
                    self.board[j][i] = (PromptNb(limits[i][0], limits[i][1]), False)

    def __str__(self) :
        s = ""
        for line in self.board :
            for n, b in line :
                s += ' | ' + (' ' if n < 10 else '') + str(n)
            s += ' |'
            s += '\t'
            for n, b in line :
                s += ' | ' + ('x' if b else ' ')
            s += ' |\n'
        return s
    def __repr__(self):
        return self.__str__()

    def check_nb(self, nb) :
        self.board = [[(n, False) if not b and nb != n else (n, True) for n, b in line] for line in self.board]

    def GetNext(self) :
        self.check_nb(PromptNb(1, 99))

    def Isdone(self) :
        for line in self.board :
            done = True
            for n, b in line :
                done &= b
            if done :
                return done
        for i in range(5) :
            done = True
            for j in range(5) :
                n, b = self.board[j][i]
                done &= b
            if done :
                return done
        return False

    def play(self) :
        while True :
            print(self)
            if self.Isdone() :
                print("Congratulation, you win !!")
                return True
            else :
                self.GetNext()
