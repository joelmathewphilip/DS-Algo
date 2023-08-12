cd Problems
count = 0
for file in *.py;
    do
        python "$file"
        count = $((count + 1))
    done

echo "Executed $count python files successfully"