#!/bin/bash
echo "====== BBR_POWERED ======"
lsmod |grep 'bbr'
wget --no-check-certificate -qO 'BBR_POWERED.sh' 'https://moeclub.org/attachment/LinuxShell/BBR_POWERED.sh' && chmod a+x BBR_POWERED.sh && bash BBR_POWERED.sh
lsmod |grep 'bbr_powered'
echo "====== new user ======"
adduser liang
usermod -a -G sudo liang
echo "====== change PWD of root ======"
sudo passwd root
echo "====== shadowsocks ======"
sudo apt-get install -y python-pip
sudo pip install -y shadowsocks
sudo apt-get install -y python-m2crypto
echo -e "{\n "server":"66.122.222.250",\n "server_port":28888,\n "local_address": "127.0.0.1",\n "local_port":1080,\n "password":"16908888",\n "timeout":300,\n "method":"rc4-md5"\n }" > /etc/shadowsocks.json
sudo chmod 755 /etc/shadowsocks.json
sudo useradd ssuser
echo "/usr/local/bin/ssserver -c /etc/shadowsocks.json -d start --user ssuser" >> /etc/rc.local
echo "====== nginx ======"
sudo apt-get update
sudo apt-get install -y nginx

echo "====== https ======"
curl  https://get.acme.sh | sh
cd ~/.acme.sh/
export DP_Id="2s83RtmH4v_VYdsZMv43pLsofGHDjNyhv"
export DP_Key="VYduoJBYjg5oPhuFNYobaC"