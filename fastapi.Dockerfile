FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install -r requirements-dev.txt

EXPOSE 5005

CMD ["uvicorn", "src.ui.fastapi_ui:app", "--host", "0.0.0.0", "--port", "5005"]
