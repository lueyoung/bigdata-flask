{% extends "layout.html" %}
{% block title %}结果{% endblock %}
{% block head %}
  {{ super() }}
{% endblock %}
{% block section %}
  <img src={{ url_for('static', filename='img/ret.{{.n}}.png') }} width="600" alt="">
{% endblock %}
{% block header %}
  {{ super() }}
{% endblock %}
{% block nav %}
  {{ super() }}
{% endblock %}
{% block footer %}
  {{ super() }}
{% endblock %}
