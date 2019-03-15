<!-- TOC -->

- [发送余额与历史记录(未打包)](#发送余额与历史记录未打包)
- [接收余额与历史记录(未打包)](#接收余额与历史记录未打包)
- [发送余额与历史记录(打包)](#发送余额与历史记录打包)
- [接收余额与历史记录(打包)](#接收余额与历史记录打包)

<!-- /TOC -->


<a id="markdown-发送余额与历史记录未打包" name="发送余额与历史记录未打包"></a>
# 发送余额与历史记录(未打包)

余额:
```bash
{
    "jsonrpc": "2.0",
    "result": {
        "confirmed": 5000000000,
        "unconfirmed": -5000000000
    },
    "id": 2
}
```

历史记录:
```bash
{
    "jsonrpc": "2.0",
    "result": [
        {# 接收
            "tx_hash": "bcf05167ed45f4a3533fb0203c06f1090a8af3f18c27930cddb208bcfcb792d1",
            "height": 1
        },
        {# 发送
            "tx_hash": "2adb024b5f2709b93ab61578d5400ea60c5699e880ff1a306544750430e21807",
            "height": 0,
            "fee": 3820
        }
    ],
    "id": 2
}
```

<a id="markdown-接收余额与历史记录未打包" name="接收余额与历史记录未打包"></a>
# 接收余额与历史记录(未打包)

余额:  
```bash
{
    "jsonrpc": "2.0",
    "result": {
        "confirmed": 0,
        "unconfirmed": 4999996180
    },
    "id": 2
}
```

历史记录: 
```bash
{
    "jsonrpc": "2.0",
    "result": [
        {# 接收
            "tx_hash": "2adb024b5f2709b93ab61578d5400ea60c5699e880ff1a306544750430e21807",
            "height": 0,
            "fee": 3820
        }
    ],
    "id": 2
}
```


<a id="markdown-发送余额与历史记录打包" name="发送余额与历史记录打包"></a>
# 发送余额与历史记录(打包)

余额:  
```bash
{
    "jsonrpc": "2.0",
    "result": {
        "confirmed": 0,
        "unconfirmed": 0
    },
    "id": 2
}
```

历史记录: 
```bash
{
    "jsonrpc": "2.0",
    "result": [
        {# 接收
            "tx_hash": "bcf05167ed45f4a3533fb0203c06f1090a8af3f18c27930cddb208bcfcb792d1",
            "height": 1
        },
        {# 发送
            "tx_hash": "2adb024b5f2709b93ab61578d5400ea60c5699e880ff1a306544750430e21807",
            "height": 102
        }
    ],
    "id": 2
}
```

<a id="markdown-接收余额与历史记录打包" name="接收余额与历史记录打包"></a>
# 接收余额与历史记录(打包)

余额:  
```bash
{
    "jsonrpc": "2.0",
    "result": {
        "confirmed": 4999996180,
        "unconfirmed": 0
    },
    "id": 2
}
```

历史记录: 
```bash
{
    "jsonrpc": "2.0",
    "result": [
        {# 接收
            "tx_hash": "2adb024b5f2709b93ab61578d5400ea60c5699e880ff1a306544750430e21807",
            "height": 102
        }
    ],
    "id": 2
}
```
