from fastapi import FastAPI, status, Request, Response
from fastapi.middleware.cors import CORSMiddleware

from urllib.parse import urlparse

import services


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/v1/{track}")
async def redirect_handler(url: str, request: Request):
    if url:
        parsed = urlparse(url)
        new_url = "%s://" % parsed.scheme + parsed.netloc
        result = parsed.geturl().replace(new_url, '')

        if 'SVSENDS_UID' in request.cookies:
            services.save_data(request.cookies['SVSENDS_UID'], result)

            return Response(status_code=status.HTTP_200_OK, content="OK")

        return Response(status_code=status.HTTP_400_BAD_REQUEST, content="INVALID UID")

    return Response(status_code=status.HTTP_400_BAD_REQUEST, content="INVALID URL")
