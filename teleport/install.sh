#! /bin/bash
[ ! $(id -u) != "0" ] || { echo "ERROR: You must be root"; exit 1; }

wget https://github.com/gravitational/teleport/releases/download/v2.4.7/teleport-v2.4.7-linux-amd64-bin.tar.gz
tar -xvf teleport-v2.4.7-linux-amd64-bin.tar.gz

BINDIR=/usr/local/bin
VARDIR=/var/lib/teleport
cd $(dirname $0)
mkdir -p $VARDIR $BINDIR
cp -f teleport tctl tsh $BINDIR/
rm teleport-v2.4.7-linux-amd64-bin.tar.gz

#