# [JPA강의] 1-1) SQL 중심적인 개발의 문제점
---
---

<br>
<br>

<img src="./JPA_img/JPA_lecture_ch.1_1/JPA_lecture_ch.1_1_1.jpg
">

혼자 책으로만 하는 것 보다는 강의로 듣고, 책으로 복습을 하는 편이 더 낫겠다는 생각을 함...

그래서 강의를 듣기로 했음!!

![](https://t1.daumcdn.net/keditor/emoticon/friends1/large/007.gif)


---
책으로 미리 예습한 부분,.

[JPA책 1장 1-1](https://gloria94682015.tistory.com/74)

---

📍 현재의 상태 ?

-   객체를 관계형 DB에서 관리함.
-   결국, SQL중심적인 개발이 됨. 즉, SQL에 의존적인 개발을 함.

📍 객체를 관계형 데이터베이스에 저장하려면 ?

-   객체 -> SQL변환 -> SQL을 RDB 에 저장.

📍 객체와 관계형 데이터베이스의 차이 ?

1.  상속
2.  연관관계
    -   객체는 참조를 사용 : member.getTeam();
    -   테이블은 외래키를 사용 : JOIN ON M.TEAM\_ID = T.TEAM\_ID
3.  데이터 타입
4.  데이터 식별 방법

-   엔티티를 신뢰할 수 없음.

```
Member member = memberDAO.find(memberid);
member.getTeam(); // ?? 진짜로 가져올 수 있는 지 알 수 없음.
member.getOrder().getDelivery(); // ??
```

-   -   내가 memberDAO.find(me mberid) 를 작성하지 않았으면,
    -   find 라는 것 으로 member 안에 어떤 값들이 담기는 지를 알 수가 없음.
    -   즉, 그 find 라는 것에 들어가서 확인을 해봐야한다는 것임.
-   모든 객체를 미리 로딩 할 수는 없다.
-   그렇기 때문에, 여러 조회 쿼리를 만들어야함.
    -   ex) findMemberWithTeam();
    -   ex) findMemberWithOrderWithDelivery();
-   상황에 따라 각 메소드를 호출해서 사용해야겠지.
-   계층형 아키택처의 진정한 의미의 계층 분할이 어려움.

📍 비교해보자면?

-   JDBC

```
String memberId = "100";
Member member1 = memberDAO.getMember(memberId);
Member member2 = memberDAO.getMember(memberId);

// 이때 member1 != member2
// 다른 객체니까.
```

-   자바 컬렉션

```
String memberId = "100";
Member member1 = list.get(memberId);
Member member2 = list.get(memberId);

// 이 때는, member1 == member2
```

-   객체답게 모델링 할수록 매핑 작업만 늘어남...

📍 이 차이를 해결하기 위해서 ?

-   JPA 를 사용함.

<br>
<br>


---

[개발 공부를 위한 블로그](https://gloria94682015.tistory.com/75) 입니다.

오류가 있다면 댓글로 알려주세요!

감사합니다.

![](https://t1.daumcdn.net/keditor/emoticon/friends1/large/017.gif)