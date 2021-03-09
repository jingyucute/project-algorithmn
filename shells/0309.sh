#/bin/bash

#######################
#  九、 条件判断        #
#######################

# 1. while 循环
number=0
while [ "$number" -lt 10 ]; do
  echo "Number = $number"
  number=$((number + 1))
done
:<<EOF
  循环条件condition可以使用test命令，跟if结构的判断条件写法一致
  while的条件部分也可以是执行一个命令 
    while echo 'ECHO'; do echo 'Hi, while looping ...'; done
  
EOF

# 2. until 循环
number=0
until [ "$number" -ge 10 ]; do
  echo "Number = $number"
  number=$((number + 1))
done
:<<EOF
  until循环与while循环恰好相反，只要不符合判断条件（判断条件失败），就不断循环执行指定的语句, 符合就退出

  while ! cp $1 $2; do
    echo 'Attempt to copy failed. waiting...'
    sleep 5
  done
EOF

# 3. for...in 循环
for i in word1 word2 word3
do
  echo $i
done

:<<EOF
  for variable in list
  do
    commands
  done

  in list的部分可以省略，这时list默认等于脚本的所有参数$@, 但是，为了可读性，最好还是不要省略
EOF

# 4. for 循环
for (( i=0; i<5; i=i+1 )); do
  echo $i
done
:<<EOF
  for (( expression1; expression2; expression3 )); do
    commands
  done
EOF

# 5. break continue
for number in 1 2 3 4 5 6
do
  echo "number is $number"
  if [ "$number" = "3" ]; then
    break
  fi
done

# 6. select 结构
# select brand in Samsung Sony iphone symphony Walton
# do
#   echo "You have chosen $brand"
# done
:<<EOF
  来生成简单的菜单

  select生成一个菜单，内容是列表list的每一项，并且每一项前面还有一个数字编号。
  Bash 提示用户选择一项，输入它的编号。
  用户输入以后，Bash 会将该项的内容存在变量name，该项的编号存入环境变量REPLY。如果用户没有输入，就按回车键，Bash 会重新输出菜单，让用户选择。
  执行命令体commands。
  执行结束后，回到第一步，重复这个过程。

EOF

#######################
#  十、  函数          #
#######################

declare -f

# 1. 简介
:<<EOF
  函数（function）是可以重复使用的代码片段，有利于代码的复用
  函数总是在当前 Shell 执行

  定义语法
  fn() {
    # codes
  }

  function fn() {
    # codes
  }

  删除一个函数，可以使用unset命令  ---  unset -f functionName
  查看当前 Shell 已经定义的所有函数，可以使用declare命令
EOF

# 2. 参数变量
function alice(){
  echo "alice: $@"
  echo "$0: $1 $2 $3 $4"
  echo "$# arguments"
}
alice in wonderland
:<<EOF
  $1~$9：函数的第一个到第9个的参数。
  $0：函数所在的脚本名。
  $#：函数的参数总数。
  $@：函数的全部参数，参数之间使用空格分隔。
  $*：函数的全部参数，参数之间使用变量$IFS值的第一个字符分隔，默认为空格，但是可以自定义
EOF

# 3. return 命令
function func_return_value {
  return 10
}
func_return_value
echo $?
:<<EOF
  return命令用于从函数返回一个值
EOF

# 4. 全局变量和局部变量，local 命令 
:<<EOF
  函数体内不仅可以声明全局变量，还可以修改全局变量
  foo=1
  fn () {
    foo=2
  }
  fn
  echo $foo  # 2
  函数里面可以用local命令声明局部变量
  fn () {
    local foo
    foo=1
    echo "fn: foo = $foo"
  }
  fn
  echo "global: foo = $foo"
EOF

