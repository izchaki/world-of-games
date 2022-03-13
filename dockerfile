FROM baseImage:python
WORKDIR /app
COPY . .
RUN python3 main_game.py