## setup
cp .tmux.conf ~/   
cp tmux@.service /usr/lib/systemd/system/   
cp init_tmux.sh /usr/local/bin   
sudo systemctl enable/start/status tmux@username