# Read_VTK
====
## VTK文件格式

ASCII or binary;
The VTK file format consists of five parts; the first three are mandatory, and the last two are optional.

* **vtk DataFile Version m.n**  
  The header line. "m.n" is the version number.
* a title
  The title may be up to 256 characters, terminated by a new line.
* **ASCII or BINARY**
  indicates the format used for subsequent data.
* **DATASET type**
  values for type are "STRUCTURED_POINTS" or "STRUCTURED_GRID" or "UNSTRUCTURED_GRID" or "POLYDATA" or "RECTILINEAR_GRID"; Depending on the type chosen, there will be further lines of keywords and values to define the data.
* **POINT_DATA n**
  The number of data items n of each type must match the number of points in the dataset.

  When describing the cells in terms of point indices, the points must be indexed starting at 0.

  All point data must use 3 coordinates. Even if your model has 2D geometry, each point must have (X,Y,Z) coordinates. Simply set Z = 0 if you want to work in 2D.


### 1. 安装
```python
pip install vtk
```
### 2. 运行
```python
python read_skull.py skull.vtk
```
### 3. 输出格式
共1991479个cells，每个cells由3个三元组组成

参考：
  [Read a .vtk file with python](https://stackoverflow.com/questions/11727822/reading-a-vtk-file-with-python)
  [VTK Files](https://people.sc.fsu.edu/~jburkardt/data/vtk/vtk.html)

  
