from game import Game
from scripts.random_generator.create_random_world import CreateRandomWorld
from save_load_game import save_game_to_json

world = CreateRandomWorld().create_world()
save_game_to_json(world, "teste_create_world.json")
