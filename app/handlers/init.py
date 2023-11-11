from aiogram import Dispatcher, Router

from app.handlers.user import router as user_router
from app.handlers.other import router as other_router


def init(dp: Dispatcher) -> None:
    routers: Router = (
        user_router,
        other_router,
    )

    for router in routers:
        dp.include_router(router)