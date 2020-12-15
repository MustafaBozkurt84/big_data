# Spark Model Deployment Optons

There are three different deployment alternatives.
Throughput and latency trade-offs for these three deployment options for generating predictions.
<img href="spark_ml_deployment_options.jpg" />

|                  | Throughput | Latency                     | Example Application       |
|------------------|------------|-----------------------------|---------------------------|
| Batch            | High       | High (hours to days)        | Customer churn prediction |
| Streaming        | Medium     | Medium (seconds to minutes) | Dynamic pricing           |
| Real-time/Online | Low        | Low (milliseconds)          | Online ad bidding         |

## 1. Batch processing
Generates predictions on a regular schedule and writes the results out to persistent storage to be served elsewhere.

## 2. Streaming
Provides a nice **trade-off between throughput and latency.** You will continuously
make predictions on micro-batches of data and get your predictions in **seconds to minutes.** But this way you have to allocate some resources to streaming predictions.

## 3. Real-time/online
Deployment **prioritizes latency over throughput** and generates predictions in a **few milliseconds.** Your infrastructure will need to support load balancing and be able to scale to many concurrent requests if there is a large spike in demand (e.g., for online retailers around the holidays).

Real-time deployment is the only option that Spark cannot meet the latency requirements for, so to use it you will need to export your model outside of Spark. For example, if you intend to use a REST
endpoint for real-time model inference (say, computing predictions in under 50 ms),
MLlib does not meet the latency requirements necessary for this application. You will need to get your feature preparation and model out of Spark, which can be time-consuming and difficult.