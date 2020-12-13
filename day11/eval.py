import numpy


def CountNeighbours(theInputMatrix,countRadius=1,borderValue=0.):
    """CountNeighbours(theInputMatrix,countRadius,borderValue) spirals around theInputMatrix to produce resultMatrix: 
    a matrix with the same dimensions as the input with with elements containing the sum of neighbour elements.
    The radius of the neighbours to include is set with counterRadius (default = 1), the value for elements beyond
    the borders is set with borderValue (default = 0.)."""
    heightFP,widthFP = theInputMatrix.shape 
    #define hight and width of input matrix
    # make a matrix same size as input matrix plus borders the same size as the neighbour radius and
    # set the border to borderValue
    withBorders = numpy.ones((heightFP+(2*countRadius),widthFP+(2*countRadius)))*borderValue
    # set the interior region to the input matrix
    withBorders[countRadius:heightFP+countRadius,countRadius:widthFP+countRadius]=theInputMatrix
    # set up an empty matrix for the results
    
    resultMatrix = numpy.zeros((heightFP,widthFP)) 
    
    minRow,minCol = 0,0
    maxRow,maxCol = 2.*countRadius,2.*countRadius
    rowVal,colVal = 0,0
    # spiral round... 
    for i in range(4*countRadius):
        while colVal<maxCol: #move right along top of spiral
            resultMatrix = resultMatrix + withBorders[rowVal:heightFP+rowVal,colVal:widthFP+colVal]
            colVal += 1
 
        while rowVal<maxRow: #move down right hand side of spiral
            resultMatrix = resultMatrix + withBorders[rowVal:heightFP+rowVal,colVal:widthFP+colVal]
            rowVal += 1
 
        while colVal>minCol: #move left along base of spiral
            resultMatrix = resultMatrix + withBorders[rowVal:heightFP+rowVal,colVal:widthFP+colVal]
            colVal -= 1
        minRow += 1
        maxCol -= 1
        while rowVal > minRow: #move up left hand side of spiral
            resultMatrix = resultMatrix + withBorders[rowVal:heightFP+rowVal,colVal:widthFP+colVal]
            rowVal -= 1
        minCol += 1
        maxRow -= 1
    return resultMatrix

####################################
# small test #
####################################

#set up the input matrix
theInputMatrix = numpy.array([(0., 0., 1., 1., 1.),(1., 1., 0., 0., 1.),(0., 1., 1., 0., 0.),(0., 0., 1., 0., 0.),(0., 1., 0., 1., 1.)])

countRadius = 1 #the radius of neighbour elements to include in the sum 
borderValue = 0. #the value to assign to elements off the edges of the 'grid'

resultMatrix = CountNeighbours(theInputMatrix,countRadius,borderValue) #call the function
print(theInputMatrix)
print(resultMatrix)