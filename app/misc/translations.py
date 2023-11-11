from app.database.requests.update import user_language_code_by_telegram_id as set_user_language_code_by_telegram_id


languages: str = ['ru']

translations: str = {
    'ru': {
        'messages': {
            'need_subscribed_to_channels': "⚠️ Для того, чтобы пользоваться ботом нужно быть подписанным на требуемые Telegram каналы.\n\n"\
                "📄 Вот список требуемых каналов для подписки:\n"\
                "{0}",
            'need_registered': "⚠️ Для использования команд нужно зарегистрироваться, используя /start.",
            'unknown': "👀 Я такой команды не знаю.",
            'user': {
                'start': {
                    'welcome': "👋 Добро пожаловать, @{0}.\n\n"\
                        "🗣 Я создан для того, чтобы помогать участникам канала <a href='https://t.me/novatesource'>NoVate Source</a> в поиске необходимой информации.\n"\
                        "👇 Для навигации по моим функциям используйте клавиатуру, которая показана ниже.\n\n"\
                        "🤝 Приятного пользования и продуктивного дня!",
                    'comeback': "С возвращением, @{0}.",
                    'referral_notifications': {
                        'not_found': "Реферальная ссылка не найдена.",
                        'for_me': "Вы стали рефералом для @{0}.",
                        'for_referrer': "По вашей реферальной ссылке перешёл @{0}.",
                    },
                },
            },
        },
        'keyboards': {
            'reply': {
            },
            'inline': {
            },
        },
    },
}


async def user_language(telegram_id: int, language_code: str) -> str:
    language: str = language_code
    if not language in languages:
        language = 'ru'
    await set_user_language_code_by_telegram_id(telegram_id=telegram_id, language_code=language)
    return language