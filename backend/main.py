from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from mysql import init_db, get_user

app = FastAPI()
init_db()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development; adjust in production
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

class User(BaseModel):
    email: str
    password: str  

@app.post("/login")
async def login(user: User):
    user_re = get_user(user.email, user.password)
    print(type(user_re))
    print(user_re[1])

    if user_re[1] == "kien@example.com":
        return {"message": f"Successful Login with {user_re}"}
    raise HTTPException(status_code=401, detail="Login Info is Wrong")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
