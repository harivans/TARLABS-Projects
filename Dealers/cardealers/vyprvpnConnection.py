from __future__ import absolute_import
import subprocess
import time
from random import shuffle


VPN_setting = {'username': 'tarunlalwani@gmail.com',
               'password': 'indian007#',
               'timeout': '30', }


servers_list=['ar1.vpn.goldenfrog.com Argentina', 'au2.vpn.goldenfrog.com Australia - Melbourne', 'au3.vpn.goldenfrog.com Australia - Perth', 'au1.vpn.goldenfrog.com Australia - Sydney', 'at1.vpn.goldenfrog.com Austria', 'bh1.vpn.goldenfrog.com Bahrain', 'be1.vpn.goldenfrog.com Belgium', 'br1.vpn.goldenfrog.com Brazil', 'ca1.vpn.goldenfrog.com Canada', 'co1.vpn.goldenfrog.com Colombia', 'cr1.vpn.goldenfrog.com Costa Rica', 'cz1.vpn.goldenfrog.com Czech Republic', 'dk1.vpn.goldenfrog.com Denmark', 'fi1.vpn.goldenfrog.com Finland', 'fr1.vpn.goldenfrog.com France', 'de1.vpn.goldenfrog.com Germany', 'hk1.vpn.goldenfrog.com Hong Kong', 'is1.vpn.goldenfrog.com Iceland', 'in1.vpn.goldenfrog.com India', 'id1.vpn.goldenfrog.com Indonesia', 'ie1.vpn.goldenfrog.com Ireland', 'it1.vpn.goldenfrog.com Italy', 'jp1.vpn.goldenfrog.com Japan', 'lt1.vpn.goldenfrog.com Lithuania', 'lu1.vpn.goldenfrog.com Luxembourg', 'my1.vpn.goldenfrog.com Malaysia', 'mx1.vpn.goldenfrog.com Mexico', 'eu1.vpn.goldenfrog.com Netherlands', 'nz1.vpn.goldenfrog.com New Zealand', 'no1.vpn.goldenfrog.com Norway', 'pa1.vpn.goldenfrog.com Panama', 'ph1.vpn.goldenfrog.com Philippines', 'pl1.vpn.goldenfrog.com Poland', 'pt1.vpn.goldenfrog.com Portugal', 'qa1.vpn.goldenfrog.com Qatar', 'ro1.vpn.goldenfrog.com Romania', 'ru1.vpn.goldenfrog.com Russia', 'sa1.vpn.goldenfrog.com Saudi Arabia', 'sg1.vpn.goldenfrog.com Singapore', 'kr1.vpn.goldenfrog.com South Korea', 'es1.vpn.goldenfrog.com Spain', 'se1.vpn.goldenfrog.com Sweden', 'ch1.vpn.goldenfrog.com Switzerland', 'tw1.vpn.goldenfrog.com Taiwan', 'th1.vpn.goldenfrog.com Thailand', 'tr1.vpn.goldenfrog.com Turkey', 'us3.vpn.goldenfrog.com USA - Austin', 'us6.vpn.goldenfrog.com USA - Chicago', 'us1.vpn.goldenfrog.com USA - Los Angeles', 'us4.vpn.goldenfrog.com USA - Miami', 'us5.vpn.goldenfrog.com USA - New York', 'us7.vpn.goldenfrog.com USA - San Francisco', 'us8.vpn.goldenfrog.com USA - Seattle', 'us2.vpn.goldenfrog.com USA - Washington', 'ae1.vpn.goldenfrog.com United Arab Emirates', 'uk1.vpn.goldenfrog.com United Kingdom', 'vn1.vpn.goldenfrog.com Vietnam']

class MyVPN():
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        while True:
            try:
                print "Using auth", self.username, self.password
                output = subprocess.check_output(
                    ['timeout', VPN_setting['timeout'], 'vyprvpn', 'l', self.username, self.password])
                # output = subprocess.check_output(['vyprvpn', 'login', 'cobbbak@gmail.com','1q2w#E$R'])
                print ('Have successfully login')
                print (output)
                if '401: Not authorized' in output:
                    self.refresh()
                    continue

                if '500' in output:
                    self.refresh()
                    continue
                break
            except subprocess.CalledProcessError, e:
                print  e.output


            except Exception as ex:
                print 'exception ' + str(ex)
                self.logout()
                self.login()

    def logout(self):
        while (True):
            try:

                output = subprocess.check_output(['timeout', VPN_setting['timeout'], 'vyprvpn', 'logout'])

                print (output)
                break
            except subprocess.CalledProcessError, e:
                print  e.output


            except Exception as ex:
                print 'exception ' + str(ex)

    def connect(self):
        while True:
            try:
                # output = subprocess.check_output(['timeout','20s','vyprvpn', 'connect',])
                print ('try to connect')
                output = subprocess.check_output(['timeout', VPN_setting['timeout'], 'vyprvpn', 'connect', ])

                print output
                break

            except subprocess.CalledProcessError, e:
                print e.output
                self.disconnect()
                self.logout()
                self.kill_vypervpn()
                self.login()


            except subprocess.CalledProcessError, e:

                print "Ping stdout output:\n", e.output

            except Exception as ex:
                print 'exception ' + str(ex)
                self.disconnect()
                time.sleep(1)

    def disconnect(self):
        while True:
            try:
                output = subprocess.check_output(['timeout', VPN_setting['timeout'], 'vyprvpn', 'd'])
                print ('Have %d bytes in output' % len(output))
                print output
                self.kill_vypervpn()
                break

            except subprocess.CalledProcessError, e:
                print "Ping stdout output:\n", e.output


            except Exception as ex:
                print 'exception ' + str(ex)

    def random_server(self):
        while True:
            try:
                self.disconnect()
                self.logout()
                self.login()
                current_server = subprocess.check_output(['timeout', '20s', 'vyprvpn', 'server', 'show'])
                print ('Current server ' + str(current_server))
                server_list = subprocess.check_output(['timeout', '20s', 'vyprvpn', 'server', 'list']).split('\n')
                if server_list[0] == "VyprVPN Servers":
                    del server_list[0]
                if server_list[len(server_list) - 1] == "":
                    del server_list[len(server_list) - 1]

                print ('try to set a random server')
                shuffle(server_list)
                splited_server = server_list[0].split(' ')
                command_list = ['timeout', '20s', 'vyprvpn', 'server', 'set']
                for one in splited_server:
                    command_list.append(one)
                output = subprocess.check_output(command_list)
                print (str(output))
                current_server = subprocess.check_output(['timeout', '20s', 'vyprvpn', 'server', 'show'])
                print ('New server ' + str(current_server))
                break

            except subprocess.CalledProcessError, e:
                print "Ping stdout output:\n", e.output
                self.login()



            except Exception as ex:
                print 'exception ' + str(ex)

    def refresh(self):
        try:
            output = subprocess.check_output(['timeout', '20s', 'vyprvpn', 'refresh'])
            print ('Have %d bytes in output' % len(output))
            print (output)
        except subprocess.CalledProcessError, e:
            print "Ping stdout output:\n", e.output


        except Exception as ex:
            print 'exception ' + str(ex)

    def kill_vypervpn(self):

        try:
            output = subprocess.check_output(['ps', 'aux', '|', 'grep', '[v]pn', '|', 'grep', '$USER', '|', 'awk', '{print $2}', '|', 'xargs' ,'kill' ,'-9'],shell=True)
            output = subprocess.check_output(['ps', 'aux', '|', 'grep', '[v]pn', '|', 'grep', '$USER', '|', 'awk', '{print $2}', '|', 'xargs' ,'kill' ,'-9'],shell=True)
            print ('Have %d bytes in output' % len(output))
            #print (output)
        except subprocess.CalledProcessError, e:
            print "Ping stdout output:\n", e.output


if __name__ == "__main__":
    try:
        m = MyVPN(username=VPN_setting['username'], password=VPN_setting['password'])
        m.random_server()
        # m.kill_vypervpn()
        m.login()
        m.connect()
        m.disconnect()
        m.logout()
    except Exception as ex:
        print (str(ex))
