# Use Ubuntu as the base image
FROM ubuntu:latest

# Set environment variables to non-interactive (to avoid prompts during installation)
ENV DEBIAN_FRONTEND=noninteractive

# Update and install PHP, cron, and other necessary utilities
RUN apt-get update && apt-get install -y \
    php \
    php-cli \
    php-mysql \
    cron \
    curl \
    php-xml \
    && rm -rf /var/lib/apt/lists/*

# Install WP-CLI
RUN curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar \
    && chmod +x wp-cli.phar \
    && mv wp-cli.phar /usr/local/bin/wp

# Create a new user "wpuser" and switch to it
RUN useradd -m -d /home/wpuser -s /bin/bash wpuser
USER wpuser

# Set working directory
WORKDIR /var/www/html

# Setup cron jobs
# Create a cron file
RUN echo "* * * * * /usr/local/bin/wp cron event run --due-now --path=/var/www/html" > /tmp/crontab_wpuser
RUN echo "* * * * * /usr/local/bin/wp action-scheduler run --path=/var/www/html" >> /tmp/crontab_wpuser

# Apply cron job for wpuser
RUN crontab /tmp/crontab_wpuser && rm /tmp/crontab_wpuser

# Switch back to root to run the cron service
USER root

# Start cron in the foreground
CMD ["cron", "-f"]
