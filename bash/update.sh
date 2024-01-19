
# getting latest packages
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
#echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | sudo tee /etc/apt/sources.list.d/google-chrome.list

# install specific packages
sudo apt install google-chrome-stable

# updating known packages
sudo apt update

# removing uncessary packages
sudo apt autoremove

# upgrading known packages to newer versions
sudo apt upgrade
