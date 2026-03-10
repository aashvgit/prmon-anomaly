# prnom-anomaly

The dataset was generated using prmon burner tests. Normal runs shows the behavior while anomaly runs were created by intentionally increasing memory or I/O usage.

# installation 
As the prmon repository was cloned and build :

git clone https://github.com/HSF/prmon.git
cd prmon
git submodule update --init --recursive
mkdir build
cd build
cmake ..
make

And after building the prmon executable was used to monitor several test workloads

#Generating data

Monitoring data was generated using prmon together with the burner test programs included in the repository.
The monitoring interval was set to one second so that a time-series of resource usage values could be recorded.

usage done as 
./package/prmon --interval 1 --max-intervals 120 -- ./package/tests/burner

normal runs were done 3 times naming them as 
runnormal1.txt
runnormal2.txt
runnormal3.txt

Two times anomaly runs were done:
memory:
runanomalymem.txt
I/O:
runanomalyio.txt

These run gave different result as compared to normal runs

#Dataset
The monitoring outputs from different runs were combined into a single dataset using Python and Pandas.
Each run was labeled so it is possible to track which experiment produced each measurement.
Among the available metrics, the PSS (Proportional Set Size) memory metric was used for anomaly detection, PSS is a useful indicator because it reflects the proportional memory usage of the monitored process.

#Detection Method

For anomaly detection two different approaches were tested.

1. IQR Method

The Interquartile Range (IQR) method is a simple statistical common approach for detecting outliers.

Q1 - 1.5 * IQR
Q3 + 1.5 * IQR

where value outside the range is considered as anomalies

as it is easy to interpret and works well when normal behaviour is stable 

2. Isolation Forest
It is a machine learning algorithm designed especially for anomaly detection. It works by isolating unusual observations using randomly generated decision trees. In this test it was applied to the PSS memory values.

#Results
The figure ../plot/anomaly_plot.png monitored memory usage over time with anomalies detected using the IQR method.

The IQR method worked well for detecting large spike in memory usage. it is simple and easy to understand but it might not perform well if the data distribution changes significantly. Isolation Forest provides a more flexible approach since it does not rely on assumptions about the distribution of the data but its results can be harder to interpret. Using both methods together gives a useful comparison between statistical and machine learning approaches. By combining time-series monitoring with anomaly detection techniques it is possible to automatically identify abnormal behavior in software workloads.This type approaches could be useful for monitoring large scientific software pipelines where manual inspection of performance data is difficult.

#AI usage
AI tools were used for runtime errors during the setup process. The experiment design, dataset generation, analysis, and interpretation was not done with the help of ai


