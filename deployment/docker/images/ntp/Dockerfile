#FROM ubuntu:artful
#FROM ubuntu:xenial
FROM buildpack-deps:jessie
#FROM ubuntu:trusty

# install ntp
RUN apt-get update && apt-get install -y ntpdate \
    && apt-get install -y ntp \
    && apt-get install -y cron \
    #&& apt-get install -y chrony\
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# use custom ntpd config file
ADD conf/ntp/ntp.conf /etc/ntp.conf
RUN chmod 644 /etc/ntp.conf


# chrony
ADD conf/chrony/chrony.conf /etc/chrony/chrony.conf
ADD conf/chrony/chrony.keys /etc/chrony/chrony.keys

# use custom crontab file 
ADD conf/crontabs/root /var/spool/cron/crontabs/root
RUN chown -R root:crontab /var/spool/cron/crontabs/root \
# must be 600
 && chmod 600 /var/spool/cron/crontabs/root

# create log file
RUN touch /var/log/cron.log

ADD scripts/entrypoint.sh entrypoint.sh
RUN chmod 777 ./entrypoint.sh
# ntp port
EXPOSE 123/udp

ENV TERM xterm 

#CMD ["/usr/sbin/ntpd", "-n"]
# start ntpd in the foreground
ENTRYPOINT [ "./entrypoint.sh" ]
#CMD [ "./entrypoint.sh" ]
CMD ntpq -p
#ENTRYPOINT ["chronyd", "-d", "-f", "/etc/chrony/chrony.conf"]

