# Flask 토이프로젝트

### 자기소개 겸 블로그(ABTest 포함)

---

### 이 프로젝트는 ABTest를 포함하고 있습니다.

AB Test란 웹 사이트 방문자를 임의로 두 집단으로 나누고, 한 집단에게는 기존 사이트를 보여주고 다른 집단에게는 새로운 사이트를 보여준 다음, 두 집단 중 어떤 집단이 더 높은 성과를 보이는지 측정하여, 새 사이트가 기존 사이트에 비해 좋은지를 정량적으로 평가하는 방식을 말합니다. 이 사이트의 경우 구독하는 경우를 기준으로 판단합니다.

---

### 사용방법

```python
#자신만의 secret_key를 설정하세요
    app.secret_key = ''
```

-   blog_abtest.py에서 설정해주세요

```python
   MYSQL_CONN = pymysql.connect(
   host= MYSQL_HOST,
   port = 3306,
   #자신의 mysql을 설정하세요(user, passwd)
   user = '',
   passwd= '',
   db = 'blog_db',
   charset= 'utf8'
)
```

-   db_model폴더의 mysql.py에서 설정해주세요

#### blog_abtest 를 실행 후 http://localhost:8080/blog/flask_blog 로 접속하시면 됩니다.

---

## 결과화면

-   template A

-   template B

UI는 BootStrap의 Examples의 Blog를 가져왔습니다.
