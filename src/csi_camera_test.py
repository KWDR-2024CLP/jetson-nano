# MIT License
# Copyright (c) 2019 JetsonHacks
# See license
# Using a CSI camera (such as the Raspberry Pi Version 2) connected to a
# NVIDIA Jetson Nano Developer Kit using OpenCV
# Drivers for the camera and OpenCV are included in the base image

import cv2  # OpenCV 라이브러리 import

# gstreamer_pipeline 함수는 CSI 카메라를 제어하기 위한 GStreamer 파이프라인 문자열을 반환합니다.
# capture_width, capture_height: 카메라 캡처 해상도
# display_width, display_height: 화면에 표시할 해상도
# framerate: 초당 프레임 수
# flip_method: 이미지를 회전시키는 방법 (예: 0은 회전 없음, 2는 상하 반전)
def gstreamer_pipeline(
    capture_width=1280,
    capture_height=720,
    display_width=1280,
    display_height=720,
    framerate=60,
    flip_method=0,
):
    return (
        "nvarguscamerasrc ! "  # NVIDIA CSI 카메라를 위한 소스
        "video/x-raw(memory:NVMM), "  # 메모리 최적화를 위해 NVMM 사용
        "width=(int)%d, height=(int)%d, "  # 캡처 해상도 지정
        "format=(string)NV12, framerate=(fraction)%d/1 ! "  # 데이터 포맷과 프레임 속도 설정
        "nvvidconv flip-method=%d ! "  # 이미지 회전 방식 지정
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "  # 출력 해상도와 포맷 지정
        "videoconvert ! "  # 포맷 변환 (BGRx → BGR)
        "video/x-raw, format=(string)BGR ! appsink"  # OpenCV와 통합하기 위해 appsink 사용
        % (
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )

# show_camera 함수는 CSI 카메라를 사용하여 실시간으로 영상을 캡처하고 화면에 표시합니다.
def show_camera():
    # GStreamer 파이프라인을 생성하여 출력
    print(gstreamer_pipeline(flip_method=0))
    
    # GStreamer 파이프라인을 사용하여 카메라 초기화
    cap = cv2.VideoCapture(gstreamer_pipeline(flip_method=0), cv2.CAP_GSTREAMER)
    
    if cap.isOpened():  # 카메라가 성공적으로 열렸는지 확인
        # OpenCV 창을 생성
        window_handle = cv2.namedWindow("CSI Camera", cv2.WINDOW_AUTOSIZE)
        
        # 창이 열려 있는 동안 반복 실행
        while cv2.getWindowProperty("CSI Camera", 0) >= 0:
            ret_val, img = cap.read()  # 프레임 읽기
            if ret_val:  # 프레임이 성공적으로 읽혔는지 확인
                cv2.imshow("CSI Camera", img)  # 프레임을 화면에 표시
            
            # ESC 키를 눌렀을 때 프로그램 종료
            keyCode = cv2.waitKey(30) & 0xFF
            if keyCode == 27:  # ESC 키의 ASCII 코드
                break
        
        # 프로그램 종료 후 리소스 해제
        cap.release()  # 카메라 자원 해제
        cv2.destroyAllWindows()  # OpenCV 창 닫기
    else:
        # 카메라를 열 수 없는 경우 오류 메시지 출력
        print("Unable to open camera")

# 메인 실행 코드
if __name__ == "__main__":
    # show_camera 함수 실행
    show_camera()  
