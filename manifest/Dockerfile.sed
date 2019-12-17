FROM lowyard/matplotlib:latest

RUN echo {{.verbose}} 
ADD app.py /
ADD img /static/img/
ADD js /static/js/
ADD templates /templates/
