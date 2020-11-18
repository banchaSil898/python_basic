"""If you are on Windows, the environment variable syntax depends on command line interpreter. On Command Prompt:

C:\path\to\app>set FLASK_APP=hello.py
And on PowerShell:

PS C:\path\to\app> $env:FLASK_APP = "hello.py"
"""

from flask import Flask, request

PAGE_ACCESS_TOKEN = ''
app =Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def webhook():
  print("hello lazada api")
  if request.method == 'GET':
    # token = request.args.get('hub.verify_token')
    # challenge = request.args.get('hub.challenge')
    token = ""
    challenge = ""
    print("token is {}".format(request))
    if token == 'totortotor':
        return str(challenge)
    return '400'
  else:
    print(request.data)
    return '200'

if __name__ == '__main__':
  app.run(debug=True)