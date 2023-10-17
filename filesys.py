##import pandas as pd
##x=pd.read_csv('std.csv')
##u=set(x['Name'])
##print(u)
##d={1,2,3,(4,2,6,6,5),6,4}
##print(d)
##d={'jan','app','mar','apr'}
##print(d)
data={'Name':['Dip','raj','sachin'],'Age':[25,35,65],'Sal':[2500,4500,1500]}
#print(data.keys())
#print(data.values())
##for i ,j in data.items():
##    print(j)

import pandas as pd
x=pd.DataFrame(data)
x.to_csv('anudip.csv',index=False)
