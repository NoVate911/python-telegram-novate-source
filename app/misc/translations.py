from app.database.requests.update import user_language_code_by_telegram_id as update_user_language_code_by_telegram_id


languages: str = ['ru', 'en']

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
                    'owner_welcome': "✅ Вам выданы права Администратора.",
                    'referral_notifications': {
                        'not_found': "❌ Пользователь с данной реферальной ссылкой не найден.",
                        'for_me': "✅ Вы стали рефералом пользователя @{0}.",
                        'for_referrer': "🛎 Вы стали реферером пользователя @{0}.",
                    },
                },
                'help': {
                    'main': "☺️ Я с радостью подскажу то, что требуется.\n"\
                        "👇 Выберите нужный пункт ниже.",
                    'information_bot': "🤖 @{0} - бот-помощник, который создан специально для канала @{1}.\n"\
                        "👀 Если у Вас появились какие-либо предложения или вопросы - присылайте их в \"{2}\".\n\n"\
                        "📌 Мы стараемся помочь каждому, поэтому, когда Вы будете задавать вопрос, то сформулируйте его правильно и корректно.",
                    'rules_use_bot': "📌 Достаточно адекватно относиться к разделу \"{0}\" и создавать адекватные запросы.",
                    'back': "✅ Вы вернулись с раздела помощи.",
                },
                'referral': {
                    'main': "📌 Приглашайте людей по вашей ссылке и поднимайтесь по рейтингу выше.",
                    'personal_statistics': "🧮 Зарегистрировано по вашей ссылке: <b>{0} участников</b>.\n"\
                        "📌 Вы являетесь рефералом пользователя @{1}.\n\n"\
                        "🗣 Реферальная ссылка для приглашения <span class='tg-spoiler'><i>(нажмите для копирования)</i></span>: <code>{2}</code>",
                    'back': "✅ Вы вернулись с раздела реферальной системы.",
                },
                'request': {
                    'main': "📌 Если возникли проблемы с ботом или же вопросы на которые бот не может ответить - создайте запрос с обращением.",
                    'create': {
                        'cancel': "✅ Вы отменили создание запроса.",
                        'message': "⌨️ Введите текст запроса:\n"\
                            "Для отмены - /cancel",
                        'message_too_short': "❌ Длина текста запроса может быть <b>от {0} символов</b>.",
                        'success': "✅ Запрос создан и направлен Администрации.\n"\
                            "👀 После рассмотрения и решения с вами свяжутся.",
                        'notification_administrator': "📌 Поступил новый запрос от @{0} (<code>{1}</code>): <b>{2}</b>",
                    },
                    'back': "✅ Вы вернулись с раздела технической поддержки.",
                },
                'donate': {
                    'transfer_credited': "✅ Перевод №<code>{0}</code> прошёл идентификацию и был подтверждён.\n"\
                        "❤️ Спасибо большое, что помогаете в развитии проектов!",
                    'main': "📌 Вы можете пожертвовать определённую сумму на развитие проектов автора.\n"\
                        "❤️ Автор выражает огромную благодарность каждому из тех, кто делает пожертвования любой суммы.",
                    'get_link': {
                        'cancel': "✅ Вы отменили получение ссылки на пожертвование.",
                        'insert_sum': "⌨️ Введите сумму пожертвования <span class='tg-spoiler'>(в рублях)</span>:\n"\
                            "Для отмены - /cancel",
                        'insert_sum_error': "❌ Сумма пожертвования должна начинаться с {0} рубля.",
                        'success': "✅ Перевод №<code>{0}</code> создан и ожидает идентификации."\
                            "🧷 Нажмите на <a href='{1}'>этот текст</a> для пожертвования.",
                    },
                    'personal_statistics': "🧮 Вы пожертвовали <b>{0} рублей</b> в развитие проектов.\n"\
                        "📌 Из этой суммы <b>{1} рублей</b> прошли идентификацию, а <b>{2} рублей</b> на данный момент не прошли её.",
                    'back': "✅ Вы вернулись с раздела пожертвования.",
                },
            },
            'admin': {
                'administrator': {
                    'main': "📌 Устанавливайте, удаляйте и смотрите активных Администратором в режиме реального времени.",
                    'cancel': "✅ Вы отменили действие.",
                    'set': {
                        'telegram_id': "⌨️ Введите Telegram ID пользователя:\n"\
                            "Для отмены - /cancel",
                        'telegram_id_error': "❌ Telegram ID пользователя не найден или он уже является Администратором.",
                        'success': "✅ Администратор @{0} (<code>{1}</code>) установлен.",
                    },
                    'unset': {
                        'telegram_id': "⌨️ Введите Telegram ID пользователя:\n"\
                            "Для отмены - /cancel",
                        'telegram_id_error': "❌ Telegram ID пользователя не найден или он не является Администратором.",
                        'success': "✅ Администратор @{0} (<code>{1}</code>) снят.",
                    },
                    'list': "📄 Список активной Администрации:\n"\
                        "{0}",
                    'back': "✅ Вы вернулись с раздела Администраторов.",
                },
                'channel': {
                    'main': "📌 Управляйте каналами для подписки прямо в боте, без его остановки.",
                    'cancel': "✅ Вы отменили действие.",
                    'add': {
                        'channel_name': "⌨️ Введите название канала <span class='tg-spoiler'>(без @)</span>:\n"\
                            "Для отмены - /cancel",
                        'channel_name_error': "❌ Канал с таким названием не найден или бот не добавлен, как Администратор.",
                        'success': "✅ Канал @{0} добавлен.\n"\
                            "📌 Для смены типа подписки используйте клавиатуру.",
                    },
                    'remove': {
                        'channel_name': "⌨️ Введите название канала <span class='tg-spoiler'>(без @)</span>:\n"\
                            "Для отмены - /cancel",
                        'channel_name_error': "❌ Канал с таким названием не добавлен в бота.",
                        'success': "✅ Канал @{0} удален.",
                    },
                    'change_need_subscribed': {
                        'channel_name': "⌨️ Введите название канала <span class='tg-spoiler'>(без @)</span>:\n"\
                            "Для отмены - /cancel",
                        'channel_name_error': "❌ Канал с таким названием не добавлен в бота.",
                        'success': "✅ Тип подписки для канала @{0} изменен на <b>{1}</b>.",
                    },
                    'list': "📄 Список добавленных каналов:\n"\
                        "{0}",
                    'back': "✅ Вы вернулись с раздела управления каналами.",
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
                    'request': {
                        'main': "⚙️ ТЕХНИЧЕСКАЯ ПОДДЕРЖКА",
                        'create': "📝 СОЗДАТЬ ЗАПРОС",
                        'back': "⬅️ НАЗАД",
                    },
                    'donate': {
                        'main': "💰 ПОЖЕРТВОВАТЬ",
                        'get_link': "🔗 ПОЛУЧИТЬ ССЫЛКУ",
                        'personal_statistics': "📊 ЛИЧНАЯ СТАТИСТИКА",
                        'back': "⬅️ НАЗАД",
                    },
                },
                'admin': {
                    'administrator': {
                        'main': "🗣 УПРАВЛЕНИЕ АДМИНИСТРАТОРАМИ",
                        'set': "✅ УСТАНОВИТЬ АДМИНИСТРАТОРА",
                        'unset': "❎ УДАЛИТЬ АДМИНИСТРАТОРА",
                        'list': "📄 СПИСОК АДМИНИСТРАЦИИ",
                        'back': "⬅️ НАЗАД",
                    },
                    'channel': {
                        'main': "📢 УПРАВЛЕНИЕ КАНАЛАМИ",
                        'add': "📥 ДОБАВИТЬ КАНАЛ",
                        'remove': "📤 УДАЛИТЬ КАНАЛ",
                        'change_need_subscribed': "⚙️ СМЕНИТЬ ТИП КАНАЛА",
                        'list': "📄 СПИСОК КАНАЛОВ",
                        'back': "⬅️ НАЗАД",
                    },
                },
            },
        },
    },
    'en': {
        'messages': {
            'need_subscribed_to_channels': "⚠️ In order to use the bot you need to be signed for the required Telegram channels.\n\n"\
                "📄 Here is a list of the required channels for subscription:\n"\
                "{0}",
            'need_registered': "⚠️ To use commands, you need to register using /start.",
            'unknown': "👀 I don't know such a team.",
            'user': {
                'start': {
                    'welcome': "👋 Welcome, @{0}.\n\n"\
                        "🗣 I was created in order to help participants in the channel <a href='https://t.me/novateesource'>Novate Source</a> in search of the necessary information.\n"\
                        "👇 For navigation by my functions, use the keyboard shown below.\n\n"\
                        "🤝 Pleasant use and productive day!",
                    'comeback': "🔥 I defined your account, @{0}.\n"\
                        "👇 Use the keyboard below for navigation.",
                    'owner_welcome': "✅ You have issued administrator rights.",
                    'referral_notifications': {
                        'not_found': "❌ The user with this referral link was not found.",
                        'for_me': "✅ You have become a user abstract @{0}.",
                        'for_referrer': "🛎 You have become a user abstract @{0}.",
                    },
                },
                'help': {
                    'main': "☺️ I will gladly tell you what is required.\n"\
                        "👇 Select the desired point below.",
                    'information_bot': "🤖 @{0} - helper, which was created specifically for the channel @{1}.\n"\
                        "👀 If you have any suggestions or questions, send them to \"{2}\".\n\n"\
                        "📌 We try to help everyone, therefore, when you ask a question, then formulate it correctly and correctly.",
                    'rules_use_bot': "📌 It is quite adequate to the section \"{0}\" and create adequate requests.",
                    'back': "✅ You returned from the section of help.",
                },
                'referral': {
                    'main': "📌 Invite people by your link and go up by the rating above.",
                    'personal_statistics': "🧮 Registered by your link: <b>{0} participants</b>.\n"\
                        "📌 You are a user abstract @{1}.\n\n"\
                        "🗣 Abstract link for inviting <span class='tg-spoiler'><i>(click for copying)</i></span>: <code>{2}</code>",
                    'back': "✅ You have returned from the section of the referral system.",
                },
                'request': {
                    'main': "📌 If there are problems with the bot or the questions to which the bot cannot answer - create a request with the appeal.",
                    'create': {
                        'cancel': "✅ You canceled the creation of a request.",
                        'message': "⌨️ Enter the text of the request:\n"\
                            "For cancellation - /cancel",
                        'message_too_short': "❌ The length of the query text can be <b>from {0} symbols</b>.",
                        'success': "✅ The request was created and sent to the administration.\n"\
                            "👀 After consideration and decisions, you will be contacted.",
                        'notification_administrator': "📌 A new request was received from @{0} (<code>{1}</code>): <b>{2}</b>",
                    },
                    'back': "✅ You returned from the section of technical support.",
                },
                'donate': {
                    'transfer_credited': "✅ Translation No.<code>{0}</code> was identified and confirmed.\n"\
                        "❤️ Thank you very much for helping in the development of projects!",
                    'main': "📌 You can donate a certain amount for the development of project projects.\n"\
                        "❤️ The author expresses great gratitude to each of those who make donations of any amount.",
                    'get_link': {
                        'cancel': "✅ You canceled the receipt of the donation link.",
                        'insert_sum': "⌨️ Enter the amount of donations <span class='tg-spoiler'>(in rubles)</span>:\n"\
                            "For cancellation - /cancel",
                        'insert_sum_error': "❌ The amount of donation should begin with {0} ruble.",
                        'success': "✅ Translation No.<code>{0}</code> created and expects identification."\
                            "🧷 Press <a href='{1}'>this text</a> for donation.",
                    },
                    'personal_statistics': "🧮 You donated <b>{0} rubles</b> to the development of projects.\n"\
                        "📌 Of this amount <b>{1} rubles</b> have been identified, and <b>{2} rubles</b> at the moment did not pass it.",
                    'back': "✅ You have returned from the donation section.",
                },
            },
            'admin': {
                'administrator': {
                    'main': "📌 Install, delete and watch actual administrator in real time.",
                    'cancel': "✅ You canceled the action.",
                    'set': {
                        'telegram_id': "⌨️ Enter Telegram ID user:\n"\
                            "For cancellation - /cancel",
                        'telegram_id_error': "❌ Telegram ID of the user was not found or he is already an administrator.",
                        'success': "✅ Administrator @{0} (<code>{1}</code>) is installed.",
                    },
                    'unset': {
                        'telegram_id': "⌨️ Enter Telegram ID user:\n"\
                            "For cancellation - /cancel",
                        'telegram_id_error': "❌ Telegram ID of the user was not found or he is not an administrator.",
                        'success': "✅ Administrator @{0} (<code>{1}</code>) was removed.",
                    },
                    'list': "📄 List of active administration:\n"\
                        "{0}",
                    'back': "✅ You have returned from the Section of Administrators.",
                },
                'channel': {
                    'main': "📌 Control channels for subscription right in the bot, without stopping it.",
                    'cancel': "✅ You canceled the action.",
                    'add': {
                        'channel_name': "⌨️ Enter the name of the channel <span class='tg-spoiler'>(without @)</span>:\n"\
                            "For cancellation - /cancel",
                        'channel_name_error': "❌ The channel with this name was not found or the bot was not added as an administrator.",
                        'success': "✅ Channel @{0} added.\n"\
                            "📌 To change the type of subscription, use the keyboard.",
                    },
                    'remove': {
                        'channel_name': "⌨️ Enter the name of the channel <span class='tg-spoiler'>(without @)</span>:\n"\
                            "For cancellation - /cancel",
                        'channel_name_error': "❌ The channel with this name is not added to the bot.",
                        'success': "✅ Channel @{0} remove.",
                    },
                    'change_need_subscribed': {
                        'channel_name': "⌨️ Enter the name of the channel <span class='tg-spoiler'>(without @)</span>:\n"\
                            "For cancellation - /cancel",
                        'channel_name_error': "❌ The channel with this name is not added to the bot.",
                        'success': "✅ The type of subscription for the channel @{0} is changed to <b>{1}</b>.",
                    },
                    'list': "📄 List of added channels:\n"\
                        "{0}",
                    'back': "✅ You returned from the channel management section.",
                },
            },
        },
        'keyboards': {
            'reply': {
                'title': "Choose a section",
                'user': {
                    'help': {
                        'main': "🧷 HELP",
                        'information_bot': "⚙️ ABOUT THE BOT",
                        'rules_use_bot': "📌 RULES FOR USE",
                        'back': "⬅️ BACK",
                    },
                    'referral': {
                        'main': "🔗 REFEREAL SYSTEM",
                        'personal_statistics': "📊 PERSONAL STATISTICS",
                        'back': "⬅️ BACK",
                    },
                    'request': {
                        'main': "⚙️ TECHNICAL SUPPORT",
                        'create': "📝 CREATE A REQUEST",
                        'back': "⬅️ BACK",
                    },
                    'donate': {
                        'main': "💰 TO SACRIFICE",
                        'get_link': "🔗 GET THE LINK",
                        'personal_statistics': "📊 PERSONAL STATISTICS",
                        'back': "⬅️ BACK",
                    },
                },
                'admin': {
                    'administrator': {
                        'main': "🗣 ADMINISTRATORS MANAGEMENT",
                        'set': "✅ INSTALL THE ADMINISTRATOR",
                        'unset': "❎ DELETE THE ADMINISTRATOR",
                        'list': "📄 LIST OF THE ADMINISTRATION",
                        'back': "⬅️ BACK",
                    },
                    'channel': {
                        'main': "📢 CHANNEL MANAGEMENT",
                        'add': "📥 ADD THE CHANNEL",
                        'remove': "📤 DELETE THE CHANNEL",
                        'change_need_subscribed': "⚙️ CHANGE THE TYPE OF CHANNEL",
                        'list': "📄 LIST OF CHANNELS",
                        'back': "⬅️ BACK",
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