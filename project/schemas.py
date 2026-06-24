from pydantic import BaseModel

class WorkoutCreate(BaseModel):
    exercise: str
    duration: int
    calories: int
    notes: str

class WorkoutResponse(WorkoutCreate):
    id: int

    class Config:
        from_attributes = True