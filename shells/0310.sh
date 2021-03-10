#/bin/bash

#######################
#  十一、  数组         #
#######################
days=(Sun Mon Tue Wed Thu Fri Sat)
echo ${days[@]}
# 1. 创建数组
:<<WOF
  逐个赋值
    ARRAY[INDEX]=value    INDEX是一个大于或等于零的整数，也可以是算术表达式
  一次性赋值
    ARRAY=(value1 value2 ... valueN)
    采用这种方式赋值，可以默认顺序，也可以指定位置
      array=(a b c)
      array=([2]=c [0]=a [1]=b)
    只为某些值指定位置，也是可以的
      names=(hatter [5]=duchess alice)
  定义数组的时候，可以使用通配符
    mp3s=( *.mp3 )  ---   将当前目录的所有 MP3 文件，放进一个数组
WOF

# 2. 读取数组
activities=( swimming "water skiing" canoeing "white-water rafting" surfing )
for i in "${activities[@]}"; do
  echo $i
done
echo '------------'
for i in ${activities[@]}; do
  echo $i
done
:<<EOF
  读取单个元素
    echo ${array[i]}    i 是索引
  读取素有成员  @和*是数组的特殊索引，表示返回数组的所有成员
    eg.
      echo ${array[@]}
      for i in "${array[@]}"
      do
        echo $i
      done
    @和*放不放在双引号之中，是有差别的, 不放在引号中，会将数组中的单个变量拆分， 强烈建议放在引号中
    拷贝数组   
      hobbies=( "\${activities[@]}" )
      hobbies=( "\${activities[@]" diving )     -- 添加新元素
  默认位置
    读取数组成员时，没有读取指定哪一个位置的成员，默认使用0号位置
      foo=(a b c d e f)
      echo \${foo}   --- a

EOF

