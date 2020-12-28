FROM homeassistant/armv7-base-ubuntu:18.04

ENV LANG C.UTF-8

RUN apt update && apt install -y git build-essential
RUN apt install -y sudo mosquitto python3-pip

RUN pip3 install paho-mqtt

RUN git clone https://github.com/WiringPi/WiringPi.git /WiringPi && cd /WiringPi && ./build && cd /
RUN git clone https://github.com/ssjowowo/Raspi-Rollo.git /Raspi-Rollo && cd /Raspi-Rollo/rcswitch-pi && make sendv2 && chmod a+x sendv2 && cp sendv2 /usr/bin/

# Copy data for add-on
COPY run.sh /
COPY quadtransmitter.py /
RUN chmod a+x /run.sh

CMD [ "/run.sh" ]