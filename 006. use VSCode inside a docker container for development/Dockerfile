FROM python:3.10-alpine

# designate a working directory
WORKDIR /project

# copy and install dependencies
COPY ./requirements.txt ./
# --no-cache-dir flag signals not to create cache directory
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the source directory which contains the code
COPY ./src ./src

# Command to run the app
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]