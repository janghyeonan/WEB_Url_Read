#사이트에 요청 보내서 읽기
import urllib.request

print(urllib.request.urlopen("http://www.renardy.co.kr").read())
