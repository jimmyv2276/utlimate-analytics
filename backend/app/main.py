from fastapi import FastAPI
from app.api import health, teams, players, games, events

app = FastAPI(title="Ulti Analytics API")

# Register routers
app.include_router(health.router)
app.include_router(teams.router)
app.include_router(players.router)
app.include_router(games.router)
app.include_router(events.router)

