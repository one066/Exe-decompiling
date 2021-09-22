# 对pyinstaller打包exe反编译

## 简述
> 主要使用别人的 `pyinstxtractor.py` 将exe还原为.pyc,然后还有将生成的stract文件中获取前8个
字节（magic）补充到目标文件，这里我用python解决了。  
> 然后使用 `uncompyle `做的将.pyc转到.py

## 使用
- `pip install uncompyle`
- 只需将exe放到 `bucket` 文件夹下，运行`main.py`,即可得到python文件
- 中间过程生成的文件全部会自动删除

## 版本
- 可能编译python版本不同，用不了(测试的3.7可以用)
