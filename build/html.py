from tool import savef

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
    print('html_build - 生成中')
    savef('index.html',INDEX)