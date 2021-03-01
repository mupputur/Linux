
"""
Write a program to get the indices of duplicated elements from given input list.
"""


def duplicated_indices(input_list):
      m=[]
      n=[]
      for indices in range(len(x)):
            if x[indices] not in m:
                  m.append(x[indices])
            else:
                  n.append(indices)
      return n


input_list1=x=[121,122,123,124,125,126,123,124,127,128,121]
resp=duplicated_indices(input_list1)
print(resp)
