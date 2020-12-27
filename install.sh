#!/bin/bash

chmod +x fileSorter.py
mkdir ~/bin
cp fileSorter.py ~/bin/fileSorter
sudo echo 'export PATH=$PATH":$HOME/bin"' >> ~/.bashrc
source ~/.bashrc
echo -e "Installation complete.\nNow you can simply type '"fileSorter path/to/directory"' to use fileSorter.\n\nNote: Don't execute this script more than once! \n"