# 3. 数组长度
:<<EOF
  ${#array[*]}、${#array[@]}
  eg.
    a[100]=foo
    echo ${#a[@]}    -- 1
    echo ${#a[100]}  -- 3

EOF

# 4. 提取数组序号
arr=([5]=a [9]=b [23]=c)
echo ${!arr[@]}  # 5 9 23
:<<EOF
  ${!array[@]}或${!array[*]}  返回有值的数组序号
  遍历数组
    for i in ${!array[@]}
    do
      echo ${array[i]}
    done
  
EOF

# 5. 提取数组成员
food=( apples bananas cucumbers dates eggs fajitas grapes )
echo ${food[@]:1:3}
echo ${food[@]: -4}
:<<EOF
  ${array[@]:position:length} 提取数组成员 -- 与子字符串类似
EOF

# 6. 追加数组成员
:<<EOF
  +=赋值运算符, 值追加到数组末尾
  foo=(a b c)
  foo+=(d e f)
EOF

# 7.删除数组
:<<EOF
  unset 删除一个数组成员
    eg.
      foo=(a b c d e f)
      unset foo[2]
      echo \${foo[@]}  # a b d e f 
  将某个成员设为空值，可以从返回值中“隐藏”这个成员
    eg.
      foo=(a b c d e f)
      foo[1]=""
      echo ${foo[@]}  # a c d e f
      echo ${#foo[@]}  # 6
  unset ArrayName  -- 清空整个数组
EOF

# 8. 关联数组
declare -A colors
colors["red"]="#ff0000"
colors["green"]="#00ff00"
colors["blue"]="#0000ff"
echo ${colors[@]}
:<<EOF
  关联数组使用字符串而不是整数作为数组索引
  declare -A 可以声明关联数组 -- 必须这么使用
EOF


############################
#  十二、 set、shopt命令     #
############################

# 1. 简介
:<<EOF
  Bash 执行脚本时，会创建一个子 Shell
  set命令用来修改子 Shell 环境的运行参数，即定制环境
  命令行下不带任何参数，直接运行set，会显示所有的环境变量和 Shell 函数
EOF

# 2. set -u
:<<EOF
  执行脚本时，如果遇到不存在的变量，Bash 默认忽略它
    eg.
      #!/usr/bin/env bash

      echo \$a
      echo bar
  set -u就用来改变这种行为。脚本在头部加上它，遇到不存在的变量就会报错，并停止执行
    eg.
      #!/usr/bin/env bash
      set -u
      echo \$a
      echo bar
  -u 还有另一种写法 -o nounset
EOF

# 3. set -x
:<<EOF
  默认情况下，脚本执行后，只输出运行结果，没有其他内容
  set -x 用来在运行结果之前，先输出执行的那一行命令
    eg.
      #!/usr/bin/env bash
      set -x
      echo bar
  -x 还有另一种写法 -o xtrace
  脚本当中如果要关闭命令输出，可以使用set +x
EOF

# 4. Bash 的错误处理
::<<EOF
  脚本里面有运行失败的命令, Bash 默认会继续执行后面的命令
  实际开发中，如果某个命令失败，往往需要脚本停止执行，防止错误累积。这时，一般采用下面的写法
    command || exit 1

    command || { echo "command failed"; exit 1; }
    
    if ! command; then echo "command failed"; exit 1; fi
    
    command
    if [ "$?" -ne 0 ]; then echo "command failed"; exit 1; fi
  如果两个命令有继承关系，只有第一个命令成功了，才能继续执行第二个命令, 使用 && 连接两个命令
EOF

# 5. set -e
:<<EOF
  对于上面的写法， 多多少少有点麻烦
  set -e 从根本上解决了这个问题，它使得脚本只要发生错误，就终止执行
  但是，某些命令的非零返回值可能不表示失败，或者开发者希望在命令失败的情况下，脚本继续执行下去， 可以使用 set +e 关闭
  -e 还有另一种写法 -o errexit
EOF

# 6. -e还有另一种写法-o errexit
:<<EOF
  set -e 有一个例外情况，就是不适用于管道命令
  Bash 会把最后一个子命令的返回值，作为整个命令的返回值。也就是说，只要最后一个子命令不失败，管道命令总是会执行成功, 所以会失效
    eg.
      #!/usr/bin/env bash
      set -e

      foo | echo a
      echo bar
  set -o pipefail 解决这种情况 ， 脚本中可以设置 set -eo pipefail
EOF

# 7. set -E 
:<<EOF
  一旦设置了-e参数，会导致函数内的错误不会被trap命令捕获
  -E参数可以纠正这个行为，使得函数也能继承trap命令
    eg.
      #!/bin/bash
      set -Eeuo pipefail

      trap "echo ERR trap fired!" ERR

      myfunc()
      {
        # 'foo' 是一个不存在的命令
        foo
      }

      myfunc
EOF

# 8. 其他参数
:<<EOF
  set -n : 等于 set -o noexec, 运行命令，只检查语法是否正确 
  set -f : 等同于set -o noglob，表示不对通配符进行文件名扩展
  set -v : 等同于set -o verbose，表示打印 Shell 接收到的每一行输入
  set -o noclobber : 防止使用重定向运算符>覆盖已经存在的文件
EOF

# 9. set 命令总结 
:<<EOF
  建议脚本头部这样写
    写法一
      set -Eeuxo pipefail
    写法二
      set -Eeux
      set -o pipefail

EOF

# 10. shopt 命令
shopt
:<<EOF
  shopt命令用来调整 Shell 的参数,跟set命令的作用很类似
  shopt 查看所有参数，以及它们各自打开和关闭的状态
  shopt [参数]   查看该参数是否打开

  shopt -s optionNameHere   打开某个参数
  shopt -u optionNameHere   关闭某个参数
  shopt -q optionNameHere   查询某个参数是否打开，但不是直接输出查询结果，而是通过命令的执行状态(\$?)表示查询结果
EOF

######################
#  十三、 脚本除错     #
######################

# 环境变量
echo  "This is line $LINENO"

function func1()
{
  echo "func1: FUNCNAME0 is ${FUNCNAME[0]}"
  echo "func1: FUNCNAME1 is ${FUNCNAME[1]}"
  echo "func1: FUNCNAME2 is ${FUNCNAME[2]}"
  func2
}

function func2()
{
  echo "func2: FUNCNAME0 is ${FUNCNAME[0]}"
  echo "func2: FUNCNAME1 is ${FUNCNAME[1]}"
  echo "func2: FUNCNAME2 is ${FUNCNAME[2]}"
}

func1

:<<EOF
  LINENO 返回在脚本里面的行号
  FUNCNAME 返回一个数组, 内容是当前的函数调用堆栈,该数组的0号成员是当前调用的函数，1号成员是调用当前函数的函数，以此类推。
  BASH_SOURCE 返回一个数组, 内容是当前的脚本调用堆栈
    eg. 
      lib1.sh
        function func1()
        {
          echo "func1: BASH_SOURCE0 is ${BASH_SOURCE[0]}"
          echo "func1: BASH_SOURCE1 is ${BASH_SOURCE[1]}"
          echo "func1: BASH_SOURCE2 is ${BASH_SOURCE[2]}"
          func2
        }
      lib2.sh
        function func2()
        {
          echo "func2: BASH_SOURCE0 is ${BASH_SOURCE[0]}"
          echo "func2: BASH_SOURCE1 is ${BASH_SOURCE[1]}"
          echo "func2: BASH_SOURCE2 is ${BASH_SOURCE[2]}"
        }
      main.sh
        #!/bin/bash
        # main.sh

        source lib1.sh
        source lib2.sh

        func1
EOF

#############################
#  十四、 mktemp、trap命令    #
#############################

# 1. 临时文件安全问题
:<<EOF
  生成临时文件应该遵循下面的规则:
    创建前检查文件是否已经存在。
    确保临时文件已成功创建。
    临时文件必须有权限的限制。
    临时文件要使用不可预测的文件名。
    脚本退出时，要删除临时文件（使用trap命令）
EOF

# 2. mktemp命令
:<<EOF
  支持唯一文件名和清除机制
  为了保证脚本退出时临时文件被删除，可以使用trap命令指定退出时的清除操作
    eg.
      #!/bin/bash
      trap 'rm -f "$TMPFILE"' EXIT

      TMPFILE=$(mktemp) || exit 1
      echo "Our temp file is $TMPFILE"
  参数:
    -d : 可以创建一个临时目录
    -p : 可以指定临时文件所在的目录, 默认$TMPDIR环境变量指定的目录，如果这个变量没设置，那么使用/tmp目录
      eg. 
        mktemp -p ~/test
    -t : 指定临时文件的文件名模板,模板的末尾必须至少包含三个连续的X字符，表示随机字符，建议至少使用六个X
      eg.
        mktemp -t mytemp.XXXXXXX
EOF

# 3. trap 命令
:<<EOF
  trap命令用来在 Bash 脚本中响应系统信号
  trap [动作] [信号1] [信号2] ...
  
  信号:
    HUP：编号1，脚本与所在的终端脱离联系。
    INT：编号2，用户按下 Ctrl + C，意图让脚本终止运行。
    QUIT：编号3，用户按下 Ctrl + 斜杠，意图退出脚本。
    KILL：编号9，该信号用于杀死进程。
    TERM：编号15，这是kill命令发出的默认信号。
    EXIT：编号0，这不是系统信号，而是 Bash 脚本特有的信号，不管什么情况，只要退出脚本就会产生。

  trap 命令的常见使用场景，就是在 Bash 脚本中指定退出时执行的清理命令
  trap命令必须放在脚本的开头。否则，它上方的任何命令导致脚本退出，都不会被它捕获
EOF

