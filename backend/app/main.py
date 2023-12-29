from fastapi import FastAPI
# from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from .api.api_v1.api import api_router
from .core.config import settings

from .database.db import Base
from .database.engine import engine

# from .middleware import ResultMiddleware

# middleware = [
#     Middleware(ResultMiddleware)
# ]

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    # middleware=middleware,
)

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=[""],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_V1_STR)


@app.on_event("startup")
async def startup():
    Base.metadata.create_all(bind=engine)


# 创建一个基础的响应模型
class BaseResponseModel(BaseModel):
    result: dict


# 路由处理程序
@app.get("/example", response_model=BaseResponseModel)
async def example():
    data = {"message": "Hello, World!"}
    return {"result": data}

