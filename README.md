## 安装说明

Python环境
python >= 2.7
clone项目和虚拟环境依赖安装
mkdir -p /data/wwwroot/ && cd /data/wwwroot
git clone https://gitee.com/careyjike_173/redis_web_client.git redis_admin
cd redis_admin && pip install -r requirements.txt

### 数据库配置
配置文件在项目目录下conf/conf.py文件中

// 数据库信息
database = {
    "name": "redis_admin",
    "host": "127.0.0.1",
    "username": "root",
    "password": "root",
    "port": "3306",
}

### 生成数据库表文件
python manage.py migrate
创建管理员用户
python manage.py createsuperuser


### 配置nginx
  server {
  listen 80;
  server_name _;
  access_log /data/wwwlogs/access_nginx.log combined;
  index index.html index.htm index.php;
  location / {
    proxy_pass http://127.0.0.1:8001;
  }
  location /static {
                expires 7d;
                autoindex on;
                add_header Cache-Control provate;
                alias /data/wwwroot/redis_admin/static;
        }
  }

### 启动 redis_admin
chmod +x start.sh
./start.sh start
启动后请检查是否监听8001端口，如未启动请查看log目录下日志信息

### 启动nginx
service nginx start
访问浏览器 http://ip/


## 配置文件说明
DEBUG

值:True/False
开启debug模式，使用请将其改为False

LOG_LEVEL

值:ERROR/WARNING/INFO/DEBUG 日志级别

socket_timeout

值: 2,数字 连接redis超时时间

scan_batch

值: 10000,数字 如果redis key过多避免导致性能问题，key列表最多获取值

mail_host

邮箱smtp服务器地址

mail_user

邮箱用户

mail_pass

邮箱密码

mail_receivers

邮件接收者

admin_mail

管理员邮箱

数据库信息

database = {
    "name": "redis_admin", //数据库名称
    "host": "127.0.0.1",   //连接地址
    "username": "root",    //用户名
    "password": "root",    //密码
    "port": "3306",        //端口
}


## 添加redis
名称: 单机redis请注意唯一性, cluster请一致性
主机: redis主机地址
端口: redis端口
DB数: 请保持和redis配置文件中db数量一致
密码: 如redis有密码请填写
如redis为cluster模式，请添加多个redis，名称保持一致并勾选类型为cluster
添加配置后请为用户配置redis权限，被授权用户需要退出登陆方可看的左侧菜单栏显示
编辑redis
这里只需要点击单元格信息即可进行修改，编辑按钮是为了提示信息


## 用户管理
这里可对用户进行管理，如添加，编辑，删除用户

重点: 添加redis配置后需要在此编辑用户，为用户授权redis并退出登陆后才可看到右侧菜单栏信息
