count = 0
for file in "Problems/*"
do
python $file
count = $((count + 1))
done

echo "Executed $count python files successfully"