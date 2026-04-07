from fastapi import FastAPI
import uvicorn
from app.env import LoanEnv, LoanAction

app = FastAPI()
env = LoanEnv()

@app.get("/")
def home():
    return {"message": "LoanWise OpenEnv is running 🚀"}

@app.post("/reset")
async def reset():
    result = await env.reset()
    return result.model_dump()


@app.post("/step")
async def step(action: dict):
    action_obj = LoanAction(**action)
    result = await env.step(action_obj)
    return result.model_dump()


#  REQUIRED main() function
def main():
    uvicorn.run("server.app:app", host="0.0.0.0", port=8000)


#  REQUIRED for validation
if __name__ == "__main__":
    main()