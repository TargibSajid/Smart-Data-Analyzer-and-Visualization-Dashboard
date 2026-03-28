import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
class Traffic:

    analysis_options = [
        "Traffic Trend Analysis",
        "Peak Hour Detection",
        "Junction Comparison",
        "Day-wise / Weekly Analysis",
        "Heatmap Analysis",
        "Anomaly Detection"
    ]

    def __init__(self, df,st,analysis_type):
        self.df = df
        self.st = st
        self.df["DateTime"] = pd.to_datetime(self.df["DateTime"])
        self.df["Date"] = self.df["DateTime"].dt.date
        self.df["Hour"] = self.df["DateTime"].dt.hour
        self.df["Day"] = self.df["DateTime"].dt.day_name()
        left, right = st.columns([1, 1])
        self.analysis_type = np.array(analysis_type)
        for x in self.analysis_type:
            if x == "Traffic Trend Analysis":
                with left:
                    self.TrafficTrendAnalyze()
            elif x == "Peak Hour Detection":
                with right:
                    self.Peak_Hour_Detection()
            elif x == "Junction Comparison":
                with left:
                    self.Junction_Comparison()
            elif x == "Day-wise / Weekly Analysis":
                with right:
                    self.Daywise_Weekly_Analysis()
            elif x == "Heatmap Analysis":
                with left:
                    self.Heatmap_Analysis()
            elif x == "Anomaly Detection":
                with right:
                    self.Anomaly_Detection()


    def TrafficTrendAnalyze(self):
        self.st.subheader("Traffic Trend Analysis")
        self.st.info("This is a placeholder for traffic trend analysis. Implement your logic here.")
        daily_trend = self.df.groupby("Date")["Vehicles"].sum()
        print(daily_trend)
        plt.figure(figsize=(8, 4))
        plt.plot(daily_trend.index, daily_trend.values)
        plt.title("Daily Traffic Trend")
        plt.xlabel("Date")
        plt.ylabel("Total Vehicles")
        plt.xticks(rotation=45)
        plt.tight_layout()
        self.st.pyplot(plt)

    def Peak_Hour_Detection(self):
        hourly_traffic = self.df.groupby("Hour")["Vehicles"].sum()
        peak_hour = hourly_traffic.idxmax()
        peak_value = hourly_traffic.max()
        self.st.subheader("Peak Hour Detection")
        self.st.info(f"The peak hour is {peak_hour}:00 with {peak_value} vehicles.")
        plt.figure(figsize=(8, 4))
        plt.bar(hourly_traffic.index, hourly_traffic.values)
        plt.title("Peak Hour Detection")
        plt.xlabel("Hour")
        plt.ylabel("Total Vehicles")
        self.st.pyplot(plt)
    def Junction_Comparison(self):
        junction_traffic = self.df.groupby("Junction")["Vehicles"].sum()
        self.st.subheader("Junction Comparison")
        self.st.info("This is a placeholder for junction comparison. Implement your logic here.")
        plt.figure(figsize=(8, 4))
        plt.bar(junction_traffic.index.astype(str), junction_traffic.values)
        plt.title("Junction Comparison")
        plt.xlabel("Junction")
        plt.ylabel("Total Vehicles")
        self.st.pyplot(plt)
    def Daywise_Weekly_Analysis(self):
        day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        daywise = self.df.groupby("Day")["Vehicles"].sum().reindex(day_order)
        self.st.subheader("Day-wise / Weekly Analysis")
        self.st.info("This is a placeholder for day-wise/weekly analysis. Implement your logic here.")
        plt.figure(figsize=(9, 4))
        plt.figure(figsize=(9, 4))
        plt.bar(daywise.index, daywise.values)
        plt.title("Day-wise Traffic Analysis")
        plt.xlabel("Day")
        plt.ylabel("Total Vehicles")
        plt.xticks(rotation=45)
        self.st.pyplot(plt)


    def Heatmap_Analysis(self):
        day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        heatmap_data = self.df.pivot_table(values="Vehicles",index="Day",columns="Hour",aggfunc="sum").reindex(day_order)
        self.st.subheader("Heatmap Analysis")
        self.st.info("This is a placeholder for heatmap analysis. Implement your logic here.")
        plt.figure(figsize=(8, 6))
        plt.imshow(heatmap_data, cmap="YlOrRd", aspect="auto")
        plt.title("Traffic Heatmap")
        plt.xlabel("Hour")
        plt.ylabel("Day")
        plt.xticks(np.arange(len(heatmap_data.columns)), heatmap_data.columns)
        plt.yticks(np.arange(len(heatmap_data.index)), heatmap_data.index)
        self.st.pyplot(plt)
    def Anomaly_Detection(self):
        self.st.subheader("Anomaly Detection")
        self.st.info("This is a placeholder for anomaly detection. Implement your logic here.")
        vehicle_mean = np.mean(self.df["Vehicles"])
        vehicle_std = np.std(self.df["Vehicles"])

        threshold_high = vehicle_mean + 2 * vehicle_std
        threshold_low = vehicle_mean - 2 * vehicle_std

        anomalies = self.df[(self.df["Vehicles"] > threshold_high) | (self.df["Vehicles"] < threshold_low)]
        traffic_time = self.df.groupby("DateTime")["Vehicles"].sum()

        mean_val = np.mean(traffic_time.values)
        std_val = np.std(traffic_time.values)
        upper = mean_val + 2 * std_val

        anomaly_points = traffic_time[traffic_time > upper]

        plt.figure(figsize=(8, 5))
        plt.plot(traffic_time.index, traffic_time.values, label="Traffic")
        plt.scatter(anomaly_points.index, anomaly_points.values, label="Anomalies")
        plt.title("Traffic Anomaly Detection")
        plt.xlabel("Time")
        plt.ylabel("Vehicles")
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        self.st.pyplot(plt)