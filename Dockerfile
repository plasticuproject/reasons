FROM python:3
ADD reasons.py /
RUN pip install requests
RUN pip install -U discord.py
CMD ["python", "./reasons.py"]
