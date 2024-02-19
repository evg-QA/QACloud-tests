FROM python:3.11

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /usr/project

# Create a volume for test results
VOLUME /usr/project/allure_results

# Copy requirements file and install dependencies
COPY requirements.txt /usr/project/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project code
COPY .. /usr/project

# Set the default command to run tests with Pytest
CMD ["pytest"]

