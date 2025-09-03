# Krótki program dla wysyłania powiadomień do chatów google.

# Jak uruchomić:

```bash

git clone <url_repo>

cd <folder gdzie masz program>

python -m venv venv
venv\Scripts\activate
pip install -r requirments.txt
python
from app import send_msg
send_msg("message")