function get_git_branch {
    if [[ $(git rev-parse --is-inside-work-tree 2> /dev/null) == true ]]; then
        #git rev-parse --abbrev-ref HEAD 2>/dev/null
        echo $(git symbolic-ref --short HEAD)
    else
        echo NOT A GIT REPO
    fi
}
export -f get_git_branch
