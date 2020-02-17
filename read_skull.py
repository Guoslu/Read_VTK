import sys

import numpy
import vtk

# 实例化Reader对象
reader = vtk.vtkPolyDataReader()
# 指定所要读取的文件名
reader.SetFileName(sys.argv[1])
# 调用Updata()方法促使管线执行
reader.Update()

polydata = reader.GetOutput()

for i in range(polydata.GetNumberOfCells()):
    pts = polydata.GetCell(i).GetPoints()
    np_pts = numpy.array([pts.GetPoint(i) for i in range(pts.GetNumberOfPoints())])
    print(i)
    print(np_pts)
