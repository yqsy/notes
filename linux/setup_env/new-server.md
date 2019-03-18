<!-- TOC -->

- [1. 证书](#1-证书)

<!-- /TOC -->



<a id="markdown-1-证书" name="1-证书"></a>
# 1. 证书

```bash
curl -O https://raw.githubusercontent.com/yqsy/linux_script/master/id_rsa.pub
mkdir ~/.ssh
chmod 700 ~/.ssh
touch ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
cat id_rsa.pub >>  ~/.ssh/authorized_keys
rm id_rsa.pub -f

# sudo sed -i "s/.*PasswordAuthentication.*/PasswordAuthentication no/g" /etc/ssh/sshd_config
sudo systemctl restart sshd

```
