"""If you are on Windows, the environment variable syntax depends on command line interpreter. On Command Prompt:

C:\path\to\app>set FLASK_APP=hello.py
And on PowerShell:

PS C:\path\to\app> $env:FLASK_APP = "hello.py"
"""

from flask import Flask, request

PAGE_ACCESS_TOKEN = 'EAADasQ0cr6oBAIXMSRPkeUBkNQYEdIViKsRYXf8UMbm7PxNZB73DVBJWECV7uV9XD6gedKrmn7tiZAsNNyudzyHhPEtMhDsKZAGBNRomu9WOmaHvTOronSCPF8JZCzsLMZC1pabd9GAo2ZCHmQZB2TOGiJOJvDPXUuYqWC6acOXyxEsaxMO552K'
app =Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def webhook():
  if request.method == 'GET':
    token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')
    print("token is {}".format(token))
    if token == 'totortotor':
      return str(challenge)
    return '400'
  else:
    print(request.data)
    return '200'

if __name__ == '__main__':
    app.run(debug=True)