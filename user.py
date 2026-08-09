import arc_agi
from arcengine import GameAction

arc = arc_agi.Arcade(arc_api_key="b1f4c3e3-4049-4f13-a333-7d79ac3f9ebc")
env = arc.make("ls20", render_mode="human")

# Take a few actions
for _ in range(20):
    action = int(input("Pick a number from 1 to 8"))
    match action:
        case 1: env.step(GameAction.ACTION1)
        case 2: env.step(GameAction.ACTION2)
        case 3: env.step(GameAction.ACTION3)
        case 4: env.step(GameAction.ACTION4)
        case 5: env.step(GameAction.ACTION5)
        case 7: env.step(GameAction.ACTION7)
        case 8: env.step(GameAction.RESET)
        case 6: 
            x = int(input("Coord 1 x from 0 to 63"))
            y = int(input("Coord 1 y from 0 to 63"))
            env.step(GameAction.ACTION6, data={"x": x, "y": y})

print(arc.get_scorecard())