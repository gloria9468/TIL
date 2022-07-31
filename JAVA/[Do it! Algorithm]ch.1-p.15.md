### [JAVA - Do it! Algorithm] ch.1 - 중앙값 구하기
--
<br>
<br>

공부한 책 :  
[Do it! 자료구조와 함께 배우는 알고리즘 입문 자바편](http://www.yes24.com/Product/Goods/60547893)
<br>
<br>
<br>


```
// p.21 - 실습 1C-1
// 3개의 정숫값을 입력하고 중앙값을 구하여 출력 
// 추가 학습 ::: 사용자에게 갯수에 상관없이 입력값을 받아서 중앙값을 구함.
public void median() {
    System.out.println("정수를 입력해주세요. 그만 입력할 경우 \"stop\"을 입력해주세요. ");
    ArrayList<Integer> al = new ArrayList<>();

    Scanner scan = new Scanner(System.in);
    String scan_in = null;
    do {
        scan_in = scan.next();
        if(!"stop".equals(scan_in)) al.add(Integer.parseInt(scan_in));
        custom_sort(al);
    } while(!"stop".equals(scan_in));

    System.out.println("입력한 숫자들은 " + al + "입니다.");
    int get_median = 0;
    double medi = (double)al.size() / 2;

    if(medi % 2 > 0) {
        //갯수가 홀수인 경우 
        medi = Math.ceil(medi);
        get_median = al.get((int)medi -1);
    }else {
        //갯수가 짝수인 경우
        get_median =  (al.get((int)medi -1) + al.get((int)medi))/2;
    }
    System.out.println("이 중 중앙값은 " + get_median);
}
void custom_sort(ArrayList<Integer> al) { //1 2 4 5 3  //1 2 3 5 4  //1 2 3 4 5
    int al_size = al.size();
    for(int i =0; i < al_size; i++ ) {
        int al_last = al.get(al_size -1);
        if(al.get(i) > al_last) {
            int get_i = al.get(i);
            al.set(i, al_last);
            al.set(al_size -1, get_i);
        }
    }
}
```

📍scan으로  값을 입력받을 때, 에러처리 해줘야함. 

-   내일 더 하는 것으로 하자.

원래 같으면, ArrayList에 있는 sort를 이용해서 풀었어야 했을 텐데, 

그냥 만들어서 해봤다.

그러니까, 생각하느라 시간이 오래 걸렸음. ㅠㅠ.

<br>


---
<br>
<br>

[개인 블로그 링크](https://gloria94682015.tistory.com/manage/newpost/?type=post&returnURL=%2Fmanage%2Fposts%2F#)

개발 공부를 위한 블로그 입니다. 

오류가 있다면 댓글로 알려주세요! 

감사합니다.


![](https://t1.daumcdn.net/keditor/emoticon/friends1/large/017.gif)