def linearsearchproduct(productlist,targetproduct):
  indices=[]
  for index, product in enumerate (productlist):
    if product==targetproduct:
      indices.append(index)
  return indices 
products=["bangles","chains","earings","bangles","rings","earings"]
target="bangles"
result=linearsearchproduct(products,target)
print(result)
    
    