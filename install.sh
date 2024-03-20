#!/bin/bash
apt-get update && apt-get upgrade
sudo sed -i -e 's/#GRUB_TERMINAL/GRUB_TERMINAL/g' /etc/default/grub
