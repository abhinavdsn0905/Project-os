import requests

class NotificationBridge:
    def dispatch_verification(self, destination_node, access_cipher, method='telegram'):
        if method == 'telegram':
            return self._transmit_telegram_alert(destination_node, access_cipher)
        return False

    def _transmit_telegram_alert(self, recipient_node, verification_code):
        try:
            response = requests.post(
                f"https://api.telegram.org/bot{ALERT_SYSTEM['bot_api']}/sendMessage",
                data={
                    'chat_id': recipient_node,
                    'text': f"Secure access cipher: {verification_code}"
                },
                timeout=5
            )
            return response.status_code == 200
        except:
            return False