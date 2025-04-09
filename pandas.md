# Pandas Tutorial
- Pandas is a Python Library.
- Pandas is used to analyze data.

# Pandas Introduction

**What is Pandas?**
- Pandas is a python library used for working with data sets.
- It has functions for analyzing, cleaning, exploring, and manipulating data.
- The name `Pandas` has a reference to both `Panel Data` and `Python data analysis` and was created by `Wes Mckinney in 2008.

**Why Use Pandas?**
- Pandas allows us to analyze big data and make conclusions based on statistical theories.
- Pandas can clean messy data sets, and make them readable and relevant.
- Relevant data is very important in data science.

**Data Science** : Data science is a branch of computer science where we study how to store, use and analyze data for deriving information from it.

**What can Pandas Do?** : Pandas give to answers about the data like:
- Is there a correlation between two or more columns.
- What is average value?
- Max Value?
- Min Value?

- Pandas are also able to delete rows that are not relevant, or contain wrong values like empty or NULL values. This is called the cleaning the data.

- To install the pandas we use the following commands

```
pip install pandas
```

# Import pandas
- Once pandas is installed, import it in our applications by adding the `import` keyword.

```
import pandas
```

**Pandas as pd**
- Pandas is usually imported under the `pd` alias.
- `alias` : In python alias are an alternate name for referring to the same thing.
- Create an alias with the `as` keyword while importing

```
import pandas as pd
```

# Checking Pandas Version
- The version string is stored under `__version__` attribute
```
import pandas as pd
print(pd.__version__)
```

# Pandas Series

**What is a Series?**
- A Pandas Series is like a column in a table.
- It is one-dimensional array holding data of any type.

**Create a simple pandas series from a list**

```
import pandas as pd
a=[1,7,2]
myvar=pd.Series(a)
print(myvar)
```
**Output**
```
0    1
1    7
2    2
dtype: object
```

# Labels
- If nothing else is specified, the values are labeled with their index number.First values has index 0, second value has index 1 etc.
- This label can be used to access a specified value.

```
# Labels
import pandas as pd
a=[1,7,2]
myvar=pd.Series(a)
print(myvar[0])
```
**Output**
```
1
```

# Create Labels
- With the `index` argument, we can name our own labels.

```
# create our own labels
import pandas as pd
a=[1,7,3]
myvar=pd.Series(a,index=['x','y','z'])
print(myvar)
```

**Output**
```
x    1
y    7
z    3
dtype: int64
```

- When we have created labels, we can access an item by referring  to the labels

```
import pandas as pd
a=[1,2,3,4]
myvar=pd.Series(a,index=['x','y','z','w'])
print(myvar['y'])
```
**Output**:
```
2
```

# Key/Value Objects as a Series
- We can also use a key/value object, like a dictionary, when creating a series.

**Create a simple pandas Series from a dictionay**

```
import pandas as pd
calories={'day1':420,'day2':380,'day3':390}
myvar=pd.Series(calories)
print(myvar)
```

**Output** 
```
day1    420
day2    380
day3    390
dtype: int64
```
**Note** : The keys of the dictionay become the labels.

- To select only some of items in the dictioanry, use the `index` argument and specify only the items we want to include in the series.

**Create a Series using only data from "day1 and "day2"**

```
import pandas as pd
calories={"day1":340,"day2":546,"day3":455}
myvar=pd.Series(calories,index=['day1','day2'])
print(myvar)
```

**Output**
```
day1    340
day2    546
dtype: int64
```

# DataFrames
- Data set in Pandas are usually multi-dimensional tables, called DataFrames.
- `Series is like a column, a DataFrame is the whole table `.

**Example**

```
import pandas as pd
data={
    "calories":[420,380,390],
    "duration":[50,40,45]
}
myvar=pd.DataFrame(data)
print(myvar)
```

**Output**

```
calories  duration
0       420        50
1       380        40
2       390        45
```

# Pandas DataFrames
**What is a DataFrame?**
- A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.

```
# Create a simple Pandas DataFrame
import pandas as pd
data={
    "calories":[444,456,457],
    "durarion":[30,35,40]
}
myvar=pd.DataFrame(data)
print(myvar)
```
**Output**

```
calories  durarion
0       444        30
1       456        35
2       457        40
```

# Locate Row
- As we can see from the result above, the DataFrame is like a table with rows and columns.
- Pandas use the `loc` attribute to return one or more specified row.

```
import pandas as pd
data={
    "calories":[100,200,300,400],
    "duration":[50,60,70,80]
}
df=pd.DataFrame(data)
print(df.loc[2])
```

**Output**

```
calories    300
duration     70
Name: 2, dtype: int64
```

**Return row 0 and 1**

```
import pandas as pd
data={
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
}
df=pd.DataFrame(data)
print(df.loc[[0,1]])
```
**Output** : 
```
Name  Age
0  John   28
1  Anna   24
```
**Note** : When using [], the result is a pandas `DataFrame`

# Named Indexes
- With the `index` argument, we can name our own indexes.

**Example** : 

```
# add a lists of names to give each row a name
import pandas as pd
data={
    "calories":[420,380,390],
    "duration":[50,40,45]
}
df=pd.DataFrame(data,index=['day1','day2','day3'])
print(df)
```

**Output** : 
```
calories  duration
day1       420        50
day2       380        40
day3       390        45
```

**Locate Named Indexes** : Use the names index in the `loc` attribute to return the specified row.

**Example** :
```
import pandas as pd
data={
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32]
}
df=pd.DataFrame(data,index=["day1","day2","day3","day4"])
print(df.loc["day2"])
```
**Output** : 
```
Name    Anna
Age       24
Name: day2, dtype: object
``` 
# Pandas Read CSV

**Read CSV Files**

- A simple way to store big data sets is to use CSV files(comma seperated files).
- CSV files contains plain text and is a well know format that can be read by everyone including pandas.

**Example** :

```
import pandas as pd
df=pd.read_csv("C:\\Users\\pc\\Downloads\\data.csv")
print(df.to_string())
```

**Output** : 
```
Duration  Pulse  Maxpulse  Calories
0          60    110       130     409.1
1          60    117       145     479.0
2          60    103       135     340.0
3          45    109       175     282.4
4          45    117       148     406.0
5          60    102       127     300.0
6          60    110       136     374.0
7          45    104       134     253.3
8          30    109       133     195.1
9          60     98       124     269.0
10         60    103       147     329.3
11         60    100       120     250.7
12         60    106       128     345.3
13         60    104       132     379.3
14         60     98       123     275.0
15         60     98       120     215.2
16         60    100       120     300.0
17         45     90       112       NaN
18         60    103       123     323.0
19         45     97       125     243.0
20         60    108       131     364.2
21         45    100       119     282.0
22         60    130       101     300.0
23         45    105       132     246.0
24         60    102       126     334.5
25         60    100       120     250.0
26         60     92       118     241.0
27         60    103       132       NaN
28         60    100       132     280.0
29         60    102       129     380.3
30         60     92       115     243.0
31         45     90       112     180.1
32         60    101       124     299.0
33         60     93       113     223.0
34         60    107       136     361.0
35         60    114       140     415.0
36         60    102       127     300.0
37         60    100       120     300.0
38         60    100       120     300.0
39         45    104       129     266.0
40         45     90       112     180.1
41         60     98       126     286.0
42         60    100       122     329.4
43         60    111       138     400.0
44         60    111       131     397.0
45         60     99       119     273.0
46         60    109       153     387.6
47         45    111       136     300.0
48         45    108       129     298.0
49         60    111       139     397.6
50         60    107       136     380.2
51         80    123       146     643.1
52         60    106       130     263.0
53         60    118       151     486.0
54         30    136       175     238.0
55         60    121       146     450.7
56         60    118       121     413.0
57         45    115       144     305.0
58         20    153       172     226.4
59         45    123       152     321.0
60        210    108       160    1376.0
61        160    110       137    1034.4
62        160    109       135     853.0
63         45    118       141     341.0
64         20    110       130     131.4
65        180     90       130     800.4
66        150    105       135     873.4
67        150    107       130     816.0
68         20    106       136     110.4
69        300    108       143    1500.2
70        150     97       129    1115.0
71         60    109       153     387.6
72         90    100       127     700.0
73        150     97       127     953.2
74         45    114       146     304.0
75         90     98       125     563.2
76         45    105       134     251.0
77         45    110       141     300.0
78        120    100       130     500.4
79        270    100       131    1729.0
80         30    159       182     319.2
81         45    149       169     344.0
82         30    103       139     151.1
83        120    100       130     500.0
84         45    100       120     225.3
85         30    151       170     300.0
86         45    102       136     234.0
87        120    100       157    1000.1
88         45    129       103     242.0
89         20     83       107      50.3
90        180    101       127     600.1
91         45    107       137       NaN
92         30     90       107     105.3
93         15     80       100      50.5
94         20    150       171     127.4
95         20    151       168     229.4
96         30     95       128     128.2
97         25    152       168     244.2
98         30    109       131     188.2
99         90     93       124     604.1
100        20     95       112      77.7
101        90     90       110     500.0
102        90     90       100     500.0
103        90     90       100     500.4
104        30     92       108      92.7
105        30     93       128     124.0
106       180     90       120     800.3
107        30     90       120      86.2
108        90     90       120     500.3
109       210    137       184    1860.4
110        60    102       124     325.2
111        45    107       124     275.0
112        15    124       139     124.2
113        45    100       120     225.3
114        60    108       131     367.6
115        60    108       151     351.7
116        60    116       141     443.0
117        60     97       122     277.4
118        60    105       125       NaN
119        60    103       124     332.7
120        30    112       137     193.9
121        45    100       120     100.7
122        60    119       169     336.7
123        60    107       127     344.9
124        60    111       151     368.5
125        60     98       122     271.0
126        60     97       124     275.3
127        60    109       127     382.0
128        90     99       125     466.4
129        60    114       151     384.0
130        60    104       134     342.5
131        60    107       138     357.5
132        60    103       133     335.0
133        60    106       132     327.5
134        60    103       136     339.0
135        20    136       156     189.0
136        45    117       143     317.7
137        45    115       137     318.0
138        45    113       138     308.0
139        20    141       162     222.4
140        60    108       135     390.0
141        60     97       127       NaN
142        45    100       120     250.4
143        45    122       149     335.4
144        60    136       170     470.2
145        45    106       126     270.8
146        60    107       136     400.0
147        60    112       146     361.9
148        30    103       127     185.0
149        60    110       150     409.4
150        60    106       134     343.0
151        60    109       129     353.2
152        60    109       138     374.0
153        30    150       167     275.8
154        60    105       128     328.0
155        60    111       151     368.5
156        60     97       131     270.4
157        60    100       120     270.4
158        60    114       150     382.8
159        30     80       120     240.9
160        30     85       120     250.4
161        45     90       130     260.4
162        45     95       130     270.0
163        45    100       140     280.9
164        60    105       140     290.8
165        60    110       145     300.0
166        60    115       145     310.2
167        75    120       150     320.4
168        75    125       150     330.4
```

**use `to_string()` to print the entire DataFrame**

- If we have a large DataFrame with many rows, pandas will only return the first 5 rows, and the last 5 rows.

**Example** : 

**print the DataFrame without the `to_string()` method:**

```
import pandas as pd
df=pd.read_csv("C:\\Users\\pc\\Downloads\\data.csv")
print(df)
```

**Output** :

```
Duration  Pulse  Maxpulse  Calories
0          60    110       130     409.1
1          60    117       145     479.0
2          60    103       135     340.0
3          45    109       175     282.4
4          45    117       148     406.0
..        ...    ...       ...       ...
164        60    105       140     290.8
165        60    110       145     300.0
166        60    115       145     310.2
167        75    120       150     320.4
168        75    125       150     330.4

