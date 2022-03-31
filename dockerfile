FROM izchaki/selenium
WORKDIR /app
COPY ./templates ./templates
COPY ./MainScores.py ./MainScores.py
COPY ./Scores.txt ./Scores.txt
COPY ./e2e.py ././e2e.py
COPY ./start.sh ./start.sh
EXPOSE 5001
