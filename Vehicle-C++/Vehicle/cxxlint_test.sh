#Fail if any command exit with error.
set -e

#exits if no directory is given as an arg
string=$1
if ((${#string} <= 0));
then
    echo No dir arg given
    exit 1
fi

# Runs cppcheck on all files within this files structure
echo
echo "############ Linting $1 dir ##############"
echo
cppcheck --quiet --enable=all --language=c++ --suppress=missingIncludeSystem --suppress=unusedFunction $1
echo
echo "LINTING COMPLETE"
