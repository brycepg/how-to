# Fish Shell

##### Environment variables
 `set -x EDITOR nvim`  
to set the default EDITOR to nvim (for git, etc)

##### Alias

Use functions

    function lsp
        ls -ah --color=always $argv | less -R
    end

http://askubuntu.com/questions/19728/differences-between-fish-and-bash-to-pass-commandline-arguments-to-alias-functio
