FROM python:3.9.18

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "src/roh-moo-hyun/extract_speech_from_pdf.py"]