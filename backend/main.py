from config import API_HOST, API_PORT, API_PREFIX, API_SECURITY_CORS, API_TITLE, STATIC_FILES, STATIC_FILES_DIRECTORY
import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware


from router.recipe_router import recipe_router

app = FastAPI(title=API_TITLE)

origins = [
    API_SECURITY_CORS
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # or specific domains
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.mount(STATIC_FILES_DIRECTORY, StaticFiles(directory=STATIC_FILES), name=STATIC_FILES)
app.include_router(router=recipe_router, prefix=API_PREFIX)


if __name__ == '__main__':
    uvicorn.run(app, host=API_HOST, port=API_PORT, reload=True)
