#!/home/~
ISO_NAME = $1
IMAGE_NAME = $2

echo "Creating image and emulating."
qemu-img create -f qcow2 $2.img 5G
qemu-img create -f qcow2 $2.qcow2 5G
qemu-system-x86_64 -enable-kvm -cdrom $1 -boot menu=on -drive file=$2 -m 5G