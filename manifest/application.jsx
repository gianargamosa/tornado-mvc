<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title></title>
    <link rel="stylesheet" href="{{ static_url("style/application.css") }}" type="text/css">
    <script src="https://unpkg.com/react@latest/dist/react.js"></script>
    <script src="https://unpkg.com/react-dom@latest/dist/react-dom.js"></script>
    <script src="https://unpkg.com/babel-standalone@6.15.0/babel.min.js"></script>
    {% block head %}{% end %}
  </head>
  <body>
    <div id="react-root"></div>
    {% block yield %}
    {% end %}
    <script type="text/javascript" src="{{ static_url("script/application.js") }}"></script>
    <script type="text/javascript" src="{{ static_url("script/jquery.js") }}"></script>
  </body>
</html>
