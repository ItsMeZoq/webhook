import argparse
import app

parser = argparse.ArgumentParser(description="Easy google chat sending")

parser.add_argument("--msg", required=True, help="msg sends messege to google chat")
args = parser.parse_args()

app.send_msg(args.msg)