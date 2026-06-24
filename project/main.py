from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

import models
import crud

from database import (
    engine,
    SessionLocal
)

from schemas import (
    WorkoutCreate,
    WorkoutResponse
)

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Workout Tracker API"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post(
    "/workouts",
    response_model=WorkoutResponse
)
def create_workout(
    workout: WorkoutCreate,
    db: Session = Depends(get_db)
):
    return crud.create_workout(db, workout)

@app.get(
    "/workouts",
    response_model=list[WorkoutResponse]
)
def get_workouts(
    db: Session = Depends(get_db)
):
    return crud.get_workouts(db)

@app.get(
    "/workouts/{workout_id}",
    response_model=WorkoutResponse
)
def get_workout(
    workout_id: int,
    db: Session = Depends(get_db)
):
    workout = crud.get_workout(
        db,
        workout_id
    )

    if not workout:
        raise HTTPException(
            status_code=404,
            detail="Workout not found"
        )

    return workout

@app.put(
    "/workouts/{workout_id}",
    response_model=WorkoutResponse
)
def update_workout(
    workout_id: int,
    workout: WorkoutCreate,
    db: Session = Depends(get_db)
):
    updated = crud.update_workout(
        db,
        workout_id,
        workout
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Workout not found"
        )

    return updated

@app.delete("/workouts/{workout_id}")
def delete_workout(
    workout_id: int,
    db: Session = Depends(get_db)
):
    deleted = crud.delete_workout(
        db,
        workout_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Workout not found"
        )

    return {
        "message": "Workout deleted successfully"
    }

@app.get("/stats/total-calories")
def total_calories(
    db: Session = Depends(get_db)
):
    workouts = crud.get_workouts(db)

    total = sum(
        workout.calories
        for workout in workouts
    )

    return {
        "total_calories": total
    }

@app.get("/stats/total-duration")
def total_duration(
    db: Session = Depends(get_db)
):
    workouts = crud.get_workouts(db)

    total = sum(
        workout.duration
        for workout in workouts
    )

    return {
        "total_minutes": total
    }