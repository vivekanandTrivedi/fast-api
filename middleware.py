from fastapi import FastAPI, Request
import time
app = FastAPI()

@app.middleware("http")
async def my_middleware(request: Request, call_next):
    print("Request received")

    response = await call_next(request)

    print("Response sent")
    return response

@app.middleware("http")

async def time_track(request: Request, call_next):
    start_time = time.time()

    response = await call_next(request)

    process_time = time.time() - start_time

    print({f"process_time: {process_time} | path : {request.url.path}"})
    return response