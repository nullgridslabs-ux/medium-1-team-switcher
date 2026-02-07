FROM python:3.11-slim
WORKDIR /app
COPY app.py .
RUN pip install flask flask-session
ENV FLAG=CTF{medium_team_switch}
EXPOSE 5000
CMD ["python","app.py"]
