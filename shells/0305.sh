#/bin/bash

##################
#  四、 变量      #
##################

# 1. 简介
:<<EOF
    Bash 变量分为环境变量和用户自定义变量
    环境变量是 Bash 环境自带的变量，进入 Shell 时已经定义好了，可以直接使用, 使用 `env` 或 `printenv` 可以查看
    自定义变量是用户在当前 Shell 里面自己定义的变量，必须先定义后使用，而且仅在当前 Shell 可用, `set` 可以显示所有变量

    Bash 变量名区分大小写
EOF

# 2. 创建变量
myvar="hello world"
:<<EOF
    定义规则:
      字母、数字和下划线字符组成
      第一个字符必须是一个字母或一个下划线，不能是数字
      不允许出现空格和标点符号
    变量可以重复赋值，后面的赋值会覆盖前面的赋值
    如果同一行定义多个变量，必须使用分号（;）分隔
EOF

# 3. 读取变量
echo $myvar
:<<EOF
    读取变量，直接在变量名前加上美元符， 变量名也可使用花括号({})包围
    如果变量不存在，Bash 不会报错，而会输出空字符
    如果变量的值本身也是变量，可以使用${!varname}的语法，读取最终的值
    如果变量值包含连续空格（或制表符和换行符），最好放在双引号里面读取
EOF

# 4. 删除变量
# unset myvar
:<<EOF
    unset 命令删除变量时， 变量名前不要加$
    这个命令不是很有用，删除变量时, 可以将变量赋值为空串
EOF

# 5. 输出变量
# export foo=bar
# bash
# echo $foo
# foo=baz
# exit
# echo $foo
:<<EOT
    用户创建的变量仅可用于当前 Shell， 可以通过 `export` 命令把变量传递给子 Shell
    子 Shell 修改了继承的变量$foo，对父 Shell 没有影响
EOT

# 6. 特殊变量
:<<EOF
    $?  --- 上一个命令的退出码，用来判断上一个命令是否执行成功
    $$  --- 当前shell的进程id， 可用来命名临时文件 LOGFILE=/tmp/output_log.$$
    $_  --- 上一个命令的最后一个参数
    $!  --- 最近一个后台执行的异步命令的进程 ID    `jobs` 差不多
    $0  --- 当前 Shell 的名称(在命令行直接执行时)或者脚本名(在脚本中执行时)
    $-  --- 为当前 Shell 的启动参数
    $@和$# --- 脚本的参数数量
EOF

# 7. 变量的默认值

:<<EOF
    ${varname:-messgage}  -- 变量varname存在且不为空，则返回它的值，否则返回messgage
    ${varname:=messgage}  -- 变量varname存在且不为空，则返回它的值，否则将它赋值message并返回messgage
    ${varname:+messgage}  -- 变量varname存在且不为空，则返回message， 否则返回空值， 用户测试变量是否存在
    ${varname:?messgage}  -- 如果变量varname存在且不为空，则返回它的值，否则打印出varname: message，并中断脚本的执行
EOF

# 8. declare 命令
:<<EOF
    declare OPTION VARIABLE=value
    可以声明一些特殊类型的变量，为变量设置一些限制
    OPTION 选项:
      -a：声明数组变量。
      -f：输出所有函数定义。
      -F：输出所有函数名。
      -i：声明整数变量。
      -l：声明变量为小写字母。
      -p：查看变量信息。
      -r：声明只读变量。
      -u：声明变量为大写字母。
      -x：该变量输出为环境变量。

    declare命令如果用在函数中，声明的变量只在函数内部有效，等同于local命令

EOF

# 9. readonly 命令
:<<EOF
    用来声明只读变量，不能改变变量值，也不能unset变量, 等同于 declare -r
    参数解释:
        -f：声明的变量为函数名
        -p：打印出所有的只读变量
        -a：声明的变量为数组
EOF

# 10. let 命令
let foo=1+2
echo $foo
let "bar = 2 + 3"
echo $bar
:<<EOF
    命令的参数表达式如果包含空格，就需要使用引号
    可以同时对多个变量赋值，赋值表达式之间使用空格分隔 let "v1 = 1" "v2 = v1++"
EOF


#####################
#  五、 字符串操作    #
#####################

# 1. 字符串长度
myPath=/home/cam/book/long.file.name
echo ${#myPath}
echo $#myPath
:<<EOT
    大括号{}是必需的，否则 Bash 会将$#理解成脚本的参数个数，将变量名理解成文本
EOT

# 2. 子字符串
echo ${myPath:4:5}
:<<eof
    ${varname:offset:length} 返回从位置offset开始（从0开始计算），长度为length的子字符串
    不能直接操作字符串，只能通过变量来读取字符串 eg: "echo \${"hello":2:3}" 报错
    如果省略length，则从位置offset开始，一直返回到字符串的结尾
    如果offset为负值，表示从字符串的末尾开始算起。注意，负数前面必须有一个空格, 避免与变量默认值混淆
eof

# 3. 搜索和替换
## 头部匹配
echo ${myPath#/*/}
echo ${myPath##/*/}
:<<EOFT
    ${variable#pattern}  ${variable##pattern}  
    前者 删除最短匹配（非贪婪匹配）的部分，返回剩余部分
    后者 删除最长匹配（贪婪匹配）的部分，返回剩余部分

    匹配模式pattern可以使用*、?、[]等通配符

    替换头部匹配的部分 --- ${variable/#pattern/string}  
    举个例子
      foo=JPG.JPG
      echo ${foo/#JPG/jpg}   -- jpg.JPG
EOFT

## 尾部匹配
echo ${myPath%.*}
echo ${myPath%%.*}
:<<EOFT
    ${variable%pattern}  ${variable%%pattern}  
    前者 删除最短匹配（非贪婪匹配）的部分，返回剩余部分
    后者 删除最长匹配（贪婪匹配）的部分，返回剩余部分

    匹配模式pattern可以使用*、?、[]等通配符
    替换尾部匹配的部分  ---  ${variable/%pattern/string}
    举个例子  
      file=foo.png
      echo ${file%.png}.jpg    --  foo.jpg
EOFT

## 匹配任意位置
path=/home/Cam/foo/foo.name
echo ${path/foo/bar}   # /home/cam/bar/foo.name
echo ${path//foo/bar}  # /home/cam/bar/bar.name
phone="5555446-1414"
echo ${phone/5?4/-}    # 55-46-1414
:<<EOF
    ${variable/pattern/string}  ${variable//pattern/string}
    前者 最长匹配（贪婪匹配）的那部分被 string 替换，但仅替换第一个匹配
    后者 最长匹配（贪婪匹配）的那部分被 string 替换，所有匹配都替换

    ${variable/#pattern/string}   ${variable/%pattern/string}   --- # 类似于正则中的"^", % 类似于 "\$"
EOF

# 4. 改变大小写
echo ${path^^}
echo ${path,,}
:<<EOF
    ${varname^^}  --  转大写
    ${varname,,}  --  转小写
EOF


#####################
#  六、 算术运算      #
#####################

# 1. 算术表达式
((foo = 5 + 6))  #  等同于 let 'foo = 5 + 6'
echo $foo
echo $((2 * 4))
(( 3 - 3))
echo $?
:<<EOF
    ((...))会自动忽略内部的空格
    算术结果不是0, 执行成功 算术结果是0， 执行失败  $?
    读取算术运算的结果 -- \$((...))
    $((...))内部可以用圆括号改变运算顺序  -- echo \$(( (2 + 3) * 4 ))  20
    $((...))结构可以嵌套  echo \$(((5**2) * 3))  等同于 $(( $((5**2)) * 3 ))  

    重要一点， 只能计算整数
    如果在$((...))里面使用字符串，Bash 会认为那是一个变量名。如果不存在同名变量，Bash 就会将其作为空值
        eg. echo $(( "hello" + 2))  2  echo $(( "hello" * 2)) 0

    $[...]是以前的语法，也可以做整数运算  -- 不建议使用
EOF

# 2. 数值的进制
echo $((0xff))
echo $((2#11111111))

:<<EOT
    number：没有任何特殊表示法的数字是十进制数（以10为底）。
    0number：八进制数。
    0xnumber：十六进制数。
    base#number：base进制的数
EOT

# 3. 位运算
echo $((16>>2))   # 4
echo $((16<<2))   # 64
echo $((17&3))    # 1
echo $((17|3))    # 19
echo $((17^3))    # 18

:<<EOF
    <<：位左移运算，把一个数字的所有位向左移动指定的位。
    >>：位右移运算，把一个数字的所有位向右移动指定的位。
    &：位的“与”运算，对两个数字的所有位执行一个AND操作。
    |：位的“或”运算，对两个数字的所有位执行一个OR操作。
    ~：位的“否”运算，对一个数字的所有位取反。
    ^：位的异或运算（exclusive or），对两个数字的所有位执行一个异或操作。
EOF

# 4. 逻辑运算
echo $((3 > 2))
echo $(( (3 > 2) || (4 <= 1) ))
a=0
echo $((a<1 ? 1 : 0))

:<<EOT
    <：小于
    >：大于
    <=：小于或相等
    >=：大于或相等
    ==：相等
    !=：不相等
    &&：逻辑与
    ||：逻辑或
    !：逻辑否
    expr1?expr2:expr3：三元条件运算符
EOT

# 5. 赋值运算
echo $((a=2))
echo $a
:<<EFO
    支持多种赋值运算符
    parameter <<= value  --- parameter = parameter << value。
    parameter >>= value  --- parameter = parameter >> value。
    parameter &= value   --- parameter = parameter & value。
    parameter |= value   --- parameter = parameter | value。
    parameter ^= value   --- parameter = parameter ^ value
EFO

# 6. 求值运算
echo $((foo = 1 + 2, 3 * 4))   # 12
echo $foo                      # 3
:<<EOF
    逗号,在\$((...))内部是求值运算符，执行前后两个表达式，并返回后一个表达式的值
EOF

# 7. expr 命令
expr 3 + 2
:<<EOF
    expr命令支持变量替换
       foo=3
       expr $foo + 2
EOF