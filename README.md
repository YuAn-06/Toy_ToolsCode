# Toy_Tools
*Some tools for time series data*

* **`FFT.py`:** **Toy code of Fast Fourier Transform for time series data and corresponding visualizations. The shape of data is **\[N,D\]**, N, D represents the number of data and dimension.**

**Original Data**:
![data](https://github.com/YuAn-06/Toy_ToolsCode/blob/main/figs/ppgas2011.png)\
**The result of ppgas2011 data after fast fourier transform**:
![fre&amp](https://github.com/YuAn-06/Toy_ToolsCode/blob/main/figs/FFT_ppgas.png)
**The result of noise reduction of the part with frequency greater than 0.1**:
![filtered](https://github.com/YuAn-06/Toy_ToolsCode/blob/main/figs/ppgas2011_filtered.png)

* **`auto_correlation.py`:** **Toy code to test autocorrelation, stationary and variable correlation for time series data and corresponding visualizations. The shape of data is **\[N,D\]**, N, D represents the number of data and dimension.**

*  **`Postional Embedding visualization.py`:** Toy code for the visualization of Postional Embedding.
  ![visual](https://github.com/YuAn-06/Toy_ToolsCode/blob/main/figs/Postional%20Embedding.jpg)
## Requirement:
* `pytorch >= 1.8`
