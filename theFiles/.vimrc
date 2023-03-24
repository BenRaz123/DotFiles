colorscheme default 

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
set tabstop=4
set expandtab
set shiftwidth=4

" Vim-Plug Stuff

" Plugins will be downloaded under the specified directory.
call plug#begin(has('nvim') ? stdpath('data') . '/plugged' : '~/.vim/plugged')

" Declare the list of plugins.

Plug 'vim-autoformat/vim-autoformat'
Plug 'prettier/vim-prettier', { 'do': 'yarn install --frozen-lockfile --production' }
Plug 'lithammer/nvim-pylance'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'ervandew/supertab'
Plug 'lervag/vimtex'
Plug 'junegunn/seoul256.vim'
Plug 'sainnhe/sonokai'
Plug 'dracula/vim'
Plug 'sheerun/vim-polyglot'
Plug 'ghifarit53/tokyonight-vim'

" List ends here. Plugins become visible to Vim after this call.
call plug#end()
