import io
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from audiocraft.models import MusicGen
import torch

import soundfile as sf

musicgen_model = {}

# Load the MusicGen model at startup
@asynccontextmanager
async def lifespan(app: FastAPI):
    musicgen_model["music"] = MusicGen.get_pretrained('facebook/musicgen-small')
    yield
    musicgen_model.clear()

app = FastAPI(lifespan=lifespan)

class MusicRequest(BaseModel):
    prompt: str

@app.get("/dummy")
def read_dummy():
    return {"message": "Hello from dummy endpoint!"}

# @app.post("/music")
# def generate_music(request: MusicRequest):
#     # Set generation parameters
#     musicgen_model["music"].set_generation_params(duration=5)
    
#     # Generate audio from text prompt
#     with torch.no_grad():
#         generated_audio = musicgen_model["music"].generate([request.prompt])
    
#     # Convert tensor to WAV format
#     audio_tensor = generated_audio[0].cpu().numpy()
#     sample_rate = 32000  # MusicGen uses 32kHz
#     wav_buffer = io.BytesIO()
#     sf.write(wav_buffer, audio_tensor.T, sample_rate, format='WAV')
#     wav_buffer.seek(0)
    
#     return StreamingResponse(wav_buffer, media_type="audio/wav")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
