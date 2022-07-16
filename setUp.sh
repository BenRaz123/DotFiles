FILES=$PWD;
cd ~;
for entry in `ls -A $FILES/theFiles`; do
    ln -s -F $FILES/theFiles/$entry ~/$entry;
done
