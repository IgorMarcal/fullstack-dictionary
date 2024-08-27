from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Configuração do banco de dados
DATABASE_URL = os.getenv("DATABASE_URL", "mysql+mysqlconnector://user:password@localhost/dbname")

# Criação do engine
engine = create_engine(DATABASE_URL, echo=True)

# Criação da base
Base = declarative_base()

# Criação da sessão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
