#!/usr/bin/env bash
python create_project_dir.py -src ../submissions/proj2/ -dst proj2/ -p P2
rm -rf __pycache__

for project in */ ; do
	for student in $project*; do
		echo $student >> grades.txt
		cd $student
		python autograder.py >> ../../grades.txt
		cd "$OLDPWD"
	done
done

python save_grades.py -dst proj2/