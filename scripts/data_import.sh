#!/bin/bash

# Define path to the data file
DATA_FILE="./data/expense_data.csv"

# Import data into PostgreSQL
psql -h $DB_HOST -U $DB_USERNAME -d $DB_NAME -c "\COPY expenses FROM $DATA_FILE DELIMITER ',' CSV HEADER;"

echo "Data import completed from $DATA_FILE"