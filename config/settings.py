# Configuration settings for the Arbitrage Bot

# Paths
BASE_PATH = '/path/to/project'
LOG_PATH = f'{BASE_PATH}/logs'

# Playwright settings
debug = False
headless = True

# Sites configuration
SITES = {
    'site1': {
        'url': 'https://example1.com',
        'api_key': 'YOUR_API_KEY_1'
    },
    'site2': {
        'url': 'https://example2.com',
        'api_key': 'YOUR_API_KEY_2'
    }
}

# Logging settings
LOG_LEVEL = 'INFO'
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'