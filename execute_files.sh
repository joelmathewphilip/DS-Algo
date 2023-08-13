#!/bin/bash
counter=0
failedCount=0
failedFileNames=()
for file in $(find | grep '.py');
    do
        #echo "Running file $file..."
        if python "$file" ;
        then
            counter=$((counter + 1))
        else
            failedCount=$((failedCount + 1)) 
             failedFileNames+=($file)   
        fi
    done

echo "Executed $counter python files successfully"
if [ $failedCount -eq 0 ] ;
then
echo "Execution of $failedCount python files failed."
else
echo "Execution of $failedCount (name below) python files failed."
for value in "${failedFileNames[@]}"
do
echo $value
done
exit 1
fi
