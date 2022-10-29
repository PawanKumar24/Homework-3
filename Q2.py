# Pawan Kumar
# ID: 2046222

class Team:
    def init(self):
        self.team_name = 'none'
        self.team_wins = 0
        self.team_losses = 0
        
    def setTeamData(self, name, win, loss):
        self.team_name = name
        self.team_wins = win
        self.team_losses = loss
        
    def get_win_percentage(self):
        return float(self.team_wins / (self.team_wins + self.team_losses))
    def printResults(self):
        if self.team_wins>self.team_losses:
            print(f'Congratulations, Team {self.team_name} has a winning average!')
        elif self.team_wins<self.team_losses:
            print(f'Team {self.team_name} has a losing average.')
    


if __name__ == '__main__':
    name = str(input())
    wins = int(input())
    loss = int(input())

    team1 = Team()
    team1.setTeamData(name, wins, loss)
    team1.printResults()
    
