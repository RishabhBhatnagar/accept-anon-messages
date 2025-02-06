serve:
	python3 main.py & 
	sleep 2
	ngrok http 5000
