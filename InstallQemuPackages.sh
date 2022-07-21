#!/home/~

clear
echo "Cloning into git repository"
git clone https://gitlab.com/qemu-project/qemu.git
pip3 install ninja --user
cd qemu
git submodule init
git submodule update --recursive
./configure
echo "Now installing necessary dependancies. Git comfy, this is gonna take a while..."
make
sudo make install
echo "All done!"