[169 rows x 4 columns]
```

# max_rows
- The number of rows returned is defined in Pandas Option settings.
- We can check our systems maximum rows with the `pd.options.display.max_rows` statement.

```
# check the number of maximum returned rows

import pandas as pd
print(pd.options.display.max_rows)
```

**Output** : 
```
60
```
- In my system the number is 60 which means that if the DataFrame contains more than 60 rows, the `print(df)` statement will return only the headers and the first and last 5 rows.
- We can change the maximum rows number with the same statement.

```
# Increase the maximum number of rows to display the entire DataFrame

import pandas as pd
pd.options.display.max_rows=9999
df=pd.read_csv("C:\\Users\\pc\\Downloads\\data.csv")
print(df)
```

**Output**
```
Duration  Pulse  Maxpulse  Calories
0          60    110       130     409.1
1          60    117       145     479.0
2          60    103       135     340.0
3          45    109       175     282.4
4          45    117       148     406.0
5          60    102       127     300.0
6          60    110       136     374.0
7          45    104       134     253.3
8          30    109       133     195.1
9          60     98       124     269.0
10         60    103       147     329.3
11         60    100       120     250.7
12         60    106       128     345.3
13         60    104       132     379.3
14         60     98       123     275.0
15         60     98       120     215.2
16         60    100       120     300.0
17         45     90       112       NaN
18         60    103       123     323.0
19         45     97       125     243.0
20         60    108       131     364.2
21         45    100       119     282.0
22         60    130       101     300.0
23         45    105       132     246.0
24         60    102       126     334.5
25         60    100       120     250.0
26         60     92       118     241.0
27         60    103       132       NaN
28         60    100       132     280.0
29         60    102       129     380.3
30         60     92       115     243.0
31         45     90       112     180.1
32         60    101       124     299.0
33         60     93       113     223.0
34         60    107       136     361.0
35         60    114       140     415.0
36         60    102       127     300.0
37         60    100       120     300.0
38         60    100       120     300.0
39         45    104       129     266.0
40         45     90       112     180.1
41         60     98       126     286.0
42         60    100       122     329.4
43         60    111       138     400.0
44         60    111       131     397.0
45         60     99       119     273.0
46         60    109       153     387.6
47         45    111       136     300.0
48         45    108       129     298.0
49         60    111       139     397.6
50         60    107       136     380.2
51         80    123       146     643.1
52         60    106       130     263.0
53         60    118       151     486.0
54         30    136       175     238.0
55         60    121       146     450.7
56         60    118       121     413.0
57         45    115       144     305.0
58         20    153       172     226.4
59         45    123       152     321.0
60        210    108       160    1376.0
61        160    110       137    1034.4
62        160    109       135     853.0
63         45    118       141     341.0
64         20    110       130     131.4
65        180     90       130     800.4
66        150    105       135     873.4
67        150    107       130     816.0
68         20    106       136     110.4
69        300    108       143    1500.2
70        150     97       129    1115.0
71         60    109       153     387.6
72         90    100       127     700.0
73        150     97       127     953.2
74         45    114       146     304.0
75         90     98       125     563.2
76         45    105       134     251.0
77         45    110       141     300.0
78        120    100       130     500.4
79        270    100       131    1729.0
80         30    159       182     319.2
81         45    149       169     344.0
82         30    103       139     151.1
83        120    100       130     500.0
84         45    100       120     225.3
85         30    151       170     300.0
86         45    102       136     234.0
87        120    100       157    1000.1
88         45    129       103     242.0
89         20     83       107      50.3
90        180    101       127     600.1
91         45    107       137       NaN
92         30     90       107     105.3
93         15     80       100      50.5
94         20    150       171     127.4
95         20    151       168     229.4
96         30     95       128     128.2
97         25    152       168     244.2
98         30    109       131     188.2
99         90     93       124     604.1
100        20     95       112      77.7
101        90     90       110     500.0
102        90     90       100     500.0
103        90     90       100     500.4
104        30     92       108      92.7
105        30     93       128     124.0
106       180     90       120     800.3
107        30     90       120      86.2
108        90     90       120     500.3
109       210    137       184    1860.4
110        60    102       124     325.2
111        45    107       124     275.0
112        15    124       139     124.2
113        45    100       120     225.3
114        60    108       131     367.6
115        60    108       151     351.7
116        60    116       141     443.0
117        60     97       122     277.4
118        60    105       125       NaN
119        60    103       124     332.7
120        30    112       137     193.9
121        45    100       120     100.7
122        60    119       169     336.7
123        60    107       127     344.9
124        60    111       151     368.5
125        60     98       122     271.0
126        60     97       124     275.3
127        60    109       127     382.0
128        90     99       125     466.4
129        60    114       151     384.0
130        60    104       134     342.5
131        60    107       138     357.5
132        60    103       133     335.0
133        60    106       132     327.5
134        60    103       136     339.0
135        20    136       156     189.0
136        45    117       143     317.7
137        45    115       137     318.0
138        45    113       138     308.0
139        20    141       162     222.4
140        60    108       135     390.0
141        60     97       127       NaN
142        45    100       120     250.4
143        45    122       149     335.4
144        60    136       170     470.2
145        45    106       126     270.8
146        60    107       136     400.0
147        60    112       146     361.9
148        30    103       127     185.0
149        60    110       150     409.4
150        60    106       134     343.0
151        60    109       129     353.2
152        60    109       138     374.0
153        30    150       167     275.8
154        60    105       128     328.0
155        60    111       151     368.5
156        60     97       131     270.4
157        60    100       120     270.4
158        60    114       150     382.8
159        30     80       120     240.9
160        30     85       120     250.4
161        45     90       130     260.4
162        45     95       130     270.0
163        45    100       140     280.9
164        60    105       140     290.8
165        60    110       145     300.0
166        60    115       145     310.2
167        75    120       150     320.4
168        75    125       150     330.4
```



# Pandas Read Json

**Read Json** : Big data sets are often stored , or extracted as JSON.
- JSON is plain text, but has the format of an object, and is well known in the world of programming including pandas.

```
# load the json file into a data frame
import pandas as pd
df=pd.read_json("C:\\Users\\pc\\Downloads\\data.json")
print(df.to_string())
```
**Output** : 

```
Duration  Pulse  Maxpulse  Calories
0          60    110       130     409.1
1          60    117       145     479.0
2          60    103       135     340.0
3          45    109       175     282.4
4          45    117       148     406.0
5          60    102       127     300.5
6          60    110       136     374.0
7          45    104       134     253.3
8          30    109       133     195.1
9          60     98       124     269.0
10         60    103       147     329.3
11         60    100       120     250.7
12         60    106       128     345.3
13         60    104       132     379.3
14         60     98       123     275.0
15         60     98       120     215.2
16         60    100       120     300.0
17         45     90       112       NaN
18         60    103       123     323.0
19         45     97       125     243.0
20         60    108       131     364.2
21         45    100       119     282.0
22         60    130       101     300.0
23         45    105       132     246.0
24         60    102       126     334.5
25         60    100       120     250.0
26         60     92       118     241.0
27         60    103       132       NaN
28         60    100       132     280.0
29         60    102       129     380.3
30         60     92       115     243.0
31         45     90       112     180.1
32         60    101       124     299.0
33         60     93       113     223.0
34         60    107       136     361.0
35         60    114       140     415.0
36         60    102       127     300.5
37         60    100       120     300.1
38         60    100       120     300.0
39         45    104       129     266.0
40         45     90       112     180.1
41         60     98       126     286.0
42         60    100       122     329.4
43         60    111       138     400.0
44         60    111       131     397.0
45         60     99       119     273.0
46         60    109       153     387.6
47         45    111       136     300.0
48         45    108       129     298.0
49         60    111       139     397.6
50         60    107       136     380.2
51         80    123       146     643.1
52         60    106       130     263.0
53         60    118       151     486.0
54         30    136       175     238.0
55         60    121       146     450.7
56         60    118       121     413.0
57         45    115       144     305.0
58         20    153       172     226.4
59         45    123       152     321.0
60        210    108       160    1376.0
61        160    110       137    1034.4
62        160    109       135     853.0
63         45    118       141     341.0
64         20    110       130     131.4
65        180     90       130     800.4
66        150    105       135     873.4
67        150    107       130     816.0
68         20    106       136     110.4
69        300    108       143    1500.2
70        150     97       129    1115.0
71         60    109       153     387.6
72         90    100       127     700.0
73        150     97       127     953.2
74         45    114       146     304.0
75         90     98       125     563.2
76         45    105       134     251.0
77         45    110       141     300.0
78        120    100       130     500.4
79        270    100       131    1729.0
80         30    159       182     319.2
81         45    149       169     344.0
82         30    103       139     151.1
83        120    100       130     500.0
84         45    100       120     225.3
85         30    151       170     300.1
86         45    102       136     234.0
87        120    100       157    1000.1
88         45    129       103     242.0
89         20     83       107      50.3
90        180    101       127     600.1
91         45    107       137       NaN
92         30     90       107     105.3
93         15     80       100      50.5
94         20    150       171     127.4
95         20    151       168     229.4
96         30     95       128     128.2
97         25    152       168     244.2
98         30    109       131     188.2
99         90     93       124     604.1
100        20     95       112      77.7
101        90     90       110     500.0
102        90     90       100     500.0
103        90     90       100     500.4
104        30     92       108      92.7
105        30     93       128     124.0
106       180     90       120     800.3
107        30     90       120      86.2
108        90     90       120     500.3
109       210    137       184    1860.4
110        60    102       124     325.2
111        45    107       124     275.0
112        15    124       139     124.2
113        45    100       120     225.3
114        60    108       131     367.6
115        60    108       151     351.7
116        60    116       141     443.0
117        60     97       122     277.4
118        60    105       125       NaN
119        60    103       124     332.7
120        30    112       137     193.9
121        45    100       120     100.7
122        60    119       169     336.7
123        60    107       127     344.9
124        60    111       151     368.5
125        60     98       122     271.0
126        60     97       124     275.3
127        60    109       127     382.0
128        90     99       125     466.4
129        60    114       151     384.0
130        60    104       134     342.5
131        60    107       138     357.5
132        60    103       133     335.0
133        60    106       132     327.5
134        60    103       136     339.0
135        20    136       156     189.0
136        45    117       143     317.7
137        45    115       137     318.0
138        45    113       138     308.0
139        20    141       162     222.4
140        60    108       135     390.0
141        60     97       127       NaN
142        45    100       120     250.4
143        45    122       149     335.4
144        60    136       170     470.2
145        45    106       126     270.8
146        60    107       136     400.0
147        60    112       146     361.9
148        30    103       127     185.0
149        60    110       150     409.4
150        60    106       134     343.0
151        60    109       129     353.2
152        60    109       138     374.0
153        30    150       167     275.8
154        60    105       128     328.0
155        60    111       151     368.5
156        60     97       131     270.4
157        60    100       120     270.4
158        60    114       150     382.8
159        30     80       120     240.9
160        30     85       120     250.4
161        45     90       130     260.4
162        45     95       130     270.0
163        45    100       140     280.9
164        60    105       140     290.8
165        60    110       145     300.4
166        60    115       145     310.2
167        75    120       150     320.4
168        75    125       150     330.4
```

# Dictionary as JSON
- **JSON=Python Dictionary**
- JSON objects have teh same format in python dictionaries
- If our JSON code is not a file, but in python dictionary , we can load it into a DataFrame Directly.

```
import pandas as pd

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)

