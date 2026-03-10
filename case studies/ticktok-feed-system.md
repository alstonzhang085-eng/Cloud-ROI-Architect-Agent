# Design TikTok Feed System

Design the recommendation feed for a short-video platform similar to TikTok.

## 1. Problem

A platform like TikTok must serve billions of personalized video recommendations with extremely low latency.

Example scale:

- DAU: 1B
- Peak concurrent users: 40M
- Infinite scroll feed
- Highly personalized recommendations
- Latency requirement: <150ms

Core challenge:

Content production << content consumption.

One uploaded video may generate millions of feed impressions.

---

## 2. Workload Modeling

Assumptions:

DAU: 1B  
Peak concurrent users: 40M  
Videos watched per session: 50  

Estimated traffic:

Feed open QPS ≈ 700k  
Metadata fetch QPS ≈ 7M  
Engagement write QPS ≈ 700k  

Observation:

Short video platforms experience extreme **read amplification**.

This workload pattern favors **fan-out on read**.

---

## 3. High-Level Architecture

Main components:

Client  
API Gateway  
Feed Service  
Candidate Generation Service  
Ranking Service  
Feature Store  
Metadata Database  
Cache Layer  
Event Streaming (Kafka)

Request flow:

Client  
→ API Gateway  
→ Feed Service  
→ Candidate Generation  
→ Ranking Service  
→ Metadata Service  
→ Client

---

## 4. Recommendation Pipeline

Large-scale recommendation systems use multi-stage ranking pipelines.

Example pipeline:

Candidate Recall  
→ Light Ranking  
→ Heavy Ranking  
→ Re-ranking  
→ Filtering

Typical scale:

Recall: 2000 candidates  
Light ranking: 500  
Heavy ranking: 100  
Final results: 10  

This pipeline reduces compute cost while preserving recommendation quality.

---

## 5. Caching Strategy

Caching is essential to meet latency requirements.

Example caches:

User candidate cache  
Feature cache  
Video metadata cache  

Candidate cache example:

Key: user_id  
Value: candidate video list  
TTL: 30 seconds  

This reduces repeated candidate generation during rapid scrolling.

---

## 6. Real-Time Data Pipeline

User engagement signals are streamed in real time.

Typical pipeline:

User Events  
→ Kafka  
→ Stream Processing  
→ Feature Store  
→ Ranking Service

Signals include:

watch time  
likes  
shares  
comments  
completion rate  

These signals update recommendation features in near real time.

---

## 7. Hot Video Problem

When a video goes viral, the system may experience traffic amplification.

Example:

1 video  
→ millions of impressions  
→ ranking storm

Mitigation strategies:

viral video caching  
precomputed ranking scores  
traffic shaping  
candidate boosting

---

## 8. Feed Freshness

Recommendation systems must balance:

Exploitation (known preferences)  
Exploration (new content discovery)

Example strategy:

90% exploitation  
10% exploration

Exploration traffic helps new creators gain exposure.

---

## 9. Avoiding Duplicate Videos

Dynamic ranking can lead to duplicate recommendations.

Solution:

Maintain a user **Seen Set**.

Implementation options:

Redis set  
Bloom filter  

This ensures users do not see the same video repeatedly.

---

## 10. Multi-Region Deployment

To support global users, the system is deployed across regions.

Example regions:

US  
EU  
APAC  

Design principles:

region-local ranking  
regional feature stores  
asynchronous replication

---

## 11. Trade-offs

Fan-out on Write

Pros:
- fast feed loading
- simple architecture

Cons:
- massive write amplification
- poor personalization
- slow signal propagation

Fan-out on Read

Pros:
- real-time ranking
- high personalization
- better exploration

Cons:
- higher compute cost
- complex ranking pipeline

Short-video platforms typically use:

fan-out on read + precomputed recall.

---

## 12. Key Takeaways

Designing a TikTok-scale feed system requires solving several hard problems:

large-scale recommendation  
low latency ranking  
real-time data pipelines  
global infrastructure  
hotspot mitigation  

The core challenge is balancing:

scalability  
personalization  
cost