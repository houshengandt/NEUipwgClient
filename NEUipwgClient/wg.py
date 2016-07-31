from os import mkdir, chdir, path
import urllib.request
import urllib.parse


class IpWg():
    def login(self, u_name, u_password):
        self.login_url = "http://ipgw.neu.edu.cn:803/srun_portal_pc.php?ac_id=1&"
        self.login_data = {'ac_id': '1',
                           'action': 'login',
                           'nas_ip': '',
                           'password': u_password,
                           'save_me': '0',
                           'url': '',
                           'user_ip': '',
                           'user_mac': '',
                           'username': u_name
                           }
        self.login_data = urllib.parse.urlencode(self.login_data).encode("GB2312")
        self.login_header = {'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
                             'Accept - Encoding': 'gzip, deflate',
                             'Accept-Language': 'zh-Hans-CN, zh-Hans; q=0.5',
                             'Cache-Control': 'no-cache',
                             'Connection': 'Keep-Alive',
                             'Content-Length': '97',
                             'Content-Type': 'application/x-www-form-urlencoded',
                             'Host': 'ipgw.neu.edu.cn:803',
                             'Referer': 'http://ipgw.neu.edu.cn:803/srun_portal_pc.php?ac_id=1&',
                             'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64;Trident / 7.0;rv:11.0) likeGecko'
                             }
        urllib.request.urlopen(urllib.request.Request(self.login_url, self.login_data, self.login_header), timeout=2)

    def get_user_info(self):
        self.get_user_info_url = "http://ipgw.neu.edu.cn:803/include/auth_action.php?k=31989"
        self.get_user_info_data = {'action': 'get_online_info',
                                   'key': ''
                                   }
        self.get_user_info_data = urllib.parse.urlencode(self.get_user_info_data).encode("GB2312")
        self.get_user_info_header = {'Accept': '* / *',
                                     'Accept - Encoding': 'gzip, deflate',
                                     'Accept - Language': 'zh - Hans - CN, zh - Hans;q = 0.5',
                                     'Cache - Control': 'no - cache',
                                     'Connection': 'Keep - Alive', 'Content - Length': '32',
                                     'Content - Type': 'application / x - www - form - urlencoded',
                                     'Host': 'ipgw.neu.edu.cn:803',
                                     'Referer': 'http: // ipgw.neu.edu.cn:803 / srun_portal_pc.php?ac_id = 1 &User - '
                                                'Agent: Mozilla / 5.0(WindowsNT10.0;WOW64;Trident / 7.0;rv:11.0) like'
                                                'Gecko',
                                     'X - Requested - With': 'XMLHttpRequest'
                                     }
        self.p = urllib.request.Request(self.get_user_info_url, self.get_user_info_data, self.get_user_info_header)
        self.getted_info = urllib.request.urlopen(self.p).read()
        return self.getted_info

    def logout(self, u_name, u_password):
        self.logout_url = "http://ipgw.neu.edu.cn:803/srun_portal_pc.php"
        self.logout_data = {'action': 'logout',
                            'ajax': '1',
                            'password': u_password,
                            'username': u_name
                            }
        self.logout_data = urllib.parse.urlencode(self.logout_data).encode("GB2312")
        self.logout_header = {'Accept': 'text / html, application / xhtml + xml, image / jxr, * / *',
                              'Accept - Encoding': 'gzip, deflate',
                              'Accept - Language': 'zh - Hans - CN, zh - Hans;q = 0.5',
                              'Cache - Control': 'no - cache',
                              'Connection': 'Keep - Alive',
                              'Content - Length': '46',
                              'Content - Type': 'application / x - www - form - urlencoded',
                              'Host': 'ipgw.neu.edu.cn:803',
                              'Referer': 'http: // ipgw.neu.edu.cn:803 / srun_portal_pc.php?ac_id = 1 &User - Agent'
                                         ': Mozilla / 5.0(WindowsNT10.0;WOW64;Trident / 7.0;rv:11.0) likeGecko'
                              }
        urllib.request.urlopen(urllib.request.Request(self.logout_url, self.logout_data, self.logout_header), timeout=2)

    def data_file(self):
        if path.isdir("c:\\IPWG") == 0:
            mkdir("c:\\IPWG")
        if path.isfile("c:\\IPWG\\doc.txt") == 0:
            chdir("c:\\IPWG")
            a = open('doc.txt', 'wt')
            a.write("校园网账号,校园网密码,0")
            a.close()


