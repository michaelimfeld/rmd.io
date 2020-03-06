FROM nikolaik/python-nodejs:python3.7-nodejs12

COPY . /var/www/app

ENV DJANGO_SETTINGS_MODULE maildelay.settings_production

WORKDIR /var/www/app

# Install python dependencies
RUN pip install -r requirements.txt

# Install sass
RUN npm install -g sass

# Install apache2 and apache2 wsgi module
RUN apt update
RUN apt install apache2 libapache2-mod-wsgi-py3 --yes --no-install-recommends

# Copy apache2 config
RUN cp deployment/000-default.conf /etc/apache2/sites-enabled/
# Enable apache2 wsgi module
RUN a2enmod wsgi

# Generate & collect static files
RUN cd app/mails/static && make css
RUN python app/manage.py collectstatic --clear --noinput

# Fix permissions
RUN chown -R www-data:www-data /var/www/app

EXPOSE 80

CMD /bin/sh -c "python app/manage.py migrate && /usr/sbin/apache2ctl -DFOREGROUND"
