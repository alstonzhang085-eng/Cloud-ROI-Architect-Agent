


This example demonstrates how to provide system context to the Architecture Compiler Engine.

The agent requires three categories of input:
	1.	System Mode
	2.	Business Workload
	3.	Physical Constraints

⸻

1️⃣ System Mode

Defines the architecture strategy and validation rules.

System Mode: SaaS-Distributed

Supported modes include:
	•	Financial-Critical
	•	SaaS-Distributed
	•	Analytics-Heavy
	•	Hybrid Enterprise

⸻

2️⃣ Business Workload

Defines system traffic and growth assumptions.

Daily Active Users (DAU): 40,000,000

Average Requests Per User Per Day: 18

Peak Traffic Multiplier: 4x

Estimated Peak QPS:
≈ 83,000


⸻

3️⃣ Physical Constraints

Defines infrastructure limitations and SLO requirements.

Regions:
- US-East
- EU-West

Latency Requirement:
<150ms API response

Availability Target:
99.99%

Data Compliance:
GDPR required for EU users


⸻

4️⃣ Architecture Draft (Optional)

Users may optionally provide a draft architecture for validation.

Example:

Client
  ↓
CDN
  ↓
API Gateway
  ↓
Service Cluster
  ↓
Redis Cache
  ↓
Aurora Global Database


⸻

5️⃣ Agent Execution

When submitted to the engine, the system will run the 8-stage architecture reasoning pipeline:
	1.	Workload Modeling
	2.	Architecture Graph Modeling
	3.	Capacity Planning
	4.	Anti-Pattern Detection
	5.	Failure Simulation
	6.	Cost Modeling
	7.	Cost Reconciliation
	8.	Architecture Report Generation

The output will be generated in the file:

examples/output-example.md

:::
