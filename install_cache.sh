sudo apt-get build-dep trafficserver

autoconf automake autotools-dev bison debhelper dh-apparmor flex gettext intltool-debian libbison-dev libcap-dev \
libexpat1-dev libfl-dev libpcre3-dev libpcrecpp0 libsigsegv2 libsqlite3-dev libssl-dev libtool m4 po-debconf \
tcl-dev tcl8.6-dev zlib1g-dev

sudo apt-get install libhwloc-dev libhwloc5 libunwind8 libunwind8-dev

sudo apt-get install software-properties-common python-software-properties

sudo add-apt-repository ppa:ubuntu-toolchain-r/test

apt-get update

cat > /etc/apt/preferences.d/xenial

apt-get -t xenial install gcc-7 g++-7

sudo apt-get install clang-5.0

sudo apt-get install git git-core

./configure && make

make check

sudo make install

cd /opt/ts
sudo bin/traffic_server -R 1
