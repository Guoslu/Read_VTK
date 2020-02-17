# Read_VTK

## VTK文件格式

ASCII or binary;
由五部分组成，前三部分必须，后两部分可选。

* **vtk DataFile Version m.n**  
  第一行 "m.n" 是版本号.
* a title
  标题最多256个字符，以换行结束.
* **ASCII or BINARY**
  indicates the format used for subsequent data.
* **DATASET type**
  共5种类型，"STRUCTURED_POINTS"、"STRUCTURED_GRID"、"UNSTRUCTURED_GRID"、"POLYDATA"、"RECTILINEAR_GRID"; 
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

  
