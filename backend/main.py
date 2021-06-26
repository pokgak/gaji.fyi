from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "Welcome to gaji.fyi!"}


@app.post("/companies/", response_model=schemas.Company)
def create_company(company: schemas.CompanyCreate, db: Session = Depends(get_db)):
    db_company = crud.get_company_by_name(db, company_name=company.name)
    if db_company:
        raise HTTPException(status_code=400, detail="Company already registered")
    return crud.create_company(db=db, company=company)


@app.get("/companies/", response_model=List[schemas.Company])
def read_companies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    companies = crud.get_companies(db, skip=skip, limit=limit)
    return companies


@app.get("/companies/{company_id}", response_model=schemas.Company)
def read_company(company_id: int, db: Session = Depends(get_db)):
    db_company = crud.get_company(db, company_id=company_id)
    if db_company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    return db_company


@app.post("/companies/{company_id}/salaries/", response_model=schemas.Salary)
def create_salary_for_company(
    company_id: int, salary: schemas.SalaryCreate, db: Session = Depends(get_db)
):
    db_company = crud.get_company(db, company_id=company_id)
    if db_company is None:
        raise HTTPException(
            status_code=404, detail=f"Company with ID {company_id} not found"
        )
    return crud.create_company_salary(db=db, salary=salary, company_id=company_id)


@app.get("/salaries/", response_model=List[schemas.Salary])
def read_salaries(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    salaries = crud.get_salaries(db, skip=skip, limit=limit)
    return salaries
