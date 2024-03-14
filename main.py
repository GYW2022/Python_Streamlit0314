import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

'Start!!!!!'

lastest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    lastest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!!!!'


st.title('Streamlit 超入門')
st.write('DataFrame')

df = pd.DataFrame({
    '1列目':[1,2,3,4],
    '2列目':[10,20,30,40]
})

st.write(df)

st.dataframe(df.style.highlight_max(axis=0))

st.table(df.style.highlight_max(axis=0))

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd

```
"""

df2 = pd.DataFrame(
   np.random.rand(20,3),
   columns=['a','b','c']
)

st.line_chart(df2)

st.area_chart(df2)

st.bar_chart(df2)

df3 = pd.DataFrame(
   np.random.rand(100,2)/[50,50]+[35.69,139.70],
   columns=['lat','lon']
)

st.map(df3)

st.write('Display Image')

if st.checkbox('Show Image'):
    img = Image.open('WechatIMG3.jpeg')
    st.image(img,caption='Zhu Ji Xiang',use_column_width=True)
    
st.sidebar.write('Interactive Widgets')

option = st.selectbox(
    '请选择一个数字。',
    list(range(1,11))
)

# '你喜欢的数字是 ',option,'。'

# text1 = st.text_input('请输入你的兴趣。')

# '你的兴趣是 ',text1,'。'

# condition1 = st.slider('你现在的健康评分是多少？',0,100,50)

# '健康评分:',condition1

text2 = st.sidebar.text_input('请输入你的兴趣。')

'你的兴趣是 ',text2,'。'

condition2 = st.sidebar.slider('你现在的健康评分是多少？',0,100,50)

'健康评分:',condition2

left_column,right_column = st.columns(2)
button1 = left_column.button('右カラムに文字を表示')
if button1:
    right_column.write('ここは右カラム')

expander1 = st.expander('問い合わせ１')
expander1.write('問い合わせ１の回答')
expander2 = st.expander('問い合わせ２')
expander2.write('問い合わせ２の回答')
expander3 = st.expander('問い合わせ３')
expander3.write('問い合わせ３の回答')

st.write('プレグレスバーの表示')


