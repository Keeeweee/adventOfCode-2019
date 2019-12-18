#!/bin/bash

set -e

if [ $# -eq 0 ]
  then
    echo "Please indicate day number you want to create."
    exit 0
fi

DAY=$1

echo "Creating day " "$DAY"

DAY_PATH="day-$DAY"
DATA_PATH="data"

[ -d "$DAY_PATH" ] && echo "Directory $DAY_PATH already exists." && exit 0

mkdir "$DAY_PATH"
touch "$DAY_PATH/first.py"
touch "$DAY_PATH/second.py"

mkdir "$DAY_PATH/$DATA_PATH"
touch "$DAY_PATH/$DATA_PATH/data.txt"
touch "$DAY_PATH/$DATA_PATH/statement.html"

echo "Done."
