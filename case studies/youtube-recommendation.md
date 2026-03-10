# Design YouTube Recommendation System

Design the recommendation system for a large video platform like YouTube.

## 1. Problem

A video platform must recommend relevant videos to billions of users.

Requirements:

- Personalized recommendations
- Billions of videos
- Real-time engagement signals
- Low latency feed generation

---

## 2. Workload Modeling

Example assumptions:

DAU: 2B  
Peak concurrent users: 100M  
Videos watched per session: 20

Estimated traffic:

Feed requests: millions per second  
Engagement signals: billions per day

---

## 3. High-Level Architecture

Main components:

Client  
API Gateway  
Recommendation Service  
Candidate Generation  
Ranking Service  
Feature Store  
Metadata Database  
Event Streaming Pipeline

---

## 4. Candidate Generation

Candidate generation retrieves potential videos from multiple sources:

Subscriptions  
Trending videos  
Similar users  
Video similarity

Typical candidate size:

1000–2000 videos.

---

## 5. Ranking Pipeline

A machine learning ranking model evaluates candidates.

Pipeline:

Candidate Generation  
→ Feature Extraction  
→ Ranking Model  
→ Re-ranking  
→ Filtering

Final output:

Top 10–20 videos.

---

## 6. Feature Store

The ranking model uses a large feature set.

Examples:

user watch history  
video metadata  
engagement signals  
user-video similarity  

Feature stores provide low latency access to these features.

---

## 7. Real-Time Data Pipeline

User actions generate events.

Examples:

watch  
like  
share  
subscribe  

Pipeline:

User Events  
→ Kafka  
→ Stream Processing  
→ Feature Store

These signals update recommendation models.

---

## 8. Hybrid Feed Strategy

Video platforms often combine multiple feed sources.

Example feed composition:

Subscriptions feed  
Recommended videos  
Trending content  
Ads

These sources are merged and re-ranked.

---

## 9. Exploration vs Exploitation

Recommendation systems must balance:

exploitation: recommend known preferences  
exploration: discover new content

Exploration traffic helps surface new creators and videos.

---

## 10. Key Takeaways

The main challenges of recommendation systems include:

large candidate space  
low latency ranking  
real-time signal processing  
personalization at scale

A typical architecture combines:

candidate generation  
machine learning ranking  
real-time data pipelines