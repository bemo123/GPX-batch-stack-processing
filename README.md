# GPX-batch-stack-processing
 Several PYTHON scripts for batch processing of GPX files. With it you manipulate multiple GPX files in one folder with one script execution. The following manipulations are available:
 - change the CREATOR field to a desired value
 - change the FILENAME to a desired value or add prefix/postfix to the filename
 - add a COMMENT to the GPX file, e.g. a disclaimer
 - create a text file with GPX details: vertical climb uphill, vertical descent downhill, lowest point, highest point, max elevation angle uphill, max elevation angle downhill
- create a new gpx with a spline interpolation of the original track


# Usage
I recommend using Anaconda Python IDE to execute the scripts. Create a new environment in Anaconda.Navigator and install the required libraries 
- scipy
- pandas
- pyproj

Then, install Spyder to your new environment using Anaconda.Navigator again. Launch Spyder and create a working directory. Download this repository with all its .py scripts into the working directory and add all GPX files that you want to manipulate.

Run the desired .py script by typing 

```python
run xyz.py
```
