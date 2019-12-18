FROM lowyard/matplotlib:latest

RUN echo {{.verbose}} 
ADD app.py /
ADD wcount.py /
ADD text /text/
ADD img /static/img/
ADD manifest/ret.html.sed /
ADD js /static/js/
ADD templates /templates/
