from fastapi import FastAPI

app = FastAPI()

@app.get("/dummy")
def read_dummy():
    return {"message": "Hello from dummy endpoint!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
