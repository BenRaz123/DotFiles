code () { VSCODE_CWD="$PWD" open -n -b "com.microsoft.VSCode" --args $* ;}
# Setting PATH for Python 3.10
# The original version is saved in .zprofile.pysave
PATH="/Library/Frameworks/Python.framework/Versions/3.10/bin:${PATH}"
export PATH

zsh ~/script.sh;

##
# Your previous /Users/johnbananas/.zprofile file was backed up as /Users/johnbananas/.zprofile.macports-saved_2022-08-26_at_12:11:26
##

# MacPorts Installer addition on 2022-08-26_at_12:11:26: adding an appropriate PATH variable for use with MacPorts.
export PATH="/opt/local/bin:/opt/local/sbin:$PATH"
# Finished adapting your PATH environment variable for use with MacPorts.

. "$HOME/.cargo/env"
