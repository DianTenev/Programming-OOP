from project.player import Player
from project.team import Team

p = Player("Dian", 99, 90, 78, 83)
print("Player name:", p.name)
print("Points sprint:", p._Player__sprint)
print("Points dribble:", p._Player__dribble)
print("Points passing:", p._Player__passing)
print("Points shooting:", p._Player__shooting)
print("\ncalling the __str__ method")
print(p)
print("\nAbout the team")
t = Team("Juventus", 99)
print("Team name:", t._Team__name)
print("Teams points:", t._Team__rating)
print("Teams players:", len(t._Team__players))
print(t.add_player(p))
print(t.add_player(p))
print("Teams players:", len(t._Team__players))
print(t.remove_player("Dian"))
print(t.remove_player("Dian"))