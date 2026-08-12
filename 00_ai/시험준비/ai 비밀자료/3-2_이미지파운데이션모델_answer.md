# 3-2 이론: 이미지 파운데이션 모델 — 해설지

---

## 문제 22. 파운데이션 모델 등장 이전의 AI 학습 방식으로 옳은 것을 고르시오.

1. 모든 작업에 동일한 모델을 사용
2. 작업별 별도 학습 필요
3. 자가 학습 기반 학습
4. 멀티모달 입력 사용

> **정답: 2**
> 파운데이션 모델 등장 이전에는 분류, 탐지, 생성 등 각 태스크마다 별도로 데이터를 모으고 모델을 학습해야 했다.

---

## 문제 25. 다음 중 이미지 생성(text-to-image) 모델이 아닌 것을 고르시오.

1. DALL-E 3
2. Midjourney v7
3. Stable Diffusion
4. SAM

> **정답: 4**
> SAM(Segment Anything Model)은 이미지 세그멘테이션 모델로, 텍스트-이미지 생성 모델이 아니다.

---

## 문제 29. SigLIP 연구에서 채택한 손실 함수를 고르시오.

1. Softmax
2. ReLU
3. Sigmoid
4. GELU

> **정답: 3**
> SigLIP은 CLIP의 Softmax 기반 대조 손실 대신 Sigmoid 손실을 사용하여 이미지-텍스트 쌍 학습의 효율성을 높인 방법이다.

---

## 문제 34. VLM에서 비전 인코더가 만족해야 하는 조건을 고르시오.

1. 이미지를 언어와 연관 지어 이해할 수 있는 능력
2. 파라미터 수가 언어 모델보다 항상 커야 함
3. 토큰화를 직접 수행할 수 있어야 함
4. 사고 능력과 언어 능력만으로 충분함

> **정답: 1**
> VLM(Vision-Language Model)의 비전 인코더는 이미지 특징을 언어 모델이 이해할 수 있는 표현으로 변환하는 역할을 해야 한다.

---

## 문제 51. 다음 중 "오픈" 이미지 생성 모델을 모두 고르시오. (단답형)

1. DALL-E 3
2. Stable Diffusion
3. Latent Diffusion Model
4. Midjourney v7

> **정답: 2, 3**
> Stable Diffusion과 Latent Diffusion Model은 오픈소스로 공개된 이미지 생성 모델이다. DALL-E 3(OpenAI)와 Midjourney v7은 상용 폐쇄형 서비스이다.
