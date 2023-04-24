# import libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

ts = pd.Series(np.random.randn(1000), index = pd.date_range('1/1/2000', periods = 1000))
ts = ts.cumsum()
ts.plot()
plt.show()

# importing libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

ts = pd.Series(np.random.randn(1000), index = pd.date_range('1/1/2000', periods = 1000))
df = pd.DataFrame(np.random.randn(1000, 4), index = ts.index,columns = list('ABCD'))
df3 = pd.DataFrame(np.random.randn(1000, 2),columns =['B', 'C']).cumsum()
df3['A'] = pd.Series(list(range(len(df))))
df3.iloc[5].plot.bar()
plt.axhline(0, color ='k')
plt.show()


# importing libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df4 = pd.DataFrame({'a': np.random.randn(1000) + 1,'b': np.random.randn(1000),'c': np.random.randn(1000) - 1},columns =['a', 'b', 'c'])
plt.figure()
df4.plot.hist(alpha = 0.5)
plt.show()

# importing libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.rand(10, 5),columns =['A', 'B', 'C', 'D', 'E'])
df.plot.box()
plt.show()

