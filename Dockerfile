FROM python:3 as builder 
WORKDIR /usr/src/app

RUN git clone https://github.com/panaglev/yaml-to-html.git
RUN apt update && apt install -y npm
RUN npm install -g @go-task/cli

COPY /digital-cafedra/resume.yaml /usr/src/app/yaml-to-html/
COPY Taskfile.yaml Taskfile.yaml
RUN cd yaml-to-html && pip install -r requirements.txt

FROM builder as build 
RUN task build

FROM busybox as lite
WORKDIR /opt/app/build
COPY --from=build /usr/src/app/yaml-to-html/result.html .
VOLUME /opt/app/build
