FROM python:3.5
MAINTAINER WangLy "xph_wangly10@163.com"
ENV PYTHONUNBUFFERD 1
RUN mkdir /knight
COPY requirements.txt /knight/
WORKDIR /knight
RUN pip install -r requirements.txt
CMD ["/bin/bash"]