from sqlalchemy import Column, Integer, String
from database import Base

class Workout(Base):
    __tablename__ = "workouts"

    id = Column(Integer, primary_key=True, index=True)
    exercise = Column(String, nullable=False)
    duration = Column(Integer)  # minutes
    calories = Column(Integer)
    notes = Column(String)