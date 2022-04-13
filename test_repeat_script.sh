#!/bin/bash
# script to run tests 'x' amount of times and report pass or fail based on hardcoded conditionals

MASTER_COUNTER=0
PASS_COUNTER=0
FAIL_COUNTER=0
END_BOOL=0
START_BOOL=0

while [ "$START_BOOL" -eq 0 ]
do

    printf "Enter the path to the repo from your home directory (ex. Documents/code_repos/7127): "
    read -r REPO_NAME
    printf "Enter the testfile name (ex. test_o2_sensor): "
    read -r TEST_FILE
    printf "Enter the number of times you want to run the test: "
    read -r NUMBER_TEST
    printf "Enter 'q' for no output file. If output is desired, enter chosen file name (ex. output_file): "
    read -r OUTPUT_FILE

    PATH_TO_FILE="${HOME}/${REPO_NAME}/build/bin/${TEST_FILE}"

    if [ -f "$PATH_TO_FILE" ];
        then
            START_BOOL=1

    else
        echo "Invalid path, please try again."

    fi

done

if [ "$OUTPUT_FILE" = "q" ];
    then
        OUTPUT_FILE=".${OUTPUT_FILE}.txt"
        rm $OUTPUT_FILE 2> /dev/null || true
    else
        OUTPUT_FILE="${OUTPUT_FILE}.txt"
        rm $OUTPUT_FILE 2> /dev/null || true
fi

LINE_TO_PARSE=7

while [ $END_BOOL -eq 0 ];
do

    $PATH_TO_FILE >> $OUTPUT_FILE

    let MASTER_COUNTER++
    echo "Test ${MASTER_COUNTER} Running..."

    # ---------------------------------------------------
    # HARDCODED CONDITIONAL -- WILL NOT WORK FOR ALL TESTS
    # TO TAILOR TO DIFFERENT TESTS:
    # CHANGE INITIAL LINE (LINE_TO_PARSE=7), PASS KEY (OK), AND LINE INCREMENTS (+ 13, + 40)
    
    LINE=$(sed "${LINE_TO_PARSE}q;d" ${OUTPUT_FILE})

    if [[ "$LINE" == *"OK"* ]];

        then 
            # PASS
            let "PASS_COUNTER=PASS_COUNTER+1"
            let "LINE_TO_PARSE = LINE_TO_PARSE + 13"
        
        else
            # FAIL
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

if [ "$OUTPUT_FILE" = ".q.txt" ];
    then
        rm $OUTPUT_FILE 2> /dev/null || true
    else
        :
fi

echo "PASSES: ${PASS_COUNTER} | FAILS: ${FAIL_COUNTER}"
