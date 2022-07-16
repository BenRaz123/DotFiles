cd ~;
for entry in `ls -A ~/Downloads/BenRazProjects/DotFiles/theFiles`; do
    ln -s -F ~/Downloads/BenRazProjects/DotFiles/theFiles/$entry ~/$entry;
done
