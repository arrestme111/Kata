# Define the base image to use.
FROM alpine

# Set the working directory.
WORKDIR /home/kata

# Install Python.
RUN apk add --no-cache python3

# Copy our source code.
COPY backend.py backend.py
COPY index.html index.html

# Create a non-root user with no password (-D).
RUN adduser -D -h /home/kata kata

# Set permissions.
RUN chown -R kata:kata /home/kata

# Switch to a non-root user.
USER kata

# Identify what TCP port will be used by our server.
EXPOSE 8000

# Start the server.
CMD ["python3", "backend.py"]
