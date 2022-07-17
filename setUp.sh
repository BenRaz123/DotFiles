cd theFiles;
brew bundle
FILES=$PWD;
cd ~;
for entry in `ls -A $FILES`; do
    ln -s -F $FILES/$entry ~/$entry;
done
