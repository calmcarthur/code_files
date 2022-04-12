#!/bin/bash
# script to run tests 'x' amount of times and report pass or fail based on hardcoded conditionals

MASTER_COUNTER=0
PASS_COUNTER=0
FAIL_COUNTER=0
END_BOOL=0
START_BOOL=0
START_COUNTER=0
LINE_TO_PARSE=7
REPO_NAME=""
TEST_FILE=""

rm output.txt 2> /dev/null || true

while [ "$START_BOOL" -eq 0 ]
do

    printf "Enter the path to the repo from your home directory (ex. Documents/code_repos/7127): "
    read -r REPO_NAME
    printf "Enter the testfile name (ex. test_o2_sensor): "
    read -r TEST_FILE
    printf "Enter the number of times you want to run the test: "
    read -r NUMBER_TEST

    PATH_TO_FILE="${HOME}/${REPO_NAME}/build/bin/${TEST_FILE}"

    if [ -f "$PATH_TO_FILE" ]
        then
            START_BOOL=1

    else
        echo "Invalid path, please try again."

    fi

done

while [ $END_BOOL -eq 0 ];
do

    $PATH_TO_FILE >> "output.txt"

    let MASTER_COUNTER++
    echo "Test ${MASTER_COUNTER} Running..."

    # ---------------------------------------------------
    # HARDCODED CONDITIONAL -- WILL NOT WORK FOR ALL TESTS
    
    LINE=$(sed "${LINE_TO_PARSE}q;d" output.txt)

    if [[ "$LINE" == *"OK"* ]];

        then 
            let "PASS_COUNTER=PASS_COUNTER+1"
            let "LINE_TO_PARSE = LINE_TO_PARSE + 13"
        
        else
            let "FAIL_COUNTER=FAIL_COUNTER+1"
            let "LINE_TO_PARSE = LINE_TO_PARSE + 40"
    
    fi
    
    # ---------------------------------------------------

    if [ "$MASTER_COUNTER" -eq "$NUMBER_TEST" ];

        then
            END_BOOL=1

        else
            continue
    
    fi

done

echo "PASSES: ${PASS_COUNTER} | FAILS: ${FAIL_COUNTER}"
