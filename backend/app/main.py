import json

from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import ResponseValidationError
from fastapi.responses import PlainTextResponse, JSONResponse
from starlette import status

from api.auth import auth

app=FastAPI(
    title="Transit-app",
    description="this is an api for a backend of management folder for a transit app",

)
app.include_router(auth)

"""
 this three methods permed to verify the endpoint of url and 
 if the data which pass on url are valid 
"""
@app.exception_handler(HTTPException)
async def http_handler(request,exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "message":"Oops! Something went wrong in your url"
        }
    )
@app.exception_handler(ResponseValidationError)
async def validation_exception_handler(request:Request,exc:ResponseValidationError):
    return PlainTextResponse(
        "this is a plain text response: "f"\n  {json.dumps(exc.errors(),indent=2)}",
        status_code=status.HTTP_400_BAD_REQUEST,
    )
@app.get("/error_endpoint")
async def raise_exception():
    raise HTTPException(status_code=400)


if __name__=="__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True)
