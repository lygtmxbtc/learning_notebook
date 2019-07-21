### 单点登录中，cookie被禁用
```text
后端生成session id并设置到cookie中，每次请求从cookie中获取到session id，
并查询到用户信息
除了cookie，常用http header来携带session id，但需手动设置
```
### 七层网络结构
```
应用层 ： 接口
表示层 ： 数据编码转换
会话层 ： 建立通信
传输层 ： tcp，udp
网络层 ： 管理网络地址，定位设备
数据链路层 ： 负责准备物理传输
物理层 ： 数据以比特流传输，接收
```
### http和https
```
由于http明文传输
对称加密，密钥依然明文
非对称加密，明文public key加密，private key解密，也可以private key加密，
public key解密。
建立通信后，服务端发送pubilc key给客户端，并保留private key，客户端对用户
密码使用public key加密后发给服务端，服务端使用private key解密获取密码。从
此，服务端和客户端使用该密码进行对称加密。
CA证书机构
服务端将public key发给CA，CA制作签名并使用private key加密证书返回给服务
端，服务端将证书发给客户端，客户端验证真伪，使用CA的public key解密证书签名。
然后客户端依照相同规则生成签名并比较解密的签名，一致则说明证书可信。
后面则以非对称加密，和对称加密方式通信
```