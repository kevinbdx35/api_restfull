# import threading
from src.api.repositories.exercice_repository import ExerciceRepository
from src.api.models.exercises import Exercise


class ExerciseServices:
    # _instance = None
    # _lock = threading.Lock()
    #
    # def __new__(cls, *args, **kwargs):
    #     if not cls._instance:
    #         with cls._lock:
    #             if cls._instance is None:
    #                 cls._instance = super(ExerciseServices, cls).__new__(cls)
    #     return cls._instance

    def __init__(self):
        self.repository = ExerciceRepository()

    def save_exercice(self, title, signature, test_filepath, timestamp, description=None):
        return self.repository.save(Exercise(title, description, signature, test_filepath, timestamp))
