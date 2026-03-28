import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
class Weather:

    analysis_options = [
        "Temperature Analysis",
        "Humidity Analysis",
        "Rainfall Analysis",
        "Wind Speed Analysis",
        "Time-Based Analysis",
        "City Comparison",
        "Correlation Analysis"
    ]

    def __init__(self, df, st, analysis_type):
        self.df = df
        self.st = st

        # datetime processing (same as traffic)
        self.df["DateTime"] = pd.to_datetime(self.df["DateTime"])
        self.df["Date"] = self.df["DateTime"].dt.date
        self.df["Hour"] = self.df["DateTime"].dt.hour
        self.df["Day"] = self.df["DateTime"].dt.day_name()

        left, right = st.columns([1, 1])
        self.analysis_type = np.array(analysis_type)

        for x in self.analysis_type:
            if x == "Temperature Analysis":
                with left:
                    self.Temperature_Analysis()
            elif x == "Humidity Analysis":
                with right:
                    self.Humidity_Analysis()
            elif x == "Rainfall Analysis":
                with left:
                    self.Rainfall_Analysis()
            elif x == "Wind Speed Analysis":
                with right:
                    self.WindSpeed_Analysis()
            elif x == "Time-Based Analysis":
                with left:
                    self.TimeBased_Analysis()
            elif x == "City Comparison":
                with right:
                    self.City_Comparison()
            elif x == "Correlation Analysis":
                with left:
                    self.Correlation_Analysis()
    def Temperature_Analysis(self):
        self.st.subheader("Temperature Analysis")

        temp_trend = self.df.groupby("Date")["Temperature"].mean()

        plt.figure(figsize=(8,4))
        plt.plot(temp_trend.index, temp_trend.values)
        plt.title("Temperature Trend")
        plt.xlabel("Date")
        plt.ylabel("Temperature")
        self.st.pyplot(plt)
    def Humidity_Analysis(self):
        self.st.subheader("Humidity Analysis")

        humidity = self.df.groupby("Date")["Humidity"].mean()

        plt.figure(figsize=(8,4))
        plt.plot(humidity.index, humidity.values)
        plt.title("Humidity Trend")
        self.st.pyplot(plt)
    def Rainfall_Analysis(self):
        self.st.subheader("Rainfall Analysis")

        rainfall = self.df.groupby("Date")["Rainfall"].sum()

        plt.figure(figsize=(8,4))
        plt.bar(rainfall.index, rainfall.values)
        plt.title("Rainfall Distribution")
        self.st.pyplot(plt)

    def WindSpeed_Analysis(self):
        self.st.subheader("Wind Speed Analysis")

        wind = self.df.groupby("Date")["WindSpeed"].mean()

        plt.figure(figsize=(8,4))
        plt.plot(wind.index, wind.values)
        plt.title("Wind Speed Trend")
        self.st.pyplot(plt)
    
    def TimeBased_Analysis(self):
        self.st.subheader("Time-Based Analysis")

        hourly_temp = self.df.groupby("Hour")["Temperature"].mean()

        plt.figure(figsize=(8,4))
        plt.plot(hourly_temp.index, hourly_temp.values)
        plt.title("Hourly Temperature Pattern")
        self.st.pyplot(plt)


    def City_Comparison(self):
        self.st.subheader("City Comparison")

        city_temp = self.df.groupby("City")["Temperature"].mean()

        plt.figure(figsize=(8,4))
        plt.bar(city_temp.index, city_temp.values)
        plt.title("City-wise Temperature")
        self.st.pyplot(plt)

    def Correlation_Analysis(self):
        self.st.subheader("Correlation Analysis")

        corr = self.df[["Temperature","Humidity","Rainfall","WindSpeed"]].corr()

        plt.figure(figsize=(6,5))
        plt.imshow(corr, cmap="coolwarm")
        plt.colorbar()

        plt.xticks(range(len(corr.columns)), corr.columns)
        plt.yticks(range(len(corr.columns)), corr.columns)

        plt.title("Weather Correlation Matrix")
        self.st.pyplot(plt)