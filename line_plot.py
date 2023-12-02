import seaborn as sb
import matplotlib.pyplot as plt
import panda as pd

var=[1,2,3,4,5,6,7,8,9]
var1=[2,8,4,6,9,2,7,3,9]
x_1=pd.DataFrame({"var":var,"var1":var1})
sb.lineplot(x='var',y='var1',data= x_1)
