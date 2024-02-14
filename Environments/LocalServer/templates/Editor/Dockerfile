FROM wordpress:cli

COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

ENV PATH="${PATH}:/home/www-data/.composer/vendor/bin"

RUN composer global config --no-plugins allow-plugins.dealerdirect/phpcodesniffer-composer-installer true

RUN composer -n global --dev require phpstan/phpstan

RUN composer -n global require --dev "squizlabs/php_codesniffer=*"
RUN composer -n global require --dev dealerdirect/phpcodesniffer-composer-installer

RUN composer -n global require --dev phpcompatibility/phpcompatibility-wp:"*"
RUN composer -n global require --dev wp-coding-standards/wpcs:"^3.0"

RUN wp package install wp-cli/doctor-command:@stable

RUN wp package install wp-cli/profile-command:@stable

WORKDIR /www