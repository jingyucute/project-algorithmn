#/bin/bash

#######################
#  七、 read 命令      #
#######################

# 1. 用法
# echo -n "输入一些文本 > "
# read text
# echo "你的输入：$text"
:<<EOF
    用户输入数据  read [-options] [variable...]
    可以输入多个数据, 若输入的变量个数小于命令给出的变量个数，则额外变量赋值为空
      eg. 
        echo Please, enter your firstname and lastname
        read FN LN
        echo "Hi! $LN, $FN !"

    读取文件
    filename=/etc/hosts
    while read myline
    do
        echo "$myline"
    done < $filename
EOF

# 2. 参数
:<<EFO
    -t : 设置超时的秒数, 超过了指定时间，用户仍然没有输入，脚本将放弃等待，继续向下执行
        echo -n "输入一些文本 > "
        if read -t 3 response; then
            echo "用户已经输入了"
        else
            echo "用户没有输入"
        fi
    -p : 指定用户输入的提示信息
        read -p "Enter one or more values > "
        echo "REPLY = '$REPLY'"
    -a : 把用户的输入赋值给一个数组
        read -a people
        echo ${people[2]}
    -n : 指定只读取若干个字符作为变量值，而不是整行读取
        read -n 3 letter
        echo $letter
    -e : 允许用户输入的时候，使用readline库提供的快捷键
    -d delimiter : 定义字符串delimiter的第一个字符作为用户输入的结束，而不是一个换行符
    -r : 不把用户输入的反斜杠字符解释为转义字符
    -s : 用户的输入不显示在屏幕上, 用户输入密码
    -u fd : 使用文件描述符fd作为输入
EFO

# 3. IFS 变量
FILE=/etc/passwd

# read -p "Enter a username > " user_name
user_name=$USER
file_info="$(grep "^$user_name:" $FILE)"

if [ -n "$file_info" ]; then
  IFS=":" read user pw uid gid name home shell <<< "$file_info"
  echo "User = '$user'"
  echo "UID = '$uid'"
  echo "GID = '$gid'"
  echo "Full Name = '$name'"
  echo "Home Dir. = '$home'"
  echo "Shell = '$shell'"
else
  echo "No such user '$user_name'" >&2
  exit 1
fi

:<<EOF
    对于IFS 赋值命令 和后面的命令不再一行， 应该这样写
      OLD_IFS="$IFS"
      IFS=":"
      read user pw uid gid name home shell <<< "$file_info"
      IFS="$OLD_IFS"
EOF


#######################
#  八、 条件判断        #
#######################

# 1. if结构
if test $USER = "foo"; then
  echo "Hello foo."
else
  echo "You are not foo."
fi
:<<EOF
    if commands; then
        commands
    [elif commands; then
        commands...]
    [else
        commands]
    fi

    单行if结构, 
      if false; then echo 'hello world'; elif true; then echo "heihei"; fi
    
    if关键字后面也可以是一条命令，该条命令执行成功, 判断条件成立
      if echo 'hi'; then echo 'hello world'; fi
    if后面可以跟任意数量的命令。所有命令都会执行，但是判断真伪只看最后一个命令
EOF

# 2. test 命令
test -f /etc/hosts
echo $?
:<<EOF
    三种形式等价 
      写法一
        test expression
      写法二
        [ expression ]
      写法三 -- 只有这种支持正则表达式
        [[ expression ]]
    eg.
      if test -e /tmp/foo.txt ; then
        echo "Found foo.txt"
      fi
      if [ -e /tmp/foo.txt ] ; then
        echo "Found foo.txt"
      fi
      if [[ -e /tmp/foo.txt ]] ; then
        echo "Found foo.txt"
      fi
EOF

