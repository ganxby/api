from fastapi import FastAPI, Cookie
from fastapi.middleware.cors import CORSMiddleware

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
async def delete_task_by_id(url: str, SVSENDS_UID: str | None = Cookie(default=None)):
    if url:
        try:
            new_url = '/' + url.split('/', 1)[1]

            if "'" in new_url:
                return 'invalid data'

            if SVSENDS_UID:
                if "'" in SVSENDS_UID:
                    return 'invalid data'

                else:
                    services.save_data(SVSENDS_UID, new_url)

                    return 200

        except IndexError:
            return 'invalid url'

        return 'no SVSENDS_UID cookie'

    return 'no url'
