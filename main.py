from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()

@app.get("/dummy")
def read_dummy():
    return {"message": "Hello from dummy endpoint!"}


@app.get("/music")
def get_music():
    def file_iterator():
        with open("dummy_music.wav", "rb") as file:
            yield from file
    return StreamingResponse(file_iterator(), media_type="audio/wav")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
