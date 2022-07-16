FILES=$PWD;
cd ~;
for entry in `ls -A ~/Downloads/BenRazProjects/DotFiles/theFiles`; do
    ln -s -F $FILES/$entry ~/$entry;
done
