1. Set your DNS server to 127.0.0.1
2. Make sure to have mkcert installed (mkcert --install)

What can you use?
1. docker-compose exec -it editor phpcs /www/wp-content/plugins/syma-devkit
2. docker-compose exec -it editor phpcbf /www/wp-content/plugins/syma-devkit
3. docker-compose exec -it editor phpstan analyse /www/wp-content/plugins/syma-devkit
4. docker-compose exec -it editor wp search-replace "Hello world" "Hello Syma" --dry-run

Notes:
- Set KernelForUDP in `~/Library/Group\ Containers/group.com.docker/settings.json` to false if you encounter issues with port 53 already in use.
- Refresh certificates by running `python3 scripts/refresh-certificates.py` from LocalServer dir.

Figure out:
- Refresh certificates automatically without calling script
- Dev Containers make this so much better?!

Next steps:
1. Make editor container dev container friendly :) (currently: no working terminal, home directory set weirdly when connecting with dev container, connect with dev container using the blue icon in the bottom left)
2. Change LTD (.syma?)

Features:
- WP-CLI
- PHPCS with support for latest WP 
- PHPStan
- XDebug
- Catch all outgoing emails
- Set your own ltd and use HTTPS

Nice to have:
- Blueprint for Github action deployment
- Matomo?

Bigger:
- Access to a community of experts