# Krótki kod dla wysyłania powiadomień do chatów google.

# Jak uruchomić:

```bash
git clone https://github.com/ItsMeZoq/webhook.git
cd webhook
wstaw swoje google chat webhooki url do "config.json"
python -m venv venv
venv\Scripts\activate
pip install -r requirments.txt

python cli.py --msg "wiadomość" --url_name "nazwa klucza twojego webhooka"
