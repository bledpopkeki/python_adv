from sqlalchemy.orm import Session
from models import Workout
from schemas import WorkoutCreate

def create_workout(db: Session, workout: WorkoutCreate):
    db_workout = Workout(**workout.dict())
    db.add(db_workout)
    db.commit()
    db.refresh(db_workout)
    return db_workout

def get_workouts(db: Session):
    return db.query(Workout).all()

def get_workout(db: Session, workout_id: int):
    return db.query(Workout).filter(
        Workout.id == workout_id
    ).first()

def update_workout(
    db: Session,
    workout_id: int,
    workout: WorkoutCreate
):
    db_workout = get_workout(db, workout_id)

    if not db_workout:
        return None

    db_workout.exercise = workout.exercise
    db_workout.duration = workout.duration
    db_workout.calories = workout.calories
    db_workout.notes = workout.notes

    db.commit()
    db.refresh(db_workout)

    return db_workout

def delete_workout(
    db: Session,
    workout_id: int
):
    db_workout = get_workout(db, workout_id)

    if not db_workout:
        return None

    db.delete(db_workout)
    db.commit()

    return db_workout