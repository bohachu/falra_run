import uvicorn
from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles


def init_app():
    global app
    app = FastAPI()
    app.add_middleware(CORSMiddleware,
                       allow_origins=['*'],
                       allow_credentials=True,
                       allow_methods=['*'],
                       allow_headers=['*'])
    Path('web').mkdir(parents=True, exist_ok=True)
    app.mount('/web', StaticFiles(directory='web'), name='web')


init_app()


@app.get('/')
def root():
    return "Hi Falra!"


@app.post("/api/falra_run/")
async def falra_run(request: Request):
    return await request.json()


# uvicorn falra_run.falra_run:app --port 8000
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
