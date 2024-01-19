# display the options
fgrep menuentry /boot/grub/grub.cfg
# make sure user has enough time to see the options and knows what to do.
printf "\
    \nfrom the above options, select which os should be the default\
    \neg: 'Windows 10 (on /dev/sda1)' or 'Ubuntu'\
    \nwhen the file opens, replace the option on the line with 'DEFAULT_GRUB' with your selected option.\
    \nsave and close the file.\n"
read -p "are you ready? (y/n) " ready
if [ "$ready" == "y" ]; then
    # open the file, user will then make changes to the file, save, and quit.
    sudo vim /etc/default/grub
    # run the update
    sudo update-grub
else
    echo "oops, run me again when you are ready."
fi
