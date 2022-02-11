from random import randint, uniform
from typing import Optional, List
from utils.activity_log import Actor


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

        actor = Actor(ACTORS[randint(0, len(ACTORS) - 1)])
        activity = ACTIVITIES[randint(0, len(ACTIVITIES) - 1)]
        return ActivityGenerator.generate_activity(actor=actor.name, activity=activity)

