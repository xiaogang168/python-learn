    #重定向文件
    with open('d:/work/test.txt', 'wt') as f:
        print('Hello World!', file=f)

   #读写二进制文件
       with open('somefile.bin', 'wb') as f:
        f.write(b'Hello World')     

    #压缩文件
    with gzip.open('somefile.gz', 'rt') as f:
        text = f.read()
    with bz2.open('somefile.bz2', 'rt') as f:
        text = f.read()

    #序列化
    import pickle
    #转储
    f = open('somefile', 'wb')
    pickle.dump(data, f)
    s = pickle.dumps(data)  #转储为字符串
    #load
    f = open('somefile', 'rb')
    data = pickle.load(f)
    data = pickle.loads(s) #恢复

    #创建临时文件和文件夹
    from tempfile import TemporaryFile
    from tempfile import TemporaryDirectory
    from tempfile import NamedTemporaryFile
    import tempfile
    #临时文件
     with TemporaryFile('w+t') as f:
        # Read/write to the file
        f.write('Hello World\n')   
        f.seek(0) #回到文件起点
        data = f.read() 
    with NamedTemporaryFile('w+t') as f:
        print('filename is:', f.name)
    with TemporaryDirectory() as dirname:
        print('dirname is:', dirname)
    print(tempfile.mkstemp())
    print(tempfile.mkdtemp())
    print(tempfile.gettempdir())

    #列出目录下的文件
    names = [name for name in os.listdir('somedir')
            if os.path.isfile(os.path.join('somedir', name))]
    #目录
    dirnames = [name for name in os.listdir('somedir')
            if os.path.isdir(os.path.join('somedir', name))]
    #筛选py文件
    pyfiles = [name for name in os.listdir('somedir')
                if name.endswith('.py')]  
    pyfiles = glob.glob('somedir/*.py')
    #获取文件状态
    file_metadata = [(name, os.stat(name)) for name in pyfiles]
          
    