from fastapi import FastAPI

from app.routers import user

app = FastAPI()

# Dynamically include routers with their prefixes
routers = [
    (user.router, "/api/users"),

]

for router, prefix in routers:
    app.include_router(router, prefix=prefix)

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}
