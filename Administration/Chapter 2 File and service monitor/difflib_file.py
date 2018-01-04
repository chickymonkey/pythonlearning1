import difflib
import codecs
text1 = """text1： 
This module provides classes and functions for comparing sequences.
including HTML and context and unified diffs.
difflib document v7.4
add string
"""
text1_lines = text1.splitlines( ) #以行进行分隔， 以便进行对比
text2 = """text2： 
This module provides classes and functions for Comparing sequences.
including HTML and context and unified diffs.
difflib document v7.5"""
text2_lines = text2.splitlines( )
d = difflib.HtmlDiff( ) #创建Differ( ) 对象
 

    
difference_html=d.make_file(text1_lines, text2_lines)
difference_html_utf=codecs.encode(difference_html,'utf')
fout=open('difference.html','wt')
#print(difference_html)
fout.write(str(difference_html_utf))
fout.close()