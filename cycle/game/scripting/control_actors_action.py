import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlActorsAction(Action):
    """
    An input action that controls the cycle.
    
    The responsibility of ControlActorsAction is to get the direction and move the cycle's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(constants.CELL_SIZE, 0)

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # left
        left1 = self._keyboard_service.is_key_down('a')
        if left1:
            self._direction = Point(-constants.CELL_SIZE, 0)
        
        # right
        right1 = self._keyboard_service.is_key_down('d')
        if right1:
            self._direction = Point(constants.CELL_SIZE, 0)
        
        # up
        up1 = self._keyboard_service.is_key_down('w')
        if up1:
            self._direction = Point(0, -constants.CELL_SIZE)
        
        # down
        down1 = self._keyboard_service.is_key_down('s')
        if down1:
            self._direction = Point(0, constants.CELL_SIZE)

        # left
        left2 = self._keyboard_service.is_key_down('j')
        if left2:
            self._direction = Point(-constants.CELL_SIZE, 0)
        
        # right
        right2 = self._keyboard_service.is_key_down('l')
        if right2:
            self._direction = Point(constants.CELL_SIZE, 0)
        
        # up
        up2 = self._keyboard_service.is_key_down('i')
        if up2:
            self._direction = Point(0, -constants.CELL_SIZE)
        
        # down
        down2 = self._keyboard_service.is_key_down('k')
        if down2:
            self._direction = Point(0, constants.CELL_SIZE)
        
        if left1 or right1 or up1 or down1:
            p1 = cast.get_first_actor("cycles")
            p1.turn_head(self._direction)
        elif left2 or right2 or up2 or down2:
            p2 = cast.get_actors("cycles")[1]
            p2.turn_head(self._direction)
        