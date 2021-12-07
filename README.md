**Secret Universe Investigation Organization Bot 2.0**

---

Secret Universe Investigation Organization Bot 2.0 hay viết tắt là SUIBOT 2.0 là 1 con bot Discord được tạo bởi hieupham1103#0188 dựa trên thư viện [Discord.py](https://github.com/Rapptz/discord.py)

Và đây chính là toàn bộ source code của SUIBOT 2.0 cho những người nào có nhu cầu tham khảo và tạo một con bot cho riêng mình.

Code có thể khó đọc vì đây là code của một người chưa có kinh nghiệm về lập trình.
Mọi người có thể ủng hộ tôi bằng cách thêm bot vào server của mình bằng link sau [Link](https://discord.com/api/oauth2/authorize?client_id=872034926130782208&amp;permissions=8&amp;scope=bot)

**Các tính năng của Bot**

---

* Mute/ Unmute
* Ping
* Văn mẫu
* Verify
* Music
* Profile Card

**Install and Setup**

---

Hãy clone code của bot về

```
git clone https://github.com/hieupham1103/SUIBOT-2.0.git
```

Tạo một file config.json và bỏ token, client id, client secret vào file config đó.

```
{
    "bottoken": "token",
    "clientid": "client id",
    "clientsecret": "client secret"
}
```

Trong file main.py có 3 nhóm lệnh hãy bỏ đi nếu không muốn dùng tính năng trong nhóm đó

```
for filename in os.listdir('./Moderator'):
    if filename.endswith('.py'):
        client.load_extension(f'Moderator.{filename[:-3]}')

for filename in os.listdir('./Music'):
    if filename.endswith('.py'):
        client.load_extension(f'Music.{filename[:-3]}')

for filename in os.listdir('./ProfileCard'):
    if filename.endswith('.py'):
        client.load_extension(f'ProfileCard.{filename[:-3]}')
```

**Setup mute và unmute**

Vào file ./Moderator/mute.py và bỏ id của role muted vào biến *tunhan* và id của kênh thông báo mute vào biến *mutechannel*

```
tunhan = 762694968930074644
mutechannel = 784235323781152769
```

**Setup verify**

Vào file ./Moderator/verify.py và bỏ role xác thực vào biến *checkrole* và id của kênh chat thông báo vào biến *chung*

```
checkrole = 856054757855461406
chung = 764510929500373023
```
