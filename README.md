# TLabs-sd-chat

# 1. 关于房间（you can ignore this part）：

| Describe |  Method  | URI | request| response |
| ---- | ---- | ---- | ---- | ---- |
| 主页(html) | GET | / |  | html页面，画面中生成房间一个按钮(房间生成) |
| 房间生成 | GET | /room/new |  | redirect to sd-web |

打开主页，按下生成房间按钮之后。
会生成一个房间url。房主进入此URL之后并将URL分享与其他组员，便可进行操作。


# 2. 组员的身份决定方法：

打开web-ui的时候，从前端访问此api，可以获得用户id以及是不是房主。

房主的定义为，第一个进入房间的人(id = 0)。

只要ip与房间不变，api返回的用户id也不会改变。

| Describe |  Method  | URI | request| response | error case |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 获取用户信息 | GET | /room/info | roomId, ipAddress | userName, isSuperUser | 超过五人的情况return error |

call： `<domain>/room/info?room_id=sampleid&ip_address=192.168.1.0`
### response sample
```
{
    "ip_address": "192.168.1.1",
    "isSuperUser": true,
    "room_id": "aaa",
    "status": true,
    "user_id": 0
}
```
# 3. 聊天室发言
使用此api，可将发言储存于后端服务器上。

| Describe |  Method  | URI | request| response |
| ---- | ---- | ---- | ---- | ---- |
| 投稿聊天 | POST | /chat/send | roomId, ipAddress | |

### request sample
POST: `<domain>/chat/send`
request json:
```
{
    "room_id": "sampleroom",
    "user_id": 4,
    "message": "bulabulabulabulabulabula, use this prompt: samesame"
}
```
### response sample
```
{
    "status": true
}
```



# 4. 取得聊天记录

使用此api，可以获取制定房间的最新30条聊天记录，以及最后发言时间。

聊天室可用此api构建。

| Describe |  Method  | URI | request| response |
| ---- | ---- | ---- | ---- | ---- |
| 获取聊天记录 | GET | /chat/history | roomId | chatHistory, newestChatDateTime |

### request
GET: `<domain>/chat/history?room_id=sampleroom`
### response:
```
{
    "chat_history": [
        {
            "created_at": "Thu, 13 Apr 2023 17:50:10 GMT",
            "message": "bulabulabulabulabulabula, use this prompt: samesame",
            "user_id": 4
        },
        {
            "created_at": "Thu, 13 Apr 2023 17:50:09 GMT",
            "message": "bulabulabulabulabulabula, use this prompt: samesame",
            "user_id": 4
        },
        {
            "created_at": "Thu, 13 Apr 2023 17:50:08 GMT",
            "message": "bulabulabulabulabulabula, use this prompt: samesame",
            "user_id": 4
        },
        {
            "created_at": "Thu, 13 Apr 2023 17:50:04 GMT",
            "message": "bulabulabulabulabulabula, use this prompt: samesame",
            "user_id": 4
        },
        {
            "created_at": "Thu, 13 Apr 2023 17:39:37 GMT",
            "message": "bulabulabulabulabulabula, use this prompt: samesame",
            "user_id": 4
        },
        {
            "created_at": "Thu, 13 Apr 2023 17:37:03 GMT",
            "message": "bulabulabulabulabulabula, use this prompt: samesame",
            "user_id": 3
        }
    ],
    "latest_date": "Thu, 13 Apr 2023 17:50:10 GMT"
}
```


# 5. 生成图像及prompt的上传

房主在web-ui那边，按下生成按钮之后，图像会以url的形式保存在前端服务器上。

前端js从html要素里取得该url，并且将prompt的文字送到后端api来，可以对该房间的最新图片/prompt信息进行登陆以及更新。

response里加了status，代表该数据的登陆成功与否。


| Describe |  Method  | URI | request| response | error case |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 更新图像 | POST | /image/upload | roomId, imageBase64, prompt | | |

### request sample
call `<domain>/image/upload`

request json:
```
{
    "room_id": "sampleroom",
    "prompt": "a picture with a man, walking with his dog",
    "image_url": "url/image.jpg"
}
```
### response sample
```
{
    "image_url": "url/image.jpg",
    "prompt": "a picture with a man, walking with his dog",
    "room_id": "sampleroom",
    "status": true
}
```


# 6. 获取最新图像&prompt

除了房主以外的其他成员，可以通过敲打这个api来获取房间内最新的prompt以及图像。


| Describe |  Method  | URI | request| response | error case |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 取得最新图像 | GET | /image/get | roomId | imageBase64(or imageURL), prompt, latestSuccessDateTime | 房间/图像记录不存在时 empty |

#### request sample
`<domain>/image/get?room_id=sampleroom`

#### response
什么都没有的情况
```
{
    "image_url": "url/image.jpg",
    "prompt": "a picture with a man, walking with his dog",
    "room_id": "sampleroom",
    "updated_at": "Sat, 15 Apr 2023 13:20:44 GMT"
}
```

# 7. 其他

- 打开前端web-ui页面时候
  - 房主： 第一个进入该房间，通过api获得的用户id为0。此时房主可以将前端网址分享给其他成员。
  - 其他成员： 在房主之后进入房间。通过api获得自己的用户id。
- 图像/prompt
  - 房主： 房主按下生成按钮之后生成图像。图像生成之后已经保存于前端web-ui的服务器内。此时无须再将图像保存于后端api服务器。只需要用api把页面的图像src获取，将次url登陆于api即可。

