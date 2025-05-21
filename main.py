import uvicorn

from fastapi import FastAPI
from fastapi.responses import FileResponse

home = FastAPI()


@home.get('/', response_class=FileResponse)
async def root():
    return 'templates/home/index.html'

if __name__ == '__main__':
    uvicorn.run(home,
                host='127.0.0.1',
                port=80)
