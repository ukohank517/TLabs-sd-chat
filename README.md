# TLabs-sd-chat

# Api一览：

### 入口处
| Describe |  Method  | URI | request| response |
| ---- | ---- | ---- | ---- | ---- |
| 主页(html) | GET | / |  | html页面，画面中生成房间一个按钮(房间生成) |
| 房间生成 | GET | /room/new |  | redirect to sd-web |


### web打开页面时使用api：

打开web-ui的时候，访问此api，可以获得用户名以及是不是第一个进入房间的

| Describe |  Method  | URI | request| response | error case |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 获取用户信息 | GET | /room/info | roomId, ipAddress | userName, isSuperUser | 超过五人的情况return error |

`localhost:5000/room/info?room_id=sampleid&ip_address=192.168.1.0`

```


```

### 图像&prompt:

房主更新图像，

其他成员取得房主最新更新的图像及prompt，可以用图像的最新更新时间来确定现在页面上表示的图是不是最新情报

| Describe |  Method  | URI | request| response | error case |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 更新图像 | POST | /image/upload | roomId, imageBase64, prompt | | |
| 取得最新图像 | GET | /image/get | roomId | imageBase64(or imageURL), prompt, latestSuccessDateTime | 房间/图像记录不存在时 empty |

### 聊天室

获取聊天记录里面包含：发言时间，发言者ip，发言者姓名，发言内容

| Describe |  Method  | URI | request| response |
| ---- | ---- | ---- | ---- | ---- |
| 投稿聊天 | POST | /chat/send | roomId, ipAddress | |
| 获取聊天记录 | GET | /chat/history | roomId | chatHistory, newestChatDateTime |
