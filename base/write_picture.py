from PIL import ImageDraw,Image,ImageFont


img=Image.open("ackground.jpg")
jgz=Image.open("jgz.jpg")
img.paste(jgz,(75,50))#paste函数的参数为(需要修改的图片，粘贴的起始点的横坐标，粘贴的起始点的纵坐标）
img.show()
draw=ImageDraw.Draw(img)
ttfront = ImageFont.truetype('simhei.ttf', 25)#设置字体大小
draw.text((60, 190),"我的内心毫无波动\n   甚至还想笑",fill=(0,0,0), font=ttfront)#drawObject.text(position,  string,  options)Position是一个二元元组，指定字符串左上角坐标，string是要写入的字符串，options选项可以为fill或者font(只能选择其中之一作为第三参量，不能两个同同时存在，要改变字体颜色，见ImageFont模块中的NOTE)。其中fill指定字的颜色，font指定字体与字的尺寸，font必须为ImageFont中指定的font类型，具体用法见ImageFont.Truetype()
img.show()