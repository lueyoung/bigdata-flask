FROM lowyard/matplotlib:latest

RUN echo 2019年 12月 18日 星期三 10:26:24 CST 
ADD app.py /
ADD wcount.py /
ADD text /text/
ADD img /static/img/
ADD manifest/ret.html.sed /
ADD js /static/js/
ADD templates /templates/
