test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

conda init --all

conda activate assignment-7-swe4s

run test_for