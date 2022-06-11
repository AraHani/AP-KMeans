# Affinity Propagation VS K-Means Clustering algorithm
# (2021-2 Big data and AI Class)

## 0. Introduction

Affinity Propagation (친밀도 전파 알고리즘) 과 K-Means Clustering 알고리즘을 비교 분석한다

Original Code in Google Colab : https://colab.research.google.com/drive/13PwxjZM8Gsw53DCGh9G2n_kBy-bEw51Y#scrollTo=Pg7Ztqenioru    
![image](https://user-images.githubusercontent.com/82162578/173171540-d811f90a-3f68-4249-b8b3-777ffcec41f1.png)

Iris 데이터를 사용하고, 이를 시각화한 자료 (꽃받침과 꽃잎 각각의 넓이, 길이에 대한 연관성이 존재함을 찾아볼 수 있다)

---

## 1. K-Means Algorithm
![image](https://user-images.githubusercontent.com/82162578/173171558-25cc8045-50c3-4452-b4d7-bc2165a44a77.png)![image](https://user-images.githubusercontent.com/82162578/173171552-32dd150b-a8cc-4ac8-84bf-9acd0b84d6fc.png)
각각 cluster = 3, cluster = 7 일때의 결과 (별의 개수 = 군집의 중심- Inertia)

![image](https://user-images.githubusercontent.com/82162578/173171707-926c0fdd-8100-45e8-bff9-88ad02cfd04e.png)![image](https://user-images.githubusercontent.com/82162578/173171711-a011f56f-0f95-4918-8f5e-c5a6ebef497e.png)

군집 (Cluster)의 개수는 코드를 통해 직접 정했다. 그래프에 따르면 cluster = 3 에서부터 군집 내부의 원소들끼리   
뭉쳐있는 정도가 매우 강함을 알 수 있다. (2 -> 3에서의 변화가 큼)

---

## 2. Affinity Propagation VS K-Means Clustering Comparison
![image](https://user-images.githubusercontent.com/82162578/173171808-e5de49d7-c2a9-46e3-b249-b4cc60529a51.png)![image](https://user-images.githubusercontent.com/82162578/173171811-80c7c84b-2acc-4dbc-aa56-307c8b44b58e.png)

Affinity Propagation : 군집 수 자동 설정 (7)   
K-Means : cluster = 7

친밀도 전파 알고리즘과 K-Means 알고리즘 모두 군집화 결과 자체는 거의 동일하다.     
K-Means 의 경우 직접 유저가 군집 개수를 설정할 수 있다.    
이는 능동적으로 cluster 개수를 설정할 수 있다는 장점일 수 있으나 최적의 군집 수를 바로 찾지 못할 경우    
수행시간이 친밀도 전파 알고리즘에 비해 오래 걸릴 수 있다.
