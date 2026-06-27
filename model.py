import random
from arcengine import GameAction, GameState
import arc_agi

arc = arc_agi.Arcade(arc_api_key="b1f4c3e3-4049-4f13-a333-7d79ac3f9ebc")

env = arc.make("ls20", render_mode="human")
if env is None:
    print("Failed to create environment")
    exit(1)

for step in range(100):
    action = random.choice(env.action_space)
    action_data = {}
    if action.is_complex():
        action_data = {
            "x": random.randint(0, 63),
            "y": random.randint(0, 63),
        }        
        
    obs = env.step(action, data=action_data)
    
    if obs and obs.state == GameState.WIN:
        print(f"Game won at step {step}!")
        break
    elif obs and obs.state == GameState.GAME_OVER:
        env.reset()

scorecard = arc.get_scorecard()
if scorecard:
    print(f"Final Score: {scorecard.score}")