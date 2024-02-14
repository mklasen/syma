FROM wordpress:php8.2-fpm-alpine

RUN apk update \
    && apk add  --no-cache git mysql-client curl libmcrypt libmcrypt-dev openssh icu-dev \
    libxml2-dev freetype-dev libpng-dev libzip-dev libjpeg-turbo-dev g++ make autoconf linux-headers \
    && docker-php-source extract \
    && pecl install redis \
    && pecl install xdebug \
    && docker-php-ext-enable xdebug redis \
    && docker-php-source delete \
    && docker-php-ext-install pdo_mysql soap intl zip \
    && curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer \
    && rm -rf /tmp/*

RUN adduser -D -u 1000 www

CMD ["php-fpm"]