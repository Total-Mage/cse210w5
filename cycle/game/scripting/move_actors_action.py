from game.scripting.action import Action


# TODO: Implement MoveActorsAction class here! 

# Override the execute(cast, script) method as follows:
# 1) get all the actors from the cast
# 2) loop through the actors
# 3) call the move_next() method on each actor

class MoveActorsAction():
    # def __init__(self):
    #     pass

    def execute(self, cast, script):
        actor_list = cast.get_all_actors()

        for actor in actor_list:
            actor.move_next()