# view system and environmental info that is being used by toolbox

# grab os version
OS_VERSION=$(lsb_release -ds)

# grab bash version (already exists)

# grab python version
PYTHON_VERSION=$(python --version)

# grab g++ compiler version
GPP_COMPILER_VERSION=$(g++ --version | grep g++)

# display results
printf "OS AND ENVIRONMENT\
      \n==================\
      \nOS          : $OS_VERSION\
      \npython      : $PYTHON_VERSION\
      \ng++ compiler: $GPP_COMPILER_VERSION\
      \n"
