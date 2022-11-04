KEYS = {
    # Key for SOTAwatchspot JA
    'ConsumerkeySOTAwatch': '',
    'ConsumersecretSOTAwatch': '',
    'AccesstokenSOTAwatch': '',
    'AccesstokensecretSOTAwatch': '',
    # Keys for POTA
    'ConsumerkeyPOTA': '',
    'ConsumersecretPOTA': '',
    'AccesstokenPOTA': '',
    'AccesstokensecretPOTA': '',

    'JAFFConsumerkey': '',
    'JAFFConsumersecret': '',
    'JAFFAccesstoken': '',
    'JAFFAccesstokensecret': '',

    'Areas': r'^JA.*',
    'Alerts': r'JA\d*/\w\w\-',
    'JASummits': r'JA\d*/\w\w\-',
    'Watchfor': r'JA\d*/\w\w\-',
    'Alertafter': ('Asia/Tokyo', 6),
    'LOCALTIME': True,
    'MapURL': 'https://maps.google.co.jp/maps?q={place}&ll={locate}&t=h&z=12',
    'VOACAP': '/home/ubuntu/pi/twitter/propdb.db',
    'VOAIMG': '/tmp/voaimg.png',

    'SOTA_URL': 'http://www.sotawatch.org/alerts.php',
    'SOTALIVE_URL': 'https://www.sotalive.net',
    'SOTAWATCH_JSON_URL': 'https://api2.sota.org.uk',
    'OUTPUT_JSON_FILE': '/usr/share/nginx/html/json/spots',
    'OUTPUT_JSON_JAFILE': '/usr/share/nginx/html/json/spotsJA',
    'ASSOC_DB': '/home/ubuntu/sotaapp/backend/database/association.db',
    'SUMMIT_DB': '/home/ubuntu/sotaapp/backend/database/summits.db',
    'ALERT_DB': '/home/ubuntu/sotaapp/backend/database/alert.db',
    'APRSLOG_DB': '/home/ubuntu/sotaapp/backend/database/aprslog.db',
    'USER_DB': '/home/ubuntu/pi/SOTAspotJA/aprs-user.db',
    'PARAMS_DB': '/home/ubuntu/pi/SOTAspotJA/params.dbm',
    'LAST3': "/home/ubuntu/pi/twitter/lastspot.txt",
    'LAST3DX': "/home/ubuntu/pi/twitter/lastspotdx.txt",
    'APRS_USER': '',
    'APRS_PASSWD': '',
    'APRS_HOST': 'japan.aprs2.net',
    'APRS_PORT': 14580,
    'TWEET_AT': "08:00",
    'ALERT_FROM': -4,
    'ALERT_TO': 36,
    'TWEET_ALERT_TO': 16,
    'UPDATE_EVERY': 20,
    'UPDATE_ALERTS_EVERY': 5,
    'UPDATE_SPOTS_EVERY': 1,
    'WINDOW_FROM': -5,
    'WINDOW_TO': 6,
    'KEEP_IN_DB': 42,
    'MID_HIST': 24,
    'MAGNIFY': 10.0,
    'TEST_USER': [],
    'EXCLUDE_USER': []
}
