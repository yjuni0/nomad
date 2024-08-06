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
        print(f"{self.team_name} get {new_player.xp} points")

    def remove_player(self, name):
        player_to_remove = None
        for player in self.players:
            if player.name == name:
                player_to_remove = player
                break
        if player_to_remove:
            self.players.remove(player_to_remove)
            print(f"{self.team_name} lost {player_to_remove.xp} point.")
        else:
            print(f"Player {name} not found.")

    def total_xp(self):
        total_xp = sum(player.xp for player in self.players)
        print(f"{self.team_name} total XP: {total_xp} points")
        return total_xp

# 팀 생성
team_red = Team("Team RED")
team_blue = Team("Team BLUE")

# 플레이어 추가 및 제거 기능


def manage_team(team):
    while True:
        action = input("player 추가, 삭제, 정지: ").strip().lower()
        if action == "추가":
            name = input("이름을 입력하세요.: ").strip()
            xp = int(input("player의 xp를 입력해주세요.: ").strip())
            team.add_player(name, xp)
        elif action == "삭제":
            name = input("이름을 입력해주세요.: ").strip()
            team.remove_player(name)
        elif action == "정지":
            break
        else:
            print("잘못 입력했습니다. player 추가, 삭제, 정지를 선택해주세요.")

def choice():
    while True:
        team_choice = input("팀을 선택해주세요 레드, 블루, 정지: ")
        if team_choice == "레드":
            manage_team(team_red)
        elif team_choice == "블루":
            manage_team(team_blue)
        elif team_choice == "정지":
            break
        else:
            print("잘못 입력했습니다. 팀을 선택해주세요 레드, 블루, 정지")            

    # 팀 XP 계산 및 결과 출력
    red_xp = team_red.total_xp()
    blue_xp = team_blue.total_xp()

    if red_xp < blue_xp:
        print("WINNER is team_blue!")
    elif red_xp > blue_xp:
        print("WINNER is team_red!")
    else:
        print("Draw!")

if __name__ == "__main__":
    choice()