print(df) 
```

**Output** : 

```
Duration  Pulse  Maxpulse  Calories
0        60    110       130       409
1        60    117       145       479
2        60    103       135       340
3        45    109       175       282
4        45    117       148       406
5        60    102       127       300
```


# Pandas - Analyzing DataFrames

**Viewing the Data** : One of the most used method for getting a quick overview of the DataFrame, is the `head()` method
- The `head()` method returns the header and a specified number of rows, starting from the top.

```
#get a quick overview by printing the first 10 rows of the DataFrame
import pandas as pd
df=pd.read_csv("C:\\Users\\pc\\Downloads\\data.csv")
print(df.head(10))
```

**Output** :

```
Duration  Pulse  Maxpulse  Calories
0        60    110       130     409.1
1        60    117       145     479.0
2        60    103       135     340.0
3        45    109       175     282.4
4        45    117       148     406.0
5        60    102       127     300.0
6        60    110       136     374.0
7        45    104       134     253.3
8        30    109       133     195.1
9        60     98       124     269.0
```

**Note : The number of rows is not specified, the `head()` method will return the top 5 rows.**

```
# Print the 5 rows of the DataFrame
import pandas as pd
df=pd.read_csv("C:\\Users\\pc\\Downloads\\data.csv")
print(df.head())
```

**Output** : 
```
Duration  Pulse  Maxpulse  Calories
0        60    110       130     409.1
1        60    117       145     479.0
2        60    103       135     340.0
3        45    109       175     282.4
4        45    117       148     406.0
```

- There is also a `tail()` method for viewing the last rows of the DataFrame.
- The `tail()` method returns the headers and a specified number of rows, starting from the bottom

```
import pandas as pd
df=pd.read_csv("C:\\Users\\pc\\Downloads\\data.csv")
print(df.tail())
```
**Output** :
```
Duration  Pulse  Maxpulse  Calories
164        60    105       140     290.8
165        60    110       145     300.0
166        60    115       145     310.2
167        75    120       150     320.4
168        75    125       150     330.4
```

# Info about the Data
- The DataFrame Object has a method `info()`, that gives our more information about the dataset.

```
import pandas as pd
df=pd.read_csv("C:\\Users\\pc\\Downloads\\data.csv")
print(df.info())
```

**Output** : 
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 169 entries, 0 to 168
Data columns (total 4 columns):
 #   Column    Non-Null Count  Dtype  
---  ------    --------------  -----  
 0   Duration  169 non-null    int64  
 1   Pulse     169 non-null    int64  
 2   Maxpulse  169 non-null    int64  
 3   Calories  164 non-null    float64
dtypes: float64(1), int64(3)
memory usage: 5.4 KB
None
```

