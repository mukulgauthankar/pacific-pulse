# ♨️ Pacific Pulse: Ocean Networks Canada Marine Heatwave Tracker
> **Ocean Hackathon Challenge:** Super El Niño Tracker  
> **Data Infrastructure:** Ocean Networks Canada (ONC) Oceans 3.0 API  
> **Focus Region:** Vancouver Island Coastal Shelf to Cascadia Margin

---

## 🌊 Overview
Satellite sea surface temperature (SST) observations are fundamentally limited to the skin layer of the ocean. During major climate anomalies such as the 2015–2016 'Godzilla' El Niño and the 2023–2024 global warming pulse, coastal fisheries managers and oceanographers urgently require sub-surface observations: **Does thermal stress remain trapped near the surface, or does it downwell into benthic shelf habitats?**

**Pacific Pulse** is an interactive, real-time monitoring engine that bridges surface-to-benthos dynamics using continuous seafloor cabled observatories off Vancouver Island.

---

## 🔬 Scientific Methodology

### 1. Hobday et al. (2016) Marine Heatwave Definition
The engine ingests calibrated daily temperature records and derives:
* **Climatological Baseline ($T_{seas}$):** 31-day rolling day-of-year mean climatology.
* **90th Percentile Threshold ($T_{90}$):** Rolling upper bound defining an anomalous thermal state.
* **Intensity Categorization:**
  * **Category I (Moderate):** 1x to 2x threshold exceedance
  * **Category II (Strong):** 2x to 3x threshold exceedance
  * **Category III (Severe):** 3x to 4x threshold exceedance
  * **Category IV (Extreme):** >4x threshold exceedance

### 2. Vertical Transect & Array Architecture
The pipeline monitors a 3-node depth gradient:
* **Folger Pinnacle (`FGPPN`, 25 m):** Euphotic shelf zone, capturing primary production, kelp holdfast depth, and juvenile salmon corridors.
* **Folger Deep (`FGPD`, 96 m):** Benthic continental shelf basin, assessing thermal downwelling, bottom-water hypoxia coupling, and groundfish habitats.
* **Barkley Canyon (`NCBC`, 400 m):** Upper continental slope, tracking open-ocean intermediate water masses.

---

## 🚀 Key Features
* **Real-Time Anomaly Detection:** Calculates thermal anomalies relative to rolling climatologies.
* **Depth Penetration Visualizer:** Directly compares 25 m vs. 96 m anomalies to evaluate vertical stratification and heat penetration.
* **Interactive Bathymetric Mapping:** Built on the Esri Ocean Basemap displaying active station locations.
* **Coastal Ecological Risk Matrix:** Automated alerts assessing thresholds for bull kelp mortality, juvenile salmon bioenergetics, and benthic oxygen ventilation.
* **Stakeholder Export:** One-click CSV reporting formatted for rapid assessment by coastal managers.

---

## 🛠️ Quickstart
```bash
pip install -r requirements.txt
streamlit run app.py
```
