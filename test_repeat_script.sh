#!/bin/bash
# script to run google test 'x' amount of times and report pass/fail count
# to tailor to non-googletest tests, modify the grep regex in the calculate_score function

take_input () {

	START_BOOL=0

	# take user conditions and validate given path
	while [ "$START_BOOL" -eq 0 ]
	do

	    printf "Enter the path to the test binary from your home directory (ex. Documents/code_repos/7127/build/bin/test_o2_sensor): "
	    read -r REPO_NAME
	    printf "Enter the number of times you want to run the test: "
	    read -r NUMBER_TEST
	    printf "Enter 'q' for no output file. If output is desired, enter chosen file name (ex. output_file): "
	    read -r OUTPUT_FILE

	    PATH_TO_FILE="${HOME}/${REPO_NAME}"

	    if [ -f "$PATH_TO_FILE" ];
			then
				START_BOOL=1

			else
				echo "Invalid path, please try again."
	    fi

	done
	
}

run_tests () {

	END_BOOL=0
	MASTER_COUNTER=0

	# delete OUTPUT_FILE if exists and set OUTPUT_FILE variable
	if [ "$OUTPUT_FILE" = "q" ];
	    then
			OUTPUT_FILE=".${OUTPUT_FILE}.txt"
			rm $OUTPUT_FILE 2> /dev/null || true

	    else
			OUTPUT_FILE="${OUTPUT_FILE}.txt"
			rm $OUTPUT_FILE 2> /dev/null || true
	fi

	# run tests 'x' times
	while [ $END_BOOL -eq 0 ];
	do

	    $PATH_TO_FILE >> $OUTPUT_FILE

	    let MASTER_COUNTER++
	    echo "Test ${MASTER_COUNTER} Running..."


	    if [ "$MASTER_COUNTER" -eq "$NUMBER_TEST" ]
			then
				END_BOOL=1

			else
				continue
	    fi

	done
	
	calculate_score
	delete_file

}

calculate_score () {

	PASS_COUNTER=0
	FAIL_COUNTER=0

	# PASS TALLY
	while read -r PASS_LINE; do
		let "PASS_COUNTER=PASS_COUNTER+${PASS_LINE}"
	done < <(grep "\[  PASSED  \]" ${PWD}/${OUTPUT_FILE} | grep "test" | grep -o '[[:digit:]]*')

	# FAIL TALLY
	while read -r FAIL_LINE; do
		let "FAIL_COUNTER=FAIL_COUNTER+${FAIL_LINE}"
	done < <(grep "\[  FAILED  \]" ${PWD}/${OUTPUT_FILE} | grep "test" | grep -o '[[:digit:]]*')

	# print passes and fails
	echo "PASSES: ${PASS_COUNTER} | FAILS: ${FAIL_COUNTER}"

}

delete_file () {

	# if specified, delete output file
	if [ "$OUTPUT_FILE" = ".q.txt" ];
	    then
			rm $OUTPUT_FILE 2> /dev/null || true

	    else
		:
	fi

}

# main
take_input
run_tests
