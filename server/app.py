from fastapi import FastAPI
import uvicorn
from app.env import LoanEnv, LoanAction

app = FastAPI()
env = LoanEnv()


#  Root endpoint (for UI)
@app.get("/")
def home():
    return {"message": "LoanWise OpenEnv is running 🚀"}


#  Allow both GET + POST (helps testing + avoids 405)
@app.api_route("/reset", methods=["GET", "POST"])
async def reset():
    result = await env.reset()
    return result.model_dump()


#  Allow both GET + POST
@app.api_route("/step", methods=["GET", "POST"])
async def step(action: dict = {}):
    action_obj = LoanAction(**action) if action else LoanAction(risk_level="low", decision="approve")
    result = await env.step(action_obj)
    return result.model_dump()


#  REQUIRED main() function (FIXED PORT)
def main():
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)


#  REQUIRED for validation
if __name__ == "__main__":
    main()