# 3. 判断表达式
## 3.1 文件判断
:<<EOF
    [ -a file ] : 如果 file 存在，则为true
    [ -b file ] : 如果 file 存在并且是一个块（设备）文件，则为true
    [ -c file ] : 如果 file 存在并且是一个字符（设备）文件，则为true
    [ -d file ] : 如果 file 存在并且是一个目录，则为true
    [ -e file ] : 如果 file 存在，则为true
    [ -f file ] : 如果 file 存在并且是一个普通文件，则为true
    [ -g file ] : 如果 file 存在并且设置了组 ID，则为true
    [ -G file ] : 如果 file 存在并且属于有效的组 ID，则为true
    [ -h file ] : 如果 file 存在并且是符号链接，则为true
    [ -r file ] : 如果 file 存在并且可读（当前用户有可读权限），则为true
    [ -s file ] : 如果 file 存在且其长度大于零，则为true
    [ -S file ] : 如果 file 存在且是一个网络 socket，则为true
    [ -t fd ]   : 如果 fd 是一个文件描述符，并且重定向到终端，则为true
    [ -w file ] : 如果 file 存在并且可写（当前用户拥有可写权限），则为true
    [ -x file ] : 如果 file 存在并且可执行（有效用户有执行／搜索权限），则为true
    [ file1 -nt file2 ] : 如果 FILE1 比 FILE2 的更新时间最近，或者 FILE1 存在而 FILE2 不存在，则为true
    [ file1 -ot file2 ] : 如果 FILE1 比 FILE2 的更新时间更旧，或者 FILE2 存在而 FILE1 不存在，则为true
    [ FILE1 -ef FILE2 ] : 如果 FILE1 和 FILE2 引用相同的设备和 inode 编号，则为true
EOF

## 3.2 字符串判断
:<<EOF
    [ string ]：如果string不为空（长度大于0），则判断为真
    [ -n string ]：如果字符串string的长度大于零，则判断为真
    [ -z string ]：如果字符串string的长度为零，则判断为真
    [ string1 = string2 ]、[ string1 == string2 ]：如果string1和string2相同，则判断为真
    [ string1 != string2 ]：如果string1和string2不相同，则判断为真
    [ string1 '>' string2 ]：如果按照字典顺序string1排列在string2之后，则判断为真
    [ string1 '<' string2 ]：如果按照字典顺序string1排列在string2之前，则判断为真

    test命令内部的>和<，必须用引号引起来
EOF

## 3.3 整数判断
:<<EOF
    [ integer1 -eq integer2 ]：如果integer1等于integer2，则为true
    [ integer1 -ne integer2 ]：如果integer1不等于integer2，则为true
    [ integer1 -le integer2 ]：如果integer1小于或等于integer2，则为true
    [ integer1 -lt integer2 ]：如果integer1小于integer2，则为true
    [ integer1 -ge integer2 ]：如果integer1大于或等于integer2，则为true
    [ integer1 -gt integer2 ]：如果integer1大于integer2，则为true
EOF

## 3.4 正则判断
INT=-5

if [[ "$INT" =~ ^-?[0-9]+$ ]]; then
  echo "INT is an integer."
else
  echo "INT is not an integer." 
fi

:<<EOF
    [[ string1 =~ regex ]]
    =~是正则比较运算符
EOF


## 3.5 test 判断的逻辑运算
:<<EOF
    AND运算：符号&&，也可使用参数-a
    OR运算：符号||，也可使用参数-o
    NOT运算：符号!

    MIN_VAL=1
    MAX_VAL=100
    INT=50
    if [ ! \( $INT -ge $MIN_VAL -a $INT -le $MAX_VAL \) ]; then
        echo "$INT is outside $MIN_VAL to $MAX_VAL."
    else
        echo "$INT is in range."
    fi
EOF

## 3.6 算术判断
if ((3==3))
then
  echo "true"
fi
:<<EOF
    算术计算的结果是非零值，则表示判断成立,跟命令的返回值正好相反
    算术条件((...))也可以用于变量赋值 
      if (( foo = 5 ));then echo "foo is $foo"; fi
    
EOF

## 3.7 普通命令的逻辑运算
:<<EOF
    使用 Bash 的命令控制操作符&&（AND）和||（OR），进行多个命令的逻辑运算
    command1 && command2     command1 || command2
    eg
      if [ condition ] && [ condition ]; then
        command
      fi
EOF

# 4. case 结构
OS=$(uname -s)
case "$OS" in
  FreeBSD) echo "This is FreeBSD" ;;
  Darwin) echo "This is Mac OSX" ;;
  AIX) echo "This is AIX" ;;
  Minix) echo "This is Minix" ;;
  Linux) echo "This is Linux" ;;
  *) echo "Failed to identify this OS" ;;
esac
:<<EOF
    case expression in
        pattern )
            commands ;;
        pattern )
            commands ;;
        ...
    esac
    pattern是表达式的值或者一个模式, 可以有多条，用来匹配多个值，每条以两个分号（;）结尾
EOF