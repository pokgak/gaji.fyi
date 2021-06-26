from enum import Enum
from typing import Optional, List
from pydantic import BaseModel


class SalaryBase(BaseModel):
    currency: str
    amount: int


class SalaryCreate(SalaryBase):
    pass


class Salary(SalaryBase):
    id: int
    company_id: int

    class Config:
        orm_mode = True


class CompanyBase(BaseModel):
    name: str
    country: str


class CompanyCreate(CompanyBase):
    pass


class Company(CompanyBase):
    id: int
    salaries: List[Salary] = []

    class Config:
        orm_mode = True