# Null Values
- The `info()` method also tell us how many Non-Null values there are present in each column and in out dataset.


# Pandas - Cleaning Data

**Data Cleaning** : Data cleaning means fixing bad data in out dataset

**Bad data could be**
- **Empty cells**
- **Data in Wrong Format**
- **Wrong data**
- **Duplicates**

# Pandas - Cleaning Empty Cells

**Empty Cells** : Empty cells can potentially give we a wrong result when we analyze data.

**Remove Rows** : One way to deal with empty cells is to remove rows that contain empty cells.
- This is usually OK, since data sets can be very big, and removing a few rows will not have a big impact on the result.

```
# Returns a new DataFrame with no empty cells
import pandas as pd
df=pd.read_csv("C:\\Users\\pc\\Downloads\\data.csv")
new_df=df.dropna()
print(new_df.to_string())
```
**Output** : 
```
Duration  Pulse  Maxpulse  Calories
0          60    110       130     409.1
1          60    117       145     479.0
2          60    103       135     340.0
3          45    109       175     282.4
4          45    117       148     406.0
5          60    102       127     300.0
6          60    110       136     374.0
7          45    104       134     253.3
8          30    109       133     195.1
9          60     98       124     269.0
10         60    103       147     329.3
11         60    100       120     250.7
12         60    106       128     345.3
13         60    104       132     379.3
14         60     98       123     275.0
15         60     98       120     215.2
16         60    100       120     300.0
17         45     90       112       NaN
18         60    103       123     323.0
19         45     97       125     243.0
20         60    108       131     364.2
21         45    100       119     282.0
22         60    130       101     300.0
23         45    105       132     246.0
24         60    102       126     334.5
25         60    100       120     250.0
26         60     92       118     241.0
27         60    103       132       NaN
28         60    100       132     280.0
29         60    102       129     380.3
30         60     92       115     243.0
31         45     90       112     180.1
32         60    101       124     299.0
33         60     93       113     223.0
34         60    107       136     361.0
35         60    114       140     415.0
36         60    102       127     300.0
37         60    100       120     300.0
38         60    100       120     300.0
39         45    104       129     266.0
40         45     90       112     180.1
41         60     98       126     286.0
42         60    100       122     329.4
43         60    111       138     400.0
44         60    111       131     397.0
45         60     99       119     273.0
46         60    109       153     387.6
47         45    111       136     300.0
48         45    108       129     298.0
49         60    111       139     397.6
50         60    107       136     380.2
51         80    123       146     643.1
52         60    106       130     263.0
53         60    118       151     486.0
54         30    136       175     238.0
55         60    121       146     450.7
56         60    118       121     413.0
57         45    115       144     305.0
58         20    153       172     226.4
59         45    123       152     321.0
60        210    108       160    1376.0
61        160    110       137    1034.4
62        160    109       135     853.0
63         45    118       141     341.0
64         20    110       130     131.4
65        180     90       130     800.4
66        150    105       135     873.4
67        150    107       130     816.0
68         20    106       136     110.4
69        300    108       143    1500.2
70        150     97       129    1115.0
71         60    109       153     387.6
72         90    100       127     700.0
73        150     97       127     953.2
74         45    114       146     304.0
75         90     98       125     563.2
76         45    105       134     251.0
77         45    110       141     300.0
78        120    100       130     500.4
79        270    100       131    1729.0
80         30    159       182     319.2
81         45    149       169     344.0
82         30    103       139     151.1
83        120    100       130     500.0
84         45    100       120     225.3
85         30    151       170     300.0
86         45    102       136     234.0
87        120    100       157    1000.1
88         45    129       103     242.0
89         20     83       107      50.3
90        180    101       127     600.1
91         45    107       137       NaN
92         30     90       107     105.3
93         15     80       100      50.5
94         20    150       171     127.4
95         20    151       168     229.4
96         30     95       128     128.2
97         25    152       168     244.2
98         30    109       131     188.2
99         90     93       124     604.1
100        20     95       112      77.7
101        90     90       110     500.0
102        90     90       100     500.0
103        90     90       100     500.4
104        30     92       108      92.7
105        30     93       128     124.0
106       180     90       120     800.3
107        30     90       120      86.2
108        90     90       120     500.3
109       210    137       184    1860.4
110        60    102       124     325.2
111        45    107       124     275.0
112        15    124       139     124.2
113        45    100       120     225.3
114        60    108       131     367.6
115        60    108       151     351.7
116        60    116       141     443.0
117        60     97       122     277.4
118        60    105       125       NaN
119        60    103       124     332.7
120        30    112       137     193.9
121        45    100       120     100.7
122        60    119       169     336.7
123        60    107       127     344.9
124        60    111       151     368.5
125        60     98       122     271.0
126        60     97       124     275.3
127        60    109       127     382.0
128        90     99       125     466.4
129        60    114       151     384.0
130        60    104       134     342.5
131        60    107       138     357.5
132        60    103       133     335.0
133        60    106       132     327.5
134        60    103       136     339.0
135        20    136       156     189.0
136        45    117       143     317.7
137        45    115       137     318.0
138        45    113       138     308.0
139        20    141       162     222.4
140        60    108       135     390.0
141        60     97       127       NaN
142        45    100       120     250.4
143        45    122       149     335.4
144        60    136       170     470.2
145        45    106       126     270.8
146        60    107       136     400.0
147        60    112       146     361.9
148        30    103       127     185.0
149        60    110       150     409.4
150        60    106       134     343.0
151        60    109       129     353.2
152        60    109       138     374.0
153        30    150       167     275.8
154        60    105       128     328.0
155        60    111       151     368.5
156        60     97       131     270.4
157        60    100       120     270.4
158        60    114       150     382.8
159        30     80       120     240.9
160        30     85       120     250.4
161        45     90       130     260.4
162        45     95       130     270.0
163        45    100       140     280.9
164        60    105       140     290.8
165        60    110       145     300.0
166        60    115       145     310.2
167        75    120       150     320.4
168        75    125       150     330.4
     Duration  Pulse  Maxpulse  Calories
0          60    110       130     409.1
1          60    117       145     479.0
2          60    103       135     340.0
3          45    109       175     282.4
4          45    117       148     406.0
5          60    102       127     300.0
6          60    110       136     374.0
7          45    104       134     253.3
8          30    109       133     195.1
9          60     98       124     269.0
10         60    103       147     329.3
11         60    100       120     250.7
12         60    106       128     345.3
13         60    104       132     379.3
14         60     98       123     275.0
15         60     98       120     215.2
16         60    100       120     300.0
18         60    103       123     323.0
19         45     97       125     243.0
20         60    108       131     364.2
21         45    100       119     282.0
22         60    130       101     300.0
23         45    105       132     246.0
24         60    102       126     334.5
25         60    100       120     250.0
26         60     92       118     241.0
28         60    100       132     280.0
29         60    102       129     380.3
30         60     92       115     243.0
31         45     90       112     180.1
32         60    101       124     299.0
33         60     93       113     223.0
34         60    107       136     361.0
35         60    114       140     415.0
36         60    102       127     300.0
37         60    100       120     300.0
38         60    100       120     300.0
39         45    104       129     266.0
40         45     90       112     180.1
41         60     98       126     286.0
42         60    100       122     329.4
43         60    111       138     400.0
44         60    111       131     397.0
45         60     99       119     273.0
46         60    109       153     387.6
47         45    111       136     300.0
48         45    108       129     298.0
49         60    111       139     397.6
50         60    107       136     380.2
51         80    123       146     643.1
52         60    106       130     263.0
53         60    118       151     486.0
54         30    136       175     238.0
55         60    121       146     450.7
56         60    118       121     413.0
57         45    115       144     305.0
58         20    153       172     226.4
59         45    123       152     321.0
60        210    108       160    1376.0
61        160    110       137    1034.4
62        160    109       135     853.0
63         45    118       141     341.0
64         20    110       130     131.4
65        180     90       130     800.4
66        150    105       135     873.4
67        150    107       130     816.0
68         20    106       136     110.4
69        300    108       143    1500.2
70        150     97       129    1115.0
71         60    109       153     387.6
72         90    100       127     700.0
73        150     97       127     953.2
74         45    114       146     304.0
75         90     98       125     563.2
76         45    105       134     251.0
77         45    110       141     300.0
78        120    100       130     500.4
79        270    100       131    1729.0
80         30    159       182     319.2
81         45    149       169     344.0
82         30    103       139     151.1
83        120    100       130     500.0
84         45    100       120     225.3
85         30    151       170     300.0
86         45    102       136     234.0
87        120    100       157    1000.1
88         45    129       103     242.0
89         20     83       107      50.3
90        180    101       127     600.1
92         30     90       107     105.3
93         15     80       100      50.5
94         20    150       171     127.4
95         20    151       168     229.4
96         30     95       128     128.2
97         25    152       168     244.2
98         30    109       131     188.2
99         90     93       124     604.1
100        20     95       112      77.7
101        90     90       110     500.0
102        90     90       100     500.0
103        90     90       100     500.4
104        30     92       108      92.7
105        30     93       128     124.0
106       180     90       120     800.3
107        30     90       120      86.2
108        90     90       120     500.3
109       210    137       184    1860.4
110        60    102       124     325.2
111        45    107       124     275.0
112        15    124       139     124.2
113        45    100       120     225.3
114        60    108       131     367.6
115        60    108       151     351.7
116        60    116       141     443.0
117        60     97       122     277.4
119        60    103       124     332.7
120        30    112       137     193.9
121        45    100       120     100.7
122        60    119       169     336.7
123        60    107       127     344.9
124        60    111       151     368.5
125        60     98       122     271.0
126        60     97       124     275.3
127        60    109       127     382.0
128        90     99       125     466.4
129        60    114       151     384.0
130        60    104       134     342.5
131        60    107       138     357.5
132        60    103       133     335.0
133        60    106       132     327.5
134        60    103       136     339.0
135        20    136       156     189.0
136        45    117       143     317.7
137        45    115       137     318.0
138        45    113       138     308.0
139        20    141       162     222.4
140        60    108       135     390.0
142        45    100       120     250.4
143        45    122       149     335.4
144        60    136       170     470.2
145        45    106       126     270.8
146        60    107       136     400.0
147        60    112       146     361.9
148        30    103       127     185.0
149        60    110       150     409.4
150        60    106       134     343.0
151        60    109       129     353.2
152        60    109       138     374.0
153        30    150       167     275.8
154        60    105       128     328.0
155        60    111       151     368.5
156        60     97       131     270.4
157        60    100       120     270.4
158        60    114       150     382.8
159        30     80       120     240.9
160        30     85       120     250.4
161        45     90       130     260.4
162        45     95       130     270.0
163        45    100       140     280.9
164        60    105       140     290.8
165        60    110       145     300.0
166        60    115       145     310.2
167        75    120       150     320.4
168        75    125       150     330.4
```

