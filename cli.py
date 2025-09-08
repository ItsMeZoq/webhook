import argparse
import app

parser = argparse.ArgumentParser(description="Easy google chat sending")

parser.add_argument("--msg", required=True, help="msg sends messege to google chat")
parser.add_argument("--url_name", required=True, help="its a key of url from config.json")
args = parser.parse_args()

app.send_msg(args.msg, args.url_name)
