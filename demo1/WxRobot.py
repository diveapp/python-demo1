import requests
import itchat

KEY = '8edce3ce905a4c1dbb965e6b35c3834d'


def _response(msg):
    # tulingApi
    api = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': KEY,
        'info': msg,
        'userid': 'wechat-robot',
    }

    try:
        r = requests.post(api, data=data).json()
        return r.get('text')
    except:
        return


def _reply(msg):
    defaultReply = 'I received: ' + msg['Text']

    reply = _response(msg['Text'])

    return reply or defaultReply


itchat.auto_login(hotReload=True)

itchat.run()
