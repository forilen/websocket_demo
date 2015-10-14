# websocket demo1

## websocket 后台服务架构

* demo代码结构
```bash
$ tree websocket_backends/
websocket_backends/
├── app.py
└── __init__.py

0 directories, 4 files
```

* 将自定义模块websocket_backends链接到python path
```bash
$ ln -sf /opt/websock_demo1/websocket_backends /usr/lib/python2.6/site-packages/
$ ls /usr/lib/python2.6/site-packages/ -al | grep websocket_backends/
lrwxrwxrwx    1 root root     38 Oct 13 17:12 websocket_backends -> /opt/websock_demo1/websocket_backends/
```
the backends of websocket uwsgi server: app.py

* 配置uwsgi启动服务: /etc/init/uwsgi.conf

* 配置websocket服务: /etc/uwsgi/vassals/websocket.ini 

* 配置nginx websocket proxy: /etc/nginx/conf.d/websocket.conf


## websocket 前端测试代码

```bash
front/
├── index.html
└── ws.js
```

### requirements

* nginx version >=1.1.4 (the proxy_http_version feature was added in NGINX version 1.1.4)
* jquery
* uwsgi


## references

* [NGINX as a WebSocket Proxy](https://www.nginx.com/blog/websocket-nginx/)
* [uwsgi websocket support](http://uwsgi-docs.readthedocs.org/en/latest/WebSockets.html)
* [Setting up Django and your web server with uWSGI and nginx](http://uwsgi-docs.readthedocs.org/en/latest/tutorials/Django_and_nginx.html)
* [websocket client js](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API/Writing_WebSocket_client_applications)
* [websocket server python](http://www.fullstackpython.com/websockets.html)
* [python-websockets](https://devcenter.heroku.com/articles/python-websockets)