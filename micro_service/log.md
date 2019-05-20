


<!-- TOC -->

- [1. 资料](#1-资料)
- [2. 实践](#2-实践)

<!-- /TOC -->

# 1. 资料

* https://www.cnblogs.com/sailrancho/p/4784763.html (lograte)
* https://superuser.com/questions/291368/log-rotation-of-stdout (standout 配合lograte)
* https://httpd.apache.org/docs/trunk/programs/rotatelogs.html
* https://elk-docker.readthedocs.io/ (elk)
* https://stackoverflow.com/questions/55357262/logstash-and-filebeat-in-the-elk-stack (filebeat读取多个文件)

# 2. 实践     
```bash
yum install httpd -y

sudo mkdir /var/log/frp
sudo chown $(id -u):$(id -g) /var/log/frp
nohup ./frps -c ./frps.ini | rotatelogs -v -e /var/log/frp/frp.log-%Y%m%d 86400 &

```
