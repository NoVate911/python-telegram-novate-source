from app.database.requests.update import user_language_code_by_telegram_id as update_user_language_code_by_telegram_id


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
                    'comeback': "🔥 Я определил ваш аккаунт, @{0}.\n"\
                        "👇 Используйте клавиатуру ниже для навигации.",
                    'referral_notifications': {
                        'not_found': "❌ Пользователь с данной реферальной ссылкой не найден.",
                        'for_me': "✅ Вы стали рефералом пользователя @{0}.",
                        'for_referrer': "🛎 Вы стали реферером пользователя @{0}.",
                    },
                },
                'help': {
                    'main': "☺️ Я с радостью подскажу то, что требуется.\n"\
                        "👇 Выберите нужный пункт ниже.",
                    'information_bot': "🤖 Информация о боте.",
                    'rules_use_bot': "📌 Правила использования бота.",
                    'back': "✅ Вы вернулись с раздела помощи.",
                },
                'referral': {
                    'main': "📌 Приглашайте людей по вашей ссылке и поднимайтесь по рейтингу выше.",
                    'personal_statistics': "🧮 Зарегистрировано по вашей ссылке: <b>{0} участников</b>.\n"\
                        "📌 Вы являетесь рефералом пользователя @{1}.\n\n"\
                        "🗣 Реферальная ссылка для приглашения <span class='tg-spoiler'><i>(нажмите для копирования)</i></span>: <code>{2}</code>",
                    'back': "✅ Вы вернулись с раздела реферальной системы.",
                },
            },
        },
        'keyboards': {
            'reply': {
                'title': "Выберите раздел",
                'user': {
                    'help': {
                        'main': "🧷 ПОМОЩЬ",
                        'information_bot': "⚙️ ИНФОРМАЦИЯ О БОТЕ",
                        'rules_use_bot': "📌 ПРАВИЛА ИСПОЛЬЗОВАНИЯ",
                        'back': "⬅️ НАЗАД",
                    },
                    'referral': {
                        'main': "🔗 РЕФЕРАЛЬНАЯ СИСТЕМА",
                        'personal_statistics': "📊 ЛИЧНАЯ СТАТИСТИКА",
                        'back': "⬅️ НАЗАД",
                    },
                },
            },
        },
    },
}


async def user_language(telegram_id: int, language_code: str) -> str:
    language: str = language_code
    if not language in languages:
        language = 'ru'
    await update_user_language_code_by_telegram_id(telegram_id=telegram_id, language_code=language)
    return language