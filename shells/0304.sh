#/bin/bash

##################
#  一、 基本语法   #
##################
# 1. -e 会转义字符串中的特殊字符
echo -e "test\ntest"

# 2. 分号
rm -rf test/
mkdir -p test ; cd test ; touch a.txt ; cd ..
:<<EOF
注意，使用分号时，第二个命令总是接着第一个命令执行，不管第一个命令执行成功或失败
EOF

# 3. 命令的组合符
ls -lh && ls -lh test
mkdir foo || make bar
rm -rf foo ; rm -rf bar
:<<EOF
    使用 && : 命令依次执行， 前面执行成功， 后面才会执行
    使用 || : 命令依次执行， 即使前面执行失败， 后面也会执行, 等同于分号
    
    
    引申: 关于 & 使用
    1.   command &     --- 将命令放在后台执行
    2.   2>&1       --- 重定向输出 将 stderr 重定向到 stdout
    举个栗子， 挂载后台执行脚本
    nohup /bin/bash  [path]/[test.sh] >> [test.log] 2>&1 &

EOF


# 4. type 命令
type -t ls
:<<EOF
    查看命令的来源
    和 which 命令相似 
EOF


#######################
#   二、 模式扩展       #
#######################

# 1.关闭/开启扩展
set -o noglob # set -f
set +o noglob # set +f

# 2. 波浪线扩展
echo ~
:<<EOF
    ~ 会扩展成当前用户的主目录
    ~user 会扩展成user用户的主目录
    ~+ 会扩展成当前目录  等效于 pwd
EOF

# 3. 问号扩展
ls test/?.txt
:<<EOF
    ? 字符代表文件路径里面的任意单个字符，不包括空字符
EOF

# 4. 星号扩展
ls test/*.txt
:<<EOF
    *字符代表文件路径里面的任意数量的任意字符，包括零个字符
    * 只会匹配当前目录，不会匹配子目录  
    ** 匹配零个或多个子目录 bash 4.0

EOF

# 5. 方括号扩展
ls test/[c].txt
ls test | grep -P "[a-c]"
:<<EOF
    方括号扩展属于文件名匹配，即扩展后的结果必须符合现有的文件路径
    [^...] 和 [!...] 匹配不在方括号里面的字符
    [start-end] 匹配一个连续的范围 , [0-9]匹配[0123456789]
EOF

# 6. 大括号扩展     
echo {1,2,3}
echo d{a,e,i,o,u}g
echo {j{p,pe}g,png}
echo {1..10..2}
echo {a..c}{1..3}
:<<EOF
    {...}扩展成大括号里面的所有值
    括号中的值用逗号隔开， 中间不能有空格
    括号中若只有但个值，需要加上逗号， 如 {a,} 才会扩展成 a
    {start..end} 扩展成一个连续序列
    如果遇到无法理解的简写，大括号模式就会原样输出，不会扩展
    大括号扩展的常见用途为新建一系列目录 mkdir {2007..2009}-{01..12}
    多个简写形式连用，会有循环处理的效果
EOF

# for i in {10..1}
# do 
#     echo "$i -- test"
# done

# 7. 变量扩展
echo ${SHELL}
echo ${!P@}
:<<EOF
    $开头的词元视为变量, 将其扩展成变量值
    ${!string*} 和 ${!string@} 返回所有匹配给定字符串string的变量名
EOF

# 8. 子命令扩展
echo `date`
echo $(ls $(pwd))
:<<EOF
    $(..) 扩展另一个命令的运行结果， 可以嵌套
EOF

# 9. 算术扩展
echo 2 + 3
A=2
echo $((A + 3))
echo $[2 + 3]
:<<EOF
    $(()) 可以扩展成整数运算的结果
EOF

# 10. 字符类
echo [[:lower:]]*
:<<EOF
    [[:class:]]表示一个字符类, 扩展成某一类特定字符之中的一个
EOF

#######################
#   三、引号和转义      #
#######################

# 1. 转义
echo \$date
echo -e "a\tb"
:<<EOF
    某些字符在 Bash 里面有特殊含义,比如 ($, & *)
    如要原样输出，需要加上反斜杠对其转义

EOF

# 2. 单引号
echo '$(echo foo)'
echo $'it\'s'
:<<EOF
    单引号用于保留字符的字面含义,各种特殊字符在单引号里面，都会变为普通字符
    echo 'it\'s' 不正确
EOF

# 3. 双引号
echo "*"
echo "$(ls)"
echo "hello
word"
:<<EOF
    双引号比单引号宽松, 大部分特殊字符在双引号里面，都会失去特殊含义，变成普通字符
    美元符号($)、反引号(``)和反斜杠(\) 依然有特殊含义
    换行符在双引号之中，会失去特殊含义，Bash 不再将其解释为命令的结束，只是作为普通的换行符。所以可以利用双引号，在命令行输入多行文本
EOF

# 4. Here文档
cat <<_EOF_
<html>
    <head>
        <title>
            The title of your page
        </title>
    </head>
    <body>
        Your page content goes here.
    </body>
</html>
_EOF_

foo='hello world'
cat << _example_
$foo
"$foo"
'$foo'
_example_

cat << "_example_"
$foo
"$foo"
'$foo'
_example_

:<< EOF
    Here 文档是一种输入多行字符串的方法，格式分成 开始标记(<<_EOF_) 和 结束标记(_EOF_), 和注释很像
    Here 文档内部会发生变量替换，同时支持反斜杠转义，但是不支持通配符扩展
    双引号和单引号也失去语法作用，变成了普通字符
    如果不希望发生变量替换，可以把 Here 文档的开始标记放在引号(单引号和双引号都可以)之中
    Here 文档的本质是重定向，它将字符串重定向输出给某个命, 所以只适合接受标准输入作为参数的命令
    command << token
        string
    token
    等于 echo string | command
EOF

# 5. Here 字符串
md5sum <<< "abc"
:<<EOF
    <<< string
    Here 字符串, 三个小于号(<<<)表示， 将字符串通过标准输入，传递给命令
EOF







