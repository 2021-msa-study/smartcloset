import asyncio

from fastmsa.command import FastMSACommand
from fastmsa.api import app

cmd = FastMSACommand()
msa = cmd.init_app()


@app.on_event("startup")
async def initial_task():
    asyncio.create_task(msa.broker.main())


if __name__ == "__main__":
    cmd.run()
