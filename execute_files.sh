#!/bin/bash
counter=0
#files=$(find | grep '.py')
#echo $files
for file in $(find | grep '.py');
    do
        echo "Running file $file..."
        python "$file"
        counter=$((counter + 1))
    done;

echo "Executed $counter python files successfully"