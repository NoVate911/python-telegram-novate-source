from aiogram import Dispatcher, Router

from app.handlers.admin.administrator import router as administrator_router


def init(dp: Dispatcher) -> None:
    routers: Router = (
        administrator_router,
    )

    for router in routers:
        dp.include_router(router)