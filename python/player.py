class Player:
    def __init__(self, name, team, xp):
        self.name = name
        self.team = team
        self.xp = xp

    def introduce(self):
        print(f"Hello I'm {self.name} and I play for {self.team}")

class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []

    def show_players(self):
        for player in self.players:
            player.introduce()

    def add_player(self, name, xp):
        new_player = Player(name, self.team_name, xp)
        self.players.append(new_player)
        print(f"{self.team_name} get {new_player.xp} point")

    def remove_player(self, name):
        for player in self.players:
            if player.name == name:
                self.players.remove(player)
                print(f"{self.team_name} lost {player.xp} points")
                break

    def total_xp(self):
        total_xp = sum(player.xp for player in self.players)
        print(f"{self.team_name} total XP: {total_xp} points")
        return total_xp

# 팀 생성 및 플레이어 추가
team_red = Team("Team RED")
team_blue = Team("Team BLUE")

team_red.add_player("YE", 1500)
team_red.add_player("JUN", 200)
team_blue.add_player("OH", 500)
team_blue.add_player("ye", 400)
team_blue.add_player("jun", 500)


# 플레이어 제거
team_blue.remove_player("jun")
team_red.remove_player("YE")
# 팀 XP 계산 및 결과 출력
red_xp = team_red.total_xp()
blue_xp = team_blue.total_xp()

if red_xp < blue_xp:
    print("WINNER is team_blue!")
elif red_xp > blue_xp:
    print("WINNER is team_red!")
else:
    print("Draw!")