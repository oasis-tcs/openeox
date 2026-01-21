#!/bin/bash

ORIG_SCHEMA=eox-core-v-1-0/schema/eox-core.json
META_SCHEMA=eox-core-v-1-0/schema/meta.json
VALIDATOR=eox-core-v-1-0/test/validator.py
STRICT_GENERATOR=eox-core-v-1-0/test/generate_strict_schema.py
TESTPATH=eox-core-v-1-0/test/validator/data/$1/*.json
EXCLUDE='oasis_openeox_tc-core-1_0-2025-6-1-02-01.json|oasis_openeox_tc-core-1_0-2025-6-1-02-03.json'
EXCLUDE_LEAP='oasis_openeox_tc-core-1_0-2025-6-1-02-02.json'

FAIL=0

# go to root of git repository
cd `dirname $0`/../../..

validate() {
  printf "%s" "Testing file $1 against schema ${SCHEMA} ... "
  if python3 $VALIDATOR $SCHEMA $1 ${META_SCHEMA}; then
    printf "%s\n" SUCCESS
  else
    printf "%s\n" FAILED
    FAIL=1
  fi

}

test_all() {
  for i in $(ls -1 ${TESTPATH} | grep -Ev "${EXCLUDE}" | grep -Ev "${EXCLUDE_LEAP}")
  do
    validate $i
  done
}

SCHEMA=$ORIG_SCHEMA
test_all

exit ${FAIL}
