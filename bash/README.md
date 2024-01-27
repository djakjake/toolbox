# **bash**

This is the safe space for all general bash scripts in the toolbox. The `set_toolbox.sh` script exists directly in the `toolbox` home directory.

# **scripts**

## **choose_default_os.sh**

This script is used to update the default boot option on a multi-boot compututer (eg: Windows 10 and Ubuntu).

1) displays all the current boot options
1) prompts the user to copy the identifier of the OS they wish to boot by default and indicates how to make the update.
1) **NOTE: requires user interaction** waits for the user to indicate that they are ready
1) opens the necessary file
1) **NOTE: requires user interaction** the user needs to copy the OS ID into the `DEFAULT_GRUB` line. Once this is done, the user needs to save and exit the file.
1) runs the update.

## **get_git_branch.sh**

This script exports the function to the bash environment, `get_git_branch`.

If the current working directory belongs to a git repository, it returns the active branch name; otherwise, it returns "NOT A GIT REPO".

I personally use this to set up my curser in my `~/.bashrc`:
```bash
reset='\e[0m'
light_red='\e[91m'
light_yellow='\e[93m'
light_green='\e[92m'
light_blue='\e[94m'

PS1="$light_red\d \t$reset | $light_yellow\s\v$reset | $light_green\$(get_git_branch)$reset | $light_blue\w$reset\n>> "
```

## **setEnv.sh $1**

This script is used to set up and/or activate a virtual python environment.

- must receive valid directory as `$1`
- Creates a new python virtual environment at `$1/vEnv`, if it doesn't already exist.
- Activates `$1/vEnv`
- if a `requirements.txt` file exists in `$1`, installs requirements.

## **update.sh**

- fetches and installs the latest stable release of Chrome
- updates all known packages
- removes any unnecessary packages
- upgrades known packages to any newer versions

