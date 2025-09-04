# Krótki kod dla wysyłania powiadomień do chatów google.

# Jak uruchomić:

```bash
git clone https://github.com/ItsMeZoq/webhook.git
cd webhook
wstaw swój google chat webhook url do "config.json"
python -m venv venv
venv\Scripts\activate
pip install -r requirments.txt

python cli.py --msg "WIADOMOŚĆ"
