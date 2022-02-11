from typing import List, Dict, Optional


class Actor:

    def __init__(self, 
        name: str,                                          # The name of the actor
        activity_experience: Optional[Dict[str, int]]=None, # The number of times they did an activity
        workmate_experience: Optional[Dict[str, int]]=None  # The number of times they worked with someone
        ) -> None:
        
        self.name = name
        self.activity_experience = {} if activity_experience is None else activity_experience
        self.workmate_experience = {} if workmate_experience is None else workmate_experience

    def __str__(self) -> str:
        return f"Name: {self.name}, Act_Exp: {self.activity_experience}, Wor_Exp: {self.workmate_experience}" 


class Task:

    def __init__(self, 
        id: str,
        activity: str,
        actors: Optional[List[Actor]]=None
        ) -> None:
        
        self.id = id
        self.activity = activity
        self.actors = [] if actors is None else actors
        self.updated_activity_actors: List[Actor] = []          # Actors whose activities we already updated
        
        if len(self.actors) > 0: self._update_actors()

    def _update_actor_relationships(self):
        for actor_to_update in self.actors:
            for other_actor in self.actors:
                if other_actor == actor_to_update:
                    continue                                    # One does not have a working relationship with themselves
                if other_actor.name in actor_to_update.workmate_experience.keys():
                    actor_to_update.workmate_experience[other_actor.name] += 1
                else:
                    actor_to_update.workmate_experience[other_actor.name] = 1
    
    def _update_actor_activities(self):
        for actor in self.actors:
            if actor in self.updated_activity_actors:
                continue                                        # Making sure we do not increase this multiple times
            if self.activity in actor.activity_experience.keys():
                actor.activity_experience[self.activity] += 1
            else:
                actor.activity_experience[self.activity] = 1
            self.updated_activity_actors.append(actor)

    def _update_actors(self):
        self._update_actor_activities()
        self._update_actor_relationships()

    def add_actor(self, actor: Actor) -> None:
        if actor in self.actors: 
            return
        self.actors.append(actor)
        self._update_actors()

    def add_actors(self, actors: List[Actor]) -> None:
        for actor in actors: self.add_actor(actor)


def test():
    actor_names = ('Krisz', 'Marci', 'Bea', 'Robi')
    arr = []
    for name in actor_names:
        arr.append(Actor(name=name))

    task1 = Task('task1', 'rendering', [arr[1], arr[3]])
    task2 = Task('task2', 'painting', [arr[0], arr[3]])
    task3 = Task('task3', 'painting')
    task3.add_actor(arr[2])
    task3.add_actor(arr[3])

    for actor in arr:
        print(actor)


if __name__ == "__main__":
    test()
