# Базовый URL сервера
BASE_URL = 'https://qa-scooter.praktikum-services.ru'
DZEN_BASE_URL = 'https://dzen.ru'

# Эндпоинты
MAIN_PAGE_ENDPOINT = '/'
ORDER_PAGE_ENDPOINT = '/order'
DZEN_PAGE_ENDPOINT = '/?yredirect=true'

# Полные URL
MAIN_PAGE = f'{BASE_URL}{MAIN_PAGE_ENDPOINT}'
ORDER_PAGE = f'{BASE_URL}{ORDER_PAGE_ENDPOINT}'
DZEN_PAGE = f'{DZEN_BASE_URL}{DZEN_PAGE_ENDPOINT}'