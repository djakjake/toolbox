function replace {
    # $1 - substring to replace
    # $2 - subtstring to replace with
    # $3 - (optional) directory to replace all instances of $1 with $2. if not received, will use current working directory
    
    # if $3 was given, make sure it is a valid directory and cd to it
    if [ -n "$3" ]; then
        if [ -d "$3" ]; then
            cwd=$(pwd)
            cd $3
        else
            echo "$3 is not a valid directory!"
            exit 1
        fi
    fi
    
    # print what will be replaced
    printf "replacing: $1\
          \nwith     : $2\
          \nin       : $(pwd)\n"
    
    # execute replacement
    grep -lr "$1" | xargs sed -i "s/$1/$2/g"
    
    # if $3 was given, change back to initial directory
    if [ -n "$3" ];
        then cd $cwd
    fi
}
export -f replace
