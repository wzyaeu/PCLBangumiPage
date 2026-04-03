from tool import savef, logs_add

INDEX = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PCL-Bangumi-Page</title>
</head>
<body>
    
</body>
</html>
'''

def html_build():
    print('html - 生成中')
    savef('index.html',INDEX)
    logs_add('html','save_file index.html','Success')