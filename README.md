# jetson-nano-test
젯슨 나노 환경 테스트 read.me 입니당
 
## 주요 개발 내용
1. **웹캠 초기화 및 테스트**
   - OpenCV를 사용하여 Jetson Nano에 연결된 웹캠 피드를  출력합니다.

2. **객체 탐지 통합 (테스트 중)**
   - YOLOv5와 같은 사전 학습된 객체 인식 모델을 활용하여 웹캠 화면에서 객체를 탐지합니다.

## 프로젝트 파일 구조
<details><summary>👈 프로젝트 파일 구조
</summary>
   
```plaintext
jetson-nano-test/
├── README.md               # 프로젝트 설명 문서
├── requirements.txt        # 프로젝트에서 사용하는 Python 라이브러리 목록
├── .gitignore              # Git에서 제외할 파일/폴더 목록
├── src/                    # 소스 코드 디렉토리
│   ├── main.py             # 메인 실행 파일 (학습 모델과 OpenCV 통합 코드)
│   ├── camera_test.py      # 웹캠 초기화 및 테스트 코드
│   ├── csi_camera_test.py  # csi 카메라 테스트 코드
```
</details>



## 젯슨 설정 방법
<details><summary> 👈  젯슨 나노 기본 설정 하는 법
</summary>
   
### - 젯슨 나노 기본 셋팅 사이트 - 
```plaintext
- nvidia developer 사이트             https://www.sdcard.org/downloads/formatter/ 
- SD카드 포맷 프로그램 사이트         https://developer.nvidia.com/embedded/downloads
- SD카드 이미지 로더 프로그램 사이트  https://www.balena.io/etcher/
```
### 순서대로 잘 따라 오기
### 1. SD 카드 포멧 하기 
### 2. OS 다운로드 (nvidia developer 에서 다운)
## 3. OS 이미지 읽기 (SD 카드에 저장 하는 단계)

![image](https://github.com/user-attachments/assets/4b4d3e50-8981-46e8-b525-0b13d052bb0b)

### 3-1. Flash from file 클릭 엔비디아에서 다운 받은 폴더 압축 해제 후 선택

![image](https://github.com/user-attachments/assets/224865b4-e5cf-4ef0-a341-27add03cc233)

### 3-2 .Select target 을 클릭해 SD카드를 선택하고 'Select' -> 완료 후 'Flash' 클릭


## 4. img 파일이 저장된 SD카드를 Jetson Nano에 연결한다.
  - 젯슨 나노 준비물(모니터, 키보드, 마우스, 전원, wifi 동글)

## 5. `system configuration` 에서 `continue` 를 클릭해 설정 시작
   - 언어 선택 = `English`
   - keyboard layout = `English(US)`
   - 와이 파이 연결하기
   - 지역 선택 = `seoul`
   - 사용자 정보 입력 =  `pick a username` , `paswword` 는 **무조건 기억하기**
   - APP Partition Size = `30422`   
   - SWAP File 생성 할지 선택
   - 전력 모드  = `MAXN`

## 6. swap 사이즈 변경   
 - 현재 사이즈 확인 `free -m`
 - `sudo gedit(nano, mousepad...)/etc/systemd/nvzramconfig.sh` 입력
 - `mem=$((("${totalmem}" / 2 / "${NRDEVICES}") * 1024))` 부분 찾기
 - `mem=$((("${totalmem}" / 2 / "${NRDEVICES}") * 1024 * 2))` 변경
 - 재부팅 후 확인 후
**이제 편하게 사용하기~**


-  [기본 세팅시 참고](#https://velog.io/@tilkoas35/Jetson-Nano-OS-%EC%84%A4%EC%B9%98-%EB%B0%8F-%EC%B4%88%EA%B8%B0-%EC%84%A4%EC%A0%95!)    
-  [swap 사이즈 변경](#https://t-shaped-person.tistory.com/20)    


</details>

## 프로젝트 파일 구조
