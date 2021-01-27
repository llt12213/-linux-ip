while :

do

	curl https://httpbin.org/ip >mail.txt

	python mail.py

	printf "Done \n"

	sleep 1h
done
