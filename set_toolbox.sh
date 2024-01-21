if [ -z "$DIR_TOOLBOX" ]; then

    declare -x DIR_TOOLBOX=$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")
    echo "set DIR_TOOLBOX to $DIR_TOOLBOX"

    declare -x PYTHONPATH=$DIR_TOOLBOX
    echo "set PYTHONPATH to $PYTHONPATH"

    declare -x PATH=$DIR_TOOLBOX:$PATH
    echo "Added $DIR_TOOLBOX to PATH"

    declare -x DIR_PYTOOLS=$DIR_TOOLBOX/pytools
    echo "set DIR_PYTOOLS to $DIR_PYTOOLS"

else

    echo "Already sourced ${BASH_SOURCE[0]}"

fi
