from random import randint, uniform
from utils.general_utils import int_to_string as its, CustomError
from typing import Optional, Tuple, List


ACTIVITIES = ('floor covering', 'rendering', 'painting')
ACTORS = ('Paula', 'Robert', 'Allen', 'Deloris', 'Brody')


class ActivityGenerator:

    @staticmethod
    def generate_activity(
        actor: str='Paula', 
        activity: str='rendering', 
        taskID: Optional[str]=None, 
        profit: float=0) -> List[str]:
        
        t_id = taskID
        if t_id is None:
            t_id = f"{activity[0]}{randint(1, 1000)}"
        return [actor, activity, t_id, profit]

    @staticmethod
    def generate_random_activity():

        actor = ACTORS[randint(0, len(ACTORS) - 1)]
        activity = ACTIVITIES[randint(0, len(ACTIVITIES) - 1)]
        profit = round(uniform(0, 10), 2)
        return ActivityGenerator.generate_activity(actor=actor, activity=activity, profit=profit)
