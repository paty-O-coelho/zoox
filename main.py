from fastapi import FastAPI
from core.configs import settings
from api.api import api_router

app = FastAPI(title="Cadastros", version="0.1.0")
app.include_router(api_router, prefix=settings.API_V1_STR)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000,
                log_level="info",reload=True,)


# @app.get("/")
# async def raiz():
#     return {"message": "Hello World"}


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True,
#                 log_level="info")