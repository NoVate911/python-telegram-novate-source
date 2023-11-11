from aiogram import Dispatcher, Router

from app.handlers.user.init import init as user_init
from app.handlers.admin.init import init as admin_init
from app.handlers.other import router as other_router


def init(dp: Dispatcher) -> None:
    routers: Router = (
        other_router,
    )

    user_init(dp=dp)
    admin_init(dp=dp)
    for router in routers:
        dp.include_router(router)