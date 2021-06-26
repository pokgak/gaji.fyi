from sqlalchemy.orm import Session

from . import models, schemas


def get_company(db: Session, company_id: int):
    return db.query(models.Company).filter(models.Company.id == company_id).first()


def get_company_by_name(db: Session, company_name: str):
    return db.query(models.Company).filter(models.Company.name == company_name).first()


def get_companies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Company).offset(skip).limit(limit).all()


def create_company(db: Session, company: schemas.CompanyCreate):
    db_company = models.Company(name=company.name, country=company.country)
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company


def get_salaries(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Salary).offset(skip).limit(limit).all()


def create_company_salary(db: Session, salary: schemas.SalaryCreate, company_id: int):
    db_salary = models.Salary(**salary.dict(), company_id=company_id)
    db.add(db_salary)
    db.commit()
    db.refresh(db_salary)
    return db_salary
