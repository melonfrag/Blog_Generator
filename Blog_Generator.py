import time

Title = ""
Time = ""
Contents = ""
input("""请确认您写的文章已复制到该目录下的PreRead.txt！
文章格式：第一行为标题，空一行后写正文部分。参见Example.txt。
按Enter继续...""")
f = open("PreRead.txt",encoding="utf-8")
s = f.read()
contents = s.split("\n")
f.close()
Title = contents[0]
Time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
try:
    contents = contents[2:]
except IndexError:
    print("生成失败，请检查PreRead.txt中的内容格式是否有误！")
while "" in contents:
    contents.remove("")
for i in range(len(contents)):
    Contents = Contents + "<p>" + contents[i] + "</p>" + "\n"
Template = """
<!DOCTYPE html>
<html lang="en-US">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

<!-- Begin Jekyll SEO tag v2.8.0 -->
<title>Frag's Blogs | fragdev.eu.org</title>
<style>

     @font-face {
      font-family: "MiSans";
      src: url("https://fragdev.eu.org/blogs/MiSans-Normal.ttf");
     }

    body{
    	font-family:"MiSans"
		}
   
    .container-lg{
    	width: 75%;
    	height:100vh;
    	display:flex;
    	flex-direction: column;
    	max-height: calc(100vh - 140px); /* 考虑底部高度 */
    	overflow-y: auto;
		}
    
  		footer {
      /* 设置底部样式 */
      height: 60px;
      text-align: center;
      padding: 20px;
		}
     
     .xtitle,.xtime {
 		width: 200px;
 		height: 200px;
 		display: inline-block;
		 }
  
</style>
<meta name="generator" content="Jekyll v3.9.3" />
<meta property="og:title" content="Blog" />
<meta property="og:locale" content="en_US" />
<meta name="description" content="Personal website" />
<meta property="og:description" content="Personal website" />
<link rel="canonical" href="https://fragdev.eu.org/blogs/2024/01/FragBlog.html" />
<meta property="og:url" content="http://fragdev.eu.org/blogs/2024/01/FragBlog.html" />
<meta property="og:site_name" content="melonfrag.github.io" />
<meta property="og:type" content="website" />
<meta name="twitter:card" content="summary" />
<meta property="twitter:title" content="Blog" />
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"WebPage","description":"personal website(?)","headline":"第一个Blog","url":"http://fragdev.eu.org/blogs/2024/01/FragBlog.html"}</script>
<!-- End Jekyll SEO tag -->

    <link rel="stylesheet" href="https://fragdev.eu.org/assets/css/style.css">

<!-- Setup Google Analytics -->



<!-- You can set your favicon here -->
<!-- link rel="shortcut icon" type="image/x-icon" href="/favicon.ico" -->

<!-- end custom head snippets -->

  </head>
  <body>
    
    <div class="container-lg px-6 my-6 markdown-body">
    <script color="102,160,255" opacity='3' zIndex="-1" count="200" src="https://cdn.bootcss.com/canvas-nest.js/2.0.4/canvas-nest.js" type="text/javascript"></script>

     
<!-- Start Contents -->  
    <h1>Frag's Blogs</h1>
      
      <div>
    <p style="font-weight: bolder; font-size:20px; display: inline;">"""+Title+"""     </p>
      <p style="font-weight: lighter; font-size:15px; display: inline;">"""+Time+"""</p>
      </div>
      <p></p>
      """+Contents+"""
     
<!-- End Contents -->  

   </div>
    <footer>
      <center><p>Powered By <a href="https://pages.github.com" target="_blank">Github Pages</a> |  © 2024 Fragdev.</p></center>
    </footer>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/anchor-js/4.1.0/anchor.min.js" integrity="sha256-lZaRhKri35AyJSypXXs4o6OPFTbTmUoltBbDCbdzegg=" crossorigin="anonymous"></script>
  </body>
</html>
"""
g = open(f'{Title}.html','w', encoding='utf-8')
g.write(Template)
g.close()
input("""
生成完毕，文章已保存至该目录下。建议您仅使用英文字母与数字命名文章，且名称不应过长。
按Enter退出程序...""")


