#!/bin/bash
counter=0
failedCount=0
for file in $(find | grep '.py');
    do
        #echo "Running file $file..."
        if python "$file" ;
        then
            counter=$((counter + 1))
        else
            failedCount=$((failedCount + 1)) 
        fi
    done;

echo "Executed $counter python files successfully"
echo "$failedCount python files failed"