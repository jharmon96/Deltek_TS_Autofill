###################################
###### Build from base image ######
##################################
FROM jackharmon/extendederp:base


RUN pip install pyvirtualdisplay
RUN pip install pathlib
RUN pip install apscheduler

###################################
####### Install source code #######
###################################

USER root

RUN mkdir -p /src
COPY ./geckodriver /usr/bin/geckodriver
ADD . / /src/
WORKDIR /src
RUN pip install ../src
WORKDIR /src/Deltek_TS_Autofill

ENTRYPOINT ["/usr/bin/env"]
CMD ["bash", "/src/build.sh"]
