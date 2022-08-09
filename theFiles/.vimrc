autocmd BufWritePost *.tex execute '!pdflatex <afile>; open *.pdf'
inoremap " ""<left>
inoremap ' ''<left>
inoremap ( ()<left>
inoremap [ []<left>
inoremap { {}<left>
inoremap {<CR> {<CR>}<ESC>O
inoremap {;<CR> {<CR>};<ESC>O

start
syntax on
filetype indent on
set number
set autoindent
set smartindent
set tabstop=3
set expandtab
set shiftwidth=2

" Vim-Plug Stuff

" Plugins will be downloaded under the specified directory.
call plug#begin(has('nvim') ? stdpath('data') . '/plugged' : '~/.vim/plugged')

" Declare the list of plugins.

Plug 'lervag/vimtex'
Plug 'junegunn/seoul256.vim'
Plug 'sainnhe/sonokai'
Plug 'dracula/vim'
Plug 'sheerun/vim-polyglot'
Plug 'ghifarit53/tokyonight-vim'

" List ends here. Plugins become visible to Vim after this call.
call plug#end()
