from pydantic import BaseModel

class APIOutput(BaseModel): #we have to define it in post method of detect
    emotion: str
    time_elapsed: float
    time_elapsed_preprocess: float
    # time_elapsed_loading: float