 #!/usr/bin/env python

function buat(){
	python3 buat.py
    git init
    git remote add origin https://github.com/Ivan-Ramadhan/$1.git
    git add .
    git commit -m "Initial commit"
    git push -u origin master

}
