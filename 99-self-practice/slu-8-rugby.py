class Player:
    def __init__(self):
        self.offside: bool = False
        # needs to be called "x" for tests. Otherwise a
        # name like "position" would be better
        self.x: float = 0
        self.team: list = []

    def move(self, dx):
        # if already offside and continues moving forward, then foul play
        if self.offside and dx > 0:
            print("Foul")

        # move player
        self.x += dx

        # "When an onside player ends up in front of an offside player,
        # then this other player becomes onside again"
        if self.offside:
            for player in self.team:
                if (player.x > self.x) and (not player.offside):
                    self.offside = False

        # if player is onside, make all players behind onside
        else:
            for player in self.team:
                if player.x < self.x:
                    player.offside = False
        

    def tackling_or_kick(self):
        # not allowed to tackle or kick when offside
        if self.offside:
            print("Foul")
        
        # "If a player kicks the ball, tackles another player or is tackled,
        # then all teammates in front of the player become offside"
        for player in self.team:
            if player.x > self.x:
                player.offside = True


    def catch_ball(self):
        # not allowed to catch when offside
        if self.offside:
            print("Foul")

def initialise_team(n):
    team = []

    for _ in range(n):
        team.append(Player())

    for player in team:
        player.team = team

    return team