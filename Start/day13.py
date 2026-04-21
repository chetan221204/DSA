# matrix=[
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12],
#     [13,14,15,16]
# ]
# n=len(matrix)
# for i in range(n):
#     for j in range(i+1,n):
#         matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
# for i in range(n):
#     matrix[i].reverse()

# # print(matrix)
# for row in matrix:
#     print(row)




# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# n=len(matrix)
# m=len(matrix[0])
# s=[]
# left=0
# right=m-1
# top=0
# bottom=n-1
# while top <=bottom and left<=right:
#     for i in range(left,right+1):
#         s.append(matrix[top][i])
#     top+=1
#     for i in range(top,bottom+1):
#         s.append(matrix[i][right])
#     right-=1
#     if top <=bottom:
#         for i in range(right,left-1,-1):
#             s.append(matrix[bottom][i])
#         bottom-=1

#     if left <=right:
#         for i in range(bottom,top-1,-1):
#             s.append(matrix[i][left])
#         left+=1
# print(s)
# for row in s:
#     print(s)


 