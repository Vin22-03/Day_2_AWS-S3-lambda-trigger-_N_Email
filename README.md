#  AWS Lambda S3 → SNS → SQS Integration Project

## Real-Time Problem Statement
"A media publishing company wants to automate notifications and processing whenever new content files are uploaded by their editorial team.
Whenever a new file (image, video, document) is uploaded to a centralized Amazon S3 bucket, the system should:

Instantly notify team leads via email 📬
- Sends an email notification via **Amazon SNS**
- Pushes metadata into a **message queue using Amazon SQS**

---

## 🔧 Services Used

| AWS Service | Purpose |
|-------------|---------|
| **S3 (Simple Storage Service)** | Trigger source – file upload event |
| **Lambda** | Executes backend logic on upload |
| **SNS (Simple Notification Service)** | Sends email alerts |
| **SQS (Simple Queue Service)** | Queues file metadata for async processing |
| **CloudWatch** | Logs function executions |

---

##  Use Case

> _“Notify stakeholders immediately when a file is uploaded and queue the file metadata for further processing by downstream systems.”_

This pattern is commonly used in:
-  Image processing pipelines
-  Invoice upload workflows
-  Video transcoding systems
-  Event-driven microservices


##  Architecture

    [ S3 Bucket]
         |
         |  (upload trigger)
         v
    [Lambda Function]
     |            |
     |            |
     v            v
    [SNS]      [SQS]

    
##  Outcomes

- Hands-on with event-driven architecture

- Shows integration of 4 core AWS services

- Demonstrates understanding of decoupled design

- Useful for DevOps, Cloud Engineer, and SDE roles

