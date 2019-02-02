---
title: haproxy
date: 2018-2-17 23:23:46
categories: [微服务]
---


<!-- TOC -->

- [实践](#实践)

<!-- /TOC -->


<a id="markdown-实践" name="实践"></a>
# 实践

```bash
mkdir -p ~/reference/haproxy_test cd ~/reference/haproxy_test

mkdir nginx1 nginx2

cat > ./nginx1/index.html << EOF
<HTML>

<TITLE>hello world</TITLE>

<BODY>

<P>nginx1</P>

</BODY>
</HTML>

EOF

cat > ./nginx2/index.html << EOF
<HTML>

<TITLE>hello world</TITLE>

<BODY>

<P>nginx2</P>

</BODY>
</HTML>

EOF

docker run --name nginx1 -d -p 10001:80 -v `pwd`/nginx1/index.html:/usr/share/nginx/html/index.html nginx
docker run --name nginx2 -d -p 10002:80 -v `pwd`/nginx2/index.html:/usr/share/nginx/html/index.html nginx

docker pull haproxy:latest


docker run -it --rm --name haproxy1 haproxy bash

# default
# https://cbonte.github.io/haproxy-dconv/1.7/configuration.html


touch haproxy.cfg

cat > ./haproxy.cfg  << EOF
defaults
    timeout connect         10s
    timeout client          1m
    timeout server          1m

frontend haproxy_inbound
    bind *:20001
    default_backend my_haproxy

backend my_haproxy
    balance roundrobin
    mode tcp
    server srv1 127.0.0.1:10001 check
    server srv2 127.0.0.1:10002 check
EOF

docker run --rm --name haproxy1 -it \
    -v `pwd`/haproxy.cfg:/usr/local/etc/haproxy/haproxy.cfg \
    --net host \
    haproxy:latest
```
