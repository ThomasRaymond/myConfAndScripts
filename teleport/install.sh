#! /bin/bash
[ ! $(id -u) != "0" ] || { echo "ERROR: You must be root"; exit 1; }

wget https://github.com/gravitational/teleport/releases/download/v2.4.7/teleport-v2.4.7-linux-amd64-bin.tar.gz
tar -xvf teleport-v2.4.7-linux-amd64-bin.tar.gz

BINDIR=/usr/local/bin
etcDIR=/etc/teleport
VARDIR=/var/lib/teleport
systemdDIR=/usr/lib/systemd/system/
cd teleport
mkdir -p $VARDIR $BINDIR $systemdDIR $etcDIR
cp -f teleport tctl tsh $BINDIR/
cd .. && rm teleport-v2.4.7-linux-amd64-bin.tar.gz

#