**Note : By default the `dropna()` method returns a new DataFrame and will not change the original**

**If we want to change the orginal DataFrame, use the `inplace=True` argument.**

```
# Remove all rows with NULL values
import pandas as pd
df=pd.read_csv("C:\\Users\\pc\\Downloads\\data.csv")
df.dropna(inplace=True)
print(df.to_string())
```

**Output**
```
Duration  Pulse  Maxpulse  Calories
0          60    110       130     409.1
1          60    117       145     479.0
2          60    103       135     340.0
3          45    109       175     282.4
4          45    117       148     406.0
5          60    102       127     300.0
6          60    110       136     374.0
7          45    104       134     253.3
8          30    109       133     195.1
9          60     98       124     269.0
10         60    103       147     329.3
11         60    100       120     250.7
12         60    106       128     345.3
13         60    104       132     379.3
14         60     98       123     275.0
15         60     98       120     215.2
16         60    100       120     300.0
18         60    103       123     323.0
19         45     97       125     243.0
20         60    108       131     364.2
21         45    100       119     282.0
22         60    130       101     300.0
23         45    105       132     246.0
24         60    102       126     334.5
25         60    100       120     250.0
26         60     92       118     241.0
28         60    100       132     280.0
29         60    102       129     380.3
30         60     92       115     243.0
31         45     90       112     180.1
32         60    101       124     299.0
33         60     93       113     223.0
34         60    107       136     361.0
35         60    114       140     415.0
36         60    102       127     300.0
37         60    100       120     300.0
38         60    100       120     300.0
39         45    104       129     266.0
40         45     90       112     180.1
41         60     98       126     286.0
42         60    100       122     329.4
43         60    111       138     400.0
44         60    111       131     397.0
45         60     99       119     273.0
46         60    109       153     387.6
47         45    111       136     300.0
48         45    108       129     298.0
49         60    111       139     397.6
50         60    107       136     380.2
51         80    123       146     643.1
52         60    106       130     263.0
53         60    118       151     486.0
54         30    136       175     238.0
55         60    121       146     450.7
56         60    118       121     413.0
57         45    115       144     305.0
58         20    153       172     226.4
59         45    123       152     321.0
60        210    108       160    1376.0
61        160    110       137    1034.4
62        160    109       135     853.0
63         45    118       141     341.0
64         20    110       130     131.4
65        180     90       130     800.4
66        150    105       135     873.4
67        150    107       130     816.0
68         20    106       136     110.4
69        300    108       143    1500.2
70        150     97       129    1115.0
71         60    109       153     387.6
72         90    100       127     700.0
73        150     97       127     953.2
74         45    114       146     304.0
75         90     98       125     563.2
76         45    105       134     251.0
77         45    110       141     300.0
78        120    100       130     500.4
79        270    100       131    1729.0
80         30    159       182     319.2
81         45    149       169     344.0
82         30    103       139     151.1
83        120    100       130     500.0
84         45    100       120     225.3
85         30    151       170     300.0
86         45    102       136     234.0
87        120    100       157    1000.1
88         45    129       103     242.0
89         20     83       107      50.3
90        180    101       127     600.1
92         30     90       107     105.3
93         15     80       100      50.5
94         20    150       171     127.4
95         20    151       168     229.4
96         30     95       128     128.2
97         25    152       168     244.2
98         30    109       131     188.2
99         90     93       124     604.1
100        20     95       112      77.7
101        90     90       110     500.0
102        90     90       100     500.0
103        90     90       100     500.4
104        30     92       108      92.7
105        30     93       128     124.0
106       180     90       120     800.3
107        30     90       120      86.2
108        90     90       120     500.3
109       210    137       184    1860.4
110        60    102       124     325.2
111        45    107       124     275.0
112        15    124       139     124.2
113        45    100       120     225.3
114        60    108       131     367.6
115        60    108       151     351.7
116        60    116       141     443.0
117        60     97       122     277.4
119        60    103       124     332.7
120        30    112       137     193.9
121        45    100       120     100.7
122        60    119       169     336.7
123        60    107       127     344.9
124        60    111       151     368.5
125        60     98       122     271.0
126        60     97       124     275.3
127        60    109       127     382.0
128        90     99       125     466.4
129        60    114       151     384.0
130        60    104       134     342.5
131        60    107       138     357.5
132        60    103       133     335.0
133        60    106       132     327.5
134        60    103       136     339.0
135        20    136       156     189.0
136        45    117       143     317.7
137        45    115       137     318.0
138        45    113       138     308.0
139        20    141       162     222.4
140        60    108       135     390.0
142        45    100       120     250.4
143        45    122       149     335.4
144        60    136       170     470.2
145        45    106       126     270.8
146        60    107       136     400.0
147        60    112       146     361.9
148        30    103       127     185.0
149        60    110       150     409.4
150        60    106       134     343.0
151        60    109       129     353.2
152        60    109       138     374.0
153        30    150       167     275.8
154        60    105       128     328.0
155        60    111       151     368.5
156        60     97       131     270.4
157        60    100       120     270.4
158        60    114       150     382.8
159        30     80       120     240.9
160        30     85       120     250.4
161        45     90       130     260.4
162        45     95       130     270.0
163        45    100       140     280.9
164        60    105       140     290.8
165        60    110       145     300.0
166        60    115       145     310.2
167        75    120       150     320.4
168        75    125       150     330.4
```

**Note:  Now, the `dropna(inplace=True)` will not return a new DataFrame, but it will removes all rows containing Null values from the original DataFrame**

# Replace Empty Values

- Another way of dealing with empty cells is to insert a new value instead.
- This way we do not have a delete the entire rows just because of some empty cells.
- The `fillna()` method allows us to replace empty cells with a value.

```
# Replace NULL values with the number 130 
import pandas as pd
df= pd.read_csv("C:\\Users\\pc\\Downloads\\data.csv")
df.fillna(130, inplace=True)
print(df.to_string())
```

**Output** : 
```
Duration  Pulse  Maxpulse  Calories
0          60    110       130     409.1
1          60    117       145     479.0
2          60    103       135     340.0
3          45    109       175     282.4
4          45    117       148     406.0
5          60    102       127     300.0
6          60    110       136     374.0
7          45    104       134     253.3
8          30    109       133     195.1
9          60     98       124     269.0
10         60    103       147     329.3
11         60    100       120     250.7
12         60    106       128     345.3
13         60    104       132     379.3
14         60     98       123     275.0
15         60     98       120     215.2
16         60    100       120     300.0
17         45     90       112     130.0
18         60    103       123     323.0
19         45     97       125     243.0
20         60    108       131     364.2
21         45    100       119     282.0
22         60    130       101     300.0
23         45    105       132     246.0
24         60    102       126     334.5
25         60    100       120     250.0
26         60     92       118     241.0
27         60    103       132     130.0
28         60    100       132     280.0
29         60    102       129     380.3
30         60     92       115     243.0
31         45     90       112     180.1
32         60    101       124     299.0
33         60     93       113     223.0
34         60    107       136     361.0
35         60    114       140     415.0
36         60    102       127     300.0
37         60    100       120     300.0
38         60    100       120     300.0
39         45    104       129     266.0
40         45     90       112     180.1
41         60     98       126     286.0
42         60    100       122     329.4
43         60    111       138     400.0
44         60    111       131     397.0
45         60     99       119     273.0
46         60    109       153     387.6
47         45    111       136     300.0
48         45    108       129     298.0
49         60    111       139     397.6
50         60    107       136     380.2
51         80    123       146     643.1
52         60    106       130     263.0
53         60    118       151     486.0
54         30    136       175     238.0
55         60    121       146     450.7
56         60    118       121     413.0
57         45    115       144     305.0
58         20    153       172     226.4
59         45    123       152     321.0
60        210    108       160    1376.0
61        160    110       137    1034.4
62        160    109       135     853.0
63         45    118       141     341.0
64         20    110       130     131.4
65        180     90       130     800.4
66        150    105       135     873.4
67        150    107       130     816.0
68         20    106       136     110.4
69        300    108       143    1500.2
70        150     97       129    1115.0
71         60    109       153     387.6
72         90    100       127     700.0
73        150     97       127     953.2
74         45    114       146     304.0
75         90     98       125     563.2
76         45    105       134     251.0
77         45    110       141     300.0
78        120    100       130     500.4
79        270    100       131    1729.0
80         30    159       182     319.2
81         45    149       169     344.0
82         30    103       139     151.1
83        120    100       130     500.0
84         45    100       120     225.3
85         30    151       170     300.0
86         45    102       136     234.0
87        120    100       157    1000.1
88         45    129       103     242.0
89         20     83       107      50.3
90        180    101       127     600.1
91         45    107       137     130.0
92         30     90       107     105.3
93         15     80       100      50.5
94         20    150       171     127.4
95         20    151       168     229.4
96         30     95       128     128.2
97         25    152       168     244.2
98         30    109       131     188.2
99         90     93       124     604.1
100        20     95       112      77.7
101        90     90       110     500.0
102        90     90       100     500.0
103        90     90       100     500.4
104        30     92       108      92.7
105        30     93       128     124.0
106       180     90       120     800.3
107        30     90       120      86.2
108        90     90       120     500.3
109       210    137       184    1860.4
110        60    102       124     325.2
111        45    107       124     275.0
112        15    124       139     124.2
113        45    100       120     225.3
114        60    108       131     367.6
115        60    108       151     351.7
116        60    116       141     443.0
117        60     97       122     277.4
118        60    105       125     130.0
119        60    103       124     332.7
120        30    112       137     193.9
121        45    100       120     100.7
122        60    119       169     336.7
123        60    107       127     344.9
124        60    111       151     368.5
125        60     98       122     271.0
126        60     97       124     275.3
127        60    109       127     382.0
128        90     99       125     466.4
129        60    114       151     384.0
130        60    104       134     342.5
131        60    107       138     357.5
132        60    103       133     335.0
133        60    106       132     327.5
134        60    103       136     339.0
135        20    136       156     189.0
136        45    117       143     317.7
137        45    115       137     318.0
138        45    113       138     308.0
139        20    141       162     222.4
140        60    108       135     390.0
141        60     97       127     130.0
142        45    100       120     250.4
143        45    122       149     335.4
144        60    136       170     470.2
145        45    106       126     270.8
146        60    107       136     400.0
147        60    112       146     361.9
148        30    103       127     185.0
149        60    110       150     409.4
150        60    106       134     343.0
151        60    109       129     353.2
152        60    109       138     374.0
153        30    150       167     275.8
154        60    105       128     328.0
155        60    111       151     368.5
156        60     97       131     270.4
157        60    100       120     270.4
158        60    114       150     382.8
159        30     80       120     240.9
160        30     85       120     250.4
161        45     90       130     260.4
162        45     95       130     270.0
163        45    100       140     280.9
164        60    105       140     290.8
165        60    110       145     300.0
166        60    115       145     310.2
167        75    120       150     320.4
168        75    125       150     330.4
```

# Replace Only For Specified Columns
- The example above replaces all empty cells in the whole Data Frame.
- To only replace empty values for one column, specify the column name for the DataFrame

```
# Replace NULL values in the "Calories" column with the number 130
import pandas as pd
df=pd.read_csv("C:\\Users\\pc\\Downloads\\data.csv")
df.fillna({"Calories":130},inplace=True)
print(df.to_string())
```

**Output** : 
```
Duration  Pulse  Maxpulse  Calories
0          60    110       130     409.1
1          60    117       145     479.0
2          60    103       135     340.0
3          45    109       175     282.4
4          45    117       148     406.0
5          60    102       127     300.0
6          60    110       136     374.0
7          45    104       134     253.3
8          30    109       133     195.1
9          60     98       124     269.0
10         60    103       147     329.3
11         60    100       120     250.7
12         60    106       128     345.3
13         60    104       132     379.3
14         60     98       123     275.0
15         60     98       120     215.2
16         60    100       120     300.0
17         45     90       112     130.0
18         60    103       123     323.0
19         45     97       125     243.0
20         60    108       131     364.2
21         45    100       119     282.0
22         60    130       101     300.0
23         45    105       132     246.0
24         60    102       126     334.5
25         60    100       120     250.0
26         60     92       118     241.0
27         60    103       132     130.0
28         60    100       132     280.0
29         60    102       129     380.3
30         60     92       115     243.0
31         45     90       112     180.1
32         60    101       124     299.0
33         60     93       113     223.0
34         60    107       136     361.0
35         60    114       140     415.0
36         60    102       127     300.0
37         60    100       120     300.0
38         60    100       120     300.0
39         45    104       129     266.0
40         45     90       112     180.1
41         60     98       126     286.0
42         60    100       122     329.4
43         60    111       138     400.0
44         60    111       131     397.0
45         60     99       119     273.0
46         60    109       153     387.6
47         45    111       136     300.0
48         45    108       129     298.0
49         60    111       139     397.6
50         60    107       136     380.2
51         80    123       146     643.1
52         60    106       130     263.0
53         60    118       151     486.0
54         30    136       175     238.0
55         60    121       146     450.7
56         60    118       121     413.0
57         45    115       144     305.0
58         20    153       172     226.4
59         45    123       152     321.0
60        210    108       160    1376.0
61        160    110       137    1034.4
62        160    109       135     853.0
63         45    118       141     341.0
64         20    110       130     131.4
65        180     90       130     800.4
66        150    105       135     873.4
67        150    107       130     816.0
68         20    106       136     110.4
69        300    108       143    1500.2
70        150     97       129    1115.0
71         60    109       153     387.6
72         90    100       127     700.0
73        150     97       127     953.2
74         45    114       146     304.0
75         90     98       125     563.2
76         45    105       134     251.0
77         45    110       141     300.0
78        120    100       130     500.4
79        270    100       131    1729.0
80         30    159       182     319.2
81         45    149       169     344.0
82         30    103       139     151.1
83        120    100       130     500.0
84         45    100       120     225.3
85         30    151       170     300.0
86         45    102       136     234.0
87        120    100       157    1000.1
88         45    129       103     242.0
89         20     83       107      50.3
90        180    101       127     600.1
91         45    107       137     130.0
92         30     90       107     105.3
93         15     80       100      50.5
94         20    150       171     127.4
95         20    151       168     229.4
96         30     95       128     128.2
97         25    152       168     244.2
98         30    109       131     188.2
99         90     93       124     604.1
100        20     95       112      77.7
101        90     90       110     500.0
102        90     90       100     500.0
103        90     90       100     500.4
104        30     92       108      92.7
105        30     93       128     124.0
106       180     90       120     800.3
107        30     90       120      86.2
108        90     90       120     500.3
109       210    137       184    1860.4
110        60    102       124     325.2
111        45    107       124     275.0
112        15    124       139     124.2
113        45    100       120     225.3
114        60    108       131     367.6
115        60    108       151     351.7
116        60    116       141     443.0
117        60     97       122     277.4
118        60    105       125     130.0
119        60    103       124     332.7
120        30    112       137     193.9
121        45    100       120     100.7
122        60    119       169     336.7
123        60    107       127     344.9
124        60    111       151     368.5
125        60     98       122     271.0
126        60     97       124     275.3
127        60    109       127     382.0
128        90     99       125     466.4
129        60    114       151     384.0
130        60    104       134     342.5
131        60    107       138     357.5
132        60    103       133     335.0
133        60    106       132     327.5
134        60    103       136     339.0
135        20    136       156     189.0
136        45    117       143     317.7
137        45    115       137     318.0
138        45    113       138     308.0
139        20    141       162     222.4
140        60    108       135     390.0
141        60     97       127     130.0
142        45    100       120     250.4
143        45    122       149     335.4
144        60    136       170     470.2
145        45    106       126     270.8
146        60    107       136     400.0
147        60    112       146     361.9
148        30    103       127     185.0
149        60    110       150     409.4
150        60    106       134     343.0
151        60    109       129     353.2
152        60    109       138     374.0
153        30    150       167     275.8
154        60    105       128     328.0
155        60    111       151     368.5
156        60     97       131     270.4
157        60    100       120     270.4
158        60    114       150     382.8
159        30     80       120     240.9
160        30     85       120     250.4
161        45     90       130     260.4
162        45     95       130     270.0
163        45    100       140     280.9
164        60    105       140     290.8
165        60    110       145     300.0
166        60    115       145     310.2
167        75    120       150     320.4
168        75    125       150     330.4
```

# Replace Using Mean, Median, or Mode
- A common way to replace empty cells, is to calculate the mean, median or mode value of the column
- Pandas uses the `mean(), median(), and mode()` methods to calculate the respective values for a specified column.

```
# calculate the MEAN, and replace any empty values with it
import pandas as pd
df=pd.read_csv("C:\\Users\\pc\\Downloads\\data.csv")
x=df["Calories"].mean()
df.fillna({"Calories":x},inplace=True)
print(df.to_string())
```
**Output** : 
```
Duration  Pulse  Maxpulse     Calories
0          60    110       130   409.100000
1          60    117       145   479.000000
2          60    103       135   340.000000
3          45    109       175   282.400000
4          45    117       148   406.000000
5          60    102       127   300.000000
6          60    110       136   374.000000
7          45    104       134   253.300000
8          30    109       133   195.100000
9          60     98       124   269.000000
10         60    103       147   329.300000
11         60    100       120   250.700000
12         60    106       128   345.300000
13         60    104       132   379.300000
14         60     98       123   275.000000
15         60     98       120   215.200000
16         60    100       120   300.000000
17         45     90       112   375.790244
18         60    103       123   323.000000
19         45     97       125   243.000000
20         60    108       131   364.200000
21         45    100       119   282.000000
22         60    130       101   300.000000
23         45    105       132   246.000000
24         60    102       126   334.500000
25         60    100       120   250.000000
26         60     92       118   241.000000
27         60    103       132   375.790244
28         60    100       132   280.000000
29         60    102       129   380.300000
30         60     92       115   243.000000
31         45     90       112   180.100000
32         60    101       124   299.000000
33         60     93       113   223.000000
34         60    107       136   361.000000
35         60    114       140   415.000000
36         60    102       127   300.000000
37         60    100       120   300.000000
38         60    100       120   300.000000
39         45    104       129   266.000000
40         45     90       112   180.100000
41         60     98       126   286.000000
42         60    100       122   329.400000
43         60    111       138   400.000000
44         60    111       131   397.000000
45         60     99       119   273.000000
46         60    109       153   387.600000
47         45    111       136   300.000000
48         45    108       129   298.000000
49         60    111       139   397.600000
50         60    107       136   380.200000
51         80    123       146   643.100000
52         60    106       130   263.000000
53         60    118       151   486.000000
54         30    136       175   238.000000
55         60    121       146   450.700000
56         60    118       121   413.000000
57         45    115       144   305.000000
58         20    153       172   226.400000
59         45    123       152   321.000000
60        210    108       160  1376.000000
61        160    110       137  1034.400000
62        160    109       135   853.000000
63         45    118       141   341.000000
64         20    110       130   131.400000
65        180     90       130   800.400000
66        150    105       135   873.400000
67        150    107       130   816.000000
68         20    106       136   110.400000
69        300    108       143  1500.200000
70        150     97       129  1115.000000
71         60    109       153   387.600000
72         90    100       127   700.000000
73        150     97       127   953.200000
74         45    114       146   304.000000
75         90     98       125   563.200000
76         45    105       134   251.000000
77         45    110       141   300.000000
78        120    100       130   500.400000
79        270    100       131  1729.000000
80         30    159       182   319.200000
81         45    149       169   344.000000
82         30    103       139   151.100000
83        120    100       130   500.000000
84         45    100       120   225.300000
85         30    151       170   300.000000
86         45    102       136   234.000000
87        120    100       157  1000.100000
88         45    129       103   242.000000
89         20     83       107    50.300000
90        180    101       127   600.100000
91         45    107       137   375.790244
92         30     90       107   105.300000
93         15     80       100    50.500000
94         20    150       171   127.400000
95         20    151       168   229.400000
96         30     95       128   128.200000
97         25    152       168   244.200000
98         30    109       131   188.200000
99         90     93       124   604.100000
100        20     95       112    77.700000
101        90     90       110   500.000000
102        90     90       100   500.000000
103        90     90       100   500.400000
104        30     92       108    92.700000
105        30     93       128   124.000000
106       180     90       120   800.300000
107        30     90       120    86.200000
108        90     90       120   500.300000
109       210    137       184  1860.400000
110        60    102       124   325.200000
111        45    107       124   275.000000
112        15    124       139   124.200000
113        45    100       120   225.300000
114        60    108       131   367.600000
115        60    108       151   351.700000
116        60    116       141   443.000000
117        60     97       122   277.400000
118        60    105       125   375.790244
119        60    103       124   332.700000
120        30    112       137   193.900000
121        45    100       120   100.700000
122        60    119       169   336.700000
123        60    107       127   344.900000
124        60    111       151   368.500000
125        60     98       122   271.000000
126        60     97       124   275.300000
127        60    109       127   382.000000
128        90     99       125   466.400000
129        60    114       151   384.000000
130        60    104       134   342.500000
131        60    107       138   357.500000
132        60    103       133   335.000000
133        60    106       132   327.500000
134        60    103       136   339.000000
135        20    136       156   189.000000
136        45    117       143   317.700000
137        45    115       137   318.000000
138        45    113       138   308.000000
139        20    141       162   222.400000
140        60    108       135   390.000000
141        60     97       127   375.790244
142        45    100       120   250.400000
143        45    122       149   335.400000
144        60    136       170   470.200000
145        45    106       126   270.800000
146        60    107       136   400.000000
147        60    112       146   361.900000
148        30    103       127   185.000000
149        60    110       150   409.400000
150        60    106       134   343.000000
151        60    109       129   353.200000
152        60    109       138   374.000000
153        30    150       167   275.800000
154        60    105       128   328.000000
155        60    111       151   368.500000
156        60     97       131   270.400000
157        60    100       120   270.400000
158        60    114       150   382.800000
159        30     80       120   240.900000
160        30     85       120   250.400000
161        45     90       130   260.400000
162        45     95       130   270.000000
163        45    100       140   280.900000
164        60    105       140   290.800000
165        60    110       145   300.000000
166        60    115       145   310.200000
167        75    120       150   320.400000
168        75    125       150   330.400000
```
**Mean= The average value(the su of all values divided by number of value)**

```
# Calculate the MEDIAN, and replace any empty values with it
import pandas as pd
df=pd.read_csv("C:\\Users\\pc\\Downloads\\data.csv")
x=df["Calories"].median()
df.fillna({"Calories":x},inplace=True)
print(df.to_string())
```
**Output** : 
```
Duration  Pulse  Maxpulse  Calories
0          60    110       130     409.1
1          60    117       145     479.0
2          60    103       135     340.0
3          45    109       175     282.4
4          45    117       148     406.0
5          60    102       127     300.0
6          60    110       136     374.0
7          45    104       134     253.3
8          30    109       133     195.1
9          60     98       124     269.0
10         60    103       147     329.3
11         60    100       120     250.7
12         60    106       128     345.3
13         60    104       132     379.3
14         60     98       123     275.0
15         60     98       120     215.2
16         60    100       120     300.0
17         45     90       112     318.6
18         60    103       123     323.0
19         45     97       125     243.0
20         60    108       131     364.2
21         45    100       119     282.0
22         60    130       101     300.0
23         45    105       132     246.0
24         60    102       126     334.5
25         60    100       120     250.0
26         60     92       118     241.0
27         60    103       132     318.6
28         60    100       132     280.0
29         60    102       129     380.3
30         60     92       115     243.0
31         45     90       112     180.1
32         60    101       124     299.0
33         60     93       113     223.0
34         60    107       136     361.0
35         60    114       140     415.0
36         60    102       127     300.0
37         60    100       120     300.0
38         60    100       120     300.0
39         45    104       129     266.0
40         45     90       112     180.1
41         60     98       126     286.0
42         60    100       122     329.4
43         60    111       138     400.0
44         60    111       131     397.0
45         60     99       119     273.0
46         60    109       153     387.6
47         45    111       136     300.0
48         45    108       129     298.0
49         60    111       139     397.6
50         60    107       136     380.2
51         80    123       146     643.1
52         60    106       130     263.0
53         60    118       151     486.0
54         30    136       175     238.0
55         60    121       146     450.7
56         60    118       121     413.0
57         45    115       144     305.0
58         20    153       172     226.4
59         45    123       152     321.0
60        210    108       160    1376.0
61        160    110       137    1034.4
62        160    109       135     853.0
63         45    118       141     341.0
64         20    110       130     131.4
65        180     90       130     800.4
66        150    105       135     873.4
67        150    107       130     816.0
68         20    106       136     110.4
69        300    108       143    1500.2
70        150     97       129    1115.0
71         60    109       153     387.6
72         90    100       127     700.0
73        150     97       127     953.2
74         45    114       146     304.0
75         90     98       125     563.2
76         45    105       134     251.0
77         45    110       141     300.0
78        120    100       130     500.4
79        270    100       131    1729.0
80         30    159       182     319.2
81         45    149       169     344.0
82         30    103       139     151.1
83        120    100       130     500.0
84         45    100       120     225.3
85         30    151       170     300.0
86         45    102       136     234.0
87        120    100       157    1000.1
88         45    129       103     242.0
89         20     83       107      50.3
90        180    101       127     600.1
91         45    107       137     318.6
92         30     90       107     105.3
93         15     80       100      50.5
94         20    150       171     127.4
95         20    151       168     229.4
96         30     95       128     128.2
97         25    152       168     244.2
98         30    109       131     188.2
99         90     93       124     604.1
100        20     95       112      77.7
101        90     90       110     500.0
102        90     90       100     500.0
103        90     90       100     500.4
104        30     92       108      92.7
105        30     93       128     124.0
106       180     90       120     800.3
107        30     90       120      86.2
108        90     90       120     500.3
109       210    137       184    1860.4
110        60    102       124     325.2
111        45    107       124     275.0
112        15    124       139     124.2
113        45    100       120     225.3
114        60    108       131     367.6
115        60    108       151     351.7
116        60    116       141     443.0
117        60     97       122     277.4
118        60    105       125     318.6
119        60    103       124     332.7
120        30    112       137     193.9
121        45    100       120     100.7
122        60    119       169     336.7
123        60    107       127     344.9
124        60    111       151     368.5
125        60     98       122     271.0
126        60     97       124     275.3
127        60    109       127     382.0
128        90     99       125     466.4
129        60    114       151     384.0
130        60    104       134     342.5
131        60    107       138     357.5
132        60    103       133     335.0
133        60    106       132     327.5
134        60    103       136     339.0
135        20    136       156     189.0
136        45    117       143     317.7
137        45    115       137     318.0
138        45    113       138     308.0
139        20    141       162     222.4
140        60    108       135     390.0
141        60     97       127     318.6
142        45    100       120     250.4
143        45    122       149     335.4
144        60    136       170     470.2
145        45    106       126     270.8
146        60    107       136     400.0
147        60    112       146     361.9
148        30    103       127     185.0
149        60    110       150     409.4
150        60    106       134     343.0
151        60    109       129     353.2
152        60    109       138     374.0
153        30    150       167     275.8
154        60    105       128     328.0
155        60    111       151     368.5
156        60     97       131     270.4
157        60    100       120     270.4
158        60    114       150     382.8
159        30     80       120     240.9
160        30     85       120     250.4
161        45     90       130     260.4
162        45     95       130     270.0
163        45    100       140     280.9
164        60    105       140     290.8
165        60    110       145     300.0
166        60    115       145     310.2
167        75    120       150     320.4
168        75    125       150     330.4
```


