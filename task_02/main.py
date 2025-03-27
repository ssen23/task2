from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

#모델 정의
class Explorer(BaseModel):
    id: int  # 탐험가의 고유 번호
    name: str  # 탐험가의 이름
    rank: str  # 탐험가의 계급 (예: 대위, 부함장 등)
    assignment: str  # 탐험가의 소속함선 (예: USS Enterprise)
    species: str  # 탐험가의 종족 (예: 인간, 벌칸 등)

class Alien(BaseModel):
    id: int
    name: str
    species: str
    homeworld: str
    affiliation: str

#데이터베이스 역할, 각 목록을 저장하는 빈 리스트
explorers_db = []
aliens_db = []

#FastAPI 애플리케이션에 여러 가지 HTTP 요청(GET, POST, PUT, DELETE)을 처리하는 엔드포인트를 설정

@app.get("/") #생성
async def read_root():
    return {"message": "Welcome to the Starfleet Data Management System!"}

@app.post("/explorers/") 
async def create_explorer(explorer: Explorer):
    explorers_db.append(explorer)
    return explorer

@app.get("/explorers/", response_model=List[Explorer]) 
async def get_explorers():
    return explorers_db

@app.get("/explorers/{explorer_id}", response_model=Explorer)
async def get_explorer(explorer_id: int):
    for explorer in explorers_db:
        if explorer.id == explorer_id:
            return explorer
    return {"error": "Explorer not found"}

@app.put("/explorers/{explorer_id}", response_model=Explorer)
async def update_explorer(explorer_id: int, explorer: Explorer):
    for index, existing_explorer in enumerate(explorers_db):
        if existing_explorer.id == explorer_id:
            explorers_db[index] = explorer
            return explorer
    return {"error": "Explorer not found"}

@app.delete("/explorers/{explorer_id}")
async def delete_explorer(explorer_id: int):
    for index, explorer in enumerate(explorers_db):
        if explorer.id == explorer_id:
            explorers_db.pop(index)
            return {"message": "Explorer deleted"}
    return {"error": "Explorer not found"}

@app.post("/aliens/")
async def create_alien(alien: Alien):
    aliens_db.append(alien)
    return alien

@app.get("/aliens/", response_model=List[Alien])
async def get_aliens():
    return aliens_db

@app.get("/aliens/{alien_id}", response_model=Alien)
async def get_alien(alien_id: int):
    for alien in aliens_db:
        if alien.id == alien_id:
            return alien
    return {"error": "Alien not found"}

@app.put("/aliens/{alien_id}", response_model=Alien)
async def update_alien(alien_id: int, alien: Alien):
    for index, existing_alien in enumerate(aliens_db):
        if existing_alien.id == alien_id:
            aliens_db[index] = alien
            return alien
    return {"error": "Alien not found"}

@app.delete("/aliens/{alien_id}")
async def delete_alien(alien_id: int):
    for index, alien in enumerate(aliens_db):
        if alien.id == alien_id:
            aliens_db.pop(index)
            return {"message": "Alien deleted"}
    return {"error": "Alien not found"}