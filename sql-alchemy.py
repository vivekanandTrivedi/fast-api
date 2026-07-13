from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from fastapi import FastAPI, Depends

DATABASE_URL = "sqlite:///./test.db"
app = FastAPI()

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)
Session = sessionmaker(bind=engine)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String)
    email = Column(String)

Base.metadata.create_all(engine)

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

@app.get("/users")
def read_roots(db: Session = Depends(get_db)):
    return {
        "message": "success"
    }

@app.post("/users")
def create_users(name : str, db: Session = Depends(get_db)):
    user = User(name=name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return {
        "message": "success",
    }