#!/usr/bin/env python

import urllib
import json
import sys


def get_token(corpid, corpsecret):
    url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=%s&corpsecret=%s" % (corpid, corpsecret)
    f = urllib.urlopen(url)
    token_json = f.read()
    f.close()
    return json.loads(token_json)


def send_message(access_token, agentid, userid, message):
    url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s" % (access_token)
    text = {'msgtype': 'text', 'agentid': agentid, 'touser': userid, 'text': {'content': message}}
    f = urllib.urlopen(url, json.dumps(text))
    result_json = f.read()
    f.close()
    return json.loads(result_json)


def main():
    if len(sys.argv) == 3:
        corpid = sys.argv[1]
        corpsecret = sys.argv[2]
    else:
        try:
            corpid = raw_input("Enter corpid: ")
            corpsecret = raw_input("Enter corpsecret: ")
        except (KeyboardInterrupt, EOFError):
            corpid = ''
            corpsecret = ''
    if not corpid or not corpsecret:
        return
    token = get_token(corpid, corpsecret)
    if token.has_key("errcode"):
        print token["errmsg"]
    else:
        access_token = token["access_token"]
        result = send_message(access_token, 0, 'shil', 'Hello From Python!')
        print result["errmsg"]


if __name__ == '__main__':
    main()
