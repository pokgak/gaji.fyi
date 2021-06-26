from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import JSON

from .database import Base


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    country = Column(String)
    # address = Column(JSON)

    salaries = relationship("Salary", back_populates="company")


class Salary(Base):
    __tablename__ = "salaries"

    id = Column(Integer, primary_key=True, index=True)
    currency = Column(String)
    amount = Column(Integer)
    company_id = Column(Integer, ForeignKey("companies.id"))

    company = relationship("Company", back_populates="salaries")
