class Chip:
    def __init__(self):
        self.total = 100
        self.bet = 0
    def win_bet(self):
        try: 
            self.total += self.bet
        except:
            print('error occured, make sure bet is an int')
        finally:
            print(f'The new chip count is {self.total}')
    def lose_bet(self):
        try:
            self.total -= self.bet
        except:
            print('error occured, make sure bet is an int')
        finally:
            print(f'The new chip count is {self.total}')