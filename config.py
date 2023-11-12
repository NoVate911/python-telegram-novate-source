DEBUGGING: bool = False

TOKEN: str = 'YOUR_TOKEN_FROM_TELEGRAM'

OWNER_TELEGRAM_ID: int = 1234567890

PAYMENTS_TOKEN: str = 'YOUR_TOKEN_FROM_YOOMONEY'
PAYMENTS_SETTINGS: str = {
    'receiver': 1234567890,
    'quickpay_form': "shop",
    'targets': "Пожертвование",
    'paymentType': "SB",
    'label': "donate_{0}_{1}_{2}",
}