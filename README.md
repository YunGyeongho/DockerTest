# Ubuntu(Virtual Box)에서의 Docker file(fast API Server) 빌드 및 이미지 실행
  
![Resized_1669268249026(1)](https://user-images.githubusercontent.com/101491213/203705256-18c817da-f315-42b2-9f82-836b1b82ef85.jpg)
  
![Resized_1669268250469(1)](https://user-images.githubusercontent.com/101491213/203705470-a01e241c-44d8-49c0-9aeb-a32d11573321.jpg)
  
검색 결과는 google custom search API를 이용하였습니다.  
최종 결과물은 root 디렉토리로 저장 되며 파일명은 gsrSortByDate.tsv입니다.  
정렬 방식은 날짜 오름차순입니다.

### API ID와 API Key가 필요합니다.  
apiID 변수와 apiKey 변수에 각각 입력해 주시면 됩니다. 
  
### 최대 페이지 셋팅  
전역 변수 setPage에 1 ~ 10 범위의 정수를 할당해주시면 됩니다. 
  
### 도커파일 빌드 하는법 
docker build -t 이미지명 .
  
### 도커 이미지 실행하는법
docker run -d -p 80:80 --name 컨테이너명 이미지명:latest
  
### 요청 주소(GET) 
host서버의 IP:80 으로 접속 하시면 됩니다.  
hostIP:80/search?keyword=키워드입력
