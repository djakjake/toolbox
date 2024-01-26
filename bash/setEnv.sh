# - must receive valid directory as `$1`
# - Creates a new python virtual environment at `$1/vEnv`.
# - Activates `$1/vEnv`
# - if a `requirements.txt` file exists in `$1`, installs requirements.

if [ -z "$DIR_VENV" ]; then

    # make sure an argument was given
    if [ -n "$1" ]; then
        DIR_VENV_RECEIVED="$(readlink -f "$1")"
        echo "received directory for virtual environment: $DIR_VENV_RECEIVED"
    else
        echo "ERROR: did not receive directory to place virtual environment!"
        exit 1
    fi

    # make sure directory exists
    if [ ! -d $DIR_VENV_RECEIVED ]; then
        echo "ERROR: $DIR_VENV_RECEIVED is not a valid directory"
        exit 2
    fi

    # derive directory location to place virtual environment
    declare -x DIR_VENV=$DIR_VENV_RECEIVED/vEnv
    echo "set DIR_ENV to $DIR_ENV"

    # create the virtual environment, if it doesn't already exist
    if [ ! -d $DIR_VENV ]; then
        echo "creating new virtual environment at $DIR_VENV"
        python3 -m venv $DIR_VENV
    else
        echo "environment $DIR_ENV already exists. skipping."
    fi

    # activate the virtual environment
    source $DIR_VENV/bin/activate

    # if a requirements.txt file exists, make sure they are installed
    FILE_VENV_REQS=$DIR_VENV_RECEIVED/requirements.txt
    if [ -f $FILE_VENV_REQS ]; then
        echo "checking installation of requirements in $FILE_VENV_REQS"
        pip install -r $FILE_VENV_REQS
    else
        echo "no requirements found in $FILE_VENV_REQS. skipping."
    fi

else

    echo "A virtual environment has already been sourced. You may want to type `deactivate` in your shell and re-run the command."

fi
