from aiogram import Dispatcher, Router

from app.handlers.admin.administrator import router as administrator_router
from app.handlers.admin.channel import router as channel_router


def init(dp: Dispatcher) -> None:
    routers: Router = (
        administrator_router,
        channel_router,
    )

    for router in routers:
        dp.include_router(router)