from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import Employee
from ..schemas import EmployeeCreate, EmployeeResponse
from ..auth import verify_token

router = APIRouter(prefix="/api/employees", tags=["Employees"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", status_code=201, response_model=EmployeeResponse)
def create_employee(emp: EmployeeCreate, db: Session = Depends(get_db), token=Depends(verify_token)):
    if db.query(Employee).filter(Employee.email == emp.email).first():
        raise HTTPException(status_code=400, detail="Email already exists")

    employee = Employee(**emp.dict())
    db.add(employee)
    db.commit()
    db.refresh(employee)
    return employee

@router.get("/", response_model=list[EmployeeResponse])
def list_employees(
    page: int = 1,
    department: str | None = None,
    role: str | None = None,
    db: Session = Depends(get_db),
    token=Depends(verify_token)
):
    query = db.query(Employee)

    if department:
        query = query.filter(Employee.department == department)
    if role:
        query = query.filter(Employee.role == role)

    return query.offset((page - 1) * 10).limit(10).all()

@router.get("/{id}", response_model=EmployeeResponse)
def get_employee(id: int, db: Session = Depends(get_db), token=Depends(verify_token)):
    emp = db.query(Employee).get(id)
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return emp

@router.put("/{id}", response_model=EmployeeResponse)
def update_employee(id: int, emp: EmployeeCreate, db: Session = Depends(get_db), token=Depends(verify_token)):
    employee = db.query(Employee).get(id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    for key, value in emp.dict().items():
        setattr(employee, key, value)

    db.commit()
    return employee

@router.delete("/{id}", status_code=204)
def delete_employee(id: int, db: Session = Depends(get_db), token=Depends(verify_token)):
    employee = db.query(Employee).get(id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    db.delete(employee)
    db.commit()
