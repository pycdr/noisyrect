cloneFromGit(){
	echo '[*error*] "noisyrect" file not found!'
	git clone https://github.com/pycdr/noisyrect
	echo '[*git*] git cloned from https://github.com/pycdr/noisyrect'
	mv ./noisyrect/* .
	echo '[*start*]'
	./noisyrect.pyc
}
compileSource(){
	echo '[*error*] error when clone'
	echo '[*py3compile*] compile "source.py" ...'
	py3compile source.py
	echo '[*fine*] compiled'
	mv ./__pycache__/* ./__pycache__/noisyrect.pyc
	mv ./__pycache__/* .
	rm -r ./__pycache__
	echo '[*start*]'
	./noisyrect.pyc
}
echo '[*start*]'
./noisyrect.pyc || compileSource || cloneFromGit || echo '[*error*] error when run game :('
echo '[*end*] exit...'
exit
