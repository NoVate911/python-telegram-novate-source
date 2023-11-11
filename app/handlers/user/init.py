from aiogram import Dispatcher, Router

from app.handlers.user.start import router as start_router
from app.handlers.user.help import router as help_router
from app.handlers.user.referral import router as referral_router
from app.handlers.user.request import router as request_router


def init(dp: Dispatcher) -> None:
    routers: Router = (
        start_router,
        help_router,
        referral_router,
        request_router,
    )

    for router in routers:
        dp.include_router(router)