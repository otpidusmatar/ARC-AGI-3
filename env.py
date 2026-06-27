import arc_agi
from arcengine import GameAction

arc = arc_agi.Arcade(arc_api_key="b1f4c3e3-4049-4f13-a333-7d79ac3f9ebc")
env = arc.make("ls20", render_mode="human")

# Take a few actions
for _ in range(100):
    env.step(GameAction.ACTION1)

print(arc.get_scorecard())