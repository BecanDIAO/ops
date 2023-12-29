import json

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse


class ResultMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)

        json_content = response.content

        try:
            data = json.loads(json_content)
        except (json.JSONDecodeError, TypeError):
            data = {}

        result_data = {"result": data}
        response.content = JSONResponse(content=result_data).body
        return response
