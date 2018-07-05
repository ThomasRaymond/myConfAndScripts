## setup
cp .tmux.conf ~/   
sudo cp tmux@.service /usr/lib/systemd/system/   
sudo cp init_tmux.sh /usr/local/bin   
sudo systemctl enable/start/status tmux@username

##add plugins
mkdir -p ~/.tmux/plugins
git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm
