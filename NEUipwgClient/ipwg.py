import urllib.request
import urllib.parse


hostname = 'http://ipgw.neu.edu.cn/ipgw/ipgw.ipgw'


class PostIt():

    def info(u_uid, u_password, u_operation_type):
        value = {'uid': u_uid, 'password': u_password, 'range': '2', 'operation': u_operation_type, 'timeout': '1'}
        value = urllib.parse.urlencode(value).encode("GB2312")
        return value


    def u_operation(value):
        urllib.request.Request(hostname